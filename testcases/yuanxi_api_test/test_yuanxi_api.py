import allure
import pytest
from utils.casedata_yaml import yaml_data


@allure.epic("远息项目接口")
class TestYuanxiApi:

    @pytest.mark.parametrize("data", yaml_data.read_yaml("yuanxi_testcase.yaml", "test_ipaddress"))
    def test_ipaddress(self, data, get_session):
        result = get_session.get_responce(data)