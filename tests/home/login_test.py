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

    @pytest.mark.run(order=2)
    def test_valid_username_and_password(self):
        self.lp.fill_the_login_form("Admin", "admin123")
        result1 = self.lp.verify_account_icon_present()
        self.ts.mark(result1, "Account icon is displayed")
        result2 = self.lp.verify_dashboard_sect_present()
        self.ts.mark(result2, "Dashboard section is displayed")
        result3 = self.lp.verify_page_title("OrangeHRM")
        self.ts.mark_final("Valid login test", result3, "Title is correct")

    @pytest.mark.run(order=1)
    def test_invalid_username_valid_passwrd(self):
        self.lp.fill_the_login_form("InvalidUsrname", "admin123")
        result1 = self.lp.verify_login_btn_is_present()
        self.ts.mark(result1, "Login button is present")
        result2 = self.lp.verify_warning_message("Invalid credentials")
        self.ts.mark_final("Invalid username and valid password test", result2, "Warning message is correct")

    @pytest.mark.run(order)
    def test_valid_username_invalid_password(self):
        pass

    def test_empty_username_valid_password(self):
        pass

    def test_valid_username_empty_password(self):
        pass

    def test_empty_fields(self):
        pass





