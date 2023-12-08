import allure
import pytest
from utils.casedata_yaml import yaml_data


@allure.epic("美客项目接口")
class TestMeikeApi:

    @pytest.mark.parametrize("data", yaml_data.read_yaml("meike_testcase.yaml", "test_login"))
    def test_login(self, data, get_session):
        result = get_session.get_responce(data)

    @pytest.mark.parametrize("data", yaml_data.read_yaml("meike_testcase.yaml", "test_banners"))
    def test_banner(self, data, get_session):
        result = get_session.get_responce(data)

    @pytest.mark.parametrize("data", yaml_data.read_yaml("meike_testcase.yaml", "test_shopcarts"))
    def test_shopcarts(self, data, get_session,get_token):
        result = get_session.get_responce(data,get_token)