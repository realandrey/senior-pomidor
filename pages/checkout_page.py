from pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_BUTTON_SELECTOR = '#checkout'
    FIRST_NAME_SELECTOR = '#first-name'
    LAST_NAME_SELECTOR = '#last-name'
    POSTAL_CODE_SELECTOR = '#postal-code'
    CONTINUE_BUTTON_SELECTOR = '[id="continue"]'
    FINISH_BUTTON_SELECTOR = '[id="finish"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-one.html'

    def start_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_is_visiable(self.FIRST_NAME_SELECTOR)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait_for_selector_and_type(self.FIRST_NAME_SELECTOR, first_name, 100)
        self.wait_for_selector_and_type(self.LAST_NAME_SELECTOR, last_name, 100)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code, 100)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)
        self.wait_for_selector_and_click(self.CONTINUE_BUTTON_SELECTOR)
        self.wait_for_selector_and_click(self.FINISH_BUTTON_SELECTOR)

