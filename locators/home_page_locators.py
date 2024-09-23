from selenium.webdriver.common.by import By


class HomePageLocators:
    HOME_PAGE = By.XPATH, '//*[@id="root"]'  # домашняя страница
    PARENT = By.CSS_SELECTOR, "div.Home_FinishButton__1_cWm"  # родитель кнопки BTN_ORDER_MIDDLE
    BTN_ORDER_MIDDLE = By.XPATH, '//button[contains(@class,"Button_Middle__1CSJM")]'  # кнопка заказать внизу
    COOKIE_BTN = By.ID, "rcc-confirm-button"   # кнопка приема куки
