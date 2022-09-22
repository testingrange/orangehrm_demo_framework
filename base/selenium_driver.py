from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utilities.logger import logger
from utilities.util import Util
import logging
from traceback import print_stack
import os

class SeleniumDriver():

    log = logger(logging.INFO)
    util = Util()

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def screenshot(self, message):
        """Saving a screenshot module"""
        proj_dir = os.getcwd()
        screenshot_fold_dir = f"{proj_dir}/screenshots/"
        screenshot_name = f"{self.util.date_time_stamp()}_{message}.png"
        full_screenshot_dir = f"{screenshot_fold_dir}{screenshot_name}"
        try:
            if not os.path.exists(screenshot_fold_dir):
                os.makedirs(screenshot_fold_dir)
            self.driver.save_screenshot(full_screenshot_dir)
            self.log.info(f"Screenshot - {screenshot_name} was saved to following directory - {screenshot_fold_dir}")
        except:
            self.log.error(f"Error occurred at attempt to save a screenshot {full_screenshot_dir}")
            print_stack()


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

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            element = self.driver.find_element(self.get_by_type(locator_type), locator)
            self.log.info(f"Element with locator - {locator} and locator_type - {locator_type} has been found")
        except:
            self.log.error(f"Element with locator - {locator} and locator_type - {locator_type} has not been found")
            print_stack()
        return element

    def clear_field(self, locator, locator_type="id"):
        try:
            self.log(f"Clear text of element with locator - {locator} and locator_type - {locator_type}")
            element = self.get_element(locator, locator_type)
            element.clear()
        except:
            self.log.error(f"Exception occurred at attempt to clear element with locator - {locator} and locator_type - {locator_type}")

    def send_keys_to_element(self, text, locator, locator_type = "id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(text)
            self.log.info(f"Text - '{text}' has been sent to element with locator - {locator} and locator_type - {locator_type}")
        except:
            self.log.error(f"Exception occurred while trying to send keys - {text} to element with locator - {locator} and locator_type - {locator_type}")
            print_stack()

    def click_on_element(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info(f"Element with locator - {locator} and locator_type - {locator_type} has been clicked on")
        except:
            self.log.error(f"Exception occurred while trying to click on element with locator - {locator} and locator_type - {locator_type}")
            print_stack()

    def wait_for_element(self, locator, locator_type='id', timeout=10, poll=0.5):
        element = None
        self.log.info(f"Waiting for element with locator - {locator} and locator_type - {locator_type} for {timeout} seconds")
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
        try:
            element = wait.until(EC.presence_of_element_located((self.get_by_type(locator_type), locator)))
            self.log.info(f"Element with locator - {locator} and locator_type - {locator_type} is present")
        except:
            self.log.error(f"Element with locator - {locator} and locator_type - {locator_type} is not present after {time} seconds")
        return element

    def is_element_present(self, locator, locator_type="id"):
        try:
            element = self.wait_for_element(locator, locator_type)
            if element is not None:
                self.log.info(f"Element with locator - {locator} and locator_type - {locator_type} is present")
                return True
            else:
                self.log.warn(f"Element with locator - {locator} and locator_type - {locator_type} is NOT present")
                return False
        except:
            self.log.error(f"Exception occurred. Element with locator {locator} and locatorType {locator_type} is NOT present")
            return False

    def get_title(self):
        title = self.driver.title
        self.log.info(f"Title of the web page is {title}")
        return title

    def get_text(self, locator, locator_type="id"):
        """
        Get Text of the element
        Provide locator and locator_type of the element to get text of it
        :param locator:
        :param locator_type:
        :param info:
        :return: text text of element
        """
        try:
            element = self.get_element(locator, locator_type)
            text = element.text
            if len(text) == 0 or text == None:
                text = element.get_attribute("innerText")
                self.log.info(f"Text of the element is - {text}")
            if len(text) != 0:
                self.log.info(f"Getting text of the element")
                self.log.info(f"The text is - {text}")
        except:
            self.log.error(f"Exception occurred while trying to get element's text")
            print_stack()
            text=None
        return text

    def is_element_displayed(self, locator, locator_type="id"):
        pass

    def page_scroll(self, scroll_by=100):
        """
        Method to scroll browser screen by pixels.
        Scroll down - positive integer example - '100'
        Scroll up - negative integer example '- 100'
        :param scroll_by:
        :return:
        """
        pass

    def switch_to_frame(self, frameLocator):
        """
        Switch to iframe using parameters is, name, index
        :param id: (str) id of the iframe
        :param name: (str) name of the iframe
        :param index: (int) index of the iframe
        :return:
        """
        self.log.info(f"Switching to the frame with frameLocator - {frameLocator}")
        self.driver.switch_to.frame(frameLocator)

    def switch_to_default_content(self):
        self.log.info("Switching back to default content")
        self.driver.switch_to.default_content()

    def get_element_attribute_value(self, attribute, locator="", locator_type="id", element=None):
        value = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            value = element.get_attribute(attribute)
            self.log.info(f"Value of the element's attribute {attribute} is {value}.")
        except:
            self.log.error(f"Exception occurred at attempt to get element's attribute - {attribute}")
        return value

    def is_element_enabled(self, locator, locator_type):
        """Check if element is enabled"""
        enabled = False
        element = self.get_element(locator, locator_type)
        try:
            self.log.info(f"Trying to check if element contains attribute 'disabled'")
            attribute_value = self.get_element_attribute_value("disabled", locator, locator_type)
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.get_element_attribute_value(attribute="class", element=element)
                self.log.info(f"Attribute value From Application Web UI is {value}")
                enabled = not("disabled" in value)
            if enabled:
                self.log.info(f"Element is enabled")
            else:
                self.log.warn(f"Element is not enabled")
        except:
            self.log.error("Element state couldn't be found")
        return enabled

    def clear_field(self, locator, locator_type='id'):
        try:
            self.log.info(f"Clearing field with locator - '{locator}' and locator_type - '{locator_type}'")
            field = self.get_element(locator, locator_type)
            num = len(field.get_attribute('value'))
            if num > 0:
                for i in range(num):
                    field.send_keys(Keys.BACKSPACE)
            self.log.info(f"Field with locator - '{locator}' and locator_type - '{locator_type}' was cleared.")
        except:
            self.log.error(f"Exception occurred while attempt to clear the field with locator - '{locator}' and locator_type - '{locator_type}'")


