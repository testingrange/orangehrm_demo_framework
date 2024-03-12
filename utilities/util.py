import time
from traceback import print_stack

from utilities.logger import logger
import logging

class Util():

    log = logger(logging.INFO)

    def date_stamp(self):
        return str(time.strftime("%Y%m%d_"))

    def date_time_stamp(self):
        return str(time.strftime("%Y%m%d_%H%M%S"))

    def current_day(self):
        return str(time.strftime("%Y-%m-%d"))

    def verify_text_match(self, expected_text, actual_text):
        if expected_text.lower() == actual_text.lower():
            self.log.info(f"Expected_text - {expected_text} has matched")
            return True
        else:
            self.log.info(f"Expected_text - {expected_text} has not matched")
            return False

    def verify_text_contain(self, expected_text, actual_text):
        pass

    def verification_message(self, message):
        message_list = message.split()
        is_pos = message_list.index('is')
        message_list.insert(is_pos+1, 'NOT')
        return " ".join(message_list)

    def sleep(self, sec, info=None):
        """
        Put execution of the script to wait for sertain time in seconds
        :param sec:
        :param info:
        :return:
        """
        try:
            if info is not None:
                self.log.info(f"Sleep for {str(sec)} seconds for {info}")
            else:
                self.log.info(f"Sleep for {str(sec)} seconds")
            time.sleep(sec)
        except:
            self.log.error("Exception occurred while executing sleep command")
            print_stack()




