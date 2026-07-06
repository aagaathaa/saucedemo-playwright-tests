import allure
import pytest

from config import config
from framework.base_test import BaseTest


@allure.feature("Checkout")
@pytest.mark.usefixtures("setup_checkout_page")
class TestCheckout(BaseTest):

    @allure.story("Validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify validation message for empty first name")
    def test_01_validate_empty_first_name(self):
        self.checkout_page.fill_user_info(
            config.EMPTY_FIRST_NAME,
            config.VALID_LAST_NAME,
            config.VALID_POST_CODE
        )

        self.checkout_page.continue_checkout()

        assert (
            self.checkout_page.get_error_message()
            == self.checkout_page.EXPECTED_ERROR_EMPTY_FN
        )

    @allure.story("Validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify validation message for empty last name")
    def test_02_validate_empty_last_name(self):
        self.checkout_page.cancel_checkout()
        self.cart_page.checkout()

        self.checkout_page.fill_user_info(
            config.VALID_FIRST_NAME,
            config.EMPTY_LAST_NAME,
            config.VALID_POST_CODE
        )

        self.checkout_page.continue_checkout()

        assert (
            self.checkout_page.get_error_message()
            == self.checkout_page.EXPECTED_ERROR_EMPTY_LN
        )

    @allure.story("Validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify validation message for empty postal code")
    def test_03_validate_empty_post_code(self):
        self.checkout_page.cancel_checkout()
        self.cart_page.checkout()

        self.checkout_page.fill_user_info(
            config.VALID_FIRST_NAME,
            config.VALID_LAST_NAME,
            config.EMPTY_POST_CODE
        )

        self.checkout_page.continue_checkout()

        assert (
            self.checkout_page.get_error_message()
            == self.checkout_page.EXPECTED_ERROR_EMPTY_PC
        )

    @allure.story("Checkout Flow")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Verify checkout can be cancelled")
    def test_04_cancel_checkout(self):
        self.checkout_page.cancel_checkout()
        self.cart_page.checkout()

        self.checkout_page.fill_user_info(
            config.VALID_FIRST_NAME,
            config.VALID_LAST_NAME,
            config.VALID_POST_CODE
        )

        self.checkout_page.continue_checkout()
        self.checkout_page.cancel_checkout()

        assert self.inventory_page.is_open()