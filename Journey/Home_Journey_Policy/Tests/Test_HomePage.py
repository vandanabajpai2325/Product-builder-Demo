
from multiprocessing.spawn import import_main_path
from os import symlink
from sre_constants import ASSERT
from turtle import title
from unittest import BaseTestSuite
import sys

sys.path.insert(0 , '../../Home_Journey_Policy/Pages')

# from BasePage import BasePage
from HomePage  import HomePage
sys.path.insert(0 , '../../Home_Journey_Policy/Config')
from Config import TestData
from Test_Base import BaseTest
#import TestDataclear

class Test_HomePage(BaseTest):
    
    def test_home_page_title_visible(self):
        self.HomePage=HomePage(self.driver)
        title = self.HomePage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE




