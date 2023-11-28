from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open sign in page "{url}"')
def step_given(context, url):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.get(url)

@when('Store original windows')
def step_store(context):
    context.original_window = context.driver.current_window_handle

@then('Click on Target terms and conditions')
def step_terms(context):
    wait = WebDriverWait(context.driver, 10)
    terms_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Target terms and conditions')]")))
    terms_link.click()

@then('Switch to the newly opened window')
def step_switch(context):
    assert len(context.driver.window_handles) > 1
    for window_handle in context.driver.window_handles:
        if window_handle != context.original_window:
            context.driver.switch_to.window(window_handle)
            break

@then('Verify Terms and Conditions page is opened')
def step_verify(context):
    wait = WebDriverWait(context.driver, 10)
    sign_in_header_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Terms & Conditions')]")))
    sign_in_header = sign_in_header_element.text
    assert "Terms & Conditions" in sign_in_header

@then('User can close new window and switch back to original')
def step_close(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
