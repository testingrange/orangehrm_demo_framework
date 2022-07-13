import pytest
from utilities.logger import logger
from base.webdriverfactory import WebDriverFactory
import logging

@pytest.fixture(scope="class")
def sessionSetUp(request, browser):
    log = logger(logging.INFO)
    web_driver = WebDriverFactory(browser)
    driver = web_driver.get_webdriver_instance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    log.info("Test session completed")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
