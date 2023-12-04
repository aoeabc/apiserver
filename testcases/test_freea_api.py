import os

import allure
import pytest
from api.yuanxi_api import yuanxi_api
from utils.data_read import data_read

# 项目路径
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# host域名
yuanxi_api_sit_host = data_read.data_ini()["host"]["api_sit_host"]
# 测试用例数据文件路径
testcase_data_path = os.path.join(project_path, "config", "freeapi.yaml")

@allure.epic("远息项目接口")
@allure.feature("随机挑选的接口")
class TestYanxi:
    @allure.story("查询用户ip地址")
    @pytest.mark.parametrize("data", data_read.read_yaml(testcase_data_path)["test_ipaddress"])
    def test_ipaddress(self,data):
        response = yuanxi_api.ipadress(data)
        assert '查询成功' in response["msg"]

    @allure.story("取随机网名")
    @pytest.mark.parametrize("data", data_read.read_yaml(testcase_data_path)["test_nickname"])
    def test_nickname(self,data):
        response = yuanxi_api.nickname(data)
        assert len(response["name"]) == data["num"]

    @allure.story("生成一句话")
    def test_randomword(self):
        response = yuanxi_api.randomword()
        assert response["msg"] == '查询成功'
        assert len(response["duanju"]) > 0

    @allure.story("翻译内容")
    @pytest.mark.parametrize("data", data_read.read_yaml(testcase_data_path)["test_translate"])
    def test_translate(self,data):
        response = yuanxi_api.translate(data)
        assert response["msg"] == '查询成功'
        assert response["content"] != ""


if __name__ == '__main__':
    pytest.main()
