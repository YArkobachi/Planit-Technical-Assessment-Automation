from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException

from utils.BasePage import WebPage
from utils.BaseElement import Element, InputElement, SelectElement
from utils.locator import Locator

from pages.cart_page import shop_products, chckd_products


class Product():
    name = str
    price = float
    bought = int

    def __init__(self, name, price, buy_btn):
        self.name = name
        self.price = float(price)
        self.buy_btn = buy_btn



class ShopPage(WebPage):
    base_url = "https://jupiter.cloud.planittesting.com/#/shop"

    #products = {}
    # forename = gener.random_string_lowercase

    @property
    def products_scope(self):
        return Element(self.drv, Locator(By.CLASS_NAME, "products"))

    @property
    def product_page_link(self):
        return Element(self.drv, Locator(By.CLASS_NAME, "product"))


    def get_product_list(self):
        try:
            # Wait for page to upload
            timeout = 30
            WebDriverWait(self.drv, timeout).until(presence_of_element_located((By.CLASS_NAME, "products")))
        except NoSuchElementException:
            print("NoSuchElementException =>" + Locator)
            return False

        try:
            if self.products_scope.web_element.is_displayed():

                els = self.drv.find_elements(By.CLASS_NAME, "product")

                for prod in els:
                    name = prod.find_element(By.CLASS_NAME, "product-title").text
                    price = float(prod.find_element(By.CLASS_NAME, "product-price").text[1:])
                    buy_btn = prod.find_element(By.CLASS_NAME, "btn")
                    shop_products[name] = Product(name, price, buy_btn)
        except NoSuchElementException:
            print("Couldn't alocate products =>" + Locator)
            return False
        return True