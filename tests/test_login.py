from pageObject.HomePage import HomePage
from pageObject.LoginPage import LoginPage
from tests.conftest import driver, login_with_employee, login_with_supervisor, CredentialKeysEnum, base_url, \
    supervisor_credentials, employee_credentials
import allure
import pytest


@allure.feature("Authentication features")
@allure.title("Test Login With Employee Account")
@pytest.mark.dependency()
def test_login_with_employee(driver, login_with_employee, employee_credentials):
    home_page = HomePage(driver=driver)
    user_name = employee_credentials[CredentialKeysEnum.USER_FULL_NAME.value]
    is_logged_in = home_page.check_home_page_is_loaded_with_userName(user_name)
    assert is_logged_in
    driver.close()


@allure.feature("Authentication features")
@allure.title("Test Login With Supervisor Account")
@pytest.mark.dependency()
def test_login_with_supervisor(driver, login_with_supervisor, supervisor_credentials):
    home_page = HomePage(driver=driver)
    user_name = supervisor_credentials[CredentialKeysEnum.USER_FULL_NAME.value]
    is_logged_in = home_page.check_home_page_is_loaded_with_userName(user_name)
    assert is_logged_in
    driver.close()


@allure.feature("Authentication features")
@allure.title("Test With Wrong UserName")
def test_login_wrong_userName(driver, base_url, employee_credentials):
    login_page = LoginPage(driver=driver)
    password = employee_credentials[CredentialKeysEnum.PASSWORD.value]
    login_page.login_with_userName_and_password(base_url, "wrong username", password)
    assert login_page.check_error_message_showed() == True
    driver.close()


@allure.feature("Authentication features")
@allure.title("Test With Wrong Password")
def test_login_wrong_password(driver, base_url, employee_credentials):
    login_page = LoginPage(driver=driver)
    user_name = employee_credentials[CredentialKeysEnum.USER_NAME.value]
    login_page.login_with_userName_and_password(base_url, user_name, "Wrong Password")
    assert login_page.check_error_message_showed() == True
    driver.close()


@allure.feature("Authentication features")
@allure.title("Test access to pages without Authentication")
def test_access_page_without_authentication(driver, base_url):
    login_page = LoginPage(driver=driver)
    driver.get(f'{base_url}HR/ManageEvaluationInstancePost')
    assert login_page.check_login_url(base_url)
    driver.close()
