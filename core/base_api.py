import json
from requests import request
from utils.log_util import logger
from utils.response_util import process_response


class ApiClient:
    def get(self, url, **kwargs):
        response = self.requests("get", url=url, **kwargs)
        return response

    def post(self, url, **kwargs):
        response = self.requests("post", url=url, **kwargs)
        return response

    def requests(self, method, url, **kwargs):
        self.request_log(method, url, **kwargs)
        response = request(method=method, url=url, **kwargs)
        process_response(response)
        return response

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
