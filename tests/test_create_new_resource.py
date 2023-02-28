def test_create_new_resource(api_client):
    data = {
        'name': 'Tatooine',
        'climate': 'arid',
        'terrain': 'desert',
        'population': '200000',
    }
    new_data = api_client.create_new_resource('planets', data)
    assert new_data['name'] == 'Tatooine'
    assert new_data['climate'] == 'arid'
    assert new_data['terrain'] == 'desert'
    assert new_data['population'] == '200000'


def test_create_new_resource_with_missing_fields(api_client):
    data = {
        'name': 'Test Planet',
        'climate': 'temperate',
        'terrain': 'mountains',
    }
    new_data = api_client.create_new_resource('planets', data)
    assert new_data.status_code == 400


def test_create_new_resource_with_invalid_data_format(api_client):
    data = {
        'name': 'Test Planet',
        'climate': 'temperate',
        'terrain': 'mountains',
        'population': 200000,
    }
    new_data = api_client.create_new_resource('planets', data)
    assert new_data.status_code == 400
