from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the URL
driver.get('https://www.amazon.com/')

# Click on orders
orders_link = driver.find_element(By.ID, 'nav-orders')
orders_link.click()

# Wait for the sign-in page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Sign in')]"))
)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'ap_email'))
)

# Verify the sign-in header and email input field
sign_in_header = driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in')]")
email_input = driver.find_element(By.ID, 'ap_email')

if sign_in_header and email_input:
    print("Test case passed!")
else:
    print("Error: Sign in header and/or email input field are not on the page.")

driver.quit()
