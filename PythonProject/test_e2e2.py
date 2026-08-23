import json
import sys
import os

from pageObjects import checkout_confirmation

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest

from pageObjects.Login import LoginPage
from pageObjects.Shop import ShopPage

test_data_path = 'data/test_e2e2.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e2(browserInstance, test_list_item):
    driver = browserInstance


    loginPage = LoginPage(driver)
    print(loginPage.get_title())
    shop = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop.add_to_cart(test_list_item["productName"])

    print(shop.get_title())
    checkout_confirmation = shop.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.delivery_address("India")
    checkout_confirmation.validate_order()











    time.sleep(8)
