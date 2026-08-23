import time

import action
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#import Explicitwait

#from locators import dropdown

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.implicitly_wait(6)
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
New_tab = driver.window_handles
driver.switch_to.window(New_tab[1])

message = driver.find_element(By.CLASS_NAME, "red").text
email = message.split(" at ")[1].split(" with ")[0]
print(email)

driver.switch_to.window(New_tab[0])

driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("123456")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "user":
        checkbox.click()
        assert checkbox.is_selected()
        time.sleep(2)
        break

driver.find_element(By.ID, "okayBtn").click()

Dropdown = driver.find_element(By.CSS_SELECTOR, "select.form-control")
select = Select(Dropdown)
options = select.options

for option in options:
    print(option.text)
    time.sleep(2)

select.select_by_visible_text("Teacher")

driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()

Emessage = (WebDriverWait(driver, 5)).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
time.sleep(2)
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
print("Error message: ", Emessage.text)




time.sleep(10)