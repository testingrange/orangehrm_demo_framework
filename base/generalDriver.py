from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.logger import logger
import logging
from traceback import print_stack

class GeneralDriver():

    log = logger(logging.INFO)

    def __init__(self, driver=webdriver.Chrome()):
        self.driver = driver

    def get_by_type(self, locator_type="id"):
        locator_type = locator_type.upper()
        if locator_type == "ID":
            return By.ID
        elif locator_type == "XPATH":
            return By.XPATH
        elif locator_type == "LINK":
            return By.PARTIAL_LINK_TEXT
        elif locator_type == "CLASS":
            return By.CLASS_NAME
        elif locator_type == "NAME":
            return By.NAME
        elif locator_type == "CSS":
            return By.CSS_SELECTOR
        elif locator_type == "TAG":
            return By.TAG_NAME
        else:
            self.log.error(f"Locator Type {locator_type} has not been recognized.")

    def get_element(self, locator, locator_typeype="id"):
        element = None
        try:
            element = self.driver.find_element(self.get_by_type(locator_type), locator)
            self.log.info(f"Element with locator - {locator} and locator_type - {locator_type} has been found")
        except:
            self.log.error(f"Element with locator - {locator} and locator_type - {locator_type} has not been found")
            print_stack()
        return element

    def send_keys_to_element(self, text, locator, locator_type = "id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(text)
            self.log.info(f"Text - '{text}' has been sent to element with locator - {lcator} and locator_type - {locator_type}")
        except:
            self.log.error(f"Exception occurred while trying to send keys - {text} to elemetn with locator - {locator} and locator_type - {locator_type}")
            print_stack()

    def click_on_element(self, locator, locator_type):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info(f"Element with locator - {lcator} and locator_type - {locator_type} has been clicked on")
        except:
            self.log_error(f"Exception occurred while trying to click on element with locator - {lcator} and locator_type - {locator_type}")
            print_stack()

    def wait_for_element(self):
        pass

