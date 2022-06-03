import inspect
import logging
import os
from selenium import webdriver
from utilities.util import time_stamp


def logger(logLevel=logging.INFO, logName=f"{time_stamp()}automation_session.log"):
    loggerName = inspect.stack()[1][3]

    logger = logging.getLogger(loggerName)
    logger.setLevel(logLevel)

    # Creating directory for log file
    project_directory = os.getcwd()
    logger_directory = project_directory+"/reports/"
    if not os.path.exists(logger_directory):
        os.makedirs(logger_directory)

    # Creating filehandler
    fileHangler = logging.FileHandler(f"{logger_directory}{logName}", mode="a")
    fileHangler.setLevel(logLevel)

    # Creating formatter
    formatter = logging.Formatter("%(asctime)s- %(name)s- %(levelname)s- %(message)s", datefmt="%Y/%m/%d_%H:%M:%S")

    fileHangler.setFormatter(formatter)
    logger.addHandler(fileHangler)
    return logger
