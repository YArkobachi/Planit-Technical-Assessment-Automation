from unittest import TestCase

from selenium import webdriver

from pages.main_page import MainPage
from pages.shop_page import ShopPage
from pages.cart_page import CartPage, buy_product_by_name




def test_case_3():
    browser = webdriver.Chrome('webDrivers\chromedriver.exe')

    #From the home page go to Shop page
    mainPage = MainPage(browser)
    mainPage.open_mainPage()
    mainPage.click_ShopPage_from_mainPage()

    shopPage = ShopPage(browser)
    shopPage.get_product_list()

    cartPage = CartPage(browser)

    #Click buy button 2 times on “Funny Cow”
    buy_product_by_name('Funny Cow', 2)

    #Click buy button 1 time on “Fluffy Bunny”
    buy_product_by_name("Fluffy Bunny")

    #Click the cart menu
    mainPage.click_CartPage_from_mainPage()


    cartPage.get_cart_itms()

    # Verify the items are in the cart
    result = cartPage.verify_cart_itms()

    browser.close()
    return result

class TestTestCase_3(TestCase):
    def test_test_case_3_success(self):
        self.assertEqual(test_case_3(), True)