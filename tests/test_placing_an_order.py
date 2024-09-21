import allure

from locators.header_locators import HeaderLocators
from locators.home_page_locators import HomePageLocators
from locators.order_locators import OrderLocatorsPage
from messages import *
from pages.order_page import OrderPage


class TestOrderBuy:
    @allure.title("Тест заказа через кнопку в хедере")
    @allure.description("Проверка оформления заказа через кнопку 'Заказать' в хедере сайта.")
    def test_order_using_header_btn(self, setup_home_page):
        """тест заказа через кнопку заказать в хедере"""
        driver = setup_home_page
        order_page = OrderPage(driver)
        with allure.step("Клик по кнопке 'Заказать' в хедере"):
            order_page.click_element(HeaderLocators.BTN_ORDER_HEADER)
        with allure.step("Оформление заказа"):
            order_page.make_order()
        with allure.step("Получение текста подтверждения заказа"):
            order_successfully_text = order_page.get_text_locator(OrderLocatorsPage.ORDER_CONFIRMED)
        with allure.step("Проверка успешного оформления заказа"):
            assert ORDER_SUCCESSFULY_MESSAGE in order_successfully_text.strip(), 'Заказ не был оформлен'

    @allure.title("Тест заказа через кнопку внизу")
    @allure.description("Проверка оформления заказа через кнопку 'Заказать' внизу сайта.")
    def test_order_using_middle_btn(self, setup_home_page):
        """тест заказа через кнопку заказать внизу"""
        driver = setup_home_page
        order_page = OrderPage(driver)
        with allure.step("Скролл до области с кнопкой"):
            order_page.scroll_page_to_element(HomePageLocators.PARENT)
        with allure.step("Клик по кнопке 'Заказать' внизу"):
            order_page.click_element(HomePageLocators.BTN_ORDER_MIDDLE)
        with allure.step("Оформление заказа"):
            order_page.make_order()
        with allure.step("Получение текста подтверждения заказа"):
            order_successfully_text = order_page.get_text_locator(OrderLocatorsPage.ORDER_CONFIRMED)
        with allure.step("Проверка успешного оформления заказа"):
            assert ORDER_SUCCESSFULY_MESSAGE in order_successfully_text.strip(), 'Заказ не был оформлен'
