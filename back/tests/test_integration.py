import pytest
from app import create_app, db
from app.models import Library
from io import BytesIO

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_add_library(client):
    response = client.post('/v1/api/library', json={'name': 'Test Library', 'data': 'Test Data'})
    assert response.status_code == 201
    assert response.json['name'] == 'Test Library'
    assert response.json['data'] == 'Test Data'

def test_get_libraries(client):
    client.post('/v1/api/library', json={'name': 'Library 1', 'data': 'Data 1'})
    client.post('/v1/api/library', json={'name': 'Library 2', 'data': 'Data 2'})
    response = client.get('/v1/api/library')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_delete_library(client):
    response = client.post('/v1/api/library', json={'name': 'Library to Delete', 'data': 'Data'})
    library_id = response.json['id']
    response = client.delete(f'/v1/api/library/{library_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Library deleted'

def test_update_library(client):
    response = client.post('/v1/api/library', json={'name': 'Library to Update', 'data': 'Old Data'})
    library_id = response.json['id']
    response = client.put(f'/v1/api/library/{library_id}', json={'name': 'Updated Library', 'data': 'New Data'})
    assert response.status_code == 200
    assert response.json['name'] == 'Updated Library'
    assert response.json['data'] == 'New Data'

def test_add_distillery(client):
    response = client.post('/v1/api/distilleries', json={'name': 'Test Distillery', 'country_id': '1'})
    print(response.json)
    assert response.status_code == 201

def test_get_distilleries(client):
    client.post('/v1/api/distilleries', json={'name': 'Distillery 1', 'country_id': '1'})
    client.post('/v1/api/distilleries', json={'name': 'Distillery 2', 'country_id': '1'})
    response = client.get('/v1/api/distilleries')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_distillery(client):
    response = client.post('/v1/api/distilleries', json={'name': 'Distillery to Get', 'country_id': '1'})
    distillery_id = response.json['id']
    response = client.get(f'/v1/api/distilleries/{distillery_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Distillery to Get'

def test_update_distillery(client):
    response1 = client.post('/v1/api/distilleries', json={'name': 'Distillery to Update', 'country_id': '1'})
    distillery_id = response1.json['id']
    print(response1)
    response = client.put(f'/v1/api/distilleries/{distillery_id}', json={'name': 'Updated Distillery', 'country_id': '2'})
    print(response)
    assert response.status_code == 200
    assert response.json['name'] == 'Updated Distillery'
    assert response.json['country_id'] == '2'

def test_delete_distillery(client):
    response = client.post('/v1/api/distilleries', json={'name': 'Distillery to Delete', 'country_id': '1'})
    distillery_id = response.json['id']
    response = client.delete(f'/v1/api/distilleries/{distillery_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Distillery deleted'

def test_add_negociant(client):
    response = client.post('/v1/api/negociants', json={'name': 'Test Negociant', 'country_id': '1'})
    assert response.status_code == 201
    assert response.json['name'] == 'Test Negociant'
    assert response.json['country_id'] == '1'

def test_get_negociants(client):
    client.post('/v1/api/negociants', json={'name': 'Negociant 1', 'country_id': '1'})
    client.post('/v1/api/negociants', json={'name': 'Negociant 2', 'country_id': '1'})
    response = client.get('/v1/api/negociants')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_negociant(client):
    response = client.post('/v1/api/negociants', json={'name': 'Negociant to Get', 'country_id': '1'})
    negociant_id = response.json['id']
    response = client.get(f'/v1/api/negociants/{negociant_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Negociant to Get'

def test_update_negociant(client):
    response = client.post('/v1/api/negociants', json={'name': 'Negociant to Update', 'country_id': '1'})
    negociant_id = response.json['id']
    response = client.put(f'/v1/api/negociants/{negociant_id}', json={'name': 'Updated Negociant', 'country_id': '2'})
    assert response.status_code == 200
    assert response.json['name'] == 'Updated Negociant'
    assert response.json['country_id'] == '2'

def test_delete_negociant(client):
    response = client.post('/v1/api/negociants', json={'name': 'Negociant to Delete', 'country_id': '1'})
    negociant_id = response.json['id']
    response = client.delete(f'/v1/api/negociants/{negociant_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Negociant deleted'

def test_add_whisky(client):
    response = client.post('/v1/api/whiskies', json={'name': 'Test Whisky', 'distillery_id': '1', 'alcohol_percentage': 40.0, 'whisky_type_id': '1', 'bottle_size_cl': 70, 'price': 50.0, 'is_peated': False})
    assert response.status_code == 201
    assert response.json['name'] == 'Test Whisky'
    assert response.json['alcohol_percentage'] == 40.0

def test_get_whiskies(client):
    client.post('/v1/api/whiskies', json={'name': 'Whisky 1', 'distillery_id': '1', 'alcohol_percentage': 40.0, 'whisky_type_id': '1', 'bottle_size_cl': 70, 'price': 50.0, 'is_peated': False})
    client.post('/v1/api/whiskies', json={'name': 'Whisky 2', 'distillery_id': '1', 'alcohol_percentage': 45.0, 'whisky_type_id': '1', 'bottle_size_cl': 70, 'price': 60.0, 'is_peated': True})
    response = client.get('/v1/api/whiskies')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_whisky(client):
    response = client.post('/v1/api/whiskies', json={'name': 'Whisky to Get', 'distillery_id': '1', 'alcohol_percentage': 40.0, 'whisky_type_id': '1', 'bottle_size_cl': 70, 'price': 50.0, 'is_peated': False})
    whisky_id = response.json['id']
    response = client.get(f'/v1/api/whiskies/{whisky_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Whisky to Get'

def test_update_whisky(client):
    response = client.post('/v1/api/whiskies', json={'name': 'Whisky to Update', 'distillery_id': '1', 'alcohol_percentage': 40.0, 'whisky_type_id': '1', 'bottle_size_cl': 70, 'price': 50.0, 'is_peated': False})
    whisky_id = response.json['id']
    response = client.put(f'/v1/api/whiskies/{whisky_id}', json={'name': 'Updated Whisky', 'alcohol_percentage': 45.0})
    assert response.status_code == 200
    assert response.json['name'] == 'Updated Whisky'
    assert response.json['alcohol_percentage'] == 45.0

def test_delete_whisky(client):
    response = client.post('/v1/api/whiskies', json={'name': 'Whisky to Delete', 'distillery_id': '1', 'alcohol_percentage': 40.0, 'whisky_type_id': '1', 'bottle_size_cl': 70, 'price': 50.0, 'is_peated': False})
    whisky_id = response.json['id']
    response = client.delete(f'/v1/api/whiskies/{whisky_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Whisky deleted'

def test_add_tasting(client):
    response = client.post('/v1/api/tastings', json={'whisky_id': '1', 'rating': 90, 'tasting_date': '2023-10-10T00:00:00.000Z'})
    assert response.status_code == 201
    assert response.json['rating'] == 90

def test_get_tastings(client):
    client.post('/v1/api/tastings', json={'whisky_id': '1', 'rating': 90, 'tasting_date': '2023-10-10T00:00:00.000Z'})
    client.post('/v1/api/tastings', json={'whisky_id': '1', 'rating': 85, 'tasting_date': '2023-10-11T00:00:00.000Z'})
    response = client.get('/v1/api/tastings')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_tasting(client):
    response = client.post('/v1/api/tastings', json={'whisky_id': '1', 'rating': 90, 'tasting_date': '2023-10-10T00:00:00.000Z'})
    tasting_id = response.json['id']
    response = client.get(f'/v1/api/tastings/{tasting_id}')
    assert response.status_code == 200
    assert response.json['rating'] == 90

def test_update_tasting(client):
    response = client.post('/v1/api/tastings', json={'whisky_id': '1', 'rating': 90, 'tasting_date': '2023-10-10T00:00:00.000Z'})
    tasting_id = response.json['id']
    response = client.put(f'/v1/api/tastings/{tasting_id}', json={'rating': 95})
    assert response.status_code == 200
    assert response.json['rating'] == 95

def test_delete_tasting(client):
    response = client.post('/v1/api/tastings', json={'whisky_id': '1', 'rating': 90, 'tasting_date': '2023-10-10T00:00:00.000Z'})
    tasting_id = response.json['id']
    response = client.delete(f'/v1/api/tastings/{tasting_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Tasting deleted'
