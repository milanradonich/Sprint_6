from locators.header_locators import HeaderLocators
from my_data import BASE_URL
from pages.order_page import OrderPage


class TestRedirectToHomePage:
    def test_redirect_to_home_page(self, driver_setup):
        """проверка, что при нажатии на лого самоката будет переход на главную страницу"""
        driver = driver_setup
        order_page = OrderPage(driver)
        order_page.click_element(HeaderLocators.BTN_ORDER_HEADER)
        order_page.click_element(HeaderLocators.LINK_SCOOTER)
        expected_url = BASE_URL
        actual_url = driver.current_url
        assert actual_url == expected_url, f"Ожидался URL: {expected_url}, но получен: {actual_url}"
