#Caroline Jenewein
import unittest
import time
from mfscrm.tests.base_ATS import MFSCRM_ATS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Service_ATS(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        MFSCRM_ATS.setUp(inst)
        user = "cjenewein"
        pwd = "development"
        MFSCRM_ATS.test_login(inst, user, pwd)

    def test_add_service(self):
        custname = "Bill Davis"
        service = "Dinner for two"
        description = "Delicious dinner!"
        location = "PKI 240"
        setup_time = "2018-12-03 12:00"
        cleanup_time = "2018-12-03 19:00"
        charge = "400.00"
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[3]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)
        select = Select(driver.find_element_by_xpath('//*[@id="id_cust_name"]'))
        select.select_by_visible_text(custname)
        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys(service)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys(description)
        elem = driver.find_element_by_id("id_location")
        elem.send_keys(location)
        driver.find_element_by_id("id_setup_time").clear()
        elem = driver.find_element_by_id("id_setup_time")
        elem.send_keys(setup_time)
        driver.find_element_by_id("id_cleanup_time").clear()
        elem = driver.find_element_by_id("id_cleanup_time")
        elem.send_keys(cleanup_time)
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys(charge)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def test_edit_service(self):
        cleanup_time = "2018-12-03 22:00"
        charge = "440.00"
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[3]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[6]/td[8]/a").click()
        time.sleep(2)
        driver.find_element_by_id("id_cleanup_time").clear()
        elem = driver.find_element_by_id("id_cleanup_time")
        elem.send_keys(cleanup_time)
        driver.find_element_by_id("id_service_charge").clear()
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys(charge)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def test_delete_service(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[3]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[6]/td[9]/a").click()
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
