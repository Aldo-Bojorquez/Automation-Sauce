#Llenado de formulario para el envio
class CheckoutPageOne:
    def __init__(self, page):
        self.page = page
        self.button_checkout = "#checkout"

    def enter_checkout(self):
        self.page.click(self.button_checkout)

#Confirmacion de envio
class CheckoutPageTwo:
    def __init__(self, page):
        self.page = page
        self.button_continue = "#continue"
        self.first_name_input = "#first-name"
        self.last_name_input = "#last-name"
        self.postal_code_input = "#postal-code"

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)
        self.page.click(self.button_continue)
        
#Confirmacion completada
class CheckoutPageFinish:
    def __init__(self, page):
        self.page = page
        self.button_finish = "#finish"

    def enter_checkout(self):
        self.page.click(self.button_finish)