import logging
from utilities import logger

class LoginPage():

    log = logger(logging.INFO)

    def __init__(self, driver):
        super.__init__(driver)
        self.driver = driver

    # Locators
    _user_name_fld = "txtUsername"
    _password_fld = "txtPassword"
    _login_btn = "btnLogin"
    _warn_msg = "spanMessage"

    def test_positive_login_and_password(self):
        pass
        
