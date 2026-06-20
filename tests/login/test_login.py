import pytest

from framework.base_test import BaseTest


@pytest.mark.usefixtures("setup_login_page")
class TestLogin(BaseTest):
    def test_01_valid_login(self):
        self.login_page.standard_user()

    def test_02_locked_user(self):
        self.login_page.locked_out_user()

        actual_error = (
            self.login_page.get_error_message())
        expected_error = (
            self.login_page.EXPECTED_LOCKED_OUT_ERROR)

        self.login_page.print_actual_expected(actual_error, expected_error)

        assert actual_error == expected_error, (
            f"Wrong error message.\n"
            f"Expected: {expected_error}\n"
            f"Actual:   {actual_error}"
        )

    def test_03_invalid_login(self):
        self.login_page.wrong_user()

        actual_error = self.login_page.get_error_message()
        expected_error = self.login_page.EXPECTED_DONT_MATCH_ERROR

        self.login_page.print_actual_expected(actual_error, expected_error)

        assert actual_error == expected_error, (
            f"Wrong error message.\n"
            f"Expected: {expected_error}\n"
            f"Actual: {actual_error}"
        )
