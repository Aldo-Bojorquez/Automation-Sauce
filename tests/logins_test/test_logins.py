import pytest
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
])
def test_login_valid_users(page, username, password):
    login_page = LoginPage(page)
    login_page.login_user(username, password)
    temp_url = os.getenv("BASE_URL") + os.getenv("ENDPOINT_INVENTORY")

    assert page.url == temp_url

def test_login_invalid_user(page):
    login_page = LoginPage(page)
    login_page.login_user("invalid_user", "invalid_passwo")
    error_message = login_page.get_error_message()

    assert "Epic sadface:" in error_message