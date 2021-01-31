from selenium.webdriver.common.by import By
import time

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.userName = "username"
        self.pswrd = "password"

    def enter_username(self, usrname):
        self.driver.find_element_by_id(self.userName).send_keys(usrname)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.pswrd).send_keys(password)

    def enter_username_and_password(self, usrname, password):
        self.driver.find_element_by_id(self.userName, self.pswrd).send_keys(usrname, password)

    def click_login(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/button[1]").click()
        time.sleep(2)
