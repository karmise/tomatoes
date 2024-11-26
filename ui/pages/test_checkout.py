from ui.pages.burger_menu import BurgerMenu
from ui.pages.checkout_page import CheckoutPage
from ui.pages.inventory_page import InventoryPage
from ui.pages.login_page import LoginPage
from ui.conftest import browser


def test_checkout_product(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    burger_menu = BurgerMenu(page)

    login_page.correct_login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form(first_name='John', last_name='Doe', postal_code='12345')
    checkout_page.wait_for_selector_and_click(checkout_page.CONTINUE_BUTTON_SELECTOR)
    checkout_page.wait_for_selector_and_click(checkout_page.FINISH_BUTTON_SELECTOR)
    checkout_page.assert_text_present_on_page('Thank you for your order!')
    burger_menu.logout_user()


def test_checkout_product_with_empty_name(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.correct_login(username='standard_user', password='secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form(first_name='John', last_name='Doe', postal_code='12345')
    checkout_page.wait_for_selector_and_click(checkout_page.CONTINUE_BUTTON_SELECTOR)
    checkout_page.assert_text_in_element(checkout_page.ERROR_SELECTOR, 'Error: First Name is required')


def test_checkout_product_with_empty_first_name(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.correct_login(username='standard_user', password='secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form(first_name='', last_name='Doe', postal_code='12345')
    checkout_page.wait_for_selector_and_click(checkout_page.CONTINUE_BUTTON_SELECTOR)
    checkout_page.assert_text_in_element(checkout_page.ERROR_SELECTOR, 'Error: Last Name is required')


def test_checkout_product_with_empty_last_name(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.correct_login(username='standard_user', password='secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form(first_name='John', last_name='', postal_code='12345')
    checkout_page.wait_for_selector_and_click(checkout_page.CONTINUE_BUTTON_SELECTOR)
    checkout_page.assert_text_in_element(checkout_page.ERROR_SELECTOR, 'Error: Last Name is required')


def test_checkout_product_with_empty_postal_code(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.correct_login(username='standard_user', password='secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form(first_name='John', last_name='Doe', postal_code='')
    checkout_page.wait_for_selector_and_click(checkout_page.CONTINUE_BUTTON_SELECTOR)
    checkout_page.assert_text_in_element(checkout_page.ERROR_SELECTOR, 'Error: Postal Code is required')