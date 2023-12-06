import os

from utils.data_read import data_read
import pytest
from api.meike_api import meike_api
from utils.log_util import logger
from utils.mysql_util import db
# 项目路径

project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 测试用例数据文件路径
testcase_data_path = os.path.join(project_path, "data", "meikeapi.yaml")


@pytest.fixture(scope="function",autouse=True)
def api_log():
    logger.info("接口测试用例开始>>>")
    yield
    logger.info("接口测试用例完成>>>")

def clean_user_data(mobile):
    db.delete_data("delete from users_verifycode where mobile ={}".format(mobile))
    db.delete_data("delete from users_userprofile where mobile ={}".format(mobile))

def get_code(mobile):
    code = db.find_one("select code from users_verifycode where mobile ={} order by id desc".format(mobile))
    return code

@pytest.fixture()
def get_banners_num():
    sql="select count(1) from goods_banner "
    banners_num=db.find_data(sql)[0]
    return banners_num

@pytest.fixture(scope="session")
def get_token():
    token=meike_api.login(data_read.read_yaml(testcase_data_path)["test_token"])["token"]
    header = {"Authorization": "JWT " + token}
    return header




