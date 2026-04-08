import pytest
from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator
import logging
import os
import datetime
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[
        logging.FileHandler(f"logs/test_run_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log", encoding='utf-8'),
        logging.StreamHandler()  
    ]
)

logger = logging.getLogger("api_test")

def log_response(response, step_name):
    logger.info(f"[{step_name}] URL: {response.url}")
    logger.info(f"[{step_name}] Status: {response.status} {response.status_text or ''}")

    try:
        body = response.json()
        logger.info(f"[{step_name}] Response Body: {json.dumps(body, ensure_ascii=False, indent=2)}")

    except Exception:
        try:
            text = response.text()
            logger.info(f"[{step_name}] Response Text: {text[:500]}{'...' if len(text) > 500 else ''}")
        except Exception:
            logger.info(f"[{step_name}] Response Body: Unable to decode")


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:

    request_context = playwright.request.new_context(
        base_url=BASE_URL,
        extra_http_headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
    )

    logger.info(f"API Request Context is created - Base URL: {BASE_URL}")

    yield request_context


    request_context.dispose()
    logger.info("API Request Context is closed")