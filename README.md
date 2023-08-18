# Automation testing framework for orangehrm_demo app (Selenium, Python, Pytest)

## Description:
Automation testing framework built for demonstration of capabilities of Selenium framework purposes. For this project [demoOrange HRM application](https://opensource-demo.orangehrmlive.com/) is used to serve as application under test. 
![img.png](orange_hrm.png) 
This app is a demo application of a well known HR management application ["Orange HRM"](https://www.orangehrm.com/) 

### Test Cases in the framework


### How to run the script:
The code can be launched directly with cli or with Jenkins or other CI/CD tool. After execution of the code the test report file is generated in html format. Log file is recording during the execution of the code and stored in reports folder and named according to the following format <yyyymmdd_automation_session.log>.

Current version of webdriver for browsers should be installed and stored to system variable.

Before executing the test script, project should be installed into directory and its directory need to be stored to pythonpath variable which should be stored into system variable.
If path to the project is not stored into system variable following command - 'set PYTHONPATH=%PYTHONPATH%;%CD%' should be used from the project directory before running the script.

To execute all test cases script, change working directory to the one with the project and use following cli command - ```pytest -v tests/test_suits/test_demo_suite.py --browser <browser_name> --html=reports/testreport_<mmddyy>.html```

Parameters for browsers names: 'chrome', 'firefox', 'ie' for Chrome, Firefox Mozilla and Internet Explorer browsers.

