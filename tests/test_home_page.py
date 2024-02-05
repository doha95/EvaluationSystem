import time
import pytest

from pageObject.HomePage import HomePage
from tests.conftest import driver, login_with_employee, login_with_supervisor
from pageObject.submitting_evaluation.EmployeeEvaluationPage import EmployeeEvaluationPage
import allure


@allure.feature("Home Page features")
@allure.title("Test User Can Tab My Evaluation ")
@pytest.mark.dependency(depends=["test_login_with_employee"])
@pytest.fixture
def test_select_my_evaluation(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    my_evaluation_page = home_page.open_employee_evaluation_page()
    assert my_evaluation_page.check_my_history_page_is_loaded() == True
    driver.close()


@allure.feature("Home Page features")
@allure.title("Test User Can Tab Evaluation History ")
@pytest.fixture
def test_select_evaluation_history(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    evaluation_history_page = home_page.open_evaluation_history_page()
    assert evaluation_history_page.check_history_page_is_loaded() == True
    driver.close()


# TODO: put it in a separate file
employee_evaluation_data = {
    "evaluationSelectionIndex": 4,
    "dislikesText": "dislikes_text",
    "likesText": "likes_text",
    "improvementsText": "improvements_text",
}

supervisor_evaluation_data = {
    "evaluationSelectionIndex": 0,
    "improvementsText": "improvements_text",
    "strengthsText": "strengths_text",
}


@allure.feature("Employee Evaluation features")
@allure.title("Test employee Can fill the evaluation form")
@pytest.mark.dependency()
def test_employee_filling_evaluation_from(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    employee_evaluation_page = home_page.open_employee_evaluation_page()
    employee_evaluation_page.set_evaluation_page_with_dictionary(employee_evaluation_data)
    employee_evaluation_page.click_save_button()
    driver.refresh()
    is_saved = employee_evaluation_page.is_evaluation_saved()
    assert is_saved == True
    employee_evaluation_page.click_submit_button()
    employee_evaluation_page.click_confirm_submit()
    assert employee_evaluation_page.check_employee_submission_date_is_located() == True
    # date should be in the
    driver.close()


@allure.feature("Supervisor Evaluation features")
@allure.title("Test Supervisor Can fill the evaluation form")
# TODO: is it the pest way? maybe we should added it as step in pytest
@pytest.mark.dependency(depends=["test_employee_filling_evaluation_from"])
def test_supervisor_filling_evaluation_from(driver, login_with_supervisor):
    home_page = HomePage(driver=driver)
    supervisor_page = home_page.open_supervisor_evaluation_team_page()
    # TODO: handle how to open specifect employee, maybe could more than one
    supervisor_evaluation_page = supervisor_page.click_open_evaluation_button()
    supervisor_evaluation_page.set_supervisor_evaluation_info_with_dictionary(supervisor_evaluation_data)
    supervisor_evaluation_page.click_save_button()
    supervisor_evaluation_page.click_submit_button()
    assert supervisor_evaluation_page.check_supervisor_submission_date_is_located()
    supervisor_evaluation_page.click_confirm_review_submit()
    assert supervisor_evaluation_page.check_review_submission_date_is_located()
    driver.close()


@allure.feature("Employee Evaluation features")
@allure.title("Test employee Can close evaluation")
@pytest.mark.dependency(depends=["test_employee_filling_evaluation_from", "test_supervisor_filling_evaluation_from"])
def test_employee_closing_evaluation(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    employee_evaluation_page = home_page.open_employee_evaluation_page()
    employee_evaluation_page.click_close_evaluation_button()
    assert employee_evaluation_page.check_close_submission_date_is_located()
    # date should be in the
    driver.close()
