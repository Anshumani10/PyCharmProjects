import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sort(browserInstance):

    driver = browserInstance

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    browserSortedVeggies = []
    #click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    #collect all veggie name -> Browsersortedveggie_list (A,B,C)
    veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for element in veggieWebElements:
        browserSortedVeggies.append(element.text)
    print(browserSortedVeggies)
    originalbrowserSortedList = browserSortedVeggies.copy()
    #sort this Browsersortedveggie_list => newSortedList (A,B,C)
    browserSortedVeggies.sort()
    #Browsersortedveggie_list == newSortedList
    assert originalbrowserSortedList == browserSortedVeggies


    time.sleep(9)


