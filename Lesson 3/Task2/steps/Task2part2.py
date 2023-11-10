from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('Open target main page "{url}"')
def step_open_website(context, url):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.get(url)
    time.sleep(4)

@when('Click on cart')
def step_click_cart_icon(context):
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]')
    cart_icon.click()
    time.sleep(4)  # Wait for 4 seconds

@then('Verify "Cart is empty" message')
def step_check_empty_cart_message(context):
    empty_cart_message = context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="boxEmptyMsg"] h1')
    assert "Your cart is empty" in empty_cart_message.text
    time.sleep(4)  # Wait for 4 seconds

@when('Click Sign In link')
def step_click_sign_in_link(context):
    sign_in_link = context.driver.find_element(By.CSS_SELECTOR, "button[class*='ButtonPrimary'][class*='BlockButton']")
    sign_in_link.click()
    time.sleep(4)  # Wait for 4 seconds

@then('Verify user can see Sign In header')
def step_check_sign_in_message(context):
    sign_in_message = context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="content-wrapper"] h1')
    assert "Sign into your Target account" in sign_in_message.text