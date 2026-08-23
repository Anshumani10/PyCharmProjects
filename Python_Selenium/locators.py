import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.bidi.browsing_context import XPathLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

#Dropdown

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")



#ID, Xpath, CSSSelector, name, classname, linkText

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath //tagname[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

# CSS tagname[attribute='value'] -> //input[@type='submit']
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Anshu")

assert "Success" in message

# ID turnout to be css

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.CLASS_NAME, "ng-pristine").send_keys("Hello Again")










time.sleep(10)