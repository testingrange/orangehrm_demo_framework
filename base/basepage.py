from base.selenium_driver import SeleniumDriver as SD
from utilities.logger import logger
from utilities.util import Util
import logging
from traceback import print_stack

class BasePage(SD):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_element_contains_text(self, text_to_verify, locator, locator_type='id'):
        """
        """
        try:
            element = self.get_element(locator, locator_type)
        except:
            pass

    def verify_title(self, title_to_verify):
        try:
            self.log.info(f"Verifying if the page has title - {title_to_verify}")
            page_title = self.get_title()
            return self.util.verify_text_match(title_to_verify, page_title)
        except:
            self.log.error(f"Verification failed")
            print_stack()
            return False