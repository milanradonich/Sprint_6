import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import HomePageLocators
from my_data import *


@pytest.fixture(scope="function")
def driver_setup():
    #driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_all_elements_located(HomePageLocators.HOME_PAGE)
    )
    yield driver
    driver.quit()
