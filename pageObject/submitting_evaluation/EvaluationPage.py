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
                             "body > div.page-container > div.page-content-wrapper > div > div.m-heading-1.border-green.m-bordered > div > div.col-md-2 > h3:nth-child(4)")
    __closed_date_locator = (By.CSS_SELECTOR,
                             "body > div.page-container > div.page-content-wrapper > div > "
                             "div.m-heading-1.border-green.m-bordered > div > div.col-md-2 > h3:nth-child(5)")
    __evaluation_cycle_date_locator = (By.CSS_SELECTOR,
                                       "body > div.page-container > div.page-content-wrapper > div > div.m-heading-1.border-green.m-bordered > div > div.col-md-10 > div:nth-child(1) > div:nth-child(2) > h3")
    __confirm_submit_button_locator = (By.CSS_SELECTOR,
                                       'body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-primary')
    __cancel_submit_button_locator = (By.CSS_SELECTOR,
                                      'body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-default')

    __evaluation_table_locator = (By.CSS_SELECTOR, '#assets-data-table > tbody')
    __submit_button_locator = (By.ID, "submitbtn")
    __save_button_locator = (By.ID, "saveButton")
    __close_evaluation_button_locator = (By.ID, "CLOSEbtn")
    __confirm_close_evaluation_button_locator = (By.ID, "save")
    __cancel_close_evaluation_button_locator = (By.ID, "close")

    def check_my_evaluation_page_is_loaded(self):
        try:
            title = self.wait_for(self.__page_title_locator).text
            return title == self.__PAGE_TITLE
        except TimeoutException:
            return False

    def fill_evaluation_table(self, evaluation_selections_IDs):
        # TODO: handle dublicate with the next function
        try:
            table = self.wait_for(self.__evaluation_table_locator)
            rows = table.find_elements(By.TAG_NAME, "tr")
            for index, row in enumerate(rows):
                # Get the cells that have only checkbox input
                selected_item = row.find_element(By.ID, evaluation_selections_IDs[index])
                # check if this element had not been checked before
                if not selected_item.is_selected():
                    selected_item.click()
        except (TimeoutException, NoSuchElementException):
            return None

    def is_evaluation_table_saved(self, evaluation_selections_IDs):
        # TODO: handle dublicate here !!
        try:
            table = self.wait_for(self.__evaluation_table_locator)
            rows = table.find_elements(By.TAG_NAME, "tr")
            for index, row in enumerate(rows):
                # Get the cells that have only checkbox input
                selected_item = row.find_element(By.ID, evaluation_selections_IDs[index])
                # check if this element had not been checked before
                if not selected_item.is_selected():
                    return False
            return True
        except (TimeoutException, NoSuchElementException):
            return None

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

    def click_confirm_submit(self):
        try:
            submit_button = self.wait_for_visibility_of_element_located(self.__confirm_submit_button_locator)
            submit_button.click()
        except TimeoutException:
            return None

    def click_cancel_submit(self):
        try:
            cancel_button = self.wait_for(self.__cancel_submit_button_locator)
            cancel_button.click()
        except TimeoutException:
            return None

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

    def click_confirm_close_review_submit(self):
        try:
            submit_button = self.wait_for_visibility_of_element_located(self.__confirm_close_evaluation_button_locator)
            submit_button.click()
        except TimeoutException:
            return None

    def click_cancel_close_submit(self):
        try:
            cancel_button = self.wait_for(self.__cancel_close_evaluation_button_locator)
            cancel_button.click()
        except TimeoutException:
            return None
