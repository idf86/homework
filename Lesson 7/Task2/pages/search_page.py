from selenium.webdriver.common.by import By

class SearchResultsPage:
    search_id = "search"
    search_button = "[data-test='@web/Search/SearchButton']"

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        search_input = self.driver.find_element(By.ID, self.search_id)
        search_input.send_keys(product_name)
        self.driver.find_element(By.CSS_SELECTOR, self.search_button).click()
