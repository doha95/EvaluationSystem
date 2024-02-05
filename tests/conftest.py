import pytest
from selenium import webdriver

from pageObject.LoginPage import LoginPage

# TODO: handle to put it into a file
URL = "http://172.22.1.141:8089/"
EMPLOYEE_USER_NAME = "test-employee5"
EMPLOYEE_PASSWORD = "45622"

Supervisor_USER_NAME = "test-supervisor4"
Supervisor_PASSWORD = "45622"


# TODO: handle this driver how to make it
# @pytest.fixture()#scope="session"  scope="class" scope="module"
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
def login_with_employee(driver):
    login_page = LoginPage(driver=driver)
    # TODO: change it into JSON data with the users
    login_page.login_with_userName_and_password(URL, EMPLOYEE_USER_NAME, EMPLOYEE_PASSWORD)
    # TODO: test the login by the userName


@pytest.fixture
def login_with_supervisor(driver):
    login_page = LoginPage(driver=driver)
    # TODO: change it into JSON data with the users
    login_page.login_with_userName_and_password(URL, Supervisor_USER_NAME, Supervisor_PASSWORD)
    # TODO: test the login by the userName
