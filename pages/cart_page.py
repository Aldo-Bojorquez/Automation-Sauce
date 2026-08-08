class CartPage:
    def __init__(self, page):
        self.page = page
        self.button_shopping_cart = "[data-test='shopping-cart-link']"

    def enter_shopping_cart(self):
        self.page.click(self.button_shopping_cart)