# the video is very low quality so
# that makes the commands look very blurry
# I'm sorry if these aren't the right ones

# search by ID
driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, 'twotabsearchtextbox')


# search by xpath
$x("//input[@type='text']*)
$x("//input[@name='field-keywords']")
$x("//input[@label='Search Amazon']")
$x("//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@name='field-keywords']")
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")

#by xpath, multiple attributes
driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute' and @value='Go']")
driver.find_element(By.XPATH, "//input[@value='Go' and @class='nav-input nav-progressive-attribute' and @type='submit']")

#search by xpath, text()
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a ']")

#contains
$x("//h2[text()='Scary-good Halloween costumes']")
$x("//h2[contains(text(), 'Scary-good Halloween costumes')]")
driver.find_element(By.XPATH, "//h2[contains(text(), 'Scary-good')]")
driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Search')]")

#parent to child
$x("//div[@id='nav-main']")
$x("//div[@id='nav-main']//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//div[@id='nav-main']//a[text()='Best Sellers']")