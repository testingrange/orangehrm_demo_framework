from pages.home.login_page import LoginPage
from pages.recruitment.candidates_page import CandidatesPage
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
        self.cp = CandidatesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_correct_required_fields_data_TCRP001(self, first_name="Stan", last_name="Smith", email="stan_smith@gmail.com"):
        self.cp.log_in_to_app()
        result1 = self.cp.verify_no_record_exists(first_name, last_name)
        self.ts.mark(result1, "Candidate record is absent before the test")
        self.cp.add_new_candidate(first_name, last_name, email)
        result2 = self.cp.verify_success_toast_message_appeared()
        self.ts.mark(result2, "Success message is present")
        result3 = self.cp.verify_record_exists(first_name, last_name)
        self.ts.mark_final("Successfully add new candidate", result3, "New candidate record is present")

    @pytest.mark.run(order=2)
    def test_correct_required_fields_data_TCRP00601(self, first_name="Adam", last_name="Jonson", email="apjonson@gmail.com", middle_name="Peter", contact_number="(999) 123-45-67", vacancy_name="Associate IT Manager", keywords="associate, it, manager", date="2022-09-01", notes="Test test test", consent="v"):
        result1 = self.cp.verify_no_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark(result1, "Candidate record is absent before the test")
        self.cp.add_new_candidate(first_name, last_name, email, middle_name, contact_number, vacancy_name, keywords, date, notes, consent)
        result2 = self.cp.verify_success_toast_message_appeared()
        self.ts.mark(result2, "Success message is present")
        result3 = self.cp.verify_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark_final("Successfully add new candidate", result3, "New candidate record is present")

    @pytest.mark.run(order=3)
    def test_correct_required_fields_data_TCRP00602(self, first_name="Steven", last_name="Jonson", email="sjonson@gmail.com", middle_name="Jeremy", contact_number="(999) 123-45-67", vacancy_name="Senior QA Lead", keywords="associate, it, manager", date="2022-09-01", notes="Test test test", consent="v"):
        result1 = self.cp.verify_no_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark(result1, "Candidate record is absent before the test")
        self.cp.add_new_candidate(first_name, last_name, email, middle_name, contact_number, vacancy_name, keywords, date, notes, consent)
        result2 = self.cp.verify_success_toast_message_appeared()
        self.ts.mark(result2, "Success message is present")
        result3 = self.cp.verify_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark_final("Successfully add new candidate", result3, "New candidate record is present")

    @pytest.mark.run(order=4)
    def test_correct_required_fields_data_TCRP00603(self, first_name="Adam", last_name="Peterson", email="peterson@gmail.com", middle_name="James", contact_number="(999) 234-54-76", vacancy_name="Software Engineer", keywords="associate, it, manager", date="2022-09-01", notes="Test test test", consent="v"):
        result1 = self.cp.verify_no_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark(result1, "Candidate record is absent before the test")
        self.cp.add_new_candidate(first_name, last_name, email, middle_name, contact_number, vacancy_name, keywords, date, notes, consent)
        result2 = self.cp.verify_success_toast_message_appeared()
        self.ts.mark(result2, "Success message is present")
        result3 = self.cp.verify_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark_final("Successfully add new candidate", result3, "New candidate record is present")

    def test_successful_deleting_existing_record_TC00611(self, first_name="Stan", last_name="Smith", email="stan_smith@gmail.com"):
        result1 = self.cp.verify_record_exists(first_name, last_name)
        self.ts.mark(result1, "Candidate record is present")
        self.cp.delete_existing_record(first_name, last_name)
        result2 = self.cp.verify_no_record_exists(first_name, last_name)
        self.ts.mark_final("Successfully delete existing record", result2, "Candidate record is absent")

    def test_correct_required_fields_data_TCRP006121(self, first_name="Adam", last_name="Jonson",
                                                    email="apjonson@gmail.com", middle_name="Peter",
                                                    contact_number="(999) 123-45-67",
                                                    vacancy_name="Associate IT Manager",
                                                    keywords="associate, it, manager", date="2022-09-01",
                                                    notes="Test test test", consent="v"):
        result1 = self.cp.verify_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark(result1, "Candidate record is present")
        self.cp.delete_existing_record(first_name, last_name, middle_name, vacancy_name, date)
        result2 = self.cp.verify_no_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark_final("Successfully delete existing record", result2, "Candidate record is absent")

    def test_correct_required_fields_data_TCRP006122(self, first_name="Steven", last_name="Jonson",
                                                email="sjonson@gmail.com", middle_name="Jeremy",
                                                contact_number="(999) 123-45-67", vacancy_name="Senior QA Lead",
                                                keywords="associate, it, manager", date="2022-09-01",
                                                notes="Test test test", consent="v"):
        result1 = self.cp.verify_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark(result1, "Candidate record is present")
        self.cp.delete_existing_record(first_name, last_name, middle_name, vacancy_name, date)
        result2 = self.cp.verify_no_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark_final("Successfully delete existing record", result2, "Candidate record is absent")

    def test_correct_required_fields_data_TCRP006123(self, first_name="Adam", last_name="Peterson",
                                                    email="peterson@gmail.com", middle_name="James",
                                                    contact_number="(999) 234-54-76", vacancy_name="Software Engineer",
                                                    keywords="associate, it, manager", date="2022-09-01",
                                                    notes="Test test test", consent="v"):
        result1 = self.cp.verify_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark(result1, "Candidate record is present")
        self.cp.delete_existing_record(first_name, last_name, middle_name, vacancy_name, date)
        result2 = self.cp.verify_no_record_exists(first_name, last_name, middle_name, vacancy_name, date)
        self.ts.mark_final("Successfully delete existing record", result2, "Candidate record is absent")