import requests


class ApiClient():
    def __init__(self, base_url: str):
        self.base_url = base_url

    def ping(self):
        response = requests.get(self.base_url)
        response.raise_for_status()
        return response.json()

    def get_resource_by_id(self, resource: str, id: str):
        response = requests.get(self.base_url + f"{resource}/{id}/")
        response.raise_for_status()
        return response.json()

    def search_for_resource(self, resource: str, data: dict):
        response = requests.get(self.base_url + f"{resource}/?search={data}")
        response.raise_for_status()
        return response.json()

    def create_new_resource(self, resource: str, data: dict):
        response = requests.post(self.base_url + f"{resource}/{data}")
        response.raise_for_status()
        return response.json()

    def update_existing_resource(self, resource: str, id: str, data: dict):
        response = requests.put(self.base_url + f"{resource}/{id}/", data=data)
        response.raise_for_status()
        return response.json()

    def delete_existing_resource(self, resource, id):
        response = requests.delete(self.base_url + f"{resource}/{id}/")
        response.raise_for_status()
        return response.json()
