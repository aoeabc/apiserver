import os
from utils.data_read import data_read
from core.base_api import ApiClient

# 项目路径
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# host域名
yuanxi_api_sit_host = data_read.data_ini()["host"]["api_sit_host"]


class ApiYuanxi(ApiClient):
    def __init__(self):
        self.yuanxi_api_sit_host = yuanxi_api_sit_host

    def ipadress(self, data):
        """
        :param data: ip地址
        :return:
        """
        response = self.post(url=self.yuanxi_api_sit_host + "/api/iplocation/", data=data)
        return response.json()

    def nickname(self,data):
        response = self.post(url=self.yuanxi_api_sit_host + "/api/wangming/", data=data)
        return response.json()

    def randomword(self):
        response = self.get(url=self.yuanxi_api_sit_host + "/api/Aword/")
        return response.json()

    def translate(self,data):
        response = self.get(url=self.yuanxi_api_sit_host + "/api/translation/",params=data)
        return response.json()


yuanxi_api=ApiYuanxi()

