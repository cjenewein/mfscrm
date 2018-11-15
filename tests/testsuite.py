import unittest
from mfscrm.tests.scenarios.service_ATS import Service_ATS
from mfscrm.tests.scenarios.product_ATS import Product_ATS
from mfscrm.tests.scenarios.customer_ATS import Customer_ATS
from mfscrm.tests.scenarios.user_ATS import User_ATS

def suite_product():
    suite = unittest.TestSuite()
    suite.addTest(Product_ATS('test_add_product'))
    suite.addTest(Product_ATS('test_edit_product'))
    suite.addTest(Product_ATS('test_delete_product'))
    return suite

def suite_service():
    suite = unittest.TestSuite()
    suite.addTest(Service_ATS('test_add_service'))
    suite.addTest(Service_ATS('test_edit_service'))
    suite.addTest(Service_ATS('test_delete_service'))
    return suite

def suite_customer():
    suite = unittest.TestSuite()
    suite.addTest(Customer_ATS('test_add_customer'))
    suite.addTest(Customer_ATS('test_edit_customer'))
    suite.addTest(Customer_ATS('test_summary_customer'))
    suite.addTest(Customer_ATS('test_delete_customer'))
    return suite

def suite_user():
    suite = unittest.TestSuite()
    suite.addTest(User_ATS('test_register_user'))
    suite.addTest(User_ATS('test_edit_profile'))
    suite.addTest(User_ATS('test_change_password'))
    suite.addTest(User_ATS('test_reset_password'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_product())
    runner.run(suite_service())
    runner.run(suite_customer())
    runner.run(suite_user())

