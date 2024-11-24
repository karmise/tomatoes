from ui.pages.login_page import LoginPage


class BurgerMenu(LoginPage):

    BURGER_MENU_BUTTON = '[class="bm-burger-button"]'
    LOGOUT_BUTTON = '[id="logout_sidebar_link"]'

    def __init__(self, page):
        super().__init__(page)

    def logout_user(self):
        self.wait_for_selector_and_click(self.BURGER_MENU_BUTTON)
        self.wait_for_selector_and_click(self.LOGOUT_BUTTON)
        self.assert_element_is_visible(self.LOGIN_BUTTON_SELECTOR)