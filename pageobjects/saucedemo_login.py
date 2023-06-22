from selenium.webdriver.common.by import By
from pageobjects.webelements import Webelements
from selenium.webdriver.support.ui import Select

class Sauce_Demo(Webelements):

    def __init__(self, driver):
        self.driver = driver

    def geturl(self, url):
        self.driver.get(url)

    def setusername(self, username):
        self.driver.find_element(By.ID, self.input_username_id).clear()
        self.driver.find_element(By.ID, self.input_username_id).send_keys(username)
        self.wait(2)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.input_password_id).clear()
        self.driver.find_element(By.ID, self.input_password_id).send_keys(password)
        self.wait(2)

    def loginconfirm(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()
        self.wait(2)

    def login_saucedemo(self, url, username, password):
        self.geturl(url)
        self.setusername(username)
        self.setpassword(password)
        self.loginconfirm()




