## DataBoss Assignment
**1. Test Cases / Scenarios**
 - Test cases are written on .docx files. There can be downloaded directly from git repository.  I wrote 6 short and basic scenarios to make easy understanding. Those scenarios cover all wanted features on assignment.
 
**2. Python Test Automation**
**Versions**
 - Python 3.9
 - Selenium 9.141.0
 - Chrome 87.0.4280.141
 - testRunner : jinja2.11.2
 
**Running from Command Line/Terminal:** Running Command Go to project path first then type `python testclassName.py` command to run tests. 
For example; successful login can be run with `python SuccessfulLogin_Test.py`

**Running from IDE:** Pull the entire project from git repository and open with any IDE (I worked on PyCharm ) and run through IDE. Becasue I wrote the test classes as a unittest classes there should created run configuration as follows;
Go to `Run-> Edit Configurations ->Python Test`  and then click on "+" button at above. Then select `Python Test ->Unittest` and add the class run configuration for all test classes. 

**İmportant Notes:**

 - I used POM (Page Object Model) Design Pattern to obstruct code repetition. Also thanks to POM written line of code was decreased. 
 - I do not made Docker entegration due to time limits
 - I used Hookes in test classes
 - I parametrized the login methods
 - I wrote some assertions in test classes

**3. JMeter Load Test Result**
Open JMeter folder from git repository first;
- The project can be opened from "GetEmployeeData.jmx" file.  Test is done for GET, PUSH, PUT and DELETE http requests.
- Test Result and reports are inside of `HTMLReports->index.html` with graphical and detailed visual materials
- There is also produced a csv file on  `TestReport1.csv`