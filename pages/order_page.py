import random

import allure

from helper import get_data_for_make_order
from messages import COMMIT_MESSAGE
from pages.base_page import BasePage
from locators.order_locators import OrderLocatorsPage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, url):
        self.navigate(url)

    def choice_station_from_select(self, locator):
        """выбор станции метро"""
        self.scroll_page_to_element(locator)
        self.click_element(locator)

    def choice_rental_period(self, locator):
        """выбор периода аренды"""
        self.wait_for_element_visible(locator)
        self.scroll_page_to_element(locator)
        self.click_element(locator)

    def choice_checkbox_random(self):
        """чекбокс цвета самоката"""
        checkboxes = [OrderLocatorsPage.CHECKBOX_BLACK, OrderLocatorsPage.CHECKBOX_GREY]
        choice = random.choice([1, 2])
        if choice == 1:
            checkbox_to_select = random.choice(checkboxes)
            self.click_element(checkbox_to_select)
        elif choice == 2:
            self.click_element(checkboxes[0])
            self.click_element(checkboxes[1])

    @allure.step("Оформление заказа end_to_end")
    def make_order(self):
        """оформление заказа end_to_end"""
        random_name, random_first_name, random_address, phone_num, data_of_rent = get_data_for_make_order()
        with allure.step("Ввод имени"):
            self.input_symbols(OrderLocatorsPage.INPUT_NAME, random_name)

        with allure.step("Ввод фамилии"):
            self.input_symbols(OrderLocatorsPage.INPUT_SEC_NAME, random_first_name)

        with allure.step("Ввод адреса"):
            self.input_symbols(OrderLocatorsPage.INPUT_ADDRESS, random_address)

        with allure.step("Выбор станции"):
            self.click_element(OrderLocatorsPage.SELECT_STATION)
            self.choice_station_from_select(OrderLocatorsPage.BTN_VALUE_STATION)  # иногда не срабатывает выбор.

        with allure.step("Ввод номера телефона"):
            self.input_symbols(OrderLocatorsPage.INPUT_PHONE, phone_num)

        with allure.step("Переход к следующему шагу"):
            self.click_element(OrderLocatorsPage.BTN_NEXT)

        with allure.step("Ввод даты аренды"):
            self.input_symbols(OrderLocatorsPage.INPUT_DATE, data_of_rent)

        with allure.step("Выбор дня аренды"):
            self.click_element(OrderLocatorsPage.SELECTED_DAY_LOCATOR)

        with allure.step("Выбор периода аренды"):
            self.click_element(OrderLocatorsPage.SELECT_RENTAL_PERIOD)
            self.choice_rental_period(OrderLocatorsPage.BTN_VALUE_PERIOD)

        with allure.step("Выбор случайного чекбокса"):
            self.choice_checkbox_random()

        with allure.step("Ввод комментария"):
            self.input_symbols(OrderLocatorsPage.INPUT_COMMIT, COMMIT_MESSAGE)

        with allure.step("Подтверждение заказа"):
            self.click_element(OrderLocatorsPage.BTN_ORDER_MIDDLE)
            self.click_element(OrderLocatorsPage.BTN_YES_CONFIRM_ORDER)

        with allure.step("Ожидание подтверждения заказа"):
            self.wait_for_element_visible(OrderLocatorsPage.ORDER_CONFIRMED)

