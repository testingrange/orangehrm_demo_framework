# Project: Automation testing framework for orangehrm_demo app (Selenium, Python, Pytest)

## Description:
![img.png](orange_hrm.png)

Automation testing framework built for the purpose of demonstration of Selenium framework testing capabilities. For this project I'm using [demoOrange HRM application](https://opensource-demo.orangehrmlive.com/) as application under test. 
Demo Orange HRM is a demo application of a well known HR management application.

### About Orange HRM:
["Orange HRM"](https://www.orangehrm.com/) is a popular open-source human resource management (HRM) software designed to help organizations manage their human resources effectively. It offers a range of features and functionalities to streamline various HR processes, including employee recruitment, onboarding, attendance tracking, leave management, performance evaluation, time and project management, payroll processing, and more.

### About testing framework:
![img.png](selenium.png)

This is a [Selenium version 3](https://www.selenium.dev/documentation/legacy/selenium_3/) testing framework designed specifically for testing the Orange HRM application but might be adapted for testing another web application as well.

For this testing framework I'm using Selenium version 3 Webdriver, which is a popular open-source framework for automating web browser interactions, primarily used for testing web applications. Selenium is powerfull, well-maintained, supported by major browsers, free to use and can be used with many programming languages. In this project I'm using it with [Python](https://www.python.org/) 

The framework adopts the Page Object Model design pattern. This pattern involves creating separate classes (page objects) that encapsulate the structure and behavior of individual web pages or components within the application. This approach enhances maintainability and readability of the test scripts.

Reporting is implemented in the framework by using [pytest-html](https://pypi.org/project/pytest-html/) pytest plugin to generate comprehensive test execution reports, detailing the pass/fail status of test cases and any errors encountered during testing. [Logging](https://docs.python.org/3/library/logging.html) functionality also implemented in the framework to capture relevant information during test execution.

The framework supports executing test cases individually, as well as in test suites, to allow for efficient and organized test runs.

The framework can be easily integrated with CI/CD systems like Jenkins or Travis CI, allowing for automated testing as part of the development pipeline.

Parallel execution of test cases in this framework implemented by [pytest-xdist](https://pypi.org/project/pytest-xdist/) plugin. The framework might offer ways to execute tests in parallel across different browsers or devices.

All the external libraries for reliability of the framework indicated in the [Pipfile](Pipfile)

#### Test Cases in the framework:


#### How to run the script:
The code can be launched directly with cli or with Jenkins or other CI/CD tool. After execution of the code the test report file is generated in html format. Log file is recording during the execution of the code and stored in reports folder and named according to the following format <yyyymmdd_automation_session.log>.

Current version of webdriver for browsers should be installed and stored to system variable.

Before executing the test script, project should be installed into directory and its directory need to be stored to pythonpath variable which should be stored into system variable.
If path to the project is not stored into system variable following command - 'set PYTHONPATH=%PYTHONPATH%;%CD%' should be used from the project directory before running the script.

To execute all test cases script, change working directory to the one with the project and use following cli command - ```pytest -v tests/test_suits/test_demo_suite.py --browser <browser_name> --html=reports/testreport_<mmddyy>.html```

Parameters for browsers names: 'chrome', 'firefox', 'ie' for Chrome, Firefox Mozilla and Internet Explorer browsers.

#### Test results:
