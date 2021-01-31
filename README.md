
## DataBoss Assignment
 **Python Test Automation**
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

**JMeter Load Test Result**
Download and extract "JMeter Test Result" folder and go to bin folder. 
- There can be opened in JMeter from "GetEmployeeData.jmx" file. 
- Test Result and reports are inside of `.bin->HTMLReports->index.html` with graphical and detailed visual materials
- There is also produced a csv file on  `.bin->TestReport1.csv`