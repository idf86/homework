$$('#twotabsearchtextbox')
$$('input#twotabsearchtextbox')
$$('.nav-input')
$$('.nav-input.nav-progressive-attribute')
$$('.nav-input.nav-progressive-attribute.ll6')
$$('input.nav-input.nav-progressive-attribute')
$$('input.nav-progressive-attribute.nav-input')
$$('.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')
$$('.icp-nav-flag-us.icp-nav-flag-lop')
$$('.icp-nav-flag-lop')
$$('.icp-nav-flag-us')
$$("[placeholder='Search Amazon']")
$$("[placeholder='Search Amazon'] [aria-label='Search Amazon']")
$$("[data-csa-c-content-id='nav_cs_bestellers']")
$$("[data-csa-c-content-id=*'nav_cs_bestellers']")
$$("[data-csa-c-content-id=*'cs_bestellers']")
$$("href*='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
$$("href*='/gp/bestsellers']")
$$("href*='nav_cs_bestsellers']")
$$("href$='nav_cs_bestsellers']")
$$("href^='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
$$("data-csa-c-type~='link']")
$$("#nav-main")
$$("#nav-main a [href*='holdeals_ranked']")


# search by CSS
driver.find_element(By.CSS_SELECTOR, 'twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# search by CSS, classes
driver.find_element(By.CSS_SELECTOR, '.nav-progressive-attribute.nav-input')
driver.find_element(By.CSS_SELECTOR, '.nav-input')
driver.find_element(By.CSS_SELECTOR, 'icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')

# search by CSS, class + tag
driver.find_element(By.CSS_SELECTOR, 'input.nav-progressive-attribute.nav-input')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox.nav-progressive-attribute.nav-input')

# search by css attributes
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'] [aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'] [aria-label='Search Amazon']")

#attribute + classes + ids
driver.find_element(By.CSS_SELECTOR, "input.nav-input[placeholder='Search Amazon'] [aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute[placeholder='Search Amazon'] [aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox.nav-input[placeholder='Search Amazon']')

#attributes contains
driver.find_element(By.CSS_SELECTOR, "[data-cs-c-content-id*='cs_bestellers']")
driver.find_element(By.CSS_SELECTOR, "[href*='nav_cs_bestsellers']")

#parent to child
driver.find_element(By.CSS_SELECTOR, "nav-main a [href*='holdeals_ranked']")