import json
import os

import jsonpath
import yaml
import configparser

from utils.init_data import InitData


class yamlUtil(InitData):
    def __init__(self):
        # 项目路径
        self.project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 测试用例数据文件路径
        self.testcase_data_path = os.path.join(self.project_path, "data")
        #配置文件地址
        self.config_path = os.path.join(self.project_path, "config", "config.ini")
        self.path = os.path.join(self.project_path, "data","extract_data.yaml")

    def read_yaml(self, path, keyname=None):
        result=self.read_data(path)
        if keyname is not None:
             return self.change_data(result[keyname])
        else:
            return result

    def read_data(self,path):
        path = os.path.join(self.testcase_data_path, path)
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data

    def write_yaml(self, path, data):
        with open(path, mode="w") as f:
            yaml.safe_dump(data, f, allow_unicode=True,sort_keys=False)



    def data_ini(self):
        config = configparser.ConfigParser()
        config.read(self.config_path, encoding="utf8")
        return config

    def change_data(self,data):
        if "request_info" in str(data):
            result=[]
            for api_case in data:
                for case_info in api_case["case_info"]:
                    result.append({"request_info":api_case["request_info"],"case_info":case_info})
            return result
        else:
            return data

    def get_jsonpath(self, data, jsonpath_data):
        result = jsonpath.jsonpath(data, jsonpath_data)
        if len(result) == 0:
            return
        elif len(result) == 1:
            return result[0]
        else:
            return result

    def init_data(self, data):
        func_name = yaml_data.read_data(self.path)
        if func_name != "":
            if data in func_name:
                result = str(func_name[data][0])
                return result
            elif "random" in data:
                return str(eval("self." + data))
            else:
                return data

    def trans_data(self, data):
        """
        处理${}中，自定义的方法
        :param data:
        :return:
        """
        str_data = json.dumps(data)
        for i in range(str_data.count("${")):
            index_start = str_data.find("${")
            index_end = str_data.find("}",index_start,-1)
            if index_start >= 0:
                func_name = str_data[index_start + 2:index_end]
                str_data = str_data.replace('${' + func_name + '}', self.init_data(func_name), 1)
        return json.loads(str_data)

yaml_data = yamlUtil()

if __name__ == '__main__':
    # data=yaml_data.read_yaml("meike_testcase.yaml","test_login")
    # print(data)
    # data = yaml_data.read_data("D:/py_scripts/apiserver/data/extract_data.yaml")
    # print(data)
    # data = yaml_data.read_yaml("D:/py_scripts/apiserver/config/freeapi.yaml")["test_nickname1"]
    # print(data)
    data=yaml_data.init_data("id")
    print(data)
