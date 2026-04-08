import pytest
from playwright.sync_api import expect
from conftest import log_response

def test_get_all_posts(api_request_context):
    response = api_request_context.get("/posts")
    log_response(response, "test_get_all_posts - GET /posts")
    expect(response).to_be_ok()
    assert response.status == 200
    data = response.json()
    assert len(data) > 0
    assert "id" in data[0]


def test_get_single_post(api_request_context):
    response = api_request_context.get("/posts/1")
    log_response(response, "test_get_single_post - GET /posts")
    expect(response).to_be_ok()
    data = response.json()
    assert data["id"] == 1
    assert "title" in data


def test_create_post(api_request_context):
    payload = {
        "title": "my first testing post",
        "body": "this is my first post for testing",
        "userId": 1
    }
    response = api_request_context.post("/posts", data=payload)
    log_response(response, "test_create_post - POST /posts")
    expect(response).to_be_ok()
    assert response.status == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["userId"] == 1


def test_update_post(api_request_context):
    payload = {"title": "Updated Title", "body": "Updated Body", "userId": 1}
    response = api_request_context.put("/posts/1", data=payload)
    log_response(response, "test_update_post - PUT /posts")
    expect(response).to_be_ok()
    data = response.json()
    assert data["title"] == "Updated Title"


def test_delete_post(api_request_context):
    response = api_request_context.delete("/posts/1")
    log_response(response, "test_delete_post - DELETE /posts")
    expect(response).to_be_ok()
    assert response.status == 200