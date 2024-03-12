from base.basepage import BasePage as BP
from utilities.logger import logger
from pages.home.login_page import LoginPage
from pages.side_nav_panel.side_nav_page import SideNavPage
from selenium.webdriver.common.keys import Keys
import logging

class CandidatesPage(BP):

    log = logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.lp = LoginPage(driver)
        self.np = SideNavPage(driver)

    # Candidates page locators
    _add_button = "//button[text()=' Add ']"  # xpath
    _reset_button = ""
    _search_button = ""
    _records_number_header = ""
    _check_all = ""
    _delete_selected_button = ""
    _add_candidate_header = "//h6[text()='Add Candidate']" # xpath
    _application_stage_header = "//h6[text()='Application Stage']" # xpath
    _consent_check_box = "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']" # xpath
    _vacancy_drop_down_btn = "//div[@class='oxd-select-text--after']" # xpath
    _drop_down_list_items = "//div[@role='listbox']//div[contains(., '{0}')]"

    # table records locators
    _table_record = "//div[@class='oxd-table-card']"  # xpath Return all records on the table
    _record_checkbox = "//div[@class='oxd-table-card']//div[@class='oxd-table-card-cell-checkbox']"  # xpath
    _pagination_next_page = "//button[@class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']/i[@class='oxd-icon bi-chevron-right']"  # xpath
    _pagination_previous_page = "//button[@class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']" # xpath

    # Add candidate form
    _date_fld = "//input[contains(@placeholder, 'yyyy-mm-dd') or contains(@placeholder, 'yyyy-dd-mm')]"  # xpath
    _toast_msg_success = "//p[text()='Successfully Saved']"  # xpath
    _candidates_button = "//a[contains (text(), 'Candidates')]" # xpath
    _first_name_fld = "firstName" # name
    _middle_name_fld = "middleName" # name
    _last_name_fld = "lastName" # name
    _email_fld = "//div[contains(@class, 'oxd-input-group__label-wrapper') and contains(.,'Email')]/following-sibling::div/input" # xpath
    _cancel_btn = "//button[text()=' Cancel ']" # xpath
    _save_btn = "//button[@type='submit']" # xpath
    _consent_to_keep_data = "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']" # xpath
    _list_box = "//div[@role='listbox']"
    _contact_number = "//div[contains (@class, 'oxd-input-group__label-wrapper') and contains(.,'Contact Number')]/following-sibling::div/input"  # xpath
    _keywords_fld = "//div/input[@placeholder='Enter comma seperated words...']"  # xpath
    _notes_field = "//div/textarea[@placeholder='Type here']"  # xpath

    # Locators
    _rec_checkbox = ""
    _hiring_manager_rec = "//div[@role='cell']/div[contains(text(), '{0}')]"
    _application_date_rec = "//div[@role='cell']/div[contains(text(), '{0}')]"
    _status_rec = "//div[@role='cell']/div[contains(text(), '{0}')]"
    _created_record = "//div[@class='oxd-table-card']/div[contains(., '{0}') and contains(., '{1} {2}{3}') and contains(., '{4}') and contains(., '{5}')]"  # xpath #0-vacancy 1-first name 2 - middle name 3 - last name 4 -date of application 5 - status
    _delete_record_btn = "//div[@class='oxd-table-card']/div[contains(., '{0}') and contains(., '{1} {2}{3}') and contains(., '{4}') and contains(., '{5}')]//i[@class='oxd-icon bi-trash']" # xpath
    _confirm_deleting_btn = "//button[contains(., ' Yes, Delete ')]" # xpath

    # date picker
    _current_date = "//div[@class='oxd-calendar-date --selected --today']" # xpath

    # Filter section
    _select_job_title_drop_down = "//label[contains(text(), 'Job Title')]/parent::div/following-sibling::div/div/div"  # xpath
    _select_vacancy_drop_down = "//label[contains(text(), 'Vacancy')]/parent::div/following-sibling::div/div/div"  # xpath
    _select_hiring_manager_drop_down = "//label[contains(text(), 'Hiring Manager')]/parent::div/following-sibling::div/div/div"  # xpath
    _select_status_drop_down = "//label[contains(text(), 'Status')]/parent::div/following-sibling::div/div/div" # xpath
    _select_method_of_application_drop_down = "//label[contains(text(), 'Method of Application')]/parent::div/following-sibling::div/div/div" # xpath

    _candidate_name_filter_field = "//input[@placeholder='Type for hints...']" # xpath
    _date_of_application_from_field = "//input[@placeholder='From']" # xpath
    _date_of_application_to_field = "//Input[@placeholder='To']" # xpath
    _keywords_field = "//Input[@placeholder='Enter comma seperated words...']" # xpath

    # Error messages
    _invalid_date_format_error_message = "//span[contains(., 'Should be a valid date in yyyy-dd-mm format')]" # xpath
    _future_date_error_message = "//span[contains(., 'Should be the current date or a previous date')]" # xpath
    _unexpected_email_format_error_message = "//span[contains(., 'Expected format: admin@example.com')]" # xpath
    _more_than_250_characters_error_message = "//span[contains(., 'Should not exceed 250 characters')]" # xpath
    _contact_number_letters_error_message = "//span[contains(., 'Allows numbers and only + - / ( )')]" # xpath
    _first_name_exceeding_30_characters_error_message = "//input[@name='firstName']/parent::div/following-sibling::span" # xpath
    _middle_name_exceeding_30_characters_error_message = "//input[@name='middleName']/parent::div/following-sibling::span" # xpath
    _last_name_exceeding_30_characters_error_message = "//input[@name='lastName']/parent::div/following-sibling::span" # xpath


    ### Add candidate page methods

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

    def select_vacancy(self, vacancy_name):
        self.select_item_from_list(vacancy_name, self._vacancy_drop_down_btn, "xpath", self._list_box, "xpath", self._drop_down_list_items)

    def enter_contact_number(self, contact_number):
        self.send_keys_to_element(contact_number, self._contact_number, "xpath")

    def enter_keywords(self, keywords):
        self.send_keys_to_element(keywords, self._keywords_fld, "xpath")

    def enter_notes(self, notes):
        self.send_keys_to_element(notes, self._notes_field, "xpath")

    def enter_date(self, date):
        self.send_keys_to_element(date, self._date_fld, "xpath")

    def click_on_save_button(self):
        self.click_on_element(self._save_btn, "xpath")

    def click_on_next_page_btn(self):
        self.click_on_element(self._pagination_next_page, "xpath")

    def verify_add_candidate_page_is_open(self):
        return self.is_element_present(self._add_candidate_header, "xpath")

    def verify_success_toast_message_appeared(self):
        return self.is_element_present(self._toast_msg_success, "xpath")

    def keep_data_consent(self, consent):
        if consent != "":
            self.click_on_element(self._consent_to_keep_data, "xpath")

    # Clear candidate page fields methods

    def clear_first_name_fld(self):
        self.clear_field(self._first_name_fld, "name")

    def clear_middle_name_fld(self):
        self.clear_field(self._middle_name_fld, "name")

    def clear_last_name_fld(self):
        self.clear_field(self._last_name_fld, "name")

    def select_first_item_vacancy_list(self):
        self.select_vacancy("-- Select --")

    def clear_email_fld(self):
        self.clear_field(self._email_fld, "xpath")

    def clear_contact_number_fld(self):
        self.clear_field(self._contact_number, "xpath")

    def clear_keywords_fld(self):
        self.clear_field(self._keywords_fld, "xpath")

    def clear_date_fld(self):
        self.clear_field(self._date_fld, "xpath")

    def clear_notes_fld(self):
        self.clear_field(self._notes_field, "xpath")

    def log_in_to_app(self):
        self.lp.fill_the_login_form("Admin", "admin123")

    def clear_all_fields(self):
        self.clear_first_name_fld()
        self.clear_middle_name_fld()
        self.clear_last_name_fld()
        self.select_first_item_vacancy_list()
        self.clear_email_fld()
        self.clear_contact_number_fld()
        self.clear_keywords_fld()
        self.clear_date_fld()
        self.clear_notes_fld()

    def add_new_candidate(self, first_name="", last_name="", email="", middle_name="", contact_number="", vacancy_name="", keywords="", date="", notes="", consent=""):
        self.np.navigate_to_recruitment_page()
        self.click_on_add_button()
        self.enter_first_name(first_name)
        self.enter_middle_name(middle_name)
        self.enter_last_name(last_name)
        self.select_vacancy(vacancy_name)
        self.enter_email(email)
        self.enter_contact_number(contact_number)
        self.enter_keywords(keywords)
        self.clear_date_fld()
        self.enter_date(date)
        self.enter_notes(notes)
        self.keep_data_consent(consent)
        self.util.sleep(2)
        self.click_on_save_button()


    ### Verification of records

    def verify_record_present(self, first_name="", last_name="", middle_name="", vacancy_name="", date="", status=""):
        self.log.info("verify_record_present starts.")
        middle_name_initial = middle_name
        if middle_name != '':
            middle_name = middle_name + ' '
        else:
            middle_name = ' '
        self.log.info(f"Check that record with first_name - '{first_name}', last_name - '{last_name}', middle_name - '{middle_name}' doesn't exist")
        if not self.is_element_present(self._created_record.format(vacancy_name, first_name, middle_name, last_name, date, status), "xpath") and self.is_element_present(self._pagination_next_page, "xpath"):
            self.log.info("Next page button exist. Checking if element exists on the next page.")
            self.click_on_next_page_btn()
            self.log.info("Click on the next page button.")
            middle_name = middle_name_initial
            return self.verify_record_present(first_name, last_name, middle_name, vacancy_name, date, status)
        else:
            self.log.info("Verifying if element exists.")
            return self.is_element_present(self._created_record.format(vacancy_name, first_name, middle_name, last_name, date, status), "xpath")

    def verify_no_record_exists(self, first_name="", last_name="", middle_name="", vacancy_name="", date="", status=""):
        self.np.navigate_to_recruitment_page()
        if self.verify_record_present(first_name, last_name, middle_name, vacancy_name, date, status):
            self.log.info(f"Deleting pre-existing record with first_name -'{first_name}' and last_name - '{last_name}' and middle_name - '{middle_name}'")
            self.delete_the_record(first_name, last_name, middle_name, vacancy_name, date, status)
            return self.verify_no_record_exists(first_name, last_name, middle_name, vacancy_name, date, status)
        else:
            return not self.verify_record_present(first_name, last_name, middle_name, vacancy_name, date, status)

    def verify_record_exists(self, first_name="", last_name="", middle_name="", vacancy_name="", date="", status=""):
        self.np.navigate_to_recruitment_page()
        return self.verify_record_present(first_name, last_name, middle_name, vacancy_name, date, status)

    def delete_the_record(self, first_name="", last_name="", middle_name="", vacancy_name="", date="", status=""):
        middle_name_initial = middle_name
        if middle_name != '':
            middle_name = middle_name + ' '
        else:
            middle_name = ' '
        if not self.is_element_present(
                self._created_record.format(vacancy_name, first_name, middle_name, last_name, date, status),
                "xpath") and self.is_element_present(self._pagination_next_page, "xpath"):
            self.log.info("Verifying if element exists on the next page")
            self.click_on_next_page_btn()
            self.log.info("Click on the next page button")
            self.delete_the_record(first_name, last_name, middle_name, vacancy_name, date, status)
        else:
            self.click_on_element(self._delete_record_btn.format(vacancy_name, first_name, middle_name, last_name, date, status), "xpath")
            self.click_on_element(self._confirm_deleting_btn, "xpath")
            self.log.info(f"Deleting the record with with first_name -'{first_name}' and last_name - '{last_name}' and middle_name - '{middle_name}'")


    def delete_existing_record(self, first_name="", last_name="", middle_name="", vacancy_name="", date="", status=""):
        self.np.navigate_to_recruitment_page()
        self.delete_the_record(first_name, last_name, middle_name, vacancy_name, date, status)

    # Filter methods

    def clear_app_date_from_field(self):
        self.clear_field(self._date_of_application_from_field, "xpath")

    def enter_app_date_from_field(self, date=""):
        self.np.navigate_to_recruitment_page()
        self.clear_app_date_from_field()
        self.send_keys_to_element(date,self._date_of_application_from_field, "xpath")
        self.send_keys_to_element(Keys.TAB, self._date_of_application_from_field, "xpath")

    def verify_invalid_date_error_present(self):
        return self.is_element_present(self._invalid_date_format_error_message, "xpath")