from selenium import webdriver
from pages.main_page import MainPage
from pages.signin_page import SignInPage

driver = webdriver.Chrome()
driver.get("https://www.target.com")

main_page = MainPage(driver)
main_page.click_sign_in()

sign_in_page = SignInPage(driver)
assert sign_in_page.is_sign_in_form_present(), "Sign In form is not present"

driver.quit()
