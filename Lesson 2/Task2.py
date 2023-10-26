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

# here are the individual search strategies. run whichever ones you'd like.

#Amazon logo
# driver.find_element(By.XPATH, "//i[@role='img']")
# $x("//i[@role='img']")

# Email field
# driver.find_element(By.XPATH, "//input[@id='ap_email']")
# $x("//input[@id='ap_email']")

# Continue button
# driver.find_element(By.XPATH, "//input[@id='continue']")
# $x("//input[@id='continue']")

# Conditions of use link
# driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")
# $x("//div[@id='legalTextRow']//a[text()='Conditions of Use']")

# Privacy Notice link
# driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']")
# $x("//div[@id='legalTextRow']//a[text()='Privacy Notice']")

# Need help link
# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# $x("//span[@class='a-expander-prompt']")

# Forgot your password link
# driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
# $x("//a[@id='auth-fpp-link-bottom']")

# Other issues with Sign-In link
# driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
# $x("//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button
# driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")
# $x("//a[@id='createAccountSubmit']")


driver.quit()