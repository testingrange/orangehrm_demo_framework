from base.basepage import BasePage as BP
from utilities.logger import logger
from pages.home.login_page import LoginPage
from pages.side_nav_panel.side_nav_page import SideNavPage
import logging



class RecruitmentPage(BP):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.lp = LoginPage(driver)
        self.np = SideNavPage(driver)


    # locators

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
    _list_box = "//div[@role='listbox']"
    _contact_number = "//div[contains (@class, 'oxd-input-group__label-wrapper') and contains(.,'Contact Number')]/following-sibling::div/input" # xpath
    _keywords_fld = "//div/input[@placeholder='Enter comma seperated words...']" # xpath
    _notes_field = "//div/textarea[@placeholder='Type here']" # xpath

    # Add candidate form
    _candidates_button = "//a[contains (text(), 'Candidates')]" # xpath
    _first_name_fld = "firstName" # name
    _middle_name_fld = "middleName" # name
    _last_name_fld = "lastName" # name
    _email_fld = "//div[contains(@class, 'oxd-input-group__label-wrapper') and contains(.,'Email')]/following-sibling::div/input" # xpath
    _cancel_btn = "//button[text()=' Cancel ']" # xpath
    _save_btn = "//button[@type='submit']" # xpath
    _consent_to_keep_data = "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']" # xpath

    # table records locators
    _table_record = "//div[@class='oxd-table-card']" # xpath Return all records on the table
    _record_checkbox = "//div[@class='oxd-table-card']//div[@class='oxd-table-card-cell-checkbox']" # xpath
    _date_fld = "//input[@placeholder='yyyy-mm-dd']" # xpath
    _toast_msg_success = "//p[text()='Successfully Saved']" # xpath

    # Locators
    _rec_checkbox = ""
    #_vacancy_rec = "//div[@role='cell']/div[contains(text(), '{0}')]"
    #_candidate_rec = "//div[@role='cell']/div[contains(text(), '{0} {1}{2}')]"
    _hiring_manager_rec = "//div[@role='cell']/div[contains(text(), '{0}')]"
    _application_date_rec = "//div[@role='cell']/div[contains(text(), '{0}')]"
    _status_rec = "//div[@role='cell']/div[contains(text(), '{0}')]"
    _created_record = "//div[@class='oxd-table-card']/div[contains(., '{0}') and contains(., '{1} {2}{3}') and contains(., '{4}') and contains(., '{5}')]"  # xpath #0-vacancy 1-first name 2 - middle name 3 - last name 4 -date of application 5 - status
    _delete_record_btn = "//div[@class='oxd-table-card']/div[contains(., '{0}') and contains(., '{1} {2}{3}') and contains(., '{4}') and contains(., '{5}')]//i[@class='oxd-icon bi-trash']" # xpath
    _confirm_deliting_btn = "//button[contains(., ' Yes, Delete ')]" # xpath
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

    def select_vacancy(self, vacancy_name):
        try:
            if vacancy_name != "":
                self.log.info(f"Selecting vacancy - {vacancy_name}")
                self.log.debug("Clicking on vacancy drop down bnt")
                self.click_on_element(self._vacancy_drop_down_btn, "xpath")
                self.actions.move_to_element(self.get_element(self._list_box, "xpath")).perform()
                self.log.debug("move to listbox element")
                self.scroll_into_view(self._drop_down_list_items.format(vacancy_name), "xpath")
                self.actions.click(self.get_element(self._drop_down_list_items.format(vacancy_name), "xpath")).perform()
        except:
            self.log.error(f"Error happened while selecting vacancy {vacancy_name}")

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

    def verify_add_candidate_page_is_open(self):
        return self.is_element_present(self._add_candidate_header, "xpath")

    def verify_success_toast_message_appeared(self):
        return self.is_element_present(self._toast_msg_success, "xpath")

    def keep_data_consent(self, consent):
        if consent != "":
            self.click_on_element(self._consent_to_keep_data, "xpath")

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

        # methods
    def verify_no_record_exists(self, first_name="", last_name="", middle_name="", vacancy_name="", date="", status=""):
        self.np.navigate_to_recruitment_page()
        if middle_name != '':
            middle_name = middle_name + ' '
        else:
            middle_name = ' '
        if not self.is_element_present(self._created_record.format(vacancy_name, first_name, middle_name, last_name, date, status), "xpath"):
            return True

    def verify_record_exists(self, first_name="", last_name="", middle_name="", vacancy_name="", date="", status=""):
        self.np.navigate_to_recruitment_page()
        if middle_name != '':
            middle_name = middle_name + ' '
        else:
            middle_name = ' '
        return self.is_element_present(self._created_record.format(vacancy_name, first_name, middle_name, last_name, date, status), "xpath")

    def delete_existing_record(self, first_name="", last_name="", middle_name="", vacancy_name="", date="", status=""):
        self.np.navigate_to_recruitment_page()
        if middle_name != '':
            middle_name = middle_name + ' '
        else:
            middle_name = ' '
        self.click_on_element(self._delete_record_btn.format(vacancy_name, first_name, middle_name, last_name, date, status), "xpath")
        self.click_on_element(self._confirm_deliting_btn, "xpath")











