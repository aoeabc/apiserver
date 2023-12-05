
import pytest

from utils.log_util import logger
from utils.mysql_util import db


@pytest.fixture(scope="function",autouse=True)
def api_log():
    logger.info("接口测试用例开始>>>")
    yield
    logger.info("接口测试用例完成>>>")

def clean_data(mobile):
    db.delete_data("delete from users_verifycode where mobile ={}".format(mobile))
    db.delete_data("delete from users_userprofile where mobile ={}".format(mobile))

def get_code(mobile):
    code = db.find_one("select code from users_verifycode where mobile ={} order by id desc".format(mobile))[0]
    return code




