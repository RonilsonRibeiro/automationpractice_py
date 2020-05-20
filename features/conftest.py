import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pathlib import Path 
import yaml


# Inicia o driver para rodar local
@pytest.fixture
def driver():     
    options = Options()
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(executable_path = "driver/chromedriver.exe", options=options)      
    driver.maximize_window()
    driver.implicitly_wait(10)        
    yield driver
    driver.quit()


