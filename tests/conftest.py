import pytest

from configuration import TestSettings
from utils.api_client import ApiClient


@pytest.fixture(scope='session')
def config():
    return TestSettings()


@pytest.fixture(scope='session')
def api_client(config):
    return ApiClient(config.base_url)


@pytest.fixture(scope='function')
def planet(api_client):
    data = {
        'name': 'Test Planet',
        'climate': 'temperate',
        'terrain': 'mountains',
        'population': '100000',
    }
    planet_data = api_client.create_new_resource('planets', data)
    yield planet_data
    api_client.delete_existing_resource('planets', planet_data['id'])
