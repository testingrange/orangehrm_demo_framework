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

    def verify_element_text_match(self, text_to_verify, locator, locator_type='id'):
        """
        Method for verification of the text of a given element
        """
        try:
            self.log.info(f"Verifying if the element contains text - '{text_to_verify}'")
            element_text = self.get_text(locator, locator_type)
            return self.util.verify_text_match(text_to_verify, element_text)
        except:
            self.log.error("Exception occurred during the verification element's text process. Verification failed.")
            print_stack()
            return False

    def verify_title(self, title_to_verify):
        try:
            self.log.info(f"Verifying if the page has title - {title_to_verify}")
            page_title = self.get_title()
            return self.util.verify_text_match(title_to_verify, page_title)
        except:
            self.log.error(f"Verification failed")
            print_stack()
            return False

    def select_item_from_list(self, item, drop_down_btn_locator, drop_down_btn_locator_type, list_box_locator, list_box_locator_type, drop_down_list_items):
        try:
            if item != "":
                self.log.info(f"Selecting item from list - {item}")
                self.log.debug("Clicking on the item list drop down bnt")
                self.click_on_element(drop_down_btn_locator, drop_down_btn_locator_type)
                self.log.info("Hover over an element")
                self.actions.move_to_element(self.get_element(list_box_locator, list_box_locator_type)).perform()
                self.scroll_into_view(drop_down_list_items.format(item), "xpath")
                self.click_on_element(drop_down_list_items.format(item), "xpath")
        except:
            self.log.error(f"Error happened while selecting item {item}")