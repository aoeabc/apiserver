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
        excp = json.dumps(data)
        for i in range(excp.count("$")):
            index_start = excp.find("$")
            index_end = excp.find(")}")
            if index_start >= 0:
                func_name = excp[index_start + 2:index_end+1]
                excp = excp.replace('${' + func_name + '}', eval(func_name),1)
        return json.loads(excp)

    def get_data(self):
        for i in range(3):
            print(random_word())


def random_word():
    fk = Faker(["zh_CN"])
    random_name = fk.word(ext_word_list=None)
    return random_name


yaml_data = yamlUtil()

if __name__ == '__main__':
    yaml_data.get_data()
        # data = yaml_data.read_yaml("D:/py_scripts/apiserver/config/freeapi.yaml")["test_nickname1"]
    # print(data)
