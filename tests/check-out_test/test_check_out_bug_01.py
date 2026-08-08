import pytest
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPageOne, CheckoutPageTwo, CheckoutPageFinish

load_dotenv()

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
])
@pytest.mark.parametrize("first_name, last_name, postal_code", [
    ("John", "Doe", "12345"),
])
def test_checkout_with_empty_cart(page, username, password, first_name, last_name, postal_code):
    login_page = LoginPage(page)
    login_page.login_user(username, password)

    cart_page = CartPage(page)
    cart_page.enter_shopping_cart()

    checkout_page_one = CheckoutPageOne(page)
    checkout_page_one.enter_checkout()

    checkout_page_two = CheckoutPageTwo(page)
    checkout_page_two.fill_checkout_form(first_name, last_name, postal_code)

    checkout_page_finish = CheckoutPageFinish(page)
    checkout_page_finish.enter_checkout()

    # Verificar que el usuario no pueda completar el proceso de compra con un carrito vacío
    assert "Your cart is empty" in page.content()