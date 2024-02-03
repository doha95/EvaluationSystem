import time

from pageObject.HomePage import HomePage
from tests.conftest import driver, login_with_employee,login_with_supervisor
from pageObject.MyEvaluationPage import MyEvaluationPage
import allure


# @allure.feature("Home Page features")
# @allure.title("Test User Can Tab My Evaluation ")
# # @pytest.mark.dependency(depends=["test_login_with_employee"])
# @pytest.fixture
# def test_select_my_evaluation(driver, login_with_employee):
#     home_page = HomePage(driver=driver)
#     my_evaluation_page = home_page.open_my_evaluation_page()
#     assert my_evaluation_page.check_my_history_page_is_loaded() == True
#     driver.close()
#
#
# @allure.feature("Home Page features")
# @allure.title("Test User Can Tab Evaluation History ")
# @pytest.fixture
# def test_select_evaluation_history(driver, login_with_employee):
#     home_page = HomePage(driver=driver)
#     evaluation_history_page = home_page.open_evaluation_history_page()
#     assert evaluation_history_page.check_history_page_is_loaded() == True
#     driver.close()

# @allure.feature("Home Page features")
# @allure.title("Test employee Can fill the evaluation form ")
# def test_filling_evaluation_from(driver, login_with_employee):
#     home_page = HomePage(driver=driver)
#     my_evaluation_page = home_page.open_my_evaluation_page()
#     # TODO: rename methode to make understandable
#     my_evaluation_page.process_table(selectionIndex=2)
#     my_evaluation_page.set_dislikes_text("dislikes_text")
#     my_evaluation_page.set_improvements_text("improvements_text")
#     my_evaluation_page.set_likes_text("likes_text")
#     my_evaluation_page.click_save_button()
#     my_evaluation_page.click_submit_button()
#     my_evaluation_page.click_confirm_submit()
#     driver.close()

@allure.feature("Home Page features")
@allure.title("Test Supervisor Can fill the evaluation form ")
def test_filling_evaluation_from(driver, login_with_supervisor):
    home_page = HomePage(driver=driver)
    my_evaluation_page = MyEvaluationPage(driver=driver)
    supervisor_evaluation = home_page.open_supervisor_evaluation_team_page()
    supervisor_evaluation.click_open_evaluation_button()
    # TODO: rename methode to make understandable
    my_evaluation_page.process_table(selectionIndex=2)
    # my_evaluation_page.set_dislikes_text("dislikes_text")
    # my_evaluation_page.set_improvements_text("improvements_text")
    # my_evaluation_page.set_likes_text("likes_text")
    my_evaluation_page.set_areas_to_reinforce_text("areas_to_reinforce_strength")
    my_evaluation_page.set_areas_of_improvements_text("areas_of_improvements_text")
    my_evaluation_page.click_save_button()
    my_evaluation_page.click_submit_button()
    my_evaluation_page.click_confirm_submit()
    driver.close()
