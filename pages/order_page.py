import random

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

    def make_order(self):
        """оформление заказа end_to_end"""
        random_name, random_first_name, random_address, phone_num, data_of_rent = get_data_for_make_order()
        self.input_symbols(OrderLocatorsPage.INPUT_NAME, random_name)
        self.input_symbols(OrderLocatorsPage.INPUT_SEC_NAME, random_first_name)
        self.input_symbols(OrderLocatorsPage.INPUT_ADDRESS, random_address)
        self.click_element(OrderLocatorsPage.SELECT_STATION)
        self.choice_station_from_select(OrderLocatorsPage.BTN_VALUE_STATION)  # иногда не срабатывает выбор.
                                                                              # Отловить причину пока не смог.
        self.input_symbols(OrderLocatorsPage.INPUT_PHONE, phone_num)
        self.click_element(OrderLocatorsPage.BTN_NEXT)
        self.input_symbols(OrderLocatorsPage.INPUT_DATE, data_of_rent)
        self.click_element(OrderLocatorsPage.SELECTED_DAY_LOCATOR)
        self.click_element(OrderLocatorsPage.SELECT_RENTAL_PERIOD)
        self.choice_rental_period(OrderLocatorsPage.BTN_VALUE_PERIOD)
        self.choice_checkbox_random()
        self.input_symbols(OrderLocatorsPage.INPUT_COMMIT, COMMIT_MESSAGE)
        self.click_element(OrderLocatorsPage.BTN_ORDER_MIDDLE)
        self.click_element(OrderLocatorsPage.BTN_YES_CONFIRM_ORDER)
        self.wait_for_element_visible(OrderLocatorsPage.ORDER_CONFIRMED)

