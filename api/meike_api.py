import os
from utils.data_read import data_read
from core.base_api import ApiClient

# 项目路径
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# host域名
meike_api_sit_host = data_read.data_ini()["host"]["api_sit_host_meike"]


class ApiMeike(ApiClient):
    def __init__(self):
        self.meike_api_sit_host = meike_api_sit_host

    def get_code(self, mobile):
        response = self.post(url=self.meike_api_sit_host + "/code/", data=mobile)
        return response.json()

    def register(self, data):
        json_data = {"code": data["code"], "password": data["password"], "username": str(data["username"])}
        response = self.post(url=self.meike_api_sit_host + "/users/", data=json_data)
        return response.json()

    def login(self, data):
        json_data = {"password": data["password"], "username": str(data["username"])}
        response = self.post(url=self.meike_api_sit_host + "/login/", data=json_data)
        return response.json()

    def banners(self):
        response = self.get(url=self.meike_api_sit_host + "/banners/")
        return response.json()

    def get_shopcarts(self, header):
        response = self.get(url=self.meike_api_sit_host + "/shopcarts/", headers=header)
        return response.json()

    def add_shopcarts(self, data,header):
        response = self.post(url=self.meike_api_sit_host + "/shopcarts/", headers=header,data=data)
        return response.json()


meike_api = ApiMeike()
