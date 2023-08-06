import datetime
import json
import os
import time
import uuid
from typing import List, Dict, Text, NoReturn
from urllib.parse import unquote

import demjson

try:
    import allure

    USE_ALLURE = True
except ModuleNotFoundError:
    USE_ALLURE = False
# import allure
from loguru import logger

from rrtv_httprunner import utils, exceptions, globalvar
from rrtv_httprunner.client import HttpSession
from rrtv_httprunner.exceptions import ValidationFailure, ParamsError
from rrtv_httprunner.ext.uploader import prepare_upload_step
from rrtv_httprunner.loader import load_project_meta, load_testcase_file
from rrtv_httprunner.models import (
    TConfig,
    TStep,
    VariablesMapping,
    StepData,
    TestCaseSummary,
    TestCaseTime,
    TestCaseInOut,
    ProjectMeta,
    TestCase,
    Hooks, data_enum, AllureParameter, DiffParameter
)
from rrtv_httprunner.parser import build_url, parse_data, parse_variables_mapping
from rrtv_httprunner.response import ResponseObject
from rrtv_httprunner.testcase import Config, Step
from rrtv_httprunner.utils import merge_variables, write_excel


class HttpRunner(object):
    config: Config
    teststeps: List[Step]

    success: bool = False  # indicate testcase execution result
    __config: TConfig
    __teststeps: List[TStep]
    __project_meta: ProjectMeta = None
    __case_id: Text = ""
    __export: List[Text] = []
    __step_datas: List[StepData] = []
    __session: HttpSession = None
    __session_variables: VariablesMapping = {}
    # time
    __start_at: float = 0
    __duration: float = 0
    # log
    __log_path: Text = ""

    def __init_tests__(self) -> NoReturn:
        self.__config = self.config.perform()
        self.__teststeps = []
        for step in self.teststeps:
            self.__teststeps.append(step.perform())

    @property
    def raw_testcase(self) -> TestCase:
        if not hasattr(self, "__config"):
            self.__init_tests__()

        return TestCase(config=self.__config, teststeps=self.__teststeps)

    def with_project_meta(self, project_meta: ProjectMeta) -> "HttpRunner":
        self.__project_meta = project_meta
        return self

    def with_session(self, session: HttpSession) -> "HttpRunner":
        self.__session = session
        return self

    def with_case_id(self, case_id: Text) -> "HttpRunner":
        self.__case_id = case_id
        return self

    def with_variables(self, variables: VariablesMapping) -> "HttpRunner":
        self.__session_variables = variables
        return self

    def with_export(self, export: List[Text]) -> "HttpRunner":
        self.__export = export
        return self

    def __call_hooks(
            self, hooks: Hooks, step_variables: VariablesMapping, hook_msg: Text,
    ) -> NoReturn:
        """ call hook actions.

        Args:
            hooks (list): each hook in hooks list maybe in two format.

                format1 (str): only call hook functions.
                    ${func()}
                format2 (dict): assignment, the value returned by hook function will be assigned to variable.
                    {"var": "${func()}"}

            step_variables: current step variables to call hook, include two special variables

                request: parsed request dict
                response: ResponseObject for current response

            hook_msg: setup/teardown request/testcase

        """
        logger.info(f"call hook actions: {hook_msg}")

        if not isinstance(hooks, List):
            logger.error(f"Invalid hooks format: {hooks}")
            return

        for hook in hooks:
            if isinstance(hook, Text):
                # format 1: ["${func()}"]
                logger.debug(f"call hook function: {hook}")
                parse_data(hook, step_variables, self.__project_meta.functions)
            elif isinstance(hook, Dict) and len(hook) == 1:
                # format 2: {"var": "${func()}"}
                var_name, hook_content = list(hook.items())[0]
                hook_content_eval = parse_data(
                    hook_content, step_variables, self.__project_meta.functions
                )
                logger.debug(
                    f"call hook function: {hook_content}, got value: {hook_content_eval}"
                )
                logger.debug(f"assign variable: {var_name} = {hook_content_eval}")
                step_variables[var_name] = hook_content_eval
            else:
                logger.error(f"Invalid hook format: {hook}")

    def __execute(self, aspect: Text, step: TStep, variables_mapping=None,
                  functions_mapping=None, ) -> NoReturn:

        def execute(opportunity):
            for s in opportunity:
                if data_enum.VAR_SYMBOL in s:
                    var_name = s.split(data_enum.VAR_SYMBOL)[1]
                    hook_content_eval = parse_data(s.split(data_enum.VAR_SYMBOL)[0], variables_mapping,
                                                   functions_mapping)
                    extract_mapping[var_name] = hook_content_eval
                    variables_mapping.update(extract_mapping)
                    logger.debug(f"assign variable: {var_name} = {hook_content_eval}")
                else:
                    parse_data(
                        s, variables_mapping, functions_mapping
                    )

        need_configured_attr = data_enum.SUPPORT_TYPES
        extract_mapping = {}
        has_attr = any(attr in step.variables for attr in need_configured_attr)  # 判断是否有数据源
        if has_attr is False and len(step.begin) == 1 and step.begin[0].startswith("cmd:"):
            has_attr = True

        if aspect == "begin":
            if not has_attr:
                has_attr = any(data_enum.DB_CONFIG_SYMBOL in begin for begin in step.begin)
            if not has_attr:
                raise Exception("data source not found, please check configuration")
            if has_attr is True and step.begin:
                logger.info("begin start execute >>>>>>")
                execute(step.begin)

        elif aspect == "end":
            if not has_attr:
                has_attr = any(data_enum.DB_CONFIG_SYMBOL in end for end in step.end)
            if not has_attr:
                raise Exception("data source not found, please check configuration")
            if has_attr is True and step.end:
                logger.info("end start execute >>>>>>")
                execute(step.end)

    def __run_step_request(self, step: TStep) -> StepData:
        """run teststep: request"""
        step_data = StepData(name=step.name)

        # parse
        prepare_upload_step(step, self.__project_meta.functions)
        request_dict = step.request.dict()
        request_dict.pop("upload", None)

        # setup hooks
        if step.begin_hooks:
            self.__call_hooks(step.begin_hooks, step.variables, "begin request")

        # execute setup
        if step.begin:
            self.__execute("begin", step, step.variables, self.__project_meta.functions)

        parsed_request_dict = parse_data(
            request_dict, step.variables, self.__project_meta.functions
        )
        parsed_request_dict["headers"].setdefault(
            "HRUN-Request-ID",
            f"HRUN-{self.__case_id}-{str(int(time.time() * 1000))[-6:]}",
        )
        step.variables["request"] = parsed_request_dict

        # begin hooks
        if step.setup_hooks:
            self.__call_hooks(step.setup_hooks, step.variables, "setup request")
        #
        # # execute setup
        # if step.setup:
        #     self.__execute("setup", step, step.variables, self.__project_meta.functions)

        # prepare arguments
        method = parsed_request_dict.pop("method")
        url_path = parsed_request_dict.pop("url")
        url = build_url(self.__config.base_url, url_path)
        parsed_request_dict["verify"] = self.__config.verify
        parsed_request_dict["json"] = parsed_request_dict.pop("req_json", {})

        a = AllureParameter()
        diff_obj = DiffParameter()
        diff_obj.base_url = self.__config.base_url
        parsed_request_dict["allure"] = a
        parsed_request_dict["diff"] = diff_obj
        # request
        resp = self.__session.request(method, url, **parsed_request_dict)
        resp_obj = ResponseObject(resp)
        step.variables["response"] = resp_obj

        # teardown hooks
        if step.teardown_hooks:
            self.__call_hooks(step.teardown_hooks, step.variables, "teardown request")

        if USE_ALLURE:
            # update allure report meta
            allure.attach(str(resp_obj.resp_obj.status_code), "状态码:", allure.attachment_type.TEXT)
            try:
                if resp_obj.resp_obj.text is not None and resp_obj.resp_obj.text != "":
                    value = demjson.decode(resp_obj.resp_obj.text)
                    if "code" in value:
                        allure.attach(str(value["code"]), "code:", allure.attachment_type.TEXT)
                    if "msg" in value:
                        allure.attach(str(value["msg"]), "msg:", allure.attachment_type.TEXT)
                    if value != {}:
                        allure.attach(json.dumps(value, ensure_ascii=False), "data:",
                                      allure.attachment_type.TEXT)
            except:
                pass
            allure.attach(a.curl, "curl:", allure.attachment_type.TEXT)

        def log_req_resp_details():
            err_msg = "\n{} DETAILED REQUEST & RESPONSE {}\n".format("*" * 32, "*" * 32)

            # log request
            err_msg += "====== request details ======\n"
            err_msg += f"url: {url}\n"
            err_msg += f"method: {method}\n"
            headers = parsed_request_dict.pop("headers", {})
            err_msg += f"headers: {headers}\n"
            for k, v in parsed_request_dict.items():
                v = utils.omit_long_data(v)
                if isinstance(v, Text):
                    v = unquote(v)
                if isinstance(v, Dict):
                    v = {k: unquote(v) for k, v in v.items() if isinstance(v, Text)}
                err_msg += f"{k}: {repr(v)}\n"

            err_msg += "\n"

            # log response
            err_msg += "====== response details ======\n"
            err_msg += f"status_code: {resp.status_code}\n"
            err_msg += f"headers: {resp.headers}\n"
            err_msg += f"body: {repr(resp.text)}\n"
            logger.error(err_msg)

        # extract
        extractors = step.extract
        extract_mapping = resp_obj.extract(extractors, step.variables, self.__project_meta.functions)
        step_data.export_vars = extract_mapping

        variables_mapping = step.variables
        variables_mapping.update(extract_mapping)

        # validate
        validators = step.validators
        if diff_obj.diff != {}:
            validators = []
            validators.append(
                {'t1': resp_obj.body, 't2': demjson.decode(diff_obj.diff["t2"].resp_obj.text), 'kwargs': {},
                 'message': ''})
        session_success = False
        try:
            resp_obj.validate(
                validators, variables_mapping, self.__project_meta.functions
            )
            session_success = True
        except ValidationFailure:
            session_success = False
            log_req_resp_details()
            # log testcase duration before raise ValidationFailure
            self.__duration = time.time() - self.__start_at
            raise
        finally:
            self.success = session_success
            step_data.success = session_success

            if hasattr(self.__session, "data"):
                # rrtv_httprunner.client.HttpSession, not locust.clients.HttpSession
                # save request & response meta data
                self.__session.data.success = session_success
                self.__session.data.validators = resp_obj.validation_results

                # save step data
                step_data.data = self.__session.data

                # end hooks
                if step.end_hooks:
                    self.__call_hooks(step.end_hooks, step.variables, "end request")

                # 执行end
                if step.end:
                    self.__execute("end", step, variables_mapping, self.__project_meta.functions)
            if globalvar.get_value("toexcel", "") != "":
                location = ""
                call = ""
                for marks in self.pytestmark:
                    if "location" == marks.name:
                        location = marks.args[0]
                    if "nocall" == marks.name:
                        call = "无"
                content = {"dir": self.config.path, "base_url": self.__config.base_url, "url": url_path,
                           "method": method, "name": self.config.name,
                           "location": location, "call": call, "response": resp_obj.body, "curl": a.curl}
                write_excel(content, globalvar.get_value("toexcel"))

        return step_data

    def __run_step_testcase(self, step: TStep) -> StepData:
        """run teststep: referenced testcase"""
        step_data = StepData(name=step.name)
        step_variables = step.variables
        step_export = step.export

        # setup hooks
        if step.setup_hooks:
            self.__call_hooks(step.setup_hooks, step_variables, "setup testcase")

        if hasattr(step.testcase, "config") and hasattr(step.testcase, "teststeps"):
            testcase_cls = step.testcase
            case_result = (
                testcase_cls()
                    .with_session(self.__session)
                    .with_case_id(self.__case_id)
                    .with_variables(step_variables)
                    .with_export(step_export)
                    .run()
            )

        elif isinstance(step.testcase, Text):
            if os.path.isabs(step.testcase):
                ref_testcase_path = step.testcase
            else:
                ref_testcase_path = os.path.join(
                    self.__project_meta.RootDir, step.testcase
                )

            case_result = (
                HttpRunner()
                    .with_session(self.__session)
                    .with_case_id(self.__case_id)
                    .with_variables(step_variables)
                    .with_export(step_export)
                    .run_path(ref_testcase_path)
            )

        else:
            raise exceptions.ParamsError(
                f"Invalid teststep referenced testcase: {step.dict()}"
            )

        # teardown hooks
        if step.teardown_hooks:
            self.__call_hooks(step.teardown_hooks, step.variables, "teardown testcase")

        step_data.data = case_result.get_step_datas()  # list of step data
        step_data.export_vars = case_result.get_export_variables()
        step_data.success = case_result.success
        self.success = case_result.success

        if step_data.export_vars:
            logger.info(f"export variables: {step_data.export_vars}")

        return step_data

    def __run_step(self, step: TStep) -> Dict:
        """run teststep, teststep maybe a request or referenced testcase"""
        logger.info(f"run step begin: {step.name} >>>>>>")

        if step.request:
            step_data = self.__run_step_request(step)
        elif step.testcase:
            step_data = self.__run_step_testcase(step)
        else:
            raise ParamsError(
                f"teststep is neither a request nor a referenced testcase: {step.dict()}"
            )

        self.__step_datas.append(step_data)
        logger.info(f"run step end: {step.name} <<<<<<\n")
        return step_data.export_vars

    def __parse_config(self, config: TConfig) -> NoReturn:
        config.variables.update(self.__session_variables)
        config.variables.update(config.datasource)
        config.variables = parse_variables_mapping(
            config.variables, self.__project_meta.functions
        )
        config.name = parse_data(
            config.name, config.variables, self.__project_meta.functions
        )
        config.base_url = parse_data(
            config.base_url, config.variables, self.__project_meta.functions
        )

    def run_testcase(self, testcase: TestCase) -> "HttpRunner":
        """run specified testcase

        Examples:
            >>> testcase_obj = TestCase(config=TConfig(...), teststeps=[TStep(...)])
            >>> HttpRunner().with_project_meta(project_meta).run_testcase(testcase_obj)

        """
        self.__config = testcase.config
        self.__teststeps = testcase.teststeps

        # prepare
        self.__project_meta = self.__project_meta or load_project_meta(
            self.__config.path
        )
        self.__parse_config(self.__config)
        self.__start_at = time.time()
        self.__step_datas: List[StepData] = []
        self.__session = self.__session or HttpSession()
        # save extracted variables of teststeps
        extracted_variables: VariablesMapping = {}
        # extracted_variables=dict()
        # run teststeps
        for step in self.__teststeps:
            # override variables
            # step variables > extracted variables from previous steps
            step.variables = merge_variables(step.variables, extracted_variables)
            # step variables > testcase config variables
            step.variables = merge_variables(step.variables, self.__config.variables)
            step.variables = merge_variables(step.variables, self.__config.datasource)

            # parse variables
            step.variables = parse_variables_mapping(
                step.variables, self.__project_meta.functions
            )

            # run step
            if USE_ALLURE:
                with allure.step(f"step: {step.name}"):
                    extract_mapping = self.__run_step(step)
            else:
                extract_mapping = self.__run_step(step)

            # save extracted variables to session variables
            extracted_variables.update(extract_mapping)

        self.__session_variables.update(extracted_variables)
        self.__duration = time.time() - self.__start_at
        return self

    def run_path(self, path: Text) -> "HttpRunner":
        if not os.path.isfile(path):
            raise exceptions.ParamsError(f"Invalid testcase path: {path}")

        testcase_obj = load_testcase_file(path)
        return self.run_testcase(testcase_obj)

    def run(self) -> "HttpRunner":
        """ run current testcase

        Examples:
            >>> TestCaseRequestWithFunctions().run()

        """
        self.__init_tests__()
        testcase_obj = TestCase(config=self.__config, teststeps=self.__teststeps)
        return self.run_testcase(testcase_obj)

    def get_step_datas(self) -> List[StepData]:
        return self.__step_datas

    def get_export_variables(self) -> Dict:
        # override testcase export vars with step export
        export_var_names = self.__export or self.__config.export
        export_vars_mapping = {}
        for var_name in export_var_names:
            if var_name not in self.__session_variables:
                raise ParamsError(
                    f"failed to export variable {var_name} from session variables {self.__session_variables}"
                )

            export_vars_mapping[var_name] = self.__session_variables[var_name]

        return export_vars_mapping

    def get_summary(self) -> TestCaseSummary:
        """get testcase result summary"""
        start_at_timestamp = self.__start_at
        start_at_iso_format = datetime.datetime.fromtimestamp(start_at_timestamp).isoformat()
        return TestCaseSummary(
            name=self.__config.name,
            success=self.success,
            case_id=self.__case_id,
            time=TestCaseTime(
                start_at=self.__start_at,
                start_at_iso_format=start_at_iso_format,
                duration=self.__duration,
            ),
            in_out=TestCaseInOut(
                config_vars=self.__config.variables,
                export_vars=self.get_export_variables(),
            ),
            log=self.__log_path,
            step_datas=self.__step_datas,
        )

    def test_start(self, param: Dict = None) -> "HttpRunner":
        """main entrance, discovered by pytest"""
        self.__init_tests__()
        self.__project_meta = self.__project_meta or load_project_meta(
            self.__config.path
        )
        self.__case_id = self.__case_id or str(uuid.uuid4())
        self.__log_path = self.__log_path or os.path.join(
            self.__project_meta.RootDir, "logs", f"{self.__case_id}.run.log"
        )
        log_handler = logger.add(self.__log_path, level="DEBUG")

        # parse config name
        config_variables = self.__config.variables
        if param:
            config_variables.update(param)
        self.__session_variables = {}
        config_variables.update(self.__session_variables)
        config_variables = {}
        self.__config.name = parse_data(
            self.__config.name, config_variables, self.__project_meta.functions
        )
        if USE_ALLURE:
            # update allure report meta
            allure.dynamic.title(self.__config.name)
            if self.__teststeps[-1].request is not None:
                requestUrl = self.__teststeps[-1].request.url
                url = str(self.__config.base_url if self.__config.base_url[-1] != "/" else self.__config.base_url[
                                                                                           0:-2]) + str(
                    requestUrl)
                allure.dynamic.description(f"URL:{url}")

        logger.info(
            f"Start to run testcase: {self.__config.name}, TestCase ID: {self.__case_id}"
        )

        try:
            return self.run_testcase(
                TestCase(config=self.__config, teststeps=self.__teststeps)
            )
        finally:
            logger.remove(log_handler)
            logger.info(f"generate testcase log: {self.__log_path}")
