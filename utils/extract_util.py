import os

from utils.casedata_yaml import yaml_data


class ExtractUtil:
    def __init__(self):
        self.yaml=yaml_data
        # 项目路径
        self.project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # extract文件地址：D:\py_scripts\apiserver\data\extract_data.yaml
        self.path = os.path.join(self.project_path, "data","extract_data.yaml")


    def get_extract_data(self,extract_data,response):
        if extract_data is not None:
            for key,expr in extract_data.items():
                data=self.yaml.get_jsonpath(response,expr)
                extract_data[key]=data
            get_yaml_data=self.yaml.read_data(self.path)
            if get_yaml_data is None:
                self.yaml.write_yaml(self.path,extract_data)
            else:
                for key,value in extract_data.items():
                    if key in get_yaml_data:
                        get_yaml_data[key]=extract_data[key]
                    else:
                        get_yaml_data.update({key:value})
                self.yaml.write_yaml(self.path, get_yaml_data)
        else:
            return

extract_util=ExtractUtil()