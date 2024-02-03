from selenium.webdriver.common.by import By
from pageObject.common.BaseModule import BaseModule
from selenium.common.exceptions import TimeoutException

image_started = "../img/starteval.gif"


class MyEvaluationPage(BaseModule):
    __PAGE_TITLE = "Employee Evaluation"
    __page_title_locator = (
        By.CSS_SELECTOR, "body > div.page-container > div.page-content-wrapper > div > h3 > b")
    __evaluation_status_image_locator = (By.CSS_SELECTOR,
                                         "body > div.page-container > div.page-content-wrapper > div > div.m-heading-1.border-green.m-bordered > div > div.col-md-10 > div:nth-child(2) > div.col-md-9 > img")

    __employee_submit_date_locator = (By.CSS_SELECTOR,
                                      "body > div.page-container > div.page-content-wrapper > div > div.m-heading-1.border-green.m-bordered > div > div.col-md-2 > h2")
    __supervisor_submit_date_locator = (By.CSS_SELECTOR,
                                        "body > div.page-container > div.page-content-wrapper > div > div.m-heading-1.border-green.m-bordered > div > div.col-md-2 > h3:nth-child(3)")
    __review_date_locator = (By.CSS_SELECTOR,
                             "body > div.page-container > div.page-content-wrapper > div > div.m-heading-1.border-green.m-bordered > div > div.col-md-2 > h3:nth-child(4)")
    __closed_date_locator = (By.CSS_SELECTOR,
                             "body > div.page-container > div.page-content-wrapper > div > div.m-heading-1.border-green.m-bordered > div > div.col-md-2 > h3:nth-child(5)")
    __evaluation_table_locator = (By.CSS_SELECTOR, '#assets-data-table > tbody')  # (By.ID, "assets-data-table")
    # Employee Feedback
    __likes_text_area_locator = (By.ID, "Likes")
    __dislikes_text_area_locator = (By.ID, "Dislikes")
    __improvements_text_area_locator = (By.ID, "Improvements")
    __submit_button_locator = (By.ID, "submitbtn")
    __save_button_locator = (By.ID, "saveButton")

    __confirm_submit_button_locator = (By.CSS_SELECTOR,
                                       'body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-primary')
    __cancel_submit_button_locator = (By.CSS_SELECTOR,
                                      'body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-default')

   # Supervisor
    __strengths_textarea_locator = (By.ID, "Strengths")
    __s_improvment_text_area_locator = (By.ID,"Areas_of_improvements")
    # close button id = CLOSEbtn for both supervisor and employee
    # edit button css = body > div.page-container > div.page-content-wrapper > div > div.text-right > button:nth-child(1)
    # confirm button id = save, close id = close

    def check_my_history_page_is_loaded(self):
        try:
            title = self.wait_for(self.__page_title_locator).text
            return title == self.__PAGE_TITLE
        except TimeoutException:
            return False

    def process_table(self, selectionIndex=0):
        # TODO: check its not less or more that the exsisted number
        try:
            table = self.wait_for(self.__evaluation_table_locator)
            rows = table.find_elements(By.TAG_NAME, "tr")
            rows_count = len(rows)
            for row in rows:
                # TODO: handle it in the selectionIndex
                # Get the cells that have only checkbox input
                cells = row.find_elements(By.TAG_NAME, "td")[1:rows_count - 2]
                selected_cell = cells[selectionIndex]
                checkbox = selected_cell.find_element(By.TAG_NAME, "input")
                checkbox.click()
        except TimeoutException:
            return None

    def set_dislikes_text(self, text):
        self.wait_for(self.__dislikes_text_area_locator).send_keys(text)

    def set_likes_text(self, text):
        self.wait_for(self.__likes_text_area_locator).send_keys(text)

    def set_improvements_text(self, text):
        self.wait_for(self.__improvements_text_area_locator).send_keys(text)

    def set_areas_to_reinforce_text(self, text):
        self.wait_for(self.__strengths_textarea_locator).send_keys(text)

    def set_areas_of_improvements_text(self, text):
        self.wait_for(self.__s_improvment_text_area_locator).send_keys(text)

    def click_save_button(self):
        save_button = self.wait_for(self.__save_button_locator)
        if save_button.is_enabled():
            save_button.click()
            return True
        else:
            return False

    def click_submit_button(self):
        submit_button = self.wait_for(self.__submit_button_locator)
        if submit_button.is_enabled():
            submit_button.click()
            return True
        return False

    def click_confirm_submit(self):
        try:
            submit_button = self.wait_for(self.__confirm_submit_button_locator)
            submit_button.click()
        except TimeoutException:
            return None

    def click_cancel_submit(self):
        try:
            cancel_button = self.wait_for(self.__cancel_submit_button_locator)
            cancel_button.click()
        except TimeoutException:
            return None
