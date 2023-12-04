from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    cart_mess = "//h1[contains(text(), 'empty')]"

    def __init__(self, driver):
        self.driver = driver

    def get_empty_cart_message(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.cart_mess)))
        return self.driver.find_element(By.XPATH, self.cart_mess).text
