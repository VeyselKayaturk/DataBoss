from selenium import webdriver
import time
import unittest

from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage
from Pages.LogoutPage import LogoutPage


class Logout(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.driver = webdriver.Chrome("./chromedriver.exe")
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
            cls.driver.get("https://hava.data-boss.com.tr/signin")

        def test_logout(self):
            login = LoginPage(self.driver)
            login.enter_username("testUser")
            login.enter_password("testUser.10")
            login.click_login()
            time.sleep(3)
            dashboard = DashboardPage(self.driver)
            dashboard.dashboardPageİsOpened()
            time.sleep(3)
            logout = LogoutPage(self.driver)
            logout.logout_from_system()

        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()

if __name__ == "__main__":
    unittest.main()