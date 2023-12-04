from selenium.webdriver.common.by import By

class MainPage:
    cart_sel = 'a[data-test="@web/CartLink"]'

    def __init__(self, driver):
        self.driver = driver

    def click_cart_icon(self):
        cart_icon = self.driver.find_element(By.CSS_SELECTOR, self.cart_sel)
        cart_icon.click()
