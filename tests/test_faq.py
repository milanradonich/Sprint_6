import time

from locators.faq_locators import FaqLocators
from messages import ANSWER_ERROR
from pages.faq_page import FaqPage


class TestFaqPage:
    def test_click_question_1(self, driver_setup):
        driver = driver_setup
        faq_page = FaqPage(driver)
        expected_text = FaqLocators.EXPECTED_ANSWER_1
        actual_text = faq_page.check_answer(FaqLocators.LINK_ASK_1, FaqLocators.LINK_ANSWER_1)
        assert actual_text == expected_text, ANSWER_ERROR

    def test_click_question_2(self, driver_setup):
        driver = driver_setup
        faq_page = FaqPage(driver)
        expected_text = FaqLocators.EXPECTED_ANSWER_2
        actual_text = faq_page.check_answer(FaqLocators.LINK_ASK_2, FaqLocators.LINK_ANSWER_2)
        assert actual_text == expected_text, ANSWER_ERROR

    def test_click_question_3(self, driver_setup):
        driver = driver_setup
        faq_page = FaqPage(driver)
        expected_text = FaqLocators.EXPECTED_ANSWER_3
        actual_text = faq_page.check_answer(FaqLocators.LINK_ASK_3, FaqLocators.LINK_ANSWER_3)
        assert actual_text == expected_text, ANSWER_ERROR

    def test_click_question_4(self, driver_setup):
        driver = driver_setup
        faq_page = FaqPage(driver)
        expected_text = FaqLocators.EXPECTED_ANSWER_4
        actual_text = faq_page.check_answer(FaqLocators.LINK_ASK_4, FaqLocators.LINK_ANSWER_4)
        assert actual_text == expected_text, ANSWER_ERROR

    def test_click_question_5(self, driver_setup):
        driver = driver_setup
        faq_page = FaqPage(driver)
        expected_text = FaqLocators.EXPECTED_ANSWER_5
        actual_text = faq_page.check_answer(FaqLocators.LINK_ASK_5, FaqLocators.LINK_ANSWER_5)
        assert actual_text == expected_text, ANSWER_ERROR

    def test_click_question_6(self, driver_setup):
        driver = driver_setup
        faq_page = FaqPage(driver)
        expected_text = FaqLocators.EXPECTED_ANSWER_6
        actual_text = faq_page.check_answer(FaqLocators.LINK_ASK_6, FaqLocators.LINK_ANSWER_6)
        assert actual_text == expected_text, ANSWER_ERROR

    def test_click_question_7(self, driver_setup):
        driver = driver_setup
        faq_page = FaqPage(driver)
        expected_text = FaqLocators.EXPECTED_ANSWER_7
        actual_text = faq_page.check_answer(FaqLocators.LINK_ASK_7, FaqLocators.LINK_ANSWER_7)
        assert actual_text == expected_text, ANSWER_ERROR

    def test_click_question_8(self, driver_setup):
        driver = driver_setup
        faq_page = FaqPage(driver)
        expected_text = FaqLocators.EXPECTED_ANSWER_8
        actual_text = faq_page.check_answer(FaqLocators.LINK_ASK_8, FaqLocators.LINK_ANSWER_8)
        assert actual_text == expected_text, ANSWER_ERROR
