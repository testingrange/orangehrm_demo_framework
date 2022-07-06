import logging
from utilities import logger
from base.generalDriver import GeneralDriver as GD

class LoginPage(GD):

    log = logger(logging.INFO)

    def __init__(self, driver):
        super.__init__(driver)
        self.driver = driver

    # Locators
    _user_name_fld = "txtUsername"  #id
    _password_fld = "txtPassword"  #id
    _login_btn = "btnLogin"  #id
    _warn_msg = "spanMessage"  #id


    # Methods
    def enter_userName(self, userName):
        self.send_keys_to_element(userName, self._user_name_fld)

    def enter_password(self, password):
        self.send_keys_to_element(password, self._password_fld)

    def click_on_login_button(self):
        self.click_on_element(self._login_btn)

    def fill_the_login_form(self, userName, password):
        self.enter_userName(userName)
        self.enter_password(password)
        self.click_on_login_button()
