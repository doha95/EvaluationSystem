from pageObject.LoginPage import LoginPage
from pageObject.HomePage import HomePage
from conftest import driver
import allure


@allure.feature("Login")
@allure.story("Valid Login")
def test_login(driver):
    login_page = LoginPage(driver=driver)
    login_page.open_login_page()
    login_page.enter_username("dtubaileh")
    login_page.enter_password("Asal@12345")
    login_page.click_login_button()
    home_page = HomePage(driver=driver)
    is_logged_in = home_page.check_home_page_is_loaded()
    assert is_logged_in == True
