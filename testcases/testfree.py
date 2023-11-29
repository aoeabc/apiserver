import pytest
import requests
from utils.data_yaml import yaml_data

path="D:/py_scripts/apiserver/config/freeapi.yaml"
@pytest.mark.parametrize("ip",yaml_data.read_yaml(path)["test_ipaddress"])
def test_ipaddress(ip):
    url = "https://www.yuanxiapi.cn/api/iplocation/"
    res=requests.post(url=url,data=ip)
    print(res.json())

@pytest.mark.parametrize("data",yaml_data.read_yaml(path)["test_nickname"])
def test_nickname(data):
    url = "https://www.yuanxiapi.cn/api/wangming/"
    name=requests.post(url=url, data=data)
    print(name.text)


def test_randomword():
    url = "https://www.yuanxiapi.cn/api/Aword/"
    data = requests.get(url=url)
    print(data.json())

@pytest.mark.parametrize("data",yaml_data.read_yaml(path)["test_translate"])
def test_translate(data):
    url = "https://www.yuanxiapi.cn/api/translation/"
    data = requests.get(url=url, params=data)
    print(data.json())


if __name__ == '__main__':
    pytest.main()
