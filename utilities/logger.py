import inspect
import logging
import os


def logger(logLevel=logging.INFO, logName=None):
    #Using this method to get name of the class/method from where the logger method is called
    loggerName = inspect.stack()[1][3]
    #creating logger and providing a name
    logger = logging.getLogger(loggerName)

    #Setting a level for logging messages. Taking the level from the arguments
    logger.setLevel(logLevel)

    #creating a variable with project directory
    project_directory = os.getcwd()

    #providing log file name with directory to filehandler and also setting up a mode 'a' - append, 'w' - write
    fileHandler = logging.FileHandler(f"{project_directory}/utilities/logreport/{logName}.log", mode='a')
    #providing a loglevel to fileHandler The log level set up by user in the parameters of the function
    fileHandler.setLevel(logLevel)

    #creating a format of the log message - time in asctime format - name of class/method - level name(DEBUG/INFO/CRITICAL/ERROR - log message
    #datefmt - format of the date stamp that will be provided into log record - year/month/day_hour:minute:seconds
    formatter = logging.Formatter("%(asctime)s- %(name)s- %(levelname)s- %(message)s", datefmt="%Y/%m/%d_%H:%M:%S")
    #providing formatter to the fileHandler
    fileHandler.setFormatter(formatter)
    #adding handler to the logger
    logger.addHandler(fileHandler)
    return logger

