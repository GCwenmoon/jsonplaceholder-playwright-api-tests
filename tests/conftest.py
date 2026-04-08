import pytest
from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator
import datetime
import os

BASE_URL = "https://jsonplaceholder.typicode.com"

os.makedirs("traces", exist_ok=True)

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    trace_path = f"traces/trace_{timestamp}.zip"

    request_context = playwright.request.new_context(
        base_url=BASE_URL,
        extra_http_headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
    )
    request_context.tracing.start(
        name="jsonplaceholder_api_test",
        screenshots=True,      
        snapshots=True,        
        sources=True
    )

    yield request_context

    request_context.tracing.stop(path=trace_path)


    request_context.dispose()