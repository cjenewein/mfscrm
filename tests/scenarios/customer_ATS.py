#Caroline Jenewein
import unittest
import time
from mfscrm.tests.base_ATS import MFSCRM_ATS
from selenium.webdriver.common.keys import Keys

class Customer_ATS(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        MFSCRM_ATS.setUp(inst)
        user = "cjenewein"
        pwd = "development"
        MFSCRM_ATS.test_login(inst, user, pwd)

    def test_add_customer(self):
        custname = "Lana Lane"
        organ = "Daily Planet"
        role = "journalist"
        bldg = "110 Mammel"
        account = "899"
        address = "8602 University Drive South"
        city = "Omaha"
        state = "Nebraska"
        zip = "68182"
        email = "lana.lane@dailyplanet.com"
        phone = "402789876"
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys(custname)
        elem = driver.find_element_by_id("id_organization")
        elem.send_keys(organ)
        elem = driver.find_element_by_id("id_role")
        elem.send_keys(role)
        elem = driver.find_element_by_id("id_bldgroom")
        elem.send_keys(bldg)
        elem = driver.find_element_by_id("id_account_number")
        elem.send_keys(account)
        elem = driver.find_element_by_id("id_address")
        elem.send_keys(address)
        elem = driver.find_element_by_id("id_city")
        elem.send_keys(city)
        elem = driver.find_element_by_id("id_state")
        elem.send_keys(state)
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys(zip)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email)
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys(phone)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def test_edit_customer(self):
        role = "reporter"
        bldg = "PKI 8"
        phone = "402789822"
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[12]/a").click()
        time.sleep(2)
        driver.find_element_by_id("id_role").clear()
        elem = driver.find_element_by_id("id_role")
        elem.send_keys(role)
        driver.find_element_by_id("id_bldgroom").clear()
        elem = driver.find_element_by_id("id_bldgroom")
        elem.send_keys(bldg)
        driver.find_element_by_id("id_phone_number").clear()
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys(phone)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def test_summary_customer(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[14]/a").click()
        time.sleep(5)

    def test_delete_customer(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[13]/a").click()
        time.sleep(1)
        alert_obj = driver.switch_to.alert
        time.sleep(1)
        alert_obj.accept()
        time.sleep(2)

    @classmethod
    def tearDownClass(inst):
        MFSCRM_ATS.test_logout(inst)
        MFSCRM_ATS.tearDown(inst)

if __name__ == "__main__":
    unittest.main()
