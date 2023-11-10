from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Click Sign In')
      def click_sign_in(context):
        context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('From right side navigation menu, click Sign In')
    def click_sign_in_from_nav(context):
        context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify Sign In Form opened')
    def verify_sign_in_opened(context):
        expected = 'Sign into your Target account'
        actual = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']").text
        assert expected == actual, f'Expected{expected} did not match actual {actual}'