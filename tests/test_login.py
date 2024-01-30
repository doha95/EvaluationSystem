from pageObject.LoginPage import LoginPage
from pageObject.HomePage import HomePage
from conftest import driver
import allure

USER_NAME = "dtubaileh"
PASSWORD = "Asal@12345"


@allure.feature("Authentication features")
@allure.title("Test With Correct Username and Password")
def test_login_with_correct_auth(driver):
    login_page = LoginPage(driver=driver)
    home_page = HomePage(driver=driver)
    login_page.open_login_page()
    # TODO: change it into JSON data with the users
    login_page.enter_username(USER_NAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()
    is_logged_in = home_page.check_home_page_is_loaded()
    assert is_logged_in == True
    home_page.click_logout()


@allure.feature("Authentication features")
@allure.title("Test With Wrong Password")
def test_login_wrong_password(driver):
    login_page = LoginPage(driver=driver)
    login_page.open_login_page()
    # TODO: change it into JSON data with the users
    login_page.enter_username(USER_NAME)
    login_page.enter_password("Wrong Password")
    login_page.click_login_button()
    assert login_page.check_error_message_showed() == True
    # TODO: asset to make the page clear the text input


@allure.feature("Authentication features")
@allure.title("Test With Wrong UserName")
def test_login_wrong_userName(driver):
    login_page = LoginPage(driver=driver)
    login_page.open_login_page()
    # TODO: change it into JSON data with the users
    login_page.enter_username("wrong username")
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()
    assert login_page.check_error_message_showed() == True
# TODO: asset to make the page clear the text input
