import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "anshu"

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
assert name in alert.text
alert.accept()











time.sleep(10)