#Caroline Jenewein
import unittest
import time
from mfscrm.tests.base_ATS import MFSCRM_ATS
from selenium.webdriver.common.keys import Keys

class User_ATS(unittest.TestCase):
    global user
    global pwd
    global email
    global firstname
    global lastname
    global birth
    global new_pwd

    #User information
    user = "batman"
    pwd = "gotham"
    new_pwd = "spiderman"
    email = "gotham@city.com"
    firstname = "Bruce"
    lastname = "Wayne"
    birth = "03/05/1989"

    @classmethod
    def setUpClass(inst):
        MFSCRM_ATS.setUp(inst)

    def test_register_user(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/p/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys(firstname)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys(pwd)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        MFSCRM_ATS.test_login(self, user, pwd)

    def test_edit_profile(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/p[1]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys(lastname)
        elem = driver.find_element_by_id("id_date_of_birth")
        elem.send_keys(birth)
        driver.find_element_by_xpath("/html/body/div/div/div/form/p/input").click()
        time.sleep(1)
        driver.get("https://foodservice-cj.herokuapp.com/home/")
        time.sleep(2)

    def test_change_password(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/p[2]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_old_password")
        elem.send_keys(pwd)
        elem = driver.find_element_by_id("id_new_password1")
        elem.send_keys(new_pwd)
        elem = driver.find_element_by_id("id_new_password2")
        elem.send_keys(new_pwd)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def test_reset_password(self):
        driver = self.driver
        MFSCRM_ATS.test_logout(self)
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div/p/a").click()
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.get("https://mailtrap.io/")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/header/div/div[2]/div/a[1]").click()
        elem = driver.find_element_by_id("user_email")
        elem.send_keys("caroline_jenewein@hotmail.com")
        elem = driver.find_element_by_id("user_password")
        elem.send_keys("development")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td[1]/div[1]/strong/a/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div/ul/li[1]").click()
        time.sleep(10)
        ## pause selenium to use the reset link
        ## extract the link out of the email
        elem = driver.find_element_by_id("id_new_password1")
        elem.send_keys(new_pwd)
        elem = driver.find_element_by_id("id_new_password2")
        elem.send_keys(new_pwd)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/form/p/input").click()
        time.sleep(1)
        MFSCRM_ATS.test_login(self, user, new_pwd)

    @classmethod
    def tearDownClass(inst):
        MFSCRM_ATS.test_logout(inst)
        MFSCRM_ATS.tearDown(inst)

if __name__ == "__main__":
    unittest.main()
