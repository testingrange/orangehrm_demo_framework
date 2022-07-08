"""
Web Driver Factory class implementation
It creates a webdriver instance based on browser configuration
"""
from selenium import webdriver
from utilities.logger import logger
import logging


class WebDriverFactory():

    log = logger(logging.INFO)

    def __init__(self, browser):
        self.browser = browser.lower()

    def get_webdriver_instance(self):
        """
        Get Webdriver instance based on the browser configuration
        :return:
        """

        baseURL = "https://opensource-demo.orangehrmlive.com/"

        if self.browser == "chrome":
            driver = webdriver.Chrome()
            self.log.info(f"Webdriver initiated with Chrome browser")
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
            self.log.info(f"Webdriver initiated with Firefox browser")
        elif self.browser == "ie":
            driver = webdriver.Ie()
            self.log.info(f"Webdriver initiated with Internet Explorer")
        else:
            driver = webdriver.Chrome()
            self.log.warn(f"Fiven type of browser IS NOT supported. Webdriver initiated with Chrome browser")

        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)
        return driver