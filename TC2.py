from unittest import TestCase

from selenium import webdriver

from pages.main_page import MainPage
from pages.contact_page import ContactPage






def test_case_2():
    browser = webdriver.Chrome('webDrivers\chromedriver.exe')
    #From the home page go to contact page
    mainPage = MainPage(browser)
    mainPage.open_mainPage()
    mainPage.click_ContactPage_from_mainPage()

    contactpage = ContactPage(browser)

    #Populate mandatory fields
    contactpage.populate_mandatory_fields()

    #Click submit button
    contactpage.submit_btn.click()

    #Validate successful submission message
    result = contactpage.validate_successful_submission_message()

    browser.close()
    return result

class TestTestCase_2(TestCase):
    def test_test_case_2_success(self):
        for _ in range(0,5):
            self.assertEqual(test_case_2(), True)