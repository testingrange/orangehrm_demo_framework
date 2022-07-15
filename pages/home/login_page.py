import logging
from utilities.logger import logger
from base.basepage import BasePage as BP
import time


class LoginPage(BP):

    log = logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _user_name_fld = "//input[@id='txtUsername']"  # xpath
    _password_fld = "txtPassword"  # id
    _login_btn = "btnLogin"  # id
    _warn_msg = "spanMessage"  # id
    _acc_icon = "welcome" # id
    _dashboard_sect = "//h1[contains(text(), 'Dashboard')]" # xpath


    # Methods
    def enter_userName(self, userName):
        self.send_keys_to_element(userName, self._user_name_fld, locator_type="xpath")

    def enter_password(self, password):
        self.send_keys_to_element(password, self._password_fld)

    def click_on_login_button(self):
        self.click_on_element(self._login_btn)

    def clear_fields(self):
        pass

    def fill_the_login_form(self, userName="", password=""):
        self.clear_fields()
        self.enter_userName(userName)
        self.enter_password(password)
        self.click_on_login_button()
        self.util.sleep(1)

    def verify_account_icon_present(self):
        return self.is_element_present(self._acc_icon)

    def verify_dashboard_sect_present(self):
        return self.is_element_present(self._dashboard_sect, "xpath")

    def verify_page_title(self, title):
        return self.verify_title(title)

    def verify_warning_message(self, warning_message):
        return self.verify_element_text_match(warning_message, self._warn_msg)

    def verify_login_btn_is_present(self):
        return self.is_element_present(self._login_btn)

    def clear_fields(self):
        usrname_fld = self.get_element(self._user_name_fld, locator_type="xpath")
        usrname_fld.clear()
        pswrd_fld = self.get_element(self._password_fld)
        pswrd_fld.clear()

