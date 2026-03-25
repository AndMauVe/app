from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_ping_status_code_200():
    response = client.get("/ping")
    assert response.status_code == 200

def test_ping_respuesta_json():
    response = client.get("/ping")
    assert response.json() == {"message": "pong"}
