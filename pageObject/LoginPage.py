from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pageObject.common.BaseModule import BaseModule


class LoginPage(BaseModule):
    __login_url = "http://213.6.2.228/"
    __user_name_locator = (By.ID, "email")
    __password_locator = (By.ID, "password")
    __login_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
    __error_message_locator = (By.CSS_SELECTOR, "body > div > div > div > div > div > span")

    def open_login_page(self):
        self.driver.get(self.__login_url)

    def enter_username(self, username):
        username_input = self.wait_for(self.__user_name_locator)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.wait_for(self.__password_locator)
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.find_element(self.__login_button_locator)
        login_button.click()

    def check_error_message_showed(self):
        try:
            error_message_element = self.wait_for(self.__error_message_locator)
            return error_message_element.is_displayed()
        except TimeoutException:
            return False
