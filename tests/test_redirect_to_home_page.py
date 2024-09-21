import allure

from locators.header_locators import HeaderLocators
from my_data import BASE_URL
from pages.order_page import OrderPage


class TestRedirectToHomePage:
    @allure.title("Проверка редиректа")
    @allure.description("Проверка, что при нажатии на лого самоката будет переход на главную страницу")
    def test_redirect_to_home_page(self, setup_home_page):
        """проверка, что при нажатии на лого самоката будет переход на главную страницу"""
        driver = setup_home_page
        order_page = OrderPage(driver)
        with allure.step("Клик по кнопке заказать"):
            order_page.click_element(HeaderLocators.BTN_ORDER_HEADER)
        with allure.step("Клик по лого самоката"):
            order_page.click_element(HeaderLocators.LINK_SCOOTER)
        expected_url = BASE_URL
        with allure.step("Получение актуального адреса"):
            actual_url = driver.current_url
        with allure.step("Проверка адреса новой страницы с ожиданием"):
            assert actual_url == expected_url, f"Ожидался URL: {expected_url}, но получен: {actual_url}"
