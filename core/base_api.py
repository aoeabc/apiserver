import requests


class ApiClient:
    def get(self, url, **kwargs):
        response = requests.get(url=url, **kwargs)
        return response

    def post(self, url, **kwargs):
        response = requests.post(url=url, **kwargs)
        return response
