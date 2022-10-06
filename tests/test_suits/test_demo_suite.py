import unittest
from tests.home.login_test import LoginTest
from tests.recruitment.candidates_test import RecruitmentTest


# Loading test cases from test classes to execute in the current test suite

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RecruitmentTest)


# Creating a test suite combining all test classes
demoTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(demoTest)