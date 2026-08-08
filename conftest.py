import pytest
import os
from playwright.sync_api import Browser, Page
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page=context.new_page()
    page.goto(os.getenv("BASE_URL"))
    yield page
    context.close()