import inspect
import logging
import os
import time
from selenium import webdriver

date_stamp = time.strftime("%Y%m%d_")

def logger(logLevel=logging.INFO, logName=f"{date_stamp}automation_session.log"):
    loggerName = inspect.stack()[1][3]

    logger = logging.getLogger(loggerName)
    logger.setLevel(logLevel)

    # Creating directory for log file
    project_directory = os.getcwd()
    logger_directory = project_directory+"/reports/"
    if not os.path.exists(logger_directory):
        os.makedirs(logger_directory)

    # Creating filehandler
    fileHandler = logging.FileHandler(f"{logger_directory}{logName}", mode="a")
    fileHandler.setLevel(logLevel)

    # Creating formatter
    formatter = logging.Formatter("%(asctime)s- %(name)s- %(levelname)s- %(message)s", datefmt="%Y/%m/%d_%H:%M:%S")

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
