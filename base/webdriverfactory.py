"""
Web Driver Factory class implementation
It creates a webdriver instance based on browser configuration
"""
from selenium import webdriver
from utilities.logger import logger
from selenium.webdriver.edge.options import Options as EdgeOptions
import logging


class WebDriverFactory():

    log = logger(logging.INFO)

    def __init__(self, browser, headless=None):
        self.browser = browser
        self.headless = headless

    def get_webdriver_instance(self):
        """
        Get Webdriver instance based on the browser configuration
        :return:
        """

        baseURL = "https://opensource-demo.orangehrmlive.com/"

        if self.browser == "chrome":
            if self.headless:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                driver = webdriver.Chrome(options=chrome_options)
            else:
                driver = webdriver.Chrome()
            self.log.info(f"Webdriver initiated with Chrome browser")
        elif self.browser == "firefox":
            if self.headless:
                firefox_options = webdriver.FirefoxOptions()
                firefox_options.add_argument('--headless')
                driver = webdriver.Firefox(options=firefox_options)
            else:
                driver = webdriver.Firefox()
            self.log.info(f"Webdriver initiated with Firefox browser")
        elif self.browser == "ie":
            if self.headless:
                ie_options = webdriver.IeOptions()
                ie_options.add_argument('--headless')
                driver = webdriver.Ie(options=ie_options)
            else:
                driver = webdriver.Ie()
            self.log.info(f"Webdriver initiated with Internet Explorer")
        else:
            driver = webdriver.Chrome()
            self.log.warn(f"Given type of browser IS NOT supported. Webdriver initiated with Chrome browser")

        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)
        self.log.info(f"Starting with {baseURL}")
        return driver

