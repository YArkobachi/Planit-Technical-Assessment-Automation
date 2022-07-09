
from unittest import TestCase

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from pages.main_page import MainPage
from pages.contact_page import ContactPage
from selenium.webdriver.common.by import By

def test_case_1():
    browser = webdriver.Chrome('webDrivers\chromedriver.exe')



    #jupiter_url = https://jupiter2.cloud.planittesting.com/#/shop

    #From the home page go to contact page
    mainPage = MainPage(browser)
    mainPage.open_mainPage()
    mainPage.click_ContactPage_from_mainPage()

    #Click submit button
    contactpage = ContactPage(browser)
    contactpage.submit_btn.click()


    # validation of error messages enable
    if contactpage.validate_error_msgs_enable() != True:
        print('test fail')
        browser.close()

    #Populate mandatory fields
    assert contactpage.populate_mandatory_fields()

    # Validate errors are gone
    if contactpage.validate_error_msgs_disable() == False:
        print('test fail')

    print("SUCCESS")
    browser.close()
    return True

class TestTestCase_1(TestCase):
    def test_test_case_1_success(self):
        self.assertEqual(test_case_1(), True)