import random

from selenium.webdriver.common.by import By


class RentalLocators:
    DAY_1 = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    DAY_2 = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    DAY_3 = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
    DAY_4 = (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']")
    DAY_5 = (By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']")
    DAY_6 = (By.XPATH, "//div[@class='Dropdown-option' and text()='шестеро суток']")
    DAY_7 = (By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']")


locators_rental = [
    RentalLocators.DAY_1,
    RentalLocators.DAY_2,
    RentalLocators.DAY_3,
    RentalLocators.DAY_4,
    RentalLocators.DAY_5,
    RentalLocators.DAY_6,
    RentalLocators.DAY_7,
]


class OrderLocatorsPage:
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SEC_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    SELECT_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    random_value = random.randint(1, 236)
    BTN_VALUE_STATION = (By.CSS_SELECTOR, f"button[value='{random_value}']")
    BTN_NEXT = (By.XPATH, '//button[text()="Далее"]')
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    SELECTED_DAY_LOCATOR = (By.CSS_SELECTOR, 'div.react-datepicker__day.react-datepicker__day--selected')
    SELECT_RENTAL_PERIOD = By.CSS_SELECTOR, 'span.Dropdown-arrow'
    random_period = random.randint(0, len(locators_rental) - 1)
    BTN_VALUE_PERIOD = locators_rental[random_period]
    CHECKBOX_BLACK = (By.XPATH, "//input[@id='black']")
    CHECKBOX_GREY = (By.XPATH, "//input[@id='grey']")
    INPUT_COMMIT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BTN_ORDER_MIDDLE = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    BTN_YES_CONFIRM_ORDER = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Да']")
    ORDER_CONFIRMED = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")



