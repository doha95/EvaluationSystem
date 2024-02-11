import time

import pytest

from pageObject.HomePage import HomePage
from conftest import driver, login_with_employee, config, base_url, login_with_supervisor, supervisor_credentials, \
    employee_credentials, login_with_hr, hr_credentials
from utills.DateProcess import is_ordered_by_date
from utills.Contants import CredentialKeysEnum
from pageObject.HrManagement import HrManagement
import allure
import random

RATING_VALUES_IDS = ["Unsatisfactory", "Improvement_Required", "Developing_Performer", "Solid_Performer",
                     "Exceeds_Expectations", "Outstanding"]


# TODO: put it in a separate file
# @pytest.fixture(scope="module")
def generate_evaluation_rating(table_rows=18):
    # TODO: make it auto according to table row num
    result = []
    for index in range(table_rows):
        # result.append(RATING_VALUES_IDS[3])
        result.append(random.choice(RATING_VALUES_IDS))
    return result


employee_evaluation_data = {
    "evaluationSelections": generate_evaluation_rating(),
    "dislikesText": "dislikes_text",
    "likesText": "likes_text",
    "improvementsText": "improvements_text",
}

supervisor_evaluation_data = {
    "evaluationSelections": generate_evaluation_rating(),
    "improvementsText": "improvements_text",
    "strengthsText": "strengths_text",
}


# TODO: put the above into a seperate file
@allure.feature("Home Page features")
@allure.title("Test initiate the evaluation cycle")
@pytest.mark.dependency()
def test_initiate_evaluation_cycle(driver, login_with_hr, employee_credentials):
    hr_ManagementPage = HrManagement(driver=driver)
    hr_ManagementPage.openManageEvaluationForEmployeeName(employee_credentials[CredentialKeysEnum.USER_FULL_NAME.value])


@allure.feature("Home Page features")
@allure.title("Test User Can Tab My Evaluation ")
def test_select_my_evaluation(driver, login_with_employee):
    home_page = HomePage(driver=driver)
    my_evaluation_page = home_page.open_employee_evaluation_page()
    assert my_evaluation_page.check_my_evaluation_page_is_loaded()


@allure.feature("Evaluation features")
@allure.title("Test employee can save the evaluation form")
@pytest.mark.dependency(depends=["test_select_my_evaluation"])
def test_employee_can_save_evaluation_from(driver, login_with_employee, ):
    home_page = HomePage(driver=driver)
    employee_evaluation_page = home_page.open_employee_evaluation_page()
    employee_evaluation_page.set_evaluation_page_with_dictionary(employee_evaluation_data)
    employee_evaluation_page.click_save_button()
    driver.refresh()
    is_saved = employee_evaluation_page.is_evaluation_page_saved_with_dictionary_info(employee_evaluation_data)
    assert is_saved


@allure.feature("Evaluation features")
@allure.title("Test employee can fill the evaluation form")
@pytest.mark.dependency(depends=["test_employee_can_save_evaluation_from"])
def test_employee_submit_evaluation_from(driver, login_with_employee, ):
    home_page = HomePage(driver=driver)
    employee_evaluation_page = home_page.open_employee_evaluation_page()
    employee_evaluation_page.click_submit_button()
    employee_evaluation_page.click_confirm_submit()
    assert employee_evaluation_page.check_employee_submission_date_is_located()
    assert employee_evaluation_page.is_evaluation_page_submited_with_dictionary_info(employee_evaluation_data)


@allure.feature("Evaluation features")
@allure.title("Test Supervisor can save the evaluation form")
@pytest.mark.dependency(depends=["test_employee_submit_evaluation_from"])
def test_supervisor_save_evaluation_from(driver, login_with_supervisor):
    home_page = HomePage(driver=driver)
    supervisor_page = home_page.open_supervisor_evaluation_team_page()
    # TODO: handle how to open specifect employee
    supervisor_evaluation_page = supervisor_page.click_open_evaluation_button()
    assert supervisor_evaluation_page.check_my_evaluation_page_is_loaded()
    supervisor_evaluation_page.set_supervisor_evaluation_info_with_dictionary(supervisor_evaluation_data)
    supervisor_evaluation_page.click_save_button()
    is_saved = supervisor_evaluation_page.is_supervisor_evaluation_page_saved_with_dictionary_info(
        supervisor_evaluation_data)
    assert is_saved


@allure.feature("Evaluation features")
@allure.title("Test Supervisor can submit the evaluation form")
@pytest.mark.dependency(depends=["test_supervisor_save_evaluation_from"])
def test_supervisor_submit_evaluation_from(driver, login_with_supervisor):
    home_page = HomePage(driver=driver)
    supervisor_page = home_page.open_supervisor_evaluation_team_page()
    # TODO: handle how to open specifect employee
    supervisor_evaluation_page = supervisor_page.click_open_evaluation_button()
    assert supervisor_evaluation_page.check_my_evaluation_page_is_loaded()
    supervisor_evaluation_page.click_submit_button()
    supervisor_evaluation_page.click_confirm_submit()
    assert supervisor_evaluation_page.check_supervisor_submission_date_is_located()
    # TODO: handle assert submisstion with the supervisor same as employee


@allure.feature("Evaluation features")
@allure.title("Test Supervisor Close the evaluation form")
@pytest.mark.dependency(depends=["test_supervisor_submit_evaluation_from"])
def test_supervisor_closing_evaluation_from(driver, login_with_supervisor):
    home_page = HomePage(driver=driver)
    supervisor_page = home_page.open_supervisor_evaluation_team_page()
    supervisor_evaluation_page = supervisor_page.click_open_evaluation_button()
    supervisor_evaluation_page.click_close_evaluation_button()
    supervisor_evaluation_page.click_confirm_close_review_submit()
    assert supervisor_evaluation_page.check_review_submission_date_is_located()


@allure.feature("Evaluation features")
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
    assert evaluation_history_page.check_history_page_is_loaded()


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
