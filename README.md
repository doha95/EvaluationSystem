# Evaluation System:
The Asal Employee Evaluation System is designed to facilitate the evaluation process for employees at Asal. 
Each employee is assigned a direct supervisor responsible for evaluating their performance.

## installation:
This project is built over a Python environment, so all the dependencies are listed in the `requirements.txt`.
1. All you have to do is set up `python`, `pip`, `Allure`.
2. Run the following command to install dependency's.
```
pip install -r requirements.txt
```


## Reporting:
The project utilizes Allure for comprehensive test reporting. To view the test results, follow these steps:
1. Run the testing command and save the result into `allure-results` file.
```
pytest --clean-alluredir --alluredir allure-results
```
2. Run the following to show results.
```
allure serve
```
This command will start a local server hosting the Allure report. Open your web browser and navigate to the provided URL to view the detailed test results.

![Test Report](./utills/images/test_results.png)


## Credentials:
To access the web application, use the provided testing accounts located in the `config.json` file. This file contains credentials for both supervisors and employees.


## Project Structures:
1. `pageObject`: Contains the Page Object Models for different components of the application, including login, home, employee evaluation, supervisor evaluation, and evaluation history.
2. `test`: Contains the test scenarios for the evaluation system.
3. `conftest`: Houses configuration fixtures required for the project.

## Limitation:
1. The system cant open the evaluation cycle automatically, and there is a serious bug regarding any changes in the evaluation cycle it does not reflect on both employee and supervisor, 
for example: changing the status for the evaluation cycle from `closed` to `opened` will reflect only on the employee but not on the supervisor it will remain `closed`.

## What New?:
1. Export the dependency's into `requirements.txt`.
2. Adding automation code for opening the evaluation cycle from the HR Account,
 **blocked by the limitation point above**.
3. put the selected browser in the JSON file, so it can run the desired browser.
4. find a way to open the evaluation for each session, currently the web having an issue.
5. adding more testing scenarios.
6. code refactoring.
