import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, CI/CD World!" in response.data

def test_version(client):
    response = client.get('/version')
    assert response.status_code == 200
    assert b"Version 1.0" in response.data