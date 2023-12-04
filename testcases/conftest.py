import os
import pytest
from utils.log_util import logger

@pytest.fixture(scope="function",autouse=True)
def api_log():
    logger.info("接口测试用例开始>>>")
    yield
    logger.info("接口测试用例完成>>>")


