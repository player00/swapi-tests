from utils.api_client import ApiClient


def test_search_for_resource(config):
    expected_name = 'Luke Skywalker'
    expected_height = '172'
    expected_mass = '77'
    expected_hair_color = 'blond'
    expected_skin_color = 'fair'
    expected_eye_color = 'blue'
    expected_birth_year = '19BBY'
    expected_gender = 'male'

    req = ApiClient(config.base_url)
    data = req.search_for_resource('people', 'Luke')

    assert len(data['results']) == 1

    asserted_data = data['results'][0]
    assert asserted_data['name'] == expected_name
    assert asserted_data['height'] == expected_height
    assert asserted_data['mass'] == expected_mass
    assert asserted_data['hair_color'] == expected_hair_color
    assert asserted_data['skin_color'] == expected_skin_color
    assert asserted_data['eye_color'] == expected_eye_color
    assert asserted_data['birth_year'] == expected_birth_year
    assert asserted_data['gender'] == expected_gender
