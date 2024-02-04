import EvaluationPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class SupervisorEvaluationPage(EvaluationPage):
    # Supervisor
    __strengths_textarea_locator = (By.ID, "Strengths")
    __improvement_text_area_locator = (By.ID, "Areas_of_improvements")
    __edit_evaluation_button_locator = (By.CSS_SELECTOR,
                                        "body > div.page-container > div.page-content-wrapper > div > div.text-right > button:nth-child(1)")
    __confirm_button_locator = (By.ID, "save")
    __cancel_button_locator = (By.ID, "close")

    def set_strengths_text(self, text):
        try:
            self.wait_for(self.__strengths_textarea_locator).send_keys(text)
        except TimeoutException:
            return None

    def set_improvements_text(self, text):
        try:
            self.wait_for(self.__improvement_text_area_locator).send_keys(text)
        except TimeoutException:
            return None

    def click_edit_evaluation_button(self):
        try:
            edit_button = self.wait_for(self.__edit_evaluation_button_locator)
            edit_button.click()
        except TimeoutException:
            return None

    def click_confirm_submit(self):
        try:
            submit_button = self.wait_for(self.__confirm_button_locator)
            submit_button.click()
        except TimeoutException:
            return None

    def click_cancel_submit(self):
        try:
            cancel_button = self.wait_for(self.__cancel_button_locator)
            cancel_button.click()
        except TimeoutException:
            return None
