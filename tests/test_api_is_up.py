import requests
import yaml

# Load the configuration file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

BASE_URL = config['base_url']


def test_api_is_up():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
