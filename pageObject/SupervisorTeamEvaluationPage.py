from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pageObject.common.BaseModule import BaseModule


class SupervisorTeamEvaluationPage(BaseModule):
    __open_evaluation_button_locator = (By.ID, "open")
    __history_evaluation_button_locator = (By.ID, "view")
    __notes_evaluation_button_locator = (By.ID, "addNote")
    __close_evaluation_button_locator = (By.ID, "close")
    __cancel_evaluation_button_locator = (By.ID, "cancel")

    def click_open_evaluation_button(self):
        self.wait_for(self.__open_evaluation_button_locator).click()

    def click_history_evaluation_button(self):
        self.wait_for(self.__history_evaluation_button_locator).click()

    def click_notes_evaluation_button(self):
        self.wait_for(self.__notes_evaluation_button_locator).click()

    def click_close_evaluation_button(self):
        self.wait_for(self.__close_evaluation_button_locator).click()

    def cancel_close_evaluation_button(self):
        self.wait_for(self.__cancel_evaluation_button_locator).click()
