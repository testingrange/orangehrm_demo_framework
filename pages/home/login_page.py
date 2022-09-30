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
    _user_name_fld = "//input[@name='username']"  # xpath
    _password_fld = "//input[@name='password']"  # xpath
    _login_btn = "//button[contains(.,' Login ')]"  # xpath
    _warn_msg = "//p[contains(.,'Invalid credentials')]"  # xpath
    _dashboard_sect = "//h1[contains(text(), 'Dashboard')]" # xpath
    _login_header = "//h5[contains(@class,'orangehrm-login-title')]"
    _orangehrm_logo = "//div[@class='orangehrm-login-logo']/img" # xpath
    _user_name_required_msg = "//form[@class='oxd-form']/div[@class='oxd-form-row'][1]//span[contains(.,'Required')]" # xpath
    _password_required_msg = "//form[@class='oxd-form']/div[@class='oxd-form-row'][2]//span[contains(.,'Required')]" # xpath
    _acc_icon = "//li//img[@class='oxd-userdropdown-img']" # xpath
    _side_pannel = "//nav[@aria-label='Sidepanel']" # xpath
    _navigation_pannel = "//nav[@aria-label='Topbar Menu']" # xpath


    # Methods
    def enter_userName(self, userName):
        self.send_keys_to_element(userName, self._user_name_fld, "xpath")

    def enter_password(self, password):
        self.send_keys_to_element(password, self._password_fld, "xpath")

    def click_on_login_button(self):
        self.click_on_element(self._login_btn, "xpath")

    def verify_username_req_message(self):
        return self.is_element_present(self._user_name_required_msg, "xpath")

    def verify_password_req_message(self):
        return self.is_element_present(self._password_required_msg, "xpath")

    def verify_login_btn_is_present(self):
        return self.is_element_present(self._login_btn, "xpath")

    def verify_login_header_is_present(self):
        return self.is_element_present(self._login_header, "xpath")

    def verify_orange_hrm_logo_is_present(self):
        return self.is_element_present(self._orangehrm_logo, "xpath")

    def verify_invalid_credentials_warning_msg(self):
        return self.is_element_present(self._warn_msg, "xpath")

    def verify_account_icon_present(self):
        return self.is_element_present(self._acc_icon, "xpath")

    def verify_side_menu_present(self):
        return self.is_element_present(self._side_pannel, "xpath")

    def verify_navigation_menu_present(self):
        return self.is_element_present(self._navigation_pannel, "xpath")

    def clear_userName_field(self):
        self.clear_field(self._user_name_fld, "xpath")

    def clear_password_field(self):
        self.clear_field(self._password_fld, "xpath")

    def clear_fields(self):
        self.clear_userName_field()
        self.clear_password_field()

    def fill_the_login_form(self, userName="", password=""):
        self.clear_fields()
        self.enter_userName(userName)
        self.enter_password(password)
        self.util.sleep(2)
        self.click_on_login_button()
