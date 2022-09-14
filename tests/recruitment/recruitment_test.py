from pages.home.login_page import LoginPage
from pages.side_nav_panel.side_nav_page import SideNavPage
from pages.recruitment.recruitment_page import RecruitmentPage
from utilities.test_status import TestStatus
from utilities.logger import logger
import logging
import unittest
import pytest

@pytest.mark.usefixtures("sessionSetUp")
class RecruitmentTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, sessionSetUp):
        self.lp = LoginPage(self.driver)
        self.np = SideNavPage(self.driver)
        self.rp = RecruitmentPage(self.driver)
        self.ts = TestStatus(self.driver)


    def test_correct_required_fields_data_TCRP001(self, first_name="Stan", last_name="Smith", email="stan_smith@gmail.com"):
        self.lp.fill_the_login_form("Admin", "admin123")
        self.np.navigate_to_recruitment_page()
        self.rp.add_new_candidate(first_name, last_name, email)
        result1 = self.rp.verify_success_toast_message_appeared()
        self.ts.mark_final("Successfully add new candidate", result1, "New candidate was successfully added")