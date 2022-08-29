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
    def test_empty_fields(self):
        self.lp.fill_the_login_form()
        result1 = self.lp.verify_username_req_message()
        self.ts.mark(result1, "Username required message is present")
        result2 = self.lp.verify_password_req_message()
        self.ts.mark(result2, "Password required message is present")
        result3 = self.lp.verify_login_btn_is_present()
        self.ts.mark_final("Empty login and password fields test", result3, "Login button is present")

    @pytest.mark.run(order=2)
    def test_invalid_username_valid_password(self):
        self.lp.fill_the_login_form("InvalidUsrname", "admin123")
        result1 = self.lp.verify_login_btn_is_present()
        self.ts.mark(result1, "Login button is present")
        result2 = self.lp.verify_invalid_credentials_warning_msg()
        self.ts.mark_final("Invalid username and valid password test", result2, "Warning message is present")

    @pytest.mark.run(order=3)
    def test_valid_username_invalid_password(self):
        self.lp.fill_the_login_form("Admin", "Invpassword")
        result1 = self.lp.verify_login_btn_is_present()
        self.ts.mark(result1, "Login button is present")
        result2 = self.lp.verify_invalid_credentials_warning_msg()
        self.ts.mark_final("Valid username and invalid password test", result2, "Warning message is present")

    @pytest.mark.run(order=4)
    def test_empty_username_valid_password(self):
        self.lp.fill_the_login_form("", "admin123")
        result1 = self.lp.verify_username_req_message()
        self.ts.mark(result1, "Required message is present")
        result2 = self.lp.verify_login_btn_is_present()
        self.ts.mark_final("Empty username and valid password test", result2, "Login button is present")

    @pytest.mark.run(order=5)
    def test_valid_username_empty_password(self):
        self.lp.clear_fields()
        self.lp.fill_the_login_form("Admin", "")
        result1 = self.lp.verify_password_req_message()
        self.ts.mark(result1, "Required message is present")
        result2 = self.lp.verify_login_btn_is_present()
        self.ts.mark_final("Valid username and empty password test", result2, "Login button is present")

    @pytest.mark.run(order=6)
    def test_valid_username_and_password(self):
        self.lp.fill_the_login_form("Admin", "admin123")
        result1 = self.lp.verify_side_menu_present()
        self.ts.mark(result1, "Side manu is displayed")
        result2 = self.lp.verify_account_icon_present()
        self.ts.mark(result2, "Account icon is displayed")
        result3 = self.lp.verify_navigation_menu_present()
        self.ts.mark_final("Valid login and password test", result3, "Navigation menu is present")