#Caroline Jenewein
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MFSCRM_ATS():

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\Caroline\Documents\python\shepherd_test_environment\myvenv\Scripts\chromedriver.exe")
        driver = self.driver
        driver.maximize_window()
        driver.get("https://foodservice-cj.herokuapp.com/")
        time.sleep(2)

    def test_login(self, user, pwd):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def test_logout(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/ul/li/a").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
