import time

import action
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

driver.implicitly_wait(6)
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Hello World")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)

time.sleep(10)

