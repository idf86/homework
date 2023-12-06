from selenium.webdriver.common.by import By
import time

class CartPage:
    view_cart = "a[href='/cart']"
    check_out = '[data-test="cart-item-groups"]'

    def __init__(self, driver):
        self.driver = driver

    def view_cart_and_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.view_cart).click()

    def verify_item_in_checkout(self, expected_text):
        time.sleep(5)
        checkout_area = self.driver.find_element(By.CSS_SELECTOR, self.check_out)
        return expected_text in checkout_area.text
