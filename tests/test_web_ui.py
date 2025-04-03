import pytest
import allure
from pages.login_page import LoginPage


@allure.feature("登录功能")
class TestLogin:
    @allure.story("成功登录")
    @allure.title("使用有效凭证登录")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, browser):
        with allure.step("打开登录页面"):
            login_page = LoginPage(browser).open()

        with allure.step("输入用户名和密码"):
            inventory_page = login_page.login("standard_user", "secret_sauce")

        with allure.step("验证登录成功"):
            assert inventory_page.is_displayed()
            # assert "inventory" in inventory_page.get_title().lower()
            assert "swag labs" in inventory_page.get_title().lower()


    @allure.story("失败登录")
    @allure.title("使用无效凭证登录")
    @allure.severity(allure.severity_level.NORMAL)
    def test_failed_login(self, browser):
        with allure.step("打开登录页面"):
            login_page = LoginPage(browser).open()

        with allure.step("输入错误的用户名和密码"):
            login_page.login("locked_out_user", "wrong_password")

        with allure.step("验证错误消息"):
            error_message = login_page.get_error_message()
            assert "username and password do not match" in error_message.lower()

    @allure.story("失败登录")
    @allure.title("锁定用户登录")
    @allure.severity(allure.severity_level.NORMAL)
    def test_locked_out_user(self, browser):
        with allure.step("打开登录页面"):
            login_page = LoginPage(browser).open()

        with allure.step("输入锁定用户的凭证"):
            login_page.login("locked_out_user", "secret_sauce")

        with allure.step("验证错误消息"):
            error_message = login_page.get_error_message()
            assert "this user has been locked out" in error_message.lower()