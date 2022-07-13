from pages.home.login_page import LoginPage
from utilities.logger import logger
from utilities.test_status import TestStatus
import logging
import unittest
import pytest

@pytest.mark.usefixtures("sessionSetUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, sessionSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_valid_login_and_password(self):
        self.lp.fill_the_login_form("Admin", "admin123")
        result1 = self.lp.verify_account_icon_present()
        self.ts.mark(result1, "Account icon is displayed")
        result2 = self.lp.verify_dashboard_sect_present()
        self.ts.mark(result2, "Dashboard section is displayed")
        result3 = self.lp.verify_page_title("OrangeHRM")
        self.ts.mark_final("Valid login test", result3, "Title is correct")



