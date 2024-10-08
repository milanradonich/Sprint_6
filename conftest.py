import pytest

from selenium import webdriver
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
    yield driver
    driver.quit()
