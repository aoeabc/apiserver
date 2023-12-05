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

    def get_code(self,mobile):
        response = self.post(url=self.meike_api_sit_host + "/code/", data=mobile)
        return response.json()

    def register(self,data):
        json_data={"code":data["code"],"password":data["password"],"username":str(data["username"])}
        response = self.post(url=self.meike_api_sit_host + "/users/", data=json_data)
        return response.json()

meike_api = ApiMeike()