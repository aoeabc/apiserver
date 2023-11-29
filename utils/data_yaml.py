import yaml


class yamlUtil:
    def read_yaml(self, path):
        with open(path, "r" ,encoding="utf-8") as f:
            return yaml.safe_load(f)

    def write_yaml(self, path, data):
        with open(path, "r") as f:
            yaml.safe_dump(data, f, allow_unicode="Ture")


yaml_data = yamlUtil()

if __name__ == '__main__':
    data=yaml_data.read_yaml("D:/py_scripts/apiservers/apiserver/config/freeapi.yaml")["test_ipaddress"]
    print(data)