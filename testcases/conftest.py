import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    print("Launching browser")
    return driver