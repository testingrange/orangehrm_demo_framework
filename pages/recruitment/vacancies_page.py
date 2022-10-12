from base.basepage import BasePage as BP
from pages.side_nav_panel.side_nav_page import SideNavPage
from pages.home.login_page import LoginPage




class VacanciesPage(BP):

    def __init__(self, driver):
        super.__init__(driver)
        self.driver = driver
        self.lp = LoginPage(driver)
        self.sp = SideNavPage(driver)

    # LOCATORS

    
