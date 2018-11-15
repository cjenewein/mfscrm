#Caroline Jenewein
import unittest
import time
from mfscrm.tests.base_ATS import MFSCRM_ATS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Product_ATS(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        MFSCRM_ATS.setUp(inst)
        user = "cjenewein"
        pwd = "development"
        MFSCRM_ATS.test_login(inst, user, pwd)

    def test_add_product(self):
        custname = "Bill Davis"
        product = "Apple pie"
        description = "Delicious homemade pie!"
        quantity = "40"
        pickup_time = "2018-12-03 12:00"
        charge = "200.00"
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[4]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)
        select = Select(driver.find_element_by_xpath('//*[@id="id_cust_name"]'))
        select.select_by_visible_text(custname)
        elem = driver.find_element_by_id("id_product")
        elem.send_keys(product)
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys(description)
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys(quantity)
        driver.find_element_by_id("id_pickup_time").clear()
        elem = driver.find_element_by_id("id_pickup_time")
        elem.send_keys(pickup_time)
        elem = driver.find_element_by_id("id_charge")
        elem.send_keys(charge)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def test_edit_product(self):
        quantity = "35"
        charge = "180.00"
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[4]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[8]/a").click()
        time.sleep(2)
        driver.find_element_by_id("id_quantity").clear()
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys(quantity)
        driver.find_element_by_id("id_charge").clear()
        elem = driver.find_element_by_id("id_charge")
        elem.send_keys(charge)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def test_delete_product(self):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[4]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[9]/a").click()
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
