from base.selenium_driver import SeleniumDriver as SD
from utilities.logger import logger
import logging


class TestStatus(SD):

    log = logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.resultList = []

    def set_result(self, result, result_message):
        """Module to add a result to a list of all test results"""
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info(f"VERIFICATION SUCCESSFUL :: {result_message}")
                else:
                    self.resultList.append("FAIL")
                    self.screenshot(result_message)
                    self.log.error(f"VERIFICATION FAILED :: {self.util.verification_message(result_message)}")
            else:
                self.resultList.append("FAIL")
                self.screenshot(result_message)
                self.log.error(f"VERIFICATION FAILED :: {{self.util.verification_message(result_message)}}")
        except:
            self.resultList.append("FAIL")
            self.screenshot(self.util.verification_message(result_message))
            self.log.error(f"Exception occurred while trying to get a test result :: {self.util.verification_message(result_message)}")

    def mark(self, result, result_message):
        """
        Module to mark a result of a test
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be the final test status of the test case
        """
        self.set_result(result, result_message)

        if "FAIL" in self.resultList:
            self.log.error(f"{test_name} failed")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(f"{test_name} successfullly completed")
            self.resultList.clear()
            assert True == True
