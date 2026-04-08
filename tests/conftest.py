import pytest
from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url=BASE_URL,
        extra_http_headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
    )
    yield request_context
    request_context.dispose()