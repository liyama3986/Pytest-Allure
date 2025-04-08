import pytest
import allure
from pages.login_page import LoginPage


@allure.feature("login module")
class TestLogin:
    @allure.story("login successfully")
    @allure.title("login with valid credential")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, browser):
        with allure.step("open login page"):
            login_page = LoginPage(browser).open()

        with allure.step("enter username and password"):
            inventory_page = login_page.login("standard_user", "secret_sauce")

        with allure.step("check login successfully"):
            assert inventory_page.is_displayed()
            # assert "inventory" in inventory_page.get_title().lower()
            assert "swag labs" in inventory_page.get_title().lower()


    @allure.story("login failed")
    @allure.title("with invalid credential")
    @allure.severity(allure.severity_level.NORMAL)
    def test_failed_login(self, browser):
        with allure.step("open login page"):
            login_page = LoginPage(browser).open()

        with allure.step("enter invalid username and password"):
            login_page.login("locked_out_user", "wrong_password")

        with allure.step("check error message"):
            error_message = login_page.get_error_message()
            assert "username and password do not match" in error_message.lower()

    @allure.story("login failed")
    @allure.title("lock out user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_locked_out_user(self, browser):
        with allure.step("open login page"):
            login_page = LoginPage(browser).open()

        with allure.step("enter locked user"):
            login_page.login("locked_out_user", "secret_sauce")

        with allure.step("check error message"):
            error_message = login_page.get_error_message()
            assert "this user has been locked out" in error_message.lower()