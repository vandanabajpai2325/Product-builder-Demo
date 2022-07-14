from calendar import WEDNESDAY
import pytest 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

# params=["chrome" , "firefox"] ,
@pytest.fixture(scope="class")
def init_driver(request):
    # if request.params=="chrome":
    web_driver=webdriver.Chrome(ChromeDriverManager().install())

    # if request.params=="firefox":
    #     web_driver=webdriver.Firefox(ChromeDriverManager().install())

    request.cls.driver= web_driver
    web_driver.delete_all_cookies()
    web_driver.implicitly_wait(50)
    web_driver.maximize_window()
    yield
    # web_driver.close()
