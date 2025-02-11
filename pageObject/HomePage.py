from selenium.webdriver.common.by import By

from pageObject.EvaluationHistoryPage import EvaluationHistoryPage
from pageObject.submitting_evaluation.SupervisorEvaluationPage import SupervisorEvaluationPage
from pageObject.submitting_evaluation.EmployeeEvaluationPage import EmployeeEvaluationPage
from pageObject.common.BaseModule import BaseModule
from selenium.common.exceptions import TimeoutException
from pageObject.SupervisorTeamEvaluationPage import SupervisorTeamEvaluationPage


class HomePage(BaseModule):
    __TITLE_NAME = "Performance Evaluation"
    # Home Locators
    __home_title_locator = (
        By.CSS_SELECTOR, "body > div.page-header.navbar.navbar-fixed-top > div > h4.text-white.text-3xl.pl-5")
    __evaluation_history_tab_locator = (
        By.CSS_SELECTOR, "body > div.page-container > div.page-sidebar-wrapper > div > ul >  li:nth-child(3)")
    __my_evaluation_tab_locator = (
        By.CSS_SELECTOR, "body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(2)")

    __user_option_dropdown_locator = (By.CSS_SELECTOR,
                                      "body > div.page-header.navbar.navbar-fixed-top > div > div.top-menu.justify-self-end > ul > li:nth-child(1)")
    __logout_button_locator = (By.CSS_SELECTOR,
                               "body > div.page-header.navbar.navbar-fixed-top > div > div.top-menu.justify-self-end > ul > li:nth-child(1) > ul > li > a")
    __current_user_name_locator = (By.CSS_SELECTOR, "body > div.page-header.navbar.navbar-fixed-top > div > div.top-menu.justify-self-end > ul > li:nth-child(1) > a > span")
    # supervisor locators only
    __supervisor_team_tab_locator = (
        By.CSS_SELECTOR, "body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(4)")
    current_evaluation_cycle_date = ""

    def check_home_page_is_loaded_with_userName(self,userName):
        try:
            login_name = self.wait_for(self.__current_user_name_locator).text
            return userName in login_name
        except TimeoutException:
            return False

    def open_employee_evaluation_page(self):
        try:
            my_evaluation_tab = self.wait_for(self.__my_evaluation_tab_locator)
            my_evaluation_tab.click()
            employeeEvaluationPage = EmployeeEvaluationPage(self.driver)
            self.current_evaluation_cycle_date = employeeEvaluationPage.get_current_evaluation_cycle()
            return employeeEvaluationPage
        except TimeoutException:
            return None

    def open_supervisor_evaluation_team_page(self):
        try:
            supervisor_team_tab = self.wait_for(self.__supervisor_team_tab_locator)
            supervisor_team_tab.click()
            return SupervisorTeamEvaluationPage(self.driver)
        except TimeoutException:
            return None

    def open_evaluation_history_page(self):
        try:
            evaluation_history_tab = self.wait_for(self.__evaluation_history_tab_locator)
            evaluation_history_tab.click()
            return EvaluationHistoryPage(self.driver)
        except TimeoutException:
            return None

    def click_logout(self):
        try:
            drop_down_element = self.wait_for(self.__user_option_dropdown_locator)
            drop_down_element.click()
            logout_button = self.wait_for(self.__logout_button_locator)
            logout_button.click()
        except TimeoutException:
            return None
