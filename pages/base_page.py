from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_page_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def find_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def find_elements(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))

    def click_element(self, locator, timeout: int = 10):
        self.find_element(locator, timeout).click()

    def input_symbols(self, locator, text, timeout: int = 10):
        self.find_element(locator, timeout).send_keys(text)

    def wait_for_element_visible(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of(self.find_element(locator, timeout)))

    def wait_for_elements_visible(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))

    def wait_for_text_in_element(self, locator, text, timeout: int = 10):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))

    def get_text_locator(self, locator, timeout: int = 10):
        return self.find_element(locator, timeout).text

    def element_to_be_clickable(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))


