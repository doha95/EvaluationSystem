from selenium.webdriver.common.by import By
from pageObject.common.BaseModule import BaseModule
from selenium.common.exceptions import NoSuchElementException, TimeoutException

image_started = "../img/starteval.gif"


class EvaluationPage(BaseModule):
    __PAGE_TITLE = "Employee Evaluation"
    __page_title_locator = (
        By.CSS_SELECTOR, "body > div.page-container > div.page-content-wrapper > div > h3 > b")
    # TODO: check with the image if you can handle it
    __evaluation_status_image_locator = (By.CSS_SELECTOR,
                                         "body > div.page-container > div.page-content-wrapper > div > "
                                         "div.m-heading-1.border-green.m-bordered > div > div.col-md-10 > "
                                         "div:nth-child(2) > div.col-md-9 > img")

    __employee_submit_date_locator = (By.CSS_SELECTOR,
                                      "body > div.page-container > div.page-content-wrapper > div > "
                                      "div.m-heading-1.border-green.m-bordered > div > div.col-md-2 > h2")
    __supervisor_submit_date_locator = (By.CSS_SELECTOR,
                                        "body > div.page-container > div.page-content-wrapper > div > "
                                        "div.m-heading-1.border-green.m-bordered > div > div.col-md-2 > h3:nth-child("
                                        "3)")
    __review_date_locator = (By.CSS_SELECTOR,
                             "body > div.page-container > div.page-content-wrapper > div > "
                             "div.m-heading-1.border-green.m-bordered > div > div.col-md-2 > h3:nth-child(4)")
    __closed_date_locator = (By.CSS_SELECTOR,
                             "body > div.page-container > div.page-content-wrapper > div > "
                             "div.m-heading-1.border-green.m-bordered > div > div.col-md-2 > h3:nth-child(5)")
    __evaluation_cycle_date_locator = (By.CSS_SELECTOR,
                                       "body > div.page-container > div.page-content-wrapper > div > div.m-heading-1.border-green.m-bordered > div > div.col-md-10 > div:nth-child(1) > div:nth-child(2) > h3")
    __evaluation_table_locator = (By.CSS_SELECTOR, '#assets-data-table > tbody')
    __submit_button_locator = (By.ID, "submitbtn")
    __save_button_locator = (By.ID, "saveButton")
    __close_evaluation_button_locator = (By.ID, "CLOSEbtn")

    def check_my_history_page_is_loaded(self):
        try:
            title = self.wait_for(self.__page_title_locator).text
            return title == self.__PAGE_TITLE
        except TimeoutException:
            return False

    def fill_evaluation_table(self, selectedRatingIndex=0):
        try:
            table = self.wait_for(self.__evaluation_table_locator)
            rows = table.find_elements(By.TAG_NAME, "tr")
            rows_count = len(rows)
            for row in rows:
                # Get the cells that have only checkbox input
                cells = row.find_elements(By.TAG_NAME, "td")[1:rows_count - 2]
                if selectedRatingIndex < 0 or selectedRatingIndex > len(cells):
                    raise Exception("the selected rating index is out of range of the evaluation table")
                selected_cell = cells[selectedRatingIndex]
                checkbox = selected_cell.find_element(By.TAG_NAME, "input")
                checkbox.click()
        except (TimeoutException, NoSuchElementException):
            return None

    # TODO: handle it in better way to fill the table, maybe to fill with out index
    # this is dummy way to check
    def is_evaluation_saved(self):
        try:
            status_image_element = self.wait_for(self.__evaluation_status_image_locator)
            image_src = status_image_element.get_attribute("src")
            if "/img/starteval.gif" in image_src:
                return True
            else:
                return False
        except (TimeoutException, NoSuchElementException):
            return False

    def click_save_button(self):
        try:
            save_button = self.wait_for(self.__save_button_locator)
            if save_button.is_enabled():
                save_button.click()
                return True
            else:
                return False
        except TimeoutException:
            return False

    def click_submit_button(self):
        try:
            submit_button = self.wait_for(self.__submit_button_locator)
            if submit_button.is_enabled():
                submit_button.click()
                return True
            return False
        except TimeoutException:
            return False

    def click_close_evaluation_button(self):
        try:
            close_button = self.wait_for(self.__close_evaluation_button_locator)
            if close_button.is_enabled():
                close_button.click()
                return True
            return False
        except TimeoutException:
            return False

    def check_employee_submission_date_is_located(self):
        try:
            employee_submission_date = self.wait_for(self.__employee_submit_date_locator)
            return True if "N/A" not in employee_submission_date.text else False
        except TimeoutException:
            return False

    def check_supervisor_submission_date_is_located(self):
        try:
            supervisor_submission_date = self.wait_for(self.__supervisor_submit_date_locator)
            return True if "N/A" not in supervisor_submission_date.text else False
        except TimeoutException:
            return False

    def check_review_submission_date_is_located(self):
        try:
            review_submission_date = self.wait_for(self.__review_date_locator)
            return True if "N/A" not in review_submission_date.text else False
        except TimeoutException:
            return False

    def check_close_submission_date_is_located(self):
        try:
            close_submission_date = self.wait_for(self.__closed_date_locator)
            return True if "N/A" not in close_submission_date.text else False
        except TimeoutException:
            return False

    def get_current_evaluation_cycle(self):
        try:
            current_evaluation_cycle = self.wait_for(self.__evaluation_cycle_date_locator)
            CYCLE_TITLE = "Evaluation Cycle : "
            return current_evaluation_cycle.text.replace(CYCLE_TITLE, "")
        except TimeoutException:
            return None
