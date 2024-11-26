from ui.pages.login_page import LoginPage


def test_error_login_message(page):
    page.login_with_problems('wrong_username555', 'wrong_password333')
    page.assert_text_in_element(LoginPage.ERROR_LOGIN_SELECTOR,
                                'Epic sadface: Username and password do not match any user in this service')