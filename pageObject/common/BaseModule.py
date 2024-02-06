from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseModule(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def wait_for(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def wait_for_url(self, url_string):
        element = self.wait.until(EC.url_to_be(url_string))
        return element

    def wait_for_visibility_of_element_located(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_multi_elements(self, locator):
        return self.driver.find_elements(*locator)
