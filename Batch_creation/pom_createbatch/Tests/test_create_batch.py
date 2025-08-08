import pytest
from selenium import webdriver
from pages.batch_creation import BatchCreation

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_create_batch(driver):
    page = BatchCreation(driver)
    page.open_page("https://preprod.testaonline.com/exam-management/create-batch")
    page.fill_batch_form("B1234", "30", "04/06/2025", "06/06/2025")
    # Add assertions here
