from selenium.webdriver.common.by import By
from pageObject.common.BaseModule import BaseModule
from selenium.common.exceptions import TimeoutException

######## Reviewed Date : N/A
class EvaluationHistoryPage(BaseModule):
    __PAGE_TITLE = "Evaluation History"
    __page_title_locator = (By.CSS_SELECTOR, "body > div.page-container > div.page-content-wrapper > div > h3")
    __collabs_Button_locator = (By.CSS_SELECTOR,
                                "body > div.page-container > div.page-content-wrapper > div > div.portlet.box.blue > div.portlet-title > div.tools > a")
    __evaluation_table_locator = (By.ID, "historyTable")
    __search_input_locator = (By.CSS_SELECTOR, "input[type=search]")

    def get_history_table_content(self):
        # table = self.check_history_page_is_loaded()
        if self.table is not None:
            # Get all rows in the table (skip the header row)
            rows = self.table.find_elements(By.TAG_NAME, "tr")[1:]
            # Initialize data structure to store table content
            table_data = []
            # Loop through each row and extract cell values
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                row_data = [cell.text for cell in cells]
                table_data.append(row_data)
            return table_data

        return []

    def check_history_page_is_loaded(self):
        try:
            title = self.wait_for(self.__page_title_locator).text
            return title == self.__PAGE_TITLE
        except TimeoutException:
            return False

    def check_presence_evaluation_table_(self):
        try:
            self.table = self.wait_for(self.__evaluation_table_locator)
            return self.table
        except TimeoutException:
            return None
