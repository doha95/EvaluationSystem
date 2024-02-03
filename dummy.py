# import pytest
# from conftest import driver
#
# # @pytest.mark.dependency
# @pytest.fixture
# def test_a(driver):
#     print("test_a")
#     driver.get("https://www.udemy.com/course/appium-and-selenium-with-python/learn/lecture/20238840#overview")
#     assert False
#
#
# # @pytest.mark.dependency(depends=["test_a"])
# def test_b(driver,test_a):
#     print("test_b")
#     driver.get("https://www.youtube.com/watch?v=1ToQ01ox7MQ")
#     assert True
#
#
# # @pytest.mark.dependency(depends=["test_a", "test_b"])
# def test_d():
#     print("test_d")
#     assert True
