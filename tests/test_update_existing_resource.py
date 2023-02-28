def test_update_existing_resource(api_client, planet):
    data = {
        'name': 'Updated Test Planet',
        'climate': 'tropical',
        'terrain': 'beaches',
        'population': '500000',
    }
    updated_data = api_client.create_new_resource(
        'planets', planet['id'], data)
    assert updated_data['name'] == 'Updated Test Planet'
    assert updated_data['climate'] == 'tropical'
    assert updated_data['terrain'] == 'beaches'
    assert updated_data['population'] == '500000'
