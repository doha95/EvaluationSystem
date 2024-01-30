import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    web_driver = webdriver.Chrome(options=options)
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()
