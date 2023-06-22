from selenium.webdriver.common.by import By
from pageobjects.webelements import Webelements
from selenium.webdriver.support.ui import Select


class Saucedemo_order(Webelements):

    def __init__(self, driver):
        self.driver = driver

    def order_product(self, fname, lname, zip_code, act_value):
        drop = Select(self.driver.find_element(By.XPATH, self.select_product_xpath))
        drop.select_by_visible_text(self.value)
        self.driver.find_element(By.XPATH, self.btn_add_cart_xpath).click()
        self.wait(2)
        self.driver.find_element(By.XPATH, self.cart_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_chk_out_xpath).click()
        self.wait(1)
        self.driver.find_element(By.ID, self.input_fname_id).send_keys(fname)
        self.driver.find_element(By.ID, self.input_lname_id).send_keys(lname)
        self.driver.find_element(By.ID, self.input_zip_id).send_keys(zip_code)
        continue_button = self.driver.find_element(By.ID, self.btn_continue_id)
        self.driver.execute_script("arguments[0].scrollIntoView();", continue_button)
        continue_button.click()
        self.wait(1)
        total_value = self.driver.find_element(By.XPATH, self.total_value_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", total_value)
        total_value_txt = total_value.text
        if total_value_txt == act_value:
            print("cost: " + total_value_txt)
        else:
            print("Total value is not correct")
            self.driver.close()
        self.driver.find_element(By.ID, self.btn_finish_id).click()
