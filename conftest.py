import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import HomePageLocators
from my_data import *


@pytest.fixture(scope="function")
def driver_setup():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def setup_home_page(driver_setup):
    driver = driver_setup
    driver.maximize_window()
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_all_elements_located(HomePageLocators.HOME_PAGE)
    )
    yield driver
