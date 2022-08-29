from base.basepage import BasePage as BP
from utilities.logger import logger
import logging


class SideNavPage(BP):
    """
    Class for side navigation panel
    common for all pages of the app.
    """

    log = logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _search = "//input[@placeholder='Search']" # xpath
    _admin = "Admin" # link or partial link
    _pim = "PIM"# link or partial link
    _leave = "Leave"# link or partial link
    _time = "Time" # link or partial link
    _recruitment = "Recruitment" # link or partial link
    _my_info = "My Info" # link or partial link
    _performance = "Performance" # link or partial link
    _dashboard = "Dashboard" # link or partial link
    _directory = "Directory" # link or partial link
    _maintenance = "Maintenance" # link or partial link
    _buzz = "Buzz" # link or partial link
    _search_toggled = "//input[contains(@class, 'oxd-input--active') and contains(@class,'toggled')]" # xpath
    _side_menue_toggle_btn = "//button[contains(@role, 'none') and contains(@type,'button')]"


    # methods
    def navigate_to_admin_page(self):
        self.click_on_element(self._admin, "link")

    def navigate_to_PIM_page(self):
        self.click_on_element(self._pim, "link")

    def navigate_to_leave_page(self):
        self.click_on_element(self._leave, "link")

    def navigate_to_time_page(self):
        self.click_on_element(self._time, "link")

    def navigate_to_recruitment_page(self):
        self.click_on_element(self._recruitment, "link")

    def navigate_to_my_info_page(self):
        self.click_on_element(self._my_info, "link")

    def navigate_to_performance_page(self):
        self.click_on_element(self._performance, "link")

    def navigate_to_dashboard_page(self):
        self.click_on_element(self._dashboard, "link")

    def navigate_to_directory_page(self):
        self.click_on_element(self._directory, "link")

    def navigate_to_maintenance_page(self):
        self.click_on_element(self._maintenance, "link")

    def navigate_to_buzz_page(self):
        self.click_on_element(self._buzz, "link")


