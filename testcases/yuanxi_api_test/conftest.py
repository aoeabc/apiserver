import os
from api.casedata_api import CasedataApi
import pytest
from utils.log_util import logger
from utils.casedata_yaml import yaml_data
from core.base_api import ApiClient

# 项目路径

project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 测试用例数据文件路径
testcase_data_path = os.path.join(project_path, "data", "meikeapi.yaml")


@pytest.fixture(scope="function", autouse=True)
def api_log():
    logger.info("接口测试用例开始>>>")
    yield
    logger.info("接口测试用例完成>>>")


@pytest.fixture(scope="module", autouse=True)
def get_session():
    host = yaml_data.data_ini()["host"]["api_sit_host_yuanxi"]
    seesions = CasedataApi(host)
    return seesions

