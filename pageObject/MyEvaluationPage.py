from selenium.webdriver.common.by import By
from pageObject.common.BaseModule import BaseModule
from selenium.common.exceptions import TimeoutException


class MyEvaluationPage(BaseModule):
    __PAGE_TITLE = "Employee Evaluation"
    __page_title_locator = (
        By.CSS_SELECTOR, "body > div.page-container > div.page-content-wrapper > div > div.form-group > h3 > b")

    def check_my_history_page_is_loaded(self):
        try:
            title = self.wait_for(self.__page_title_locator).text
            return title == self.__PAGE_TITLE
        except TimeoutException:
            return False
