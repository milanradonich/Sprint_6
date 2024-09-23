import allure
import pytest

from locators.faq_locators import FaqLocators
from messages import ANSWER_ERROR
from pages.faq_page import FaqPage


class TestFaqPage:
    @pytest.mark.parametrize("link_ask, link_answer, expected_answer", [
        (FaqLocators.LINK_ASK_1, FaqLocators.LINK_ANSWER_1, FaqLocators.EXPECTED_ANSWER_1),
        (FaqLocators.LINK_ASK_2, FaqLocators.LINK_ANSWER_2, FaqLocators.EXPECTED_ANSWER_2),
        (FaqLocators.LINK_ASK_3, FaqLocators.LINK_ANSWER_3, FaqLocators.EXPECTED_ANSWER_3),
        (FaqLocators.LINK_ASK_4, FaqLocators.LINK_ANSWER_4, FaqLocators.EXPECTED_ANSWER_4),
        (FaqLocators.LINK_ASK_5, FaqLocators.LINK_ANSWER_5, FaqLocators.EXPECTED_ANSWER_5),
        (FaqLocators.LINK_ASK_6, FaqLocators.LINK_ANSWER_6, FaqLocators.EXPECTED_ANSWER_6),
        (FaqLocators.LINK_ASK_7, FaqLocators.LINK_ANSWER_7, FaqLocators.EXPECTED_ANSWER_7),
        (FaqLocators.LINK_ASK_8, FaqLocators.LINK_ANSWER_8, FaqLocators.EXPECTED_ANSWER_8),
    ])
    @allure.title("Проверка раздела FAQ на отображение правильных ответов")
    @allure.description("Тест проверяет, что по клику на вопрос отображается правильный ответ")
    def test_click_accordion(self, setup_home_page, link_ask, link_answer, expected_answer):
        driver = setup_home_page
        faq_page = FaqPage(driver)
        with allure.step("Клик по вопросу"):
            actual_text = faq_page.check_answer(link_ask, link_answer, expected_answer)
        with allure.step("Проверка текста ответа"):
            assert actual_text == expected_answer, ANSWER_ERROR
