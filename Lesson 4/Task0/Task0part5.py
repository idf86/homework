from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Search for {product_text})
      def search_product(context, product_text):
        context.driver.find_element(By.ID, 'search').send_keys(product)
        context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
        sleep(6)


@then('Verify search worked for {search_result}')
    def verify_search(context, search_result):
        search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").click()
        assert search_result in search_results_header, f'Expected text {search_result} not in {search_results_header}'


@then('Verify {expected_keyword} in search result url')
    def verify_search_url(context, expected_keyword):
        assert expected_keyword in context.driver.current_url, \
        f'Expected {expected_keyword} not in {context.driver.current_url}'