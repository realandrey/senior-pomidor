from pages.base_page import BasePage

class LogoutPage(BasePage):
    BURGER_SELECTOR = '[id="react-burger-menu-btn"]'
    LOGOUT_BUTTON_SELECTOR  = '[id="logout_sidebar_link"]'
    LOGIN_BUTTON_SELECTOR = '.submit-button'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-two.html'

    def open_burger_menu(self):
        self.wait_for_selector_and_click(self.BURGER_SELECTOR)
        self.assert_element_is_visiable(self.LOGOUT_BUTTON_SELECTOR)

    def start_logout(self):
        self.wait_for_selector_and_click(self.LOGOUT_BUTTON_SELECTOR)
        self.assert_element_is_visiable(self.LOGIN_BUTTON_SELECTOR)