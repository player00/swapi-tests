import requests
import pytest
import yaml

# Load the configuration file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

BASE_URL = config['base_url']


@pytest.fixture(scope='function')
def planet():
    data = {
        'name': 'Test Planet',
        'climate': 'temperate',
        'terrain': 'mountains',
        'population': '100000',
    }
    response = requests.post(BASE_URL + 'planets/', json=data)
    assert response.status_code == 201
    planet_data = response.json()
    yield planet_data
    response = requests.delete(BASE_URL + f"planets/{planet_data['id']}/")
    assert response.status_code == 204
