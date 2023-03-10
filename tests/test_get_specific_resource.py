def test_get_specific_resource(api_client):
    data = api_client.get_resource_by_id('people', '1')
    assert data['name'] == 'Luke Skywalker'
    assert data['height'] == '172'
    assert data['mass'] == '77'
    assert data['hair_color'] == 'blond'
    assert data['skin_color'] == 'fair'
    assert data['eye_color'] == 'blue'
    assert data['birth_year'] == '19BBY'
    assert data['gender'] == 'male'
