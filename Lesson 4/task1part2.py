# features/steps/target_circle_steps.py
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I open the website "{url}"')
def open_website(context, url):
    context.driver.get('https://www.target.com/')

@when('Verify user can click on the Target Circle link')
def click_target_circle_link(context):
    target_circle_link = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/GlobalHeader/UtilityHeader/TargetCircle']")
    target_circle_link.click()

@then('Verify "1% earnings" header is present')
def verify_first_benefit_header(context, header):
    first_benefit_header = context.driver.find_element(By.CSS_SELECTOR, "")
    assert header in first_benefit_header.text

@then('Verify "Hundreds of deals" header is present"')
def verify_second_benefit_header(context, header):
    second_benefit_header = context.driver.find_element(By.CSS_SELECTOR, "")
    assert header in second_benefit_header.text

@then('Verify "Community support votes" header is present')
def verify_third_benefit_header(context, header):
    third_benefit_header = context.driver.find_element(By.CSS_SELECTOR, "")
    assert header in third_benefit_header.text

@then('Verify "Target Circle Partnerships" header is present')
def verify_fourth_benefit_header(context, header):
    fourth_benefit_header = context.driver.find_element(By.CSS_SELECTOR, "")
    assert header in fourth_benefit_header.text

@then('I should see the fifth benefits header "{header}"')
def step_verify_fifth_benefit_header(context, header):
    fifth_benefit_header = context.driver.find_element(By.CSS_SELECTOR, 'your-css-selector-for-fifth-benefit-header')
    assert header in fifth_benefit_header.text
