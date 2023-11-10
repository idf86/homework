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
    time.sleep(3)


@when('Verify user can click on the Target Circle link')
def step_target_circle_link(context):
    target_circle_link = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/GlobalHeader/UtilityHeader/TargetCircle']")
    target_circle_link.click()
    time.sleep(3)


@then('Verify Earnings box')
def search_earnings(context):
    context.earnings_box = context.driver.find_element(By.XPATH, "//h3[contains(text(),'earnings')]")


@then('Verify Deals box')
def search_deals(context):
    context.deals_box = context.driver.find_element(By.XPATH, "//h3[contains(text(),'of deals')]")


@then('Verify Birthday box')
def search_birthday(context):
    context.birthday_box = context.driver.find_element(By.XPATH, "//h3[contains(text(),'Birthday gift')]")


@then('Verify Community box')
def search_community(context):
    context.community_box = context.driver.find_element(By.XPATH, "//h3[contains(text(),'votes')]")


@then('Verify Partnerships box')
def search_community(context):
    context.partnership_box = context.driver.find_element(By.XPATH, "//h3[contains(text(),'partnerships')]")


if context.earnings_box and context.deals_box and context.birthday_box and context.community_box and context.partnership_box:
    print("Test case passed!")
else:
    print("Error: One of these boxes was not verified.")


@then('Verify user can search')
def step_search(context):
    search_input = context.browser.find_element(By.ID, "search")
    search_input.send_keys("pokemon")
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    time.sleep(3)


@then('Verify product can be added to cart')
def step_product(context):
    product_link = "a[href*='mon-eevee-evolution-building-set']"
    add_product = context.driver.find_element(By.CSS_SELECTOR, product_link)
    add_product.click()
    time.sleep(3)
    big_ol_button = context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor76151960")
    big_ol_button.click()
    time.sleep(3)


@then('Verify user can checkout')
def verify_checkout(context):
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]')
    cart_icon.click()
    time.sleep(3)


@then('Verify user can see price of product')
def verify_price(context):
    checkout_area = context.driver.find_element(By.CSS_SELECTOR, '[data-test="cart-item-groups"]')
    assert "MEGA Pokémon Eevee Evolution Building Set - 470pcs" in checkout_area.text
