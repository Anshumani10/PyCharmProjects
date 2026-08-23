import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest


def test_e2e(browserInstance):
    driver = browserInstance

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    driver.find_element(By.ID, "password").send_keys("Learning@830$3mK2")
    driver.find_element(By.ID, "signInBtn").click()

    driver.find_element(By.LINK_TEXT, "Shop").click()
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    print(len(products))

    for product in products:
        product_name = product.find_element(By.XPATH, "div/h4/a").text
        if product_name == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()
    driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    driver.find_element(By.ID, "country").send_keys("ind")
    wait = WebDriverWait(driver, 8)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    success_text = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success! Thank you!" in success_text

    time.sleep(8)

