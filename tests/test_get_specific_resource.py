import requests
import yaml

# Load the configuration file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

BASE_URL = config['base_url']


def test_get_specific_resource():
    response = requests.get(BASE_URL + 'people/1')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'Luke Skywalker'
    assert data['height'] == '172'
    assert data['mass'] == '77'
    assert data['hair_color'] == 'blond'
    assert data['skin_color'] == 'fair'
    assert data['eye_color'] == 'blue'
    assert data['birth_year'] == '19BBY'
    assert data['gender'] == 'male'
