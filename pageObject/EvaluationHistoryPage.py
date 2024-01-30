from selenium.webdriver.common.by import By
from pageObject.common.BaseModule import BaseModule
from selenium.common.exceptions import TimeoutException


class EvaluationHistoryPage(BaseModule):
    __PAGE_TITLE = "Evaluation History"
    __page_title_locator = (By.CSS_SELECTOR, "body > div.page-container > div.page-content-wrapper > div > h3")
    __collabs_Button_locator = (By.CSS_SELECTOR,
                                "body > div.page-container > div.page-content-wrapper > div > div.portlet.box.blue > div.portlet-title > div.tools > a")
    __evaluation_table_locator = (By.ID, "historyTable")

    def check_history_page_is_loaded(self):
        try:
            title = self.wait_for(self.__page_title_locator).text
            return title == self.__PAGE_TITLE
        except TimeoutException:
            return False

    def check_presence_evaluation_table_(self):
        try:
            table = self.wait_for(self.__evaluation_table_locator)
            return table
        except TimeoutException:
            return False
