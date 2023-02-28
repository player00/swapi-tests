from utils.api_client import ApiClient


def test_api_is_up(config):
    req = ApiClient(config.base_url)
    req.ping()
