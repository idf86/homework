from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('Open target main page"')
def step_open_website(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(4)

@when('Click on cart')
def step_click_cart_icon(context):
    time.sleep(4)  # Wait for 4 seconds
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="@web/CartLink"]')
    cart_icon.click()
    time.sleep(4)  # Wait for 4 seconds

@then('Verify "Cart is empty" message')
def step_check_empty_cart_message(context):
    time.sleep(4)  # Wait for 4 seconds
    empty_cart_message = context.driver.find_element(By.CSS_SELECTOR, '.styles__StyledHeading-sc-1xmf98v-0 > span')
    assert "Your cart is empty" in empty_cart_message.text

@when('Click Sign In link')
def step_click_sign_in_link(context):
    time.sleep(4)  # Wait for 4 seconds
    sign_in_link = context.driver.find_element(By.CSS_SELECTOR, '.styles__LinkText-sc-1e1g60c-3')
    sign_in_link.click()
    time.sleep(4)  # Wait for 4 seconds

@then('Verify user can see Sign In header')
def step_check_sign_in_message(context):
    time.sleep(4)  # Wait for 4 seconds
    sign_in_message = context.driver.find_element(By.CSS_SELECTOR, '.styles__StyledHeading-sc-1xmf98v-0 > span')
    assert "Sign into your Target account" in sign_in_message.text
