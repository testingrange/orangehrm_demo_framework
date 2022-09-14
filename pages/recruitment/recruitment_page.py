from base.basepage import BasePage as BP
from utilities.logger import logger
import logging
#from utilities.util import Util



class RecruitmentPage(BP):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.util = Util()


    # locators

    _add_button = "//button[text()=' Add ']"  # xpath
    _vacancies_button = ""
    _reset_button = ""
    _search_button = ""
    _records_number_header = ""
    _check_all = ""
    _delete_selected_button = ""
    _add_candidate_header = "//h6[text()='Add Candidate']" # xpath
    _application_stage_header = "//h6[text()='Application Stage']" # xpath
    _consent_check_box = "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']" # xpath

    # Add candidate form
    _candidates_button = "//a[contains (text(), 'Candidates')]" # xpath
    _first_name_fld = "firstName" # name
    _middle_name_fld = "middleName" # name
    _last_name_fld = "lastName" # name
    _email_fld = "//div[contains(@class, 'oxd-input-group__label-wrapper') and contains(.,'Email')]/following-sibling::div/input" # xpath
    _cancel_btn = "//button[text()=' Cancel ']" # xpath
    _save_btn = "//button[@type='submit']" # xpath
    _vacancy_drop_down = "//div[@class='oxd-select-text oxd-select-text--active']" # xpath
    _consent_to_keep_data = "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']" # xpath

    # table records locators
    _table_record = "//div[@class='oxd-table-card']" # xpath Return all records on the table
    _record_checkbox = "//div[@class='oxd-table-card']//div[@class='oxd-table-card-cell-checkbox']" # xpath
    _date_of_application_input_fld = "//input[@placeholder='yyyy-mm-dd']" # xpath
    _toast_msg_success = "//p[text()='Successfully Saved']" # xpath

    #date picker

    _current_date = "//div[@class='oxd-calendar-date --selected --today']" # xpath


    def verify_date_is_current(self):
        self.verify_element_text_match(self.util.current_day(),self._current_date, "xpath")

    def click_on_add_button(self):
        self.click_on_element(self._add_button, "xpath")

    def enter_first_name(self, first_name):
        self.send_keys_to_element(first_name, self._first_name_fld, "name")

    def enter_middle_name(self, middle_name):
        self.send_keys_to_element(middle_name, self._middle_name_fld, "name")

    def enter_last_name(self, last_name):
        self.send_keys_to_element(last_name, self._last_name_fld, "name")

    def enter_email(self, email):
        self.send_keys_to_element(email, self._email_fld, "xpath")

    def click_on_save_button(self):
        self.click_on_element(self._save_btn, "xpath")

    def verify_add_candidate_page_is_open(self):
        self.is_element_present(self._add_candidate_header, "xpath")

    def verify_success_toast_message_appeared(self):
        self.is_element_displayed(self._toast_msg_success, "xpath")

    def keep_data_consent(self, consent):
        if consent != "":
            self.click_on_element(self._consent_to_keep_data, "xpath")

    def add_new_candidate(self, first_name="", last_name="", email="", middle_name="", contact_number="", vacancy="", keywords="", date="", notes="", consent=""):
        self.click_on_add_button()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.click_on_save_button()






