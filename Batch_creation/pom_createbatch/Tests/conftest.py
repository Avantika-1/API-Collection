

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

'''
@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize WebDriver"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


'''

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def test_open_testalogin():
    driver = webdriver.Edge()
    driver.get("https://preprod.testaonline.com/signin")
    time.sleep(100)
    email = driver.find_element(By.CSS_SELECTOR, "[type='email']")
    email.send_keys("abhijeet@radiantinfonet.com")
    email = driver.find_element(By.NAME, "password")
    email.send_keys("Abhijeet@123")
    loginbutton = driver.find_element (By.XPATH, "//button[normalize-space()='Login']")
    loginbutton.click()


    
