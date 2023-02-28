import requests


class ApiClient():
    def __init__(self, base_url):
        self.base_url = base_url

    def ping(self):
        response = requests.get(self.base_url)
        response.raise_for_status()
        return response.json()

    def get_resource_by_id(self, resource, id):
        response = requests.get(self.base_url + f"{resource}/{id}/")
        response.raise_for_status()
        return response.json()

    def search_for_resource(self, resource, data):
        response = requests.get(self.base_url + f"{resource}/?search={data}")
        response.raise_for_status()
        return response.json()

    def create_new_resource(self, resource, data):
        response = requests.post(self.base_url + f"{resource}/{data}")
        response.raise_for_status()
        return response.json()

    def update_existing_resource(self, resource, id, data):
        response = requests.put(self.base_url + f"{resource}/{id}/", data=data)
        response.raise_for_status()
        return response.json()
