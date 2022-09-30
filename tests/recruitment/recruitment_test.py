from pages.home.login_page import LoginPage
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
        self.rp = RecruitmentPage(self.driver)
        self.ts = TestStatus(self.driver)


    def test_correct_required_fields_data_TCRP001(self, first_name="Stan", last_name="Smith", email="stan_smith@gmail.com"):
        self.rp.log_in_to_app()
        self.rp.add_new_candidate(first_name, last_name, email)
        result1 = self.rp.verify_success_toast_message_appeared()
        self.ts.mark(result1, "Success message is present")
        result2 = self.rp.verify_record_exists(first_name, last_name)
        self.ts.mark_final("Successfully add new candidate", result2, "New candidate record is present")

    def test_correct_required_fields_data_TCRP00601(self, first_name="Adam", last_name="Jonson", email="apjonson@gmail.com", middle_name="Peter", contact_number="(999) 123-45-67", vacancy_name="Associate IT Manager", keywords="associate, it, manager", date="2022-09-01", notes="Test test test", consent="v"):
        self.rp.add_new_candidate(first_name, last_name, email, middle_name, contact_number, vacancy_name, keywords, date, notes, consent)
        result1 = self.rp.verify_success_toast_message_appeared()
        self.ts.mark(result1, "Success message is present")
        result2 = self.rp.verify_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark_final("Successfully add new candidate", result2, "New candidate record is present")

    def test_correct_required_fields_data_TCRP00602(self, first_name="Steven", last_name="Jonson", email="sjonson@gmail.com", middle_name="Jeremy", contact_number="(999) 123-45-67", vacancy_name="Senior QA Lead", keywords="associate, it, manager", date="2022-09-01", notes="Test test test", consent="v"):
        self.rp.add_new_candidate(first_name, last_name, email, middle_name, contact_number, vacancy_name, keywords, date, notes, consent)
        result1 = self.rp.verify_success_toast_message_appeared()
        self.ts.mark(result1, "Success message is present")
        result2 = self.rp.verify_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark_final("Successfully add new candidate", result2, "New candidate record is present")

    def test_correct_required_fields_data_TCRP00603(self, first_name="Adam", last_name="Peterson", email="peterson@gmail.com", middle_name="James", contact_number="(999) 234-54-76", vacancy_name="VP - Sales & Marketing", keywords="associate, it, manager", date="2022-09-01", notes="Test test test", consent="v"):
        self.rp.add_new_candidate(first_name, last_name, email, middle_name, contact_number, vacancy_name, keywords, date, notes, consent)
        result1 = self.rp.verify_success_toast_message_appeared()
        self.ts.mark(result1, "Success message is present")
        result2 = self.rp.verify_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark_final("Successfully add new candidate", result2, "New candidate record is present")