import requests


def test_api_is_up(config):
    response = requests.get(config.base_url)
    assert response.status_code == 200
