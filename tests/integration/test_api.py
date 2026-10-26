"""Integration tests for the FastAPI calculator endpoints."""

import pytest
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


@pytest.mark.parametrize(
    "endpoint,a,b,expected",
    [
        ("/add", 2, 3, 5),
        ("/subtract", 8, 3, 5),
        ("/multiply", 4, 3, 12),
        ("/divide", 10, 2, 5),
    ],
)
def test_calculation_endpoints(endpoint, a, b, expected):
    response = client.post(endpoint, json={"a": a, "b": b})

    assert response.status_code == 200
    assert response.json() == {"result": expected}


def test_divide_endpoint_returns_helpful_error_for_zero():
    response = client.post("/divide", json={"a": 10, "b": 0})

    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero."}


def test_calculator_page_loads():
    response = client.get("/")

    assert response.status_code == 200
    assert "FastAPI Calculator" in response.text
    assert 'id="add"' in response.text


def test_endpoint_rejects_missing_number():
    response = client.post("/add", json={"a": 2})

    assert response.status_code == 422