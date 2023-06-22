import allure
import pytest
from selenium.webdriver.common.by import By
from pageobjects.saucedemo_login import Sauce_Demo
from pageobjects.saucedemo_order import Saucedemo_order
from pageobjects.webelements import Webelements
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen

class Test_Saucedemo(Webelements):
    logger = LogGen.test_logDemo()
    baseURL = ReadConfig.getAPPURL()
    Uname1 = ReadConfig.getusename1()
    Uname2 = ReadConfig.getusename2()
    Pword = ReadConfig.getpassword()

    # Testcase 1
    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_success_login(self, setup):
        self.driver = setup
        self.lp = Sauce_Demo(self.driver)
        self.lp.login_saucedemo(url=self.baseURL, username=self.Uname1, password=self.Pword)
        if self.driver.find_element(By.XPATH, self.act_logo).is_displayed():
            self.logger.info("********* TestCase-1 (test_success_login) Passed *******")
            self.driver.save_screenshot("/Users/ganeshkumar/PycharmProjects/Sauce_Demo/screenshots/test_success_login.png")
            assert True
        else:
            self.logger.info("********* TestCase-1 (test_success_login) failed *******")
            assert False
        self.driver.quit()

    # Testcase 2
    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_fail_login(self, setup):
        self.driver = setup
        self.lp = Sauce_Demo(self.driver)
        self.lp.login_saucedemo(url=self.baseURL, username=self.Uname2, password=self.Pword)
        value = self.driver.find_element(By.XPATH, "//div[@class='error-message-container error']/h3[1]")
        error_message = value.text
        if error_message == self.act_error_msg:
            self.logger.info("********* TestCase-2 (test_fail_login) Passed *******")
            self.driver.save_screenshot("/Users/ganeshkumar/PycharmProjects/Sauce_Demo/screenshots/test_fail_login.png")
            assert True
        else:
            self.logger.info("********* TestCase-2 (test_fail_login) failed *******")
            assert False
        self.driver.quit()

    # Testcase 3
    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_product(self, setup):
        self.driver = setup
        self.lp = Sauce_Demo(self.driver)
        self.order = Saucedemo_order(self.driver)
        self.lp.login_saucedemo(url=self.baseURL, username=self.Uname1, password=self.Pword)
        self.order.order_product(fname=self.fname, lname=self.lname, zip_code=self.zip_code, act_value=self.act_value)
        check_out_complete = self.driver.find_element(By.XPATH, self.check_out_complete_xpath)
        complete_msg = check_out_complete.text
        if complete_msg == self.check_out_msg:
            self.logger.info("********* TestCase-3 (test_order_product) Passed *******")
            self.driver.save_screenshot(
                "/Users/ganeshkumar/PycharmProjects/Sauce_Demo/screenshots/test_order_product.png")
            assert True
        else:
            self.logger.info("********* TestCase-3 (test_order_product) failed *******")
            assert False
        self.driver.quit()
