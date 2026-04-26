import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app, init_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    init_db()
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_add(client):
    response = client.post('/add', data={
        "name": "Test",
        "age": "25",
        "weight": "70"
    }, follow_redirects=True)

    assert response.status_code == 200