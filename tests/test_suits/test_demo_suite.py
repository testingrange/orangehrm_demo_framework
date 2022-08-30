import unittest
from tests.home.login_test import LoginTest


# Loading test cases from test classes to execute in the current test suite

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)



# Creating a test suite combining all test classes
demoTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(demoTest)