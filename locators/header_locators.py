from selenium.webdriver.common.by import By


class HeaderLocators:
    BTN_ORDER_HEADER = By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']"  # кнопка заказать в хедере
    LINK_LOGO = By.CLASS_NAME, "Header_LogoYandex__3TSOI"  # лого яндекс
    LINK_SCOOTER = By.CLASS_NAME, "Header_LogoScooter__3lsAR"  # лого скутер
    BTN_ORDER_STATUS = By.CLASS_NAME, "Header_Link__1TAG7"  # Статус заказа
    INPUT_ORDER = By.CLASS_NAME, "nput_Input__1iN_Z"  # поле номера заказа
    BTN_GO = (By.XPATH, "//button[text()='Go!']")

