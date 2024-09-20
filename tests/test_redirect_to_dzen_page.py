from selenium.webdriver.support.wait import WebDriverWait
from locators.header_locators import HeaderLocators
from selenium.webdriver.support import expected_conditions as EC
from my_data import *
from pages.order_page import OrderPage


class TestRedirectToDzenPage:
    def test_redirect_to_dzen_page(self, driver_setup):
        """проверка, что при нажатии на лого яндекс откроется новая вкладка dzen"""
        driver = driver_setup
        order_page = OrderPage(driver)
        order_page.click_element(HeaderLocators.BTN_ORDER_HEADER)
        order_page.click_element(HeaderLocators.LINK_LOGO)
        wait = WebDriverWait(driver, 10)
        original_window = driver.current_window_handle
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        wait.until(EC.title_contains(DZEN_TITLE))
        expected_url = DZEN_URL
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Ожидался URL: {expected_url}, но получен: {actual_url}"
