from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#open the url
driver.get('https://www.amazon.com/')

#click on orders:
orders_link = driver.find_element(By.ID, 'nav-orders')
orders_link.click()

#gotta wait bc amazon loads SO slowly
sleep(5)

#to verify
sign_in_header = driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in')]")
email_input = driver.find_element(By.ID, 'ap_email')

if sign_in_header and email_input:
    print("Test case passed!")
else:
    print("Error: Sign in header and/or email input field are not on the page.")

driver.quit()