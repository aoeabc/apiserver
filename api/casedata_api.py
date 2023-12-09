import allure
from core.base_api import ApiClient
from utils.assert_util import assert_check
from utils.casedata_yaml import yaml_data
from utils.extract_util import extract_util


class CasedataApi(ApiClient):
    def __init__(self, host):
        self.host = host

    def get_responce(self, data, header=None):
        data=yaml_data.trans_data(data)
        request_info = data["request_info"]
        url = request_info["url"]
        allure.dynamic.story(request_info["title"])
        method = request_info["method"]
        case_info = data["case_info"]
        assert_data = case_info.pop("assert_data", None)
        extract_data = case_info.pop("extract", None)
        response = self.api_client(method=method, url=self.host + url,headers=header, **case_info).json()
        extract_util.get_extract_data(extract_data,response)
        assert_check.assert_check(data=assert_data, respon=response)
        return response

if __name__ == '__main__':
    host=yaml_data.data_ini()["host"]["api_sit_host_meike"]
    seesion = CasedataApi(host)
