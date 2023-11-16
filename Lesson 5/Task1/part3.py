from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@given('Open target main page "{url}"')
def step_open_website(context, url):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.get(url)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
    )

@when('Verify user can click on the Target Circle link')
def step_target_circle_link(context):
    target_circle_link = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/GlobalHeader/UtilityHeader/TargetCircle']")
    target_circle_link.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'earnings')]"))
    )

@then('Verify Earnings box')
def search_earnings(context):
    context.earnings_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'earnings')]"))
    )

@then('Verify Deals box')
def search_deals(context):
    context.deals_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Hundreds')]"))
    )

@then('Verify Birthday box')
def search_birthday(context):
    context.birthday_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Birthday gift')]"))
    )

@then('Verify Community box')
def search_community(context):
    context.community_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'votes')]"))
    )

@then('Verify Partnerships box')
def search_partnerships(context):
    context.partnership_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Partnerships')]"))
    )

@then('Verify all boxes are present')
def verify_all_boxes(context):
    # This step assumes previous 'Verify' steps have successfully found the elements,
    # so no additional WebDriverWait is necessary here.
    if context.earnings_box and context.deals_box and context.birthday_box and context.community_box and context.partnership_box:
        print("Test case passed!")
    else:
        print("Error: One of these boxes was not verified.")

@then('Verify user can search')
def step_search(context):
    search_input = context.driver.find_element(By.ID, "search")
    search_input.send_keys("Eevee Evolution Building Set")
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='mon-eevee-evolution-building-set']"))
    )

@then('Verify product can be added to cart')
def step_product(context):
    product_link = "a[href*='mon-eevee-evolution-building-set']"
    add_product = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, product_link))
    )
    add_product.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "addToCartButtonOrTextIdFor76151960"))
    )
    big_ol_button = context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor76151960")
    big_ol_button.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/cart']"))
    )

@then('Verify user can checkout')
def verify_checkout(context):
    view_cart_button_selector = "a[href='/cart']"
    view_cart_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, view_cart_button_selector))
    )
    view_cart_button.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="cart-item-groups"]'))
    )

@then('Verify user can see price of product')
def verify_price(context):
    checkout_area = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="cart-item-groups"]'))
    )
    assert "MEGA Pokémon Eevee Evolution Building Set - 470pcs" in checkout_area.text
    context.driver.quit()
