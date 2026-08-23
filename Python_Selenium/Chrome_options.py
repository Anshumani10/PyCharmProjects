import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Miscellaneous import chrome_options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

print(driver.title)







time.sleep(9)