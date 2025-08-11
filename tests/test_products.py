import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    catalogs = client.get("/catalogs/").json()
    assert catalogs, "No catalogs found — run test_create_catalog first."
    catalog_id = catalogs[0]["id"]

    response = client.post("/products/", json={
        "name": "Test Product",
        "price": 20,
        "quantity": 5,
        "catalog_id": catalog_id
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["catalog_id"] == catalog_id

def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(prod["name"] == "Test Product" for prod in data)
