from base.basepage import BasePage as BP
from utilities.logger import logger
import logging


class RecruitmentPage(BP):

    def __init__(self):
        self.driver = driver
        super().__init__(driver)


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
