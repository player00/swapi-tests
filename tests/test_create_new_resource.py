from utils.api_client import ApiClient


def test_create_new_resource(config):
    data = {
        'name': 'Tatooine',
        'climate': 'arid',
        'terrain': 'desert',
        'population': '200000',
    }
    req = ApiClient(config.base_url)
    new_data = req.create_new_resource('planets', data)
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
    req = ApiClient(config.base_url)
    new_data = req.create_new_resource('planets', data)
    assert new_data.status_code == 400


def test_create_new_resource_with_invalid_data_format(config):
    data = {
        'name': 'Test Planet',
        'climate': 'temperate',
        'terrain': 'mountains',
        'population': 200000,
    }
    req = ApiClient(config.base_url)
    new_data = req.create_new_resource('planets', data)
    assert new_data.status_code == 400
