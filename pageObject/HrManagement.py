from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from pageObject.common.BaseModule import BaseModule


class HrManagement(BaseModule):
    __manage_evaluation_locators = (
        By.CSS_SELECTOR, 'body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(5)')
    __employee_selection_locators = (By.ID, 'name')
    __change_cycle_December2023_locators = (By.CSS_SELECTOR, "#manageEvalTable > tbody > tr:nth-child(12)")#'#change')

    def openManageEvaluationForEmployeeName(self, selected_name):
        try:
            manage_evaluation_tab = self.wait_for(self.__manage_evaluation_locators)
            manage_evaluation_tab.click()
            employee_selection_tab = self.wait_for(self.__employee_selection_locators)
            employee_names_options_elements = employee_selection_tab.find_elements(By.TAG_NAME, "option")
            founded_employee_name_element = None
            for option in employee_names_options_elements:
                if option.text == selected_name:
                    founded_employee_name_element = option
                    break
            if founded_employee_name_element:
                founded_employee_name_element.click()
                cycle_december_2023_element = self.wait_for(self.__change_cycle_December2023_locators)
                cycle_december_2023_element.find_element(By.ID,"change").click()
                evaluation_status_element = self.wait_for((By.ID,"newStatus"))
                evaluation_status_element.find_element(By.CSS_SELECTOR,"option[value='Started']").click()
                self.wait_for((By.ID,"showtoast")).click()
                #TODO: check if no error ashown or goes into "Manage Evaluation Instance" page
            else:
                raise Exception(f"Error: Cant find an employee with name: {selected_name}")

        except (TimeoutException, NoSuchElementException):
            print("cant locate manage evaluation tab")
            return None

    # def searchInEmployeeName(self, employee_name):
