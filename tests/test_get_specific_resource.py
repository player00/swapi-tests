import requests


def test_get_specific_resource(config):
    response = requests.get(config.base_url + 'people/1')
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
