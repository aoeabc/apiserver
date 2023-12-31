import json
from requests import request
from core.base_response import ResponceBase
from utils.log_util import logger


class ApiClient:
    def get(self, url, **kwargs):
        response = self.api_client("get", url=url, **kwargs)
        return response

    def post(self, url, **kwargs):
        response = self.api_client("post", url=url, **kwargs)
        return response

    def api_client(self, method, url, **kwargs):
        self.request_log(method, url, **kwargs)
        response = request(method=method, url=url, **kwargs)
        self.process_response(response)
        return response

    def process_response(self,response):
        if response.status_code in (200, 201):
            ResponceBase.success = True
            ResponceBase.body = response.json()
        else:
            logger.info("接口请求失败")
        logger.info("接口返回数据>>>{}".format(json.dumps(response.json(), indent=2, ensure_ascii=False)))

    def request_log(self, method, url, **kwargs):
        logger.info("接口请求方法>>>{}".format(method))
        logger.info("接口请求地址>>>{}".format(url))
        if "data" in dict(**kwargs):
            logger.info("接口请求参数>>>\n{}".format(json.dumps(kwargs["data"],indent=2,ensure_ascii=False)))
        if "json" in dict(**kwargs):
            logger.info("接口请求参数>>>{}".format(json.dumps(kwargs["json"],indent=2,ensure_ascii=False)))
        if "params" in dict(**kwargs):
            logger.info("接口请求参数>>>\n{}".format(json.dumps(kwargs["params"],indent=2,ensure_ascii=False)))
        if "headers" in dict(**kwargs):
            logger.info("接口请求参数>>>{}".format(json.dumps(kwargs["headers"],indent=2,ensure_ascii=False)))
