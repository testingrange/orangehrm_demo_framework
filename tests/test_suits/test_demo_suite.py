import unittest
from tests.home.login_test import LoginTest
from tests.recruitment.candidates_test import CandidatesTest


# Loading test cases from test classes to execute in the current test suite

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CandidatesTest)


# Creating a test suite combining all test classes
demoTest = unittest.TestSuite([tc1, tc2])
#smokeTest = unittest.TestSuite([tc1])

#
# unittest.TextTestRunner(verbosity=2).run(tc1)
unittest.TextTestRunner(verbosity=2).run(demoTest)