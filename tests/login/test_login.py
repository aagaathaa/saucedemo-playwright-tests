import allure
import pytest

from framework.base_test import BaseTest


@allure.feature("Login")
@pytest.mark.usefixtures("setup_login_page")
class TestLogin(BaseTest):

    @allure.story("Successful Login")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Verify successful login with valid credentials")
    def test_01_valid_login(self):
        self.login_page.standard_user()

    @allure.story("Locked User")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify locked user cannot log in")
    def test_02_locked_user(self):
        self.login_page.locked_out_user()

        actual_error = self.login_page.get_error_message()
        expected_error = self.login_page.EXPECTED_LOCKED_OUT_ERROR

        self.login_page.print_actual_expected(actual_error, expected_error)

        assert actual_error == expected_error, (
            f"Wrong error message.\n"
            f"Expected: {expected_error}\n"
            f"Actual:   {actual_error}"
        )

    @allure.story("Invalid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify login fails with invalid credentials")
    def test_03_invalid_login(self):
        self.login_page.wrong_user()

        actual_error = self.login_page.get_error_message()
        expected_error = self.login_page.EXPECTED_DONT_MATCH_ERROR

        self.login_page.print_actual_expected(actual_error, expected_error)

        assert actual_error == expected_error, (
            f"Wrong error message.\n"
            f"Expected: {expected_error}\n"
            f"Actual:   {actual_error}"
        )