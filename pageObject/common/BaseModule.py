from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseModule(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def wait_for(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def find_element(self, locator):
        return self.driver.find_element(*locator)

