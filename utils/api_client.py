import requests


class APIClient:

    def get(self, url, **kwargs):
        return requests.get(url, **kwargs)

    def post(self, url, **kwargs):
        return requests.post(url, **kwargs)

    def put(self, url, **kwargs):
        return requests.put(url, **kwargs)

    def delete(self, url, **kwargs):
        return requests.delete(url, **kwargs)
