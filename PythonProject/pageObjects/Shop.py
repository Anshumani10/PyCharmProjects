from selenium.webdriver.common.by import By

from pageObjects.checkout_confirmation import Checkout_confirmation
from utils.browser_utils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shopLink = (By.LINK_TEXT, "Shop")
        self.shop_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_to_cart(self, product_name):

        self.driver.find_element(*self.shopLink).click()
        products = self.driver.find_elements(*self.shop_cards)
        print(len(products))

        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()


    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = Checkout_confirmation(self.driver)
        return checkout_confirmation






