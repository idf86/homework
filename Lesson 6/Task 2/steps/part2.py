from behave import given, when, then
from selenium import webdriver
from pages.main_page import MainPage
from pages.cart_page import CartPage


@given('Open "{url}"')
def open_target_website(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    context.main_page = MainPage(context.driver)

@when('Click on Cart icon')
def click_on_cart_icon(context):
    context.main_page.click_cart_icon()
    context.cart_page = CartPage(context.driver)

@then('Verify "Your cart is empty" message is shown')
def verify_empty_cart_message(context):
    message = context.cart_page.get_empty_cart_message()
    assert "Your cart is empty" in message, f"Expected 'Your cart is empty' but got '{message}'"
