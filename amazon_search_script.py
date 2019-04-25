from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome('drivers/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click on help link
driver.find_element(By.XPATH, "//div[@id='nav-xshop']/a[text()='Help']").click()

# type cancel order
el = driver.find_element(By.ID, 'helpsearch')
el.clear()
el.send_keys('Cancel order')

# click on go button
driver.find_element(By.CLASS_NAME, 'a-button-input').click()

# find text
element = driver.find_element(By.TAG_NAME, 'body')
assert 'Cancel Items or Orders' in element.text

driver.quit()
