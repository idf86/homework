from selenium.webdriver.common.by import By
import time

class ProductPage:
    add_link = "a[href*='mon-eevee-evolution-building-set']"
    add_to_cart_button_xpath = "//button[@aria-label='Add to cart for MEGA Pokémon Eevee Evolution Building Set - 470pcs']"

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.add_link).click()
        time.sleep(3)
        add_to_cart_button = self.driver.find_element(By.XPATH, self.add_to_cart_button_xpath)
        add_to_cart_button.click()
        time.sleep(2)