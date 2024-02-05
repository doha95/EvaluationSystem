from selenium.webdriver.common.by import By
from pageObject.common.BaseModule import BaseModule
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class EvaluationHistoryPage(BaseModule):
    __PAGE_TITLE = "Evaluation History"
    __page_title_locator = (By.CSS_SELECTOR, "body > div.page-container > div.page-content-wrapper > div > h3")
    __collabs_Button_locator = (By.CSS_SELECTOR,
                                "body > div.page-container > div.page-content-wrapper > div > div.portlet.box.blue > div.portlet-title > div.tools > a")
    __evaluation_table_locator = (By.CSS_SELECTOR, "#historyTable > tbody")
    __search_input_locator = (By.CSS_SELECTOR, "input[type=search]")
    __view_history_title_locator = (
    By.CSS_SELECTOR, "body > div.page-container > div.page-content-wrapper > div > div.form-group > h3 > b")
    __EMPLOYEE_EVALUATION_TITLE = "Employee Evaluation"
    __table_element = None

    def check_history_page_is_loaded(self):
        try:
            title = self.wait_for(self.__page_title_locator).text
            return title == self.__PAGE_TITLE
        except TimeoutException:
            return False

    def search_for_evaluation_table(self, search_text):
        try:
            search_input = self.wait_for(self.__search_input_locator)
            search_input.clear()
            search_input.send_keys(search_text)
        except TimeoutException:
            return None

    def get_evaluation_table_content(self):
        try:
            self.__table_element = self.wait_for(self.__evaluation_table_locator)
            evaluation_data = []
            rows = self.__table_element.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) >= 3:
                    # TODO: make it as enum
                    view_button = cells[2]
                    if cells[1].text == "Closed":
                        view_button = row.find_element(By.ID, "view")
                    evaluation_data.append({"cycle": cells[0].text, "status": cells[1].text, "action": view_button})
                else:
                    return ValueError("Invalid table count with format, the table should have three elements")
            return evaluation_data
        except (TimeoutException, NoSuchElementException):
            return []

    def check_user_history_page_is_loaded(self):
        try:
            title = self.wait_for(self.__view_history_title_locator).text
            return title == self.__EMPLOYEE_EVALUATION_TITLE
        except TimeoutException:
            return False
