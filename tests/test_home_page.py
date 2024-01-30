from pageObject.LoginPage import LoginPage
from pageObject.HomePage import HomePage
from conftest import driver
import allure


@allure.feature("Home Page features")
@allure.title("Test User Can Tab My Evaluation ")
def test_select_my_evaluation(driver):
    home_page = HomePage(driver=driver)
    my_evaluation_page = home_page.open_my_evaluation_page()
    assert my_evaluation_page.check_my_history_page_is_loaded() == True


@allure.feature("Home Page features")
@allure.title("Test User Can Tab Evaluation History ")
def test_select_my_evaluation(driver):
    home_page = HomePage(driver=driver)
    evaluation_history_page = home_page.open_evaluation_history_page()
    assert evaluation_history_page.check_history_page_is_loaded() == True
