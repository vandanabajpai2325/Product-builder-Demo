
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
from BasePage import BasePage
sys.path.insert(0 , '../../Home_Journey_Policy/Config')
from Config import TestData
# this class is the parent of all the page
# it contains all generic method and utilities for all the pages 

class HomePage(BasePage):
    def __init__(self , driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        
# Get the title of the home page 
    def test_home_page_title(self , title):
         return self.driver.get_title(title) 


