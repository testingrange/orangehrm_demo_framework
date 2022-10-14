# orangehrm_demo_framework

Orange HRM application automation testing framework demoOrange HRM application automation testing framework demo

A demo automation testing framework for a well known HR management application "Orange HRM" it's demo web app. This is on going project on github where I'm adding more functionality over time. The framework is built with
following technologies - Python, Selenium Webdriver, Pytest and Unittest. Information about current version of required packages as well as current python version 
can be found in Pipfile. 

The code can be launched directly with cli or with Jenkins or other CI/CD tool. After execution of the code the test report file is generated in html format. Log file is recording during the execution of the code and stored in reports folder and named according to the following format <yyyymmdd_automation_session.log>.

Current version of webdriver for browsers should be installed and stored to system variable.

To execute all test cases script, change working directory to the one with the project and use following cli command - pytest -v tests/test_suits/test_demo_suite.py --browser <browser_name> --html=reports/testreport_<mmddyy>.html

Parameters for browsers names: 'chrome', 'firefox', 'ie' for Chrome, Firefox Mozilla and Internet Explorer browsers.

