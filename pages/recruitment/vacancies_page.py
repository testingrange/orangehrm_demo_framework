from base.basepage import BasePage as BP
from pages.side_nav_panel.side_nav_page import SideNavPage
from pages.home.login_page import LoginPage




class VacanciesPage(BP):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.lp = LoginPage(driver)
        self.sp = SideNavPage(driver)

    # LOCATORS
    _hiring_manager_options = "//div[@role='listbox']//div[@role='option']"

    _vacancies_btn = "//li/a[text() = 'Vacancies']" # xpath
    _add_button = "//button[text() = ' Add ']" # xpath
    _record = "//div[@class='oxd-table-card']/div[contains(., '{0}') and contains(., '{1}') and contains(., '{2}') and contains(., '{3}')]"  # xpath # 0- vacancy, 1 - Job Title, 2 - Hiring Manager, 3 - Status
    _job_title_dropdown = "//div[contains(@class, 'oxd-input-field-bottom-space') and contains(., 'Job Title')]//div[@class='oxd-select-text-input']" # xpath
    _vacany_dropdown = "//div[contains(@class, 'oxd-input-field-bottom-space') and contains(., 'Vacancy')]//div[@class='oxd-select-text-input']" # xpath
    _hiring_management = "//div[contains(@class, 'oxd-input-field-bottom-space') and contains(., 'Hiring Manager')]//div[@class='oxd-select-text-input']" # xpath
    _status = "//div[contains(@class, 'oxd-input-field-bottom-space') and contains(., 'Status')]//div[@class='oxd-select-text-input']" # xpath
    _reset_btn = "//button[text() = ' Reset ']" # xpath
    _search_btn = "//button[text() = ' Search ']" # xpath

    _vacancy_name_fld = "//div[contains (@class,'oxd-input-group oxd-input-field-bottom-space') and contains (.,'Vacancy Name')]//input" # xpath
    _vacancy_drop_down_btn = "//div[@class='oxd-select-text--after']"  # xpath
    _drop_down_list_items = "//div[@role='listbox']//div[contains(., '{0}')]" # xpath
    _list_box = "//div[@role='listbox']" # xpath
    _description_field = "textarea" # tag
    _hiring_manager_field = "//input[@placeholder='Type for hints...']"
    _num_positions_fld = "//div[.='Number of Positions']//input"
    _save_btn = "//button[@type='submit']"
    _cancel_btn = "//button[text()=' Cancel ']"


    # METHODS

    def click_vacancies_button(self):
        self.click_on_element(self._vacancies_btn, "xpath")

    def click_add_button(self):
        self.click_on_element(self._add_button, "xpath")

    def type_in_vacancy_name_fld(self, vacancy_name):
        self.send_keys_to_element(vacancy_name, self._vacancy_name_fld, "xpath")

    def select_job_title(self, job_title):
        self.select_item_from_list(vacancy_name, self._vacancy_drop_down_btn, "xpath", self._list_box, "xpath", self._drop_down_list_items)

    def type_in_description(self, description=None):
        self.send_keys_to_element(description, self._description_field, "tag")

    def type_in_hiring_manager(self, description):
        self.send_keys_to_element(description, self._hiring_manager_field, "xpath")

    def type_in_number_pos(self, num):
        self.send_keys_to_element(num, self._num_positions_fld, "xpath")

    def click_on_save_btn(self):
        self.click_on_element(self._save_btn, "xpath")

    def add_vacancy(self, vacancy_name="", job_title="", description="", hiring_manager="", num_of_pos=""):
        pass
