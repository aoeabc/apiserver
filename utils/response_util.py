import json

from core.base_response import ResponceBase
from utils.log_util import logger


def process_response(response):
    if response.status_code in (200,201):
        ResponceBase.success=True
        logger.info("接口返回数据>>>{}".format(json.dumps(response.json(),indent=2,ensure_ascii=False)))
        ResponceBase.body=response.json()
    else:
        logger.info("接口请求失败")