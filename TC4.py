from unittest import TestCase

from selenium import webdriver

from pages.main_page import MainPage
from pages.shop_page import ShopPage
from pages.cart_page import CartPage, buy_product_by_name




def test_case_4():
    browser = webdriver.Chrome('webDrivers\chromedriver.exe')

    #From the home page go to Shop page
    mainPage = MainPage(browser)
    mainPage.open_mainPage()
    mainPage.click_ShopPage_from_mainPage()

    shopPage = ShopPage(browser)
    shopPage.get_product_list()

    cartPage = CartPage(browser)

    #Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear
    buy_product_by_name("Stuffed Frog",2)
    buy_product_by_name("Fluffy Bunny",5)
    buy_product_by_name("Valentine Bear",3)


    #Go to the cart page
    mainPage.click_CartPage_from_mainPage()

    cartPage.get_cart_itms()

    #Verify the price for each product
    if cartPage.verify_price_for_each_product() == False:
        print("FAIL")
        browser.close()
        return False

    #Verify that each product’s sub total = product price * quantity
    if cartPage.verify_price_for_each_subtotal() == False:
        print("FAIL")
        browser.close()
        return False

    #Verify that total = sum(sub totals)
    if cartPage.verify_total() == False:
        print("FAIL")
        browser.close()
        return False


    print("SUCCESS")
    browser.close()
    return True

class TestTestCase_4(TestCase):
    def test_test_case_4_success(self):
        self.assertEqual(test_case_4(), True)