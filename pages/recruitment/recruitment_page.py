from base.basepage import BasePage as BP
from utilities.logger import logger
import logging
from utilities.util import Util



class RecruitmentPage(BP):

    def __init__(self):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()


    # locators

    _candidates_button =
    _vacancies_button =
    _reset_button =
    _search_button =
    _add_button =
    _records_number_header =
    _check_all =
    _delete_selected_button =
    # table records locators
    _table_record = "//div[@class='oxd-table-card']" # xpath Return all records on the table
    _record_checkbox = "//div[@class='oxd-table-card']//div[@class='oxd-table-card-cell-checkbox']" # xpath
    _date_of_application_input_fld = "//input[@placeholder='yyyy-mm-dd']" # xpath
    _toast_msg_success = "//p[text()='Successfully Saved']" # xpath

    #date picker

    _current_date = "//div[@class='oxd-calendar-date --selected --today']" # xpath


    def verify_date_is_current(self):
        self.verify_element_text_match(self.util.current_day(),self._current_date, "xpath")
