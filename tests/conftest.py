import requests
import pytest

from configuration import TestSettings


@pytest.fixture(scope='session')
def config():
    return TestSettings()


@pytest.fixture(scope='function')
def planet(config):
    data = {
        'name': 'Test Planet',
        'climate': 'temperate',
        'terrain': 'mountains',
        'population': '100000',
    }
    response = requests.post(config.base_url + 'planets/', json=data)
    assert response.status_code == 201
    planet_data = response.json()
    yield planet_data
    response = requests.delete(config.base_url + f"planets/{planet_data['id']}/")
    assert response.status_code == 204
