import requests


def test_update_existing_resource(config, planet):
    data = {
        'name': 'Updated Test Planet',
        'climate': 'tropical',
        'terrain': 'beaches',
        'population': '500000',
    }
    response = requests.put(
        config.base_url + f"planets/{planet['id']}/", data=data)
    assert response.status_code == 200
    updated_data = response.json()
    assert updated_data['name'] == 'Updated Test Planet'
    assert updated_data['climate'] == 'tropical'
    assert updated_data['terrain'] == 'beaches'
    assert updated_data['population'] == '500000'
