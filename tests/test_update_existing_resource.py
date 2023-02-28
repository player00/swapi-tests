import requests
import yaml
from conftest import planet

# Load the configuration file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

BASE_URL = config['base_url']


def test_update_existing_resource(planet):
    data = {
        'name': 'Updated Test Planet',
        'climate': 'tropical',
        'terrain': 'beaches',
        'population': '500000',
    }
    response = requests.put(BASE_URL + f"planets/{planet['id']}/", data=data)
    assert response.status_code == 200
    updated_data = response.json()
    assert updated_data['name'] == 'Updated Test Planet'
    assert updated_data['climate'] == 'tropical'
    assert updated_data['terrain'] == 'beaches'
    assert updated_data['population'] == '500000'
