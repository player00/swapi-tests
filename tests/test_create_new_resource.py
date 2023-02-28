import requests


def test_create_new_resource(config):
    data = {
        'name': 'Tatooine',
        'climate': 'arid',
        'terrain': 'desert',
        'population': '200000',
    }
    response = requests.post(config.base_url + 'planets/', json=data)
    assert response.status_code == 201
    new_data = response.json()
    assert new_data['name'] == 'Tatooine'
    assert new_data['climate'] == 'arid'
    assert new_data['terrain'] == 'desert'
    assert new_data['population'] == '200000'


def test_create_new_resource_with_missing_fields(config):
    data = {
        'name': 'Test Planet',
        'climate': 'temperate',
        'terrain': 'mountains',
    }
    response = requests.post(config.base_url + 'planets/', json=data)
    assert response.status_code == 400


def test_create_new_resource_with_invalid_data_format(config):
    data = {
        'name': 'Test Planet',
        'climate': 'temperate',
        'terrain': 'mountains',
        'population': 200000,
    }
    response = requests.post(config.base_url + 'planets/', json=data)
    assert response.status_code == 400
