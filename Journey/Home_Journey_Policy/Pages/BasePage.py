
from xml.dom.minidom import Element
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

sys.path.insert(0 , '../../Home_Journey_Policy/Config')
from Config import TestData
# this class is the parent of all the page
# it contains all generic method and utilities for all the pages 

class BasePage():
    def __init__(self, driver):
        self.driver = driver
    def do_click(self, by_locator):
        WebDriverWait(self.driver , 10).until(EC.visibility_of_element_located(by_locator)).click()
    
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enable(self , by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title


