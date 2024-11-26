from ui.pages.login_page import LoginPage
from ui.conftest import browser


def test_error_login_message(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.login_with_problems('wrong_username555', 'wrong_password333')
    login_page.assert_text_in_element(LoginPage.ERROR_SELECTOR,
                                      'Epic sadface: Username and password do not match any user in this service')