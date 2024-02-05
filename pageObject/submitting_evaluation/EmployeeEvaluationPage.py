# import EvaluationPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pageObject.submitting_evaluation.EvaluationPage import EvaluationPage


class EmployeeEvaluationPage(EvaluationPage):
    __likes_text_area_locator = (By.ID, "Likes")
    __dislikes_text_area_locator = (By.ID, "Dislikes")
    __improvements_text_area_locator = (By.ID, "Improvements")

    __confirm_submit_button_locator = (By.CSS_SELECTOR,
                                       'body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-primary')
    __cancel_submit_button_locator = (By.CSS_SELECTOR,
                                      'body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-default')

    def set_dislikes_text(self, text):
        self.wait_for(self.__dislikes_text_area_locator).send_keys(text)

    def set_likes_text(self, text):
        self.wait_for(self.__likes_text_area_locator).send_keys(text)

    def set_improvements_text(self, text):
        self.wait_for(self.__improvements_text_area_locator).send_keys(text)

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

    def set_evaluation_page_with_dictionary(self, dictionary_data):
        self.fill_evaluation_table(dictionary_data["evaluationSelectionIndex"])
        self.set_likes_text(dictionary_data["likesText"])
        self.set_dislikes_text(dictionary_data["dislikesText"])
        self.set_improvements_text(dictionary_data["improvementsText"])
