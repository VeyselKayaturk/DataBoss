from selenium.webdriver.common.by import By
import time

class DashboardPage():

    def __init__(self, driver):
        self.driver=driver
        self.dashboardTitleText = "dashboard"

    def dashboardPageİsOpened(self):
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[1]/div[2]/div[1]/div[2]")
        print(element.text)
        assert element.text == "Dashboard"
        time.sleep(3)

