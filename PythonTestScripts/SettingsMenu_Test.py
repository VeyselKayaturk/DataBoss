from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import unittest

from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage


class SettingMenu(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.driver = webdriver.Chrome("./chromedriver.exe")
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
            cls.driver.get("https://hava.data-boss.com.tr/signin")

        def test_setting_menu(self):
            login = LoginPage(self.driver)
            login.enter_username("testUser")
            login.enter_password("testUser.10")
            login.click_login()
            time.sleep(3)
            dashboard = DashboardPage(self.driver)
            dashboard.dashboardPageİsOpened()
            time.sleep(3)

            self.driver.find_element(By.CSS_SELECTOR, 'a[href="/settings"]').click()
            time.sleep(2)

            #assert user is on Simple Search page
            element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[1]/div[2]/div[1]/div[2]")
            print(element.text)
            assert element.text == "Settings"


            profilePage = self.driver.find_element(By.CLASS_NAME, 'ant-card-head-title')
            assert profilePage.text == 'Profile Page'


            #assert the texts ara exist on the page
            assert self.driver.page_source.find('Username : testUser')
            assert self.driver.page_source.find('Email : test@data-boss.com.tr')
            assert self.driver.page_source.find('Language : en')

        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()

if __name__ == "__main__":
    unittest.main()