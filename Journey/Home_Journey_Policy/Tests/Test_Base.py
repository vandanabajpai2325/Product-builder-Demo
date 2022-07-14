from ast import Pass
from msilib.schema import Class
import pytest 
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    Pass

    
