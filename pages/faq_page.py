import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.faq_locators import FaqLocators
from pages.base_page import BasePage


class FaqPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_answer(self, locator, accordion_id):
        self.wait_for_element_visible(locator)  # этим повысил проходимость теста
        self.scroll_page_to_element(locator)
        #time.sleep(1)
        self.wait_for_element_visible(locator)  # этим повысил проходимость теста
        self.click_element(locator)
        self.wait_for_element_visible(accordion_id)
        return self.get_accordion_text(accordion_id)

    def get_accordion_text(self, accordion_id):
        return self.get_text_locator(accordion_id)

