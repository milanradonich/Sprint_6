from locators.header_locators import HeaderLocators
from locators.home_page_locators import HomePageLocators
from locators.order_locators import OrderLocatorsPage
from messages import *
from pages.order_page import OrderPage


class TestOrderBuy:
    def test_order_using_header_btn(self, driver_setup):
        """тест заказа через кнопку заказать в хедере"""
        driver = driver_setup
        order_page = OrderPage(driver)
        order_page.click_element(HeaderLocators.BTN_ORDER_HEADER)
        order_page.make_order()
        order_successfully_text = order_page.get_text_locator(OrderLocatorsPage.ORDER_CONFIRMED)
        assert ORDER_SUCCESSFULY_MESSAGE in order_successfully_text.strip(), 'Заказ не был оформлен'

    def test_order_using_middle_btn(self, driver_setup):
        """тест заказа через кнопку заказать внизу"""
        driver = driver_setup
        order_page = OrderPage(driver)
        order_page.scroll_page_to_element(HomePageLocators.PARENT)
        order_page.click_element(HomePageLocators.BTN_ORDER_MIDDLE)
        order_page.make_order()
        order_successfully_text = order_page.get_text_locator(OrderLocatorsPage.ORDER_CONFIRMED)
        assert ORDER_SUCCESSFULY_MESSAGE in order_successfully_text.strip(), 'Заказ не был оформлен'

