import allure

from pages.base_page import BasePage


class FaqPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_answer(self, locator, accordion_id, text_answer):
        with allure.step("Ожидание видимости элемента"):
            self.wait_for_element_visible(locator)  # этим повысил проходимость теста для лисы
        with allure.step("Прокрутка страницы к вопросу"):
            self.scroll_page_to_element(locator)
        with allure.step("Ожидание кликабельности вопроса"):
            self.element_to_be_clickable(locator)  # этим повысил проходимость теста для лисы
        with allure.step("Клик по вопросу"):
            self.click_element(locator)
        with allure.step("Ожидание текста в ответе"):
            self.wait_for_text_in_element(accordion_id, text_answer)
        with allure.step("Ожидание видимости ответа"):
            self.wait_for_element_visible(accordion_id)
        with allure.step("Получение текста из ответа"):
            return self.get_accordion_text(accordion_id)

    def get_accordion_text(self, accordion_id):
        return self.get_text_locator(accordion_id)

