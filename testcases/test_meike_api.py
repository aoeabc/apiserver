import os
import allure
import pytest
from api.meike_api import meike_api
from testcases.conftest import clean_user_data, get_code
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
        clean_user_data(mobile)
        meike_api.get_code(data_read.read_yaml(testcase_data_path)["test_code"])
        code = get_code(mobile)
        json_data = data["paramas"]
        json_data["code"] = code
        response = meike_api.register(json_data)
        if str(json_data["mobile"]) == "13488010001":
            assert response["username"] == str(mobile)
        else:
            assert '请先获取验证码' in response["code"]

    @allure.story("账号登录")
    @pytest.mark.parametrize("data", data_read.read_yaml(testcase_data_path)["test_login"])
    def test_login(self, data):
        allure.dynamic.title(data["title"])
        response = meike_api.login(data["paramas"])
        print(response)

    @allure.story("获取首页轮播数据")
    def test_banners(self,get_banners_num):
        allure.dynamic.title("获取首页轮播数据")
        response = meike_api.banners()
        assert len(response) == get_banners_num

    @allure.story("加入购物车")
    @pytest.mark.parametrize("data", data_read.read_yaml(testcase_data_path)["test_shopcarts"])
    def test_add_shopcarts(self,data,get_token):
        allure.dynamic.title(data["title"])
        response = meike_api.add_shopcarts(data["paramas"],get_token)
        assert len(response) > 0

    @allure.story("查询购物车")
    def test_get_shopcarts(self,get_token):
        allure.dynamic.title("查询购物车")
        response = meike_api.get_shopcarts(get_token)
        assert len(response) > 0

if __name__ == '__main__':
    pytest.main()