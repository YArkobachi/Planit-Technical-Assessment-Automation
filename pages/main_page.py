from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

from utils.BasePage import WebPage
from utils.BaseElement import Element, InputElement
from utils.locator import Locator


class MainPage(WebPage):

    base_url = "https://jupiter.cloud.planittesting.com/#/"
    #base_url = "https://jupiter2.cloud.planittesting.com/#/shop"

    @property
    def contact_page_link(self):
        return Element(self.drv, Locator(By.XPATH,'//*[@id="nav-contact"]/a'))

    @property
    def shop_page_link(self):
        return Element(self.drv, Locator(By.XPATH, '//*[@id="nav-shop"]/a'))
        #return Element(self.drv, Locator(By.ID, '"nav-shop'))

    def open_mainPage(self):
        mainPage = MainPage(self.drv)
        try:
            mainPage.start_chrome(mainPage.url)
        except NoSuchElementException:
            print("Couldn't open =>" + self.drv.current_url)
            return False

    def click_ContactPage_from_mainPage(self):

        try:
            elms = self.drv.find_elements(By.CLASS_NAME, "nav")
            nav_Contact = elms[0].find_element(By.ID, "nav-contact")
            nav_Contact.click()
            return True
        except NoSuchElementException:
            print("Couldn't open =>" + self.drv.current_url)
            return False

    def click_ShopPage_from_mainPage(self):

        try:
            elms = self.drv.find_elements(By.CLASS_NAME, "nav")
            nav_Contact = elms[0].find_element(By.ID, "nav-shop")
            nav_Contact.click()
            return True
        except NoSuchElementException:
            print("Couldn't open =>" + self.drv.current_url)
            return False

    def click_CartPage_from_mainPage(self):

        try:
            elms = self.drv.find_elements(By.CLASS_NAME, "nav")
            nav_Cart = elms[1].find_element(By.ID, "nav-cart")
            nav_Cart.click()
        except NoSuchElementException:
            print("Couldn't open =>" + self.drv.current_url)
            return False
        # Wait for page to upload
        timeout = 30
        WebDriverWait(self.drv, timeout).until(presence_of_element_located((By.CLASS_NAME, "table")))
