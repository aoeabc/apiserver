import configparser
import os
# 项目路径
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# config.ini文件路径
config_path = os.path.join(project_path, "config", "config.ini")


def data_ini():
    config=configparser.ConfigParser()
    config.read(config_path,encoding="utf8")
    return config


if __name__ == '__main__':
    data=data_ini("D:/py_scripts/apiserver/config/config.ini")
    print(data["host"]["api_sit_host"])