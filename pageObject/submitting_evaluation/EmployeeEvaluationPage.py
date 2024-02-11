# import EvaluationPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pageObject.submitting_evaluation.EvaluationPage import EvaluationPage
from utills.StringProcess import remove_special_characters_and_spaces
from utills.EvaluationRatingGenerator import EmployeeEvaluationRatingGenerator, SupervisorEvaluationRatingGenerator


class EmployeeEvaluationPage(EvaluationPage):
    __likes_text_area_locator = (By.ID, "Likes")
    __dislikes_text_area_locator = (By.ID, "Dislikes")
    __improvements_text_area_locator = (By.ID, "Improvements")
    __display_evaluation_data_table_locator = (By.CSS_SELECTOR, '#display-data-table > tbody')
    __likes_textarea_after_submission_locator = (By.ID, "What_did_you_like_about_the_past_period_")
    __dislikes_textarea_after_submission_locator = (By.ID, "What_did_you_dislike_about_the_past_period_")
    __improvements_textarea_after_submission_locator = (
        By.ID, "What_can_ASAL_do_for_you_to_make_you_perform_your_job_better_")

    # display-data-table > tbody > tr:nth-child(4) > td:nth-child(2)

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

    def get_dislikes_text(self):
        dis_likes = self.wait_for(self.__dislikes_text_area_locator)
        return dis_likes.text

    def get_likes_text(self):
        likes = self.wait_for(self.__likes_text_area_locator)
        return likes.text

    def get_improvements_text(self):
        improvement = self.wait_for(self.__improvements_text_area_locator)
        return improvement.text

    def set_evaluation_page_with_generated_data(self, generated_data=EmployeeEvaluationRatingGenerator()):
        self.fill_evaluation_table(generated_data.evaluationSelections)
        self.set_likes_text(generated_data.likesText)
        self.set_dislikes_text(generated_data.dislikesText)
        self.set_improvements_text(generated_data.improvementsText)

    def is_evaluation_page_saved_with_generated_data(self, generated_data=EmployeeEvaluationRatingGenerator()):
        table_result = self.is_evaluation_table_saved(generated_data.evaluationSelections)
        isLikesSaved = self.get_likes_text() == generated_data.likesText
        isDisLikesSaved = self.get_dislikes_text() == generated_data.dislikesText
        isImprovementsSaved = self.get_improvements_text() == generated_data.improvementsText
        return table_result and isLikesSaved and isDisLikesSaved and isImprovementsSaved

    def is_evaluation_table_saved_After_submission(self, evaluationSelections):
        # TODO: handle dublicate here !!
        try:
            table = self.wait_for(self.__display_evaluation_data_table_locator)
            rows = table.find_elements(By.TAG_NAME, "tr")
            for index, row in enumerate(rows):
                # Get the cells that have only checkbox input
                evaluation_rate = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)")
                expected_string = remove_special_characters_and_spaces(evaluationSelections[index])
                actual_string = remove_special_characters_and_spaces(evaluation_rate.text)
                # check if this element had not been checked before
                if expected_string != actual_string:
                    return False
            return True
        except (TimeoutException, NoSuchElementException):
            return None

    # TODO: refactor it
    def is_evaluation_page_submited_with_generated_data(self, generated_data=EmployeeEvaluationRatingGenerator()):
        table_result = self.is_evaluation_table_saved_After_submission(generated_data.evaluationSelections)
        isLikesSaved = self.wait_for(self.__likes_textarea_after_submission_locator).text == generated_data.likesText
        isDisLikesSaved = self.wait_for(
            self.__dislikes_textarea_after_submission_locator).text == generated_data.dislikesText
        isImprovementsSaved = self.wait_for(
            self.__improvements_textarea_after_submission_locator).text == generated_data.improvementsText

        return table_result and isLikesSaved and isDisLikesSaved and isImprovementsSaved
