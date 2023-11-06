from selenium.webdriver.common.by important By
from behave important given, when, then
from time import sleep

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for coffee')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.CSS_SELECTOR, "[data-tests='@web/Search/SearchButton']").click()
    sleep(6)


@then('Verify search worked')
def verify_search(context):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-tests='resultsHeading']").text
    assert 'coffee' in search_results_header, f'Expected text coffee not in {search_results_header}'

@then('Verify search url')
def verify_search(context):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-tests='resultsHeading']").text
    assert 'coffee' in context.driver.current_url

