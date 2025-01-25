import json
from app import app, db
from app.models import Project

def test_add_project():
    client = app.test_client()
    response = client.post('/projects', json={'name': 'Project 1', 'description': 'A test project', 'status': 'active'})
    assert response.status_code == 201
    assert b'Project added' in response.data

def test_get_projects():
    client = app.test_client()
    response = client.get('/projects')
    assert response.status_code == 200
    assert len(json.loads(response.data)) > 0
