import time

import pytest

from pageObject.HomePage import HomePage
from conftest import driver, login_with_employee, config, base_url, login_with_supervisor, supervisor_credentials, \
    employee_credentials
from utills.DateProcess import is_ordered_by_date
import allure

# TODO: put it in a separate file
employee_evaluation_data = {
    "evaluationSelectionIndex": 4,
    "dislikesText": "dislikes_text",
    "likesText": "likes_text",
    "improvementsText": "improvements_text",
}

supervisor_evaluation_data = {
    "evaluationSelectionIndex": 4,
    "improvementsText": "improvements_text",
    "strengthsText": "strengths_text",
}


@allure.feature("Home Page features")
@allure.title("Test User Can Tab My Evaluation ")
@pytest.mark.dependency(depends=["test_login_with_employee"])
def test_select_my_evaluation(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    my_evaluation_page = home_page.open_employee_evaluation_page()
    assert my_evaluation_page.check_my_history_page_is_loaded() == True


@allure.feature("Employee Evaluation features")
@allure.title("Test employee Can fill the evaluation form")
@pytest.mark.dependency()
def test_employee_filling_evaluation_from(driver, login_with_employee):
    # TODO: convert it into two test cases
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


@allure.feature("Supervisor Evaluation features")
@allure.title("Test Supervisor Can fill and submit the evaluation form")
# TODO: is it the pest way? maybe we should added it as step in pytest
@pytest.mark.dependency(depends=["test_employee_filling_evaluation_from"])
def test_supervisor_submit_evaluation_from(driver, login_with_supervisor):
    home_page = HomePage(driver=driver)
    supervisor_page = home_page.open_supervisor_evaluation_team_page()
    # TODO: handle how to open specifect employee
    supervisor_evaluation_page = supervisor_page.click_open_evaluation_button()
    supervisor_evaluation_page.set_supervisor_evaluation_info_with_dictionary(supervisor_evaluation_data)
    supervisor_evaluation_page.click_save_button()
    supervisor_evaluation_page.click_submit_button()
    supervisor_evaluation_page.click_confirm_submit()
    assert supervisor_evaluation_page.check_supervisor_submission_date_is_located()


@allure.feature("Supervisor Evaluation features")
@allure.title("Test Supervisor Close the evaluation form")
# TODO: is it the pest way? maybe we should added it as step in pytest
@pytest.mark.dependency(depends=["test_supervisor_submit_evaluation_from"])
def test_supervisor_closing_evaluation_from(driver, login_with_supervisor):
    home_page = HomePage(driver=driver)
    supervisor_page = home_page.open_supervisor_evaluation_team_page()
    supervisor_evaluation_page = supervisor_page.click_open_evaluation_button()
    supervisor_evaluation_page.click_close_evaluation_button()
    supervisor_evaluation_page.click_confirm_close_review_submit()
    assert supervisor_evaluation_page.check_review_submission_date_is_located()


@allure.feature("Employee Evaluation features")
@allure.title("Test employee Can close evaluation")
@pytest.mark.dependency(depends=["test_supervisor_closing_evaluation_from"])
def test_employee_closing_evaluation(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    employee_evaluation_page = home_page.open_employee_evaluation_page()
    employee_evaluation_page.click_close_evaluation_button()
    employee_evaluation_page.click_confirm_close_review_submit()
    assert employee_evaluation_page.check_close_submission_date_is_located()


@allure.feature("Home Page features")
@allure.title("Test User Can Tab Evaluation History")
@pytest.mark.dependency(depends=["test_employee_closing_evaluation"])
def test_select_evaluation_history(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    evaluation_history_page = home_page.open_evaluation_history_page()
    assert evaluation_history_page.check_history_page_is_loaded() == True


@allure.feature("Evaluation History features")
@allure.title("Test History table is in displayed in chronological order")
def test_evaluation_history_is_displayed_in_chronological_order(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    evaluation_history_page = home_page.open_evaluation_history_page()
    evaluation_data = evaluation_history_page.get_evaluation_table_content()
    listed_cycles_date = [item["cycle"] for item in evaluation_data if "cycle" in item]
    assert is_ordered_by_date(listed_cycles_date)


@allure.feature("Evaluation History features")
@allure.title("Test user can find his current cycle evaluation history")
def test_search_current_cycle_evaluation_history(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    evaluation_history_page = home_page.open_evaluation_history_page()
    evaluation_history_page.search_for_evaluation_table(home_page.current_evaluation_cycle_date)
    evaluation_data = evaluation_history_page.get_evaluation_table_content()
    assert len(evaluation_data) > 0


@allure.feature("Evaluation History features")
@allure.title("Test user can view his submission when the evaluation is closed")
@pytest.mark.dependency(depends=["test_employee_closing_evaluation"])
def test_open_evaluation_when_closed(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    evaluation_history_page = home_page.open_evaluation_history_page()
    evaluation_history_page.search_for_evaluation_table(home_page.current_evaluation_cycle_date)
    evaluation_data = evaluation_history_page.get_evaluation_table_content()
    # get the `Action` item for the closed evaluation
    for item in evaluation_data:
        if item["status"] == "Closed":
            closed_action_item = item["action"]
            closed_action_item.click()

    assert evaluation_history_page.check_user_history_page_is_loaded()
