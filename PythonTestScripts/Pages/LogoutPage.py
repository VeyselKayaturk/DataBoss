from selenium.webdriver.common.by import By
import time

class LogoutPage():

    def __init__(self, driver):
        self.driver = driver

    def logout_from_system(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/section/aside/div/ul/li[2]/ul/li[3]").click()
        time.sleep(3)

        element = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/button[2]")
        print(element.text)
        assert element.text == "Login with LDAP"