import json

import yaml
from faker import Faker


class yamlUtil:
    def read_yaml(self, path):
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return self.trans_data(data)

    def write_yaml(self, path, data):
        with open(path, "r") as f:
            yaml.safe_dump(data, f, allow_unicode="Ture")

    def trans_data(self, data):
        str_data = json.dumps(data)
        for i in range(str_data.count("$")):
            index_start = str_data.find("$")
            index_end = str_data.find(")}")
            if index_start >= 0:
                func_name = str_data[index_start + 2:index_end+1]
                str_data = str_data.replace('${' + func_name + '}', eval(func_name),1)
        return json.loads(str_data)


def random_word():
    fk = Faker(["zh_CN"])
    random_name = fk.word(ext_word_list=None)
    return random_name


yaml_data = yamlUtil()

if __name__ == '__main__':
    yaml_data.trans_data()
        # data = yaml_data.read_yaml("D:/py_scripts/apiserver/config/freeapi.yaml")["test_nickname1"]
    # print(data)
