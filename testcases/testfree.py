import os
import pytest
import requests
from api.yuanxi_api import yuanxi_api
from utils.data_read import data_read

# 项目路径
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# host域名
yuanxi_api_sit_host = data_read.data_ini()["host"]["api_sit_host"]
# 测试用例数据文件路径
testcase_data_path = os.path.join(project_path, "config", "freeapi.yaml")


@pytest.mark.parametrize("data", data_read.read_yaml(testcase_data_path)["test_ipaddress"])
def test_ipaddress(data):
    response = yuanxi_api.ipadress(data)
    assert response["msg"] == '缓存查询成功'


@pytest.mark.parametrize("data", data_read.read_yaml(testcase_data_path)["test_nickname"])
def test_nickname(data):
    response = yuanxi_api.nickname(data)
    assert len(response["name"]) == data["num"]


def test_randomword():
    response = yuanxi_api.randomword()
    assert response["msg"] == '查询成功'
    assert len(response["duanju"]) > 0


@pytest.mark.parametrize("data", data_read.read_yaml(testcase_data_path)["test_translate"])
def test_translate(data):
    response = yuanxi_api.translate(data)
    assert response["msg"] == '查询成功'
    assert response["content"] != ""


if __name__ == '__main__':
    pytest.main()
