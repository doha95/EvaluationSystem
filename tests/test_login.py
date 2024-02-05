from pageObject.HomePage import HomePage
from pageObject.LoginPage import LoginPage
from tests.conftest import driver, login_with_employee, login_with_supervisor
import allure
import pytest

URL = "http://172.22.1.141:8089/"
EMPLOYEE_USER_NAME = "test-employee5"
EMPLOYEE_PASSWORD = "45622"

Supervisor_USER_NAME = "test-supervisor4"
Supervisor_PASSWORD = "45622"


@allure.feature("Authentication features")
@allure.title("Test Login With Employee Account")
@pytest.mark.dependency()
def test_login_with_employee(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    # TODO: test the login by the userName
    is_logged_in = home_page.check_home_page_is_loaded()
    assert is_logged_in == True
    driver.close()


@allure.feature("Authentication features")
@allure.title("Test Login With Supervisor Account")
@pytest.mark.dependency()
def test_login_with_supervisor(driver, login_with_supervisor):
    home_page = HomePage(driver=driver)
    # TODO: change it into JSON data with the users
    # TODO: test the login by the userName
    is_logged_in = home_page.check_home_page_is_loaded()
    assert is_logged_in == True
    driver.close()
    # home_page.click_logout()


@allure.feature("Authentication features")
@allure.title("Test With Wrong UserName")
def test_login_wrong_userName(driver):
    login_page = LoginPage(driver=driver)
    # TODO: change it into JSON data with the users
    login_page.login_with_userName_and_password(URL, "wrong username", EMPLOYEE_PASSWORD)
    assert login_page.check_error_message_showed() == True
    # TODO: asset to make the page clear the text input


@allure.feature("Authentication features")
@allure.title("Test With Wrong Password")
def test_login_wrong_password(driver):
    login_page = LoginPage(driver=driver)
    # TODO: change it into JSON data with the users
    login_page.login_with_userName_and_password(URL, EMPLOYEE_USER_NAME, "Wrong Password")
    assert login_page.check_error_message_showed() == True
    # TODO: asset to make the page clear the text input


@allure.feature("Authentication features")
@allure.title("Test access to pages without Authentication")
def test_login_wrong_password(driver):
    # TODO: handel it with refactor
    driver.get("http://172.22.1.141:8089/HR/ManageEvaluationInstancePost")
