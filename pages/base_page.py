from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from support.logging import logger
from time import sleep


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, end_url=''):
        url = f'https://soft.reelly.io/{end_url}'
        self.driver.get(url)
        # logger.info(f'Opening URL {url}')
        sleep(5)
        self.driver.refresh()

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def refresh(self):
        self.driver.refresh()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.send_keys(text)

    def wait_for_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable: {locator}'
        )

    def wait_for_element_clickable_click(self, *locator):
        e = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable: {locator}'
        )
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element did not disappear: {locator}'
        )

    def wait_for_element_to_appear(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator),
                        message=f'element did not appear: {locator}')

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, \
            f'Error, expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Error, expected partial text {expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_part_of_url):
        self.wait.until(EC.url_contains(expected_part_of_url))