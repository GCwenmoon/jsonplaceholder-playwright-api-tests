import pytest
from playwright.sync_api import expect


def test_get_all_users(api_request_context):
    response = api_request_context.get("/users")
    expect(response).to_be_ok()
    data = response.json()
    assert len(data) >= 5
    assert "name" in data[0]
    assert "email" in data[0]


def test_get_single_user(api_request_context):
    response = api_request_context.get("/users/1")
    expect(response).to_be_ok()
    data = response.json()
    assert data["id"] == 1
    assert "@" in data["email"]