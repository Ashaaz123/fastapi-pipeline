from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_about():
    response = client.get("/about")
    assert response.status_code == 200

def test_contact():
    response = client.get("/contact")
    assert response.status_code == 200