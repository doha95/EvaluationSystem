from pageObject.submitting_evaluation.EvaluationPage import EvaluationPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utills.EvaluationRatingGenerator import SupervisorEvaluationRatingGenerator


class SupervisorEvaluationPage(EvaluationPage):
    # Supervisor
    __strengths_textarea_locator = (By.ID, "Strengths")
    __improvement_text_area_locator = (By.ID, "Areas_of_improvements")
    __edit_evaluation_button_locator = (By.CSS_SELECTOR,
                                        "body > div.page-container > div.page-content-wrapper > div > div.text-right > button:nth-child(1)")

    def set_strengths_text(self, text):
        try:
            strength = self.wait_for(self.__strengths_textarea_locator)
            strength.clear()
            strength.send_keys(text)
        except TimeoutException:
            return None

    def set_improvements_text(self, text):
        try:
            improvements = self.wait_for(self.__improvement_text_area_locator)
            improvements.clear()
            improvements.send_keys(text)
        except TimeoutException:
            return None

    def get_strengths_text(self):
        try:
            strength = self.wait_for(self.__strengths_textarea_locator)
            return strength.text
        except TimeoutException:
            return None

    def get_improvements_text(self):
        try:
            improvements = self.wait_for(self.__improvement_text_area_locator)
            return improvements.text
        except TimeoutException:
            return None

    def click_edit_evaluation_button(self):
        try:
            edit_button = self.wait_for(self.__edit_evaluation_button_locator)
            edit_button.click()
        except TimeoutException:
            return None

    def set_supervisor_evaluation_info_with_generated_info(self, generated_info=SupervisorEvaluationRatingGenerator()):
        self.fill_evaluation_table(generated_info.evaluationSelections)
        self.set_improvements_text(generated_info.improvementsText)
        self.set_strengths_text(generated_info.strengthsText)

    def is_supervisor_evaluation_page_saved_with_generated_info(self,
                                                                generated_info=SupervisorEvaluationRatingGenerator()):
        table_result = self.is_evaluation_table_saved(generated_info.evaluationSelections)
        isStrengthsText = self.get_strengths_text() == generated_info.strengthsText
        isImprovementsText = self.get_improvements_text() == generated_info.improvementsText

        return table_result and isImprovementsText and isStrengthsText
