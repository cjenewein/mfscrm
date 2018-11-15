#Caroline Jenewein
import unittest
import time
from mfscrm.tests.base_ATS import MFSCRM_ATS
from mfscrm.tests.library.GetData import get_csv_data
from ddt import ddt, data, unpack
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

@ddt
class Product_CSV_ATS(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        MFSCRM_ATS.setUp(inst)
        user = "cjenewein"
        pwd = "development"
        MFSCRM_ATS.test_login(inst, user, pwd)

    @data(*get_csv_data('products.csv'))
    @unpack
    def test_add_product(self, custname, product, description, quantity, pickup_time, charge):
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


    @classmethod
    def tearDownClass(inst):
        MFSCRM_ATS.test_logout(inst)
        MFSCRM_ATS.tearDown(inst)

if __name__ == "__main__":
    unittest.main()
