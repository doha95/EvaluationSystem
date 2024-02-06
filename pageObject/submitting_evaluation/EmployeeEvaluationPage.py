# import EvaluationPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pageObject.submitting_evaluation.EvaluationPage import EvaluationPage


class EmployeeEvaluationPage(EvaluationPage):
    __likes_text_area_locator = (By.ID, "Likes")
    __dislikes_text_area_locator = (By.ID, "Dislikes")
    __improvements_text_area_locator = (By.ID, "Improvements")

    def set_dislikes_text(self, text):
        dis_likes = self.wait_for(self.__dislikes_text_area_locator)
        dis_likes.clear()
        dis_likes.send_keys(text)

    def set_likes_text(self, text):
        likes = self.wait_for(self.__likes_text_area_locator)
        likes.clear()
        likes.send_keys(text)

    def set_improvements_text(self, text):
        improvement = self.wait_for(self.__improvements_text_area_locator)
        improvement.clear()
        improvement.send_keys(text)

    def set_evaluation_page_with_dictionary(self, dictionary_data):
        self.fill_evaluation_table(dictionary_data["evaluationSelectionIndex"])
        self.set_likes_text(dictionary_data["likesText"])
        self.set_dislikes_text(dictionary_data["dislikesText"])
        self.set_improvements_text(dictionary_data["improvementsText"])
