import pytest
from app import app, db
from app.models import User
from flask_login import login_user

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.create_all()
    yield app.test_client()
    db.drop_all()

def test_register(client):
    response = client.post('/register', data=dict(username='testuser', email='test@test.com', password='password'), follow_redirects=True)
    assert b'Login' in response.data

def test_login(client):
    user = User(username='testuser', email='test@test.com', password='hashedpassword')
    db.session.add(user)
    db.session.commit()
    response = client.post('/login', data=dict(email='test@test.com', password='password'), follow_redirects=True)
    assert b'Dashboard' in response.data
