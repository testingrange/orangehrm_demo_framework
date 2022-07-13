import time
from utilities.logger import logger
import logging

class Util():

    log = logger(logging.INFO)

    def date_stamp(self):
        return str(time.strftime("%Y%m%d_"))

    def date_time_stamp(self):
        return str(time.strftime("%Y%m%d_%H%M%S"))

    def verify_text_match(self, expected_text, actual_text):
        if expected_text.lower() == actual_text.lower():
            self.log.info(f"Expected_text - {expected_text} has matched")
            return True
        else:
            self.log.info(f"Expected_text - {expected_text} has not matched")
            return False

    def verification_message(self, message):
        message_list = message.split()
        is_pos = message_list.index('is')
        message_list.insert(is_pos+1, "NOT")
        return " ".join(message_list)



