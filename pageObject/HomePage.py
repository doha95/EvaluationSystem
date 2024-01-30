from selenium.webdriver.common.by import By

from pageObject.EvaluationHistoryPage import EvaluationHistoryPage
from pageObject.common.BaseModule import BaseModule
from selenium.common.exceptions import TimeoutException


class HomePage(BaseModule):
    __TITLE_NAME = "Performance Evaluation"
    # Home Locators
    __home_title_locator = (
        By.CSS_SELECTOR, "body > div.page-header.navbar.navbar-fixed-top > div > h4.text-white.text-3xl.pl-5")
    __evaluation_history_tab_locator = (
        By.CSS_SELECTOR, "body > div.page-container > div.page-sidebar-wrapper > div > ul > li.nav-item.active > a")
    __my_evaluation_tab_locator = (
        By.CSS_SELECTOR, "body > div.page-container > div.page-sidebar-wrapper > div > ul > li.nav-item.active > a")

    __user_option_dropdown_locator = (By.CSS_SELECTOR,
                                    "body > div.page-header.navbar.navbar-fixed-top > div > div.top-menu.justify-self-end > ul > li:nth-child(1)")
    __logout_button_locator = (By.CSS_SELECTOR,
                               "body > div.page-header.navbar.navbar-fixed-top > div > div.top-menu.justify-self-end > ul > li:nth-child(1) > ul > li > a")

    def check_home_page_is_loaded(self):
        try:
            title = self.wait_for(self.__home_title_locator).text
            return title == self.__TITLE_NAME
        except TimeoutException:
            return False

    def open_my_evaluation_page(self):
        my_evaluation_tab = self.wait_for(self.__my_evaluation_tab_locator)
        my_evaluation_tab.click()
        # TODO: return MyEvaluationPage

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
