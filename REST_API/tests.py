import pytest
from app import app, users, next_id

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_users(client):
    global users
    users.clear()
    response = client.get('/users')
    assert response.status_code == 200
    assert response.get_json() == []

def test_create_user(client):
    global users, next_id
    users.clear()
    next_id = 1
    response = client.post('/users', json={"name": "Szymon", "lastname": "Kalinowski"})
    assert response.status_code == 201
    assert len(users) == 1
    assert users[1] == {"id": 1, "name": "Szymon", "lastname": "Kalinowski"}

def test_get_user(client):
    global users
    users[1] = {"id": 1, "name": "Szymon", "lastname": "Kalinowski"}
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.get_json() == {"id": 1, "name": "Szymon", "lastname": "Kalinowski"}
