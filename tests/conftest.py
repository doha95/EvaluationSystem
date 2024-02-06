import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
import json
from enum import Enum


class CredentialKeysEnum(Enum):
    USER_NAME = 'userName'
    PASSWORD = 'password'
    USER_FULL_NAME = 'userFullName'


@pytest.fixture(scope="session")
def config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("The JSON file was not found.")
    except json.JSONDecodeError:
        print("The JSON file contains invalid JSON data.")
    except Exception as error:
        print(f"An error occurred while reading the JSON file: {error}")


@pytest.fixture(scope="session")
def base_url(config):
    try:
        return config["url"]
    except Exception as error:
        print(f"An error occurred while reading the JSON file: {error}")


@pytest.fixture(scope="session")
def supervisor_credentials(config):
    try:
        return config["supervisor_credentials"]
    except Exception as error:
        print(f"An error occurred while reading the JSON file: {error}")


@pytest.fixture(scope="session")
def employee_credentials(config):
    try:
        return config["employee_credentials"]
    except Exception as error:
        print(f"An error occurred while reading the JSON file: {error}")


# TODO: handle how we should manage scope the driver
@pytest.fixture(scope="module")
def driver():
    # TODO: handle to create it in singleton
    sizes = [(320, 480), (768, 1024), (1440, 900)]  # Different screen sizes to test
    options = webdriver.ChromeOptions()
    web_driver = webdriver.Chrome(options=options)
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@pytest.fixture
def login_with_employee(driver, base_url, employee_credentials):
    login_page = LoginPage(driver=driver)
    # TODO: change it into JSON data with the users
    user_name = employee_credentials[CredentialKeysEnum.USER_NAME.value]
    password = employee_credentials[CredentialKeysEnum.PASSWORD.value]
    login_page.login_with_userName_and_password(base_url, user_name, password)
    # TODO: test the login by the userName


@pytest.fixture
def login_with_supervisor(driver,base_url,supervisor_credentials):
    login_page = LoginPage(driver=driver)
    # TODO: change it into JSON data with the users
    user_name = supervisor_credentials[CredentialKeysEnum.USER_NAME.value]
    password = supervisor_credentials[CredentialKeysEnum.PASSWORD.value]
    login_page.login_with_userName_and_password(base_url, user_name, password)
    # TODO: test the login by the userName
