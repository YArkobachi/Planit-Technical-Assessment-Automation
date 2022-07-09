from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from utils.BasePage import WebPage
from utils.BaseElement import Element, InputElement
from utils.locator import Locator

from utils.generators import Generator

class ContactPage(WebPage):

    base_url = "https://jupiter.cloud.planittesting.com/#/contact"

    forename = str

    @property
    def submit_btn(self):
        return Element(self.drv, Locator(By.CLASS_NAME, 'btn-contact'))

    @property
    def forename_txtBox(self):
        return InputElement(self.drv, Locator(By.ID, 'forename'))

    @property
    def email_txtBox(self):
        return InputElement(self.drv, Locator(By.ID, 'email'))

    @property
    def message_txtBox(self):
        return InputElement(self.drv, Locator(By.ID, 'message'))


    @property
    def forename_err_msg(self):
        return Element(self.drv, Locator(By.ID, 'forename-err'))

    @property
    def email_err_msg(self):
        return Element(self.drv, Locator(By.ID, 'email-err'))

    @property
    def message_err_msg(self):
        return Element(self.drv, Locator(By.ID, 'message-err'))

    @property
    def sucess_submit_msg(self):
        return Element(self.drv, Locator(By.CLASS_NAME, 'alert-success'))

    def validate_error_msgs_enable(self):
        try:
            if (self.forename_err_msg.is_displayed and self.email_err_msg.is_displayed and self.message_err_msg.is_displayed) == True:
                return True
        except NoSuchElementException:
            print("NoSuchElementException =>" + Locator)
            return False

    def validate_error_msgs_disable(self):
        try:
            self.drv.find_element(By.ID, 'forename-err').is_displayed()
            return False
        except NoSuchElementException:
            print("contactpage.forename_err.is_displayed = False")

        try:
            self.drv.find_element(By.ID, 'email-err').is_displayed()
            return False
        except NoSuchElementException:
            print("contactpage.email_err.is_displayed = False")

        try:
            self.drv.find_element(By.ID, 'message-err').is_displayed()
            return False
        except NoSuchElementException:
            print("contactpage.message_err.is_displayed = False")
        return True

    def populate_mandatory_fields(self):
        # Populate mandatory fields
        generate = Generator()

        # generate and populate forename
        self.forename = generate.random_string_lowercase()
        try:
            self.forename_txtBox.text = self.forename
        except NoSuchElementException:
            print("NoSuchElementException =>" + Locator)
            return False

        # generate and populate email
        email = generate.random_email()
        try:
            self.email_txtBox.text = email
        except NoSuchElementException:
            print("NoSuchElementException =>" + Locator)
            return False

        # generate and populate message
        message = generate.random_string_lowercase() + generate.random_string_uppercase()
        try:
            self.message_txtBox.text = message
        except NoSuchElementException:
            print("NoSuchElementException =>" + Locator)
            return False
        return True

    #Validate successful submission message
    def validate_successful_submission_message(self):
        # Populate mandatory fields
        submission_message = self.sucess_submit_msg.find()

        if (submission_message.text == "Thanks " + self.forename + ", we appreciate your feedback."):
            print("SUCCESS")
            return True
        else:
            print(submission_message.text)
            return False