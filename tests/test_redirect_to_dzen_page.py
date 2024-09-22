import allure
from locators.header_locators import HeaderLocators
from my_data import *
from pages.order_page import OrderPage


class TestRedirectToDzenPage:
    @allure.title("Проверка открытия новой вкладки ")
    @allure.description("Проверка, что при нажатии на лого яндекс откроется новая вкладка dzen")
    def test_redirect_to_dzen_page(self, setup_home_page):
        """проверка, что при нажатии на лого яндекс откроется новая вкладка dzen"""
        driver = setup_home_page
        order_page = OrderPage(driver)
        with allure.step("Клик по кнопке заказать"):
            order_page.click_element(HeaderLocators.BTN_ORDER_HEADER)
        with allure.step("Клик по лого"):
            order_page.click_element(HeaderLocators.LINK_LOGO)
        with allure.step("Ожидание открытия второго окна"):
            order_page.open_new_tab()
        with allure.step("Проверка имени заголовка страницы"):
            order_page.wait_for_title(DZEN_TITLE)
            expected_url = DZEN_URL
            actual_url = order_page.get_current_url()
        with allure.step("Проверка адреса вкладки с ожиданием"):
            assert actual_url == expected_url, f"Ожидался URL: {expected_url}, но получен: {actual_url}"
