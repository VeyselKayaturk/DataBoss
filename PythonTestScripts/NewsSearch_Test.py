from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import unittest
from Pages.LoginPage import LoginPage


class NewsSearch(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.driver = webdriver.Chrome("./chromedriver.exe")
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
            cls.driver.get("https://hava.data-boss.com.tr/signin")

        def test_news_search(self):
            login = LoginPage(self.driver)
            login.enter_username("testUser")
            login.enter_password("testUser.10")
            login.click_login()

            self.driver.find_element(By.CSS_SELECTOR, 'a[href="/simple-search"]').click()
            time.sleep(2)

            # assert user is on Simple Search page
            element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[1]/div[2]/div[1]/div[2]")
            print(element.text)
            assert element.text == "Simple Search"

            self.driver.find_element(By.XPATH, '//*[@id="search-tab"]/div/div/div[2]/div/div/div/div/div/div/img').click()
            time.sleep(3)
            # assert opened Options includes 'Eksisozluk' and 'News'
            openedOptions = self.driver.find_elements(By.CLASS_NAME, 'ant-select-dropdown-menu-item')
            print(openedOptions[0].text)
            print(openedOptions[1].text)
            assert openedOptions[0].text == "Eksisozluk"
            assert openedOptions[1].text == "News"

            openedOptions[1].click()  # select News from opened slectionbox
            time.sleep(3)

            # click on anywhere (DataBoss logo) to close dropdown menü and focus to serrch button
            self.driver.find_element(By.XPATH, '//*[@id="search-tab"]/div/div/div[1]/img').click()

            # click on seach button to navigate search results page
            self.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/section/div[1]/div[2]/div[2]/div/div/div/div[2]/span/span').click()
            time.sleep(3)

            # search specific tag/index from search result page
            self.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/section/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/span/input').send_keys(
                "Marsilya'dan Gustavo açıklaması: Zor durumdayız")

            self.driver.find_element(By.XPATH, '//*[@id="search-tab"]/div[1]/div/div[2]/span/span').click()
            time.sleep(3)

            contentisExist = self.driver.find_element_by_xpath(
                '//*[@id="content-tab"]/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]')
            print(contentisExist.text)
            assert contentisExist.text == "Marsilya'dan Gustavo açıklaması: Zor durumdayız"

        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()

if __name__ == "__main__":
    unittest.main()