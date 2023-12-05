import os
import allure
import pytest
from api.meike_api import meike_api
from testcases.conftest import clean_data, get_code
from utils.data_read import data_read
from utils.mysql_util import db

# 项目路径

project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 测试用例数据文件路径
testcase_data_path = os.path.join(project_path, "data", "meikeapi.yaml")


@allure.epic("美客项目接口")
@allure.feature("个人信息模块")
class TestYanxi:
    @allure.story("注册账号")
    @pytest.mark.parametrize("data", data_read.read_yaml(testcase_data_path)["test_register"])
    def test_register(self, data):
        allure.dynamic.title(data["title"])
        mobile = data_read.read_yaml(testcase_data_path)["test_code"]["mobile"]
        clean_data(mobile)
        meike_api.get_code(data_read.read_yaml(testcase_data_path)["test_code"])
        code = get_code(mobile)
        json_data = data["paramas"]
        json_data["code"] = code
        response = meike_api.register(json_data)
        if str(json_data["mobile"]) == "13488010001":
            assert response["username"] == str(mobile)
        else:
            assert '请先获取验证码' in response["code"]
