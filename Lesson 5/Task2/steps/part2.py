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
        EC.presence_of_element_located((By.ID, "search"))
    )

@when('Verify user can search')
def step_search(context):
    search_input = context.driver.find_element(By.ID, "search")
    search_input.send_keys("kids fleece hoodie")
    search_button = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    search_button.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='kids-fleece-hoodie']"))
    )

@then('Verify product is loaded')
def step_product(context):
    product_link = "a[href*='lands-end-kids-softest-fleece-jacket']"
    find_product = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, product_link))
    )
    find_product.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "productDetails"))
    )

@then('Verify user can see options')
def verify_options(context):
    color_options = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ColorSelect__StyledColorSelect-sc-1v2maoc-0 img"))
    )
    for color_option in color_options:
        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable(color_option)
        )
        color_option.click()
