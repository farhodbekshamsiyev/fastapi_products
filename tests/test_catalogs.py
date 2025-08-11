import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_catalog():
    response = client.post("/catalogs/", json={"name": "Test Catalogs"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Catalogs"
    assert "id" in data

def test_get_catalogs():
    response = client.get("/catalogs/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(cat["name"] == "Test Catalogs" for cat in data)
