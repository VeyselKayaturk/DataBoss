from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage


class UnsuccessfulLogin(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.driver = webdriver.Chrome("./chromedriver.exe")
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
            cls.driver.get("https://hava.data-boss.com.tr/signin")

        def test_login_invalid(self):
            login = LoginPage(self.driver)
            login.enter_username("DataBoss")
            login.enter_password("DataBoss.10")
            login.click_login()
            element = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/span/div/div/div")
            print(element.text)
            assert element.text == "400:Kullanıcı adı veya şifre hatalı."

        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
