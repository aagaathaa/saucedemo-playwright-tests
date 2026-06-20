import pytest

from config import config
from framework.base_test import BaseTest


@pytest.mark.usefixtures("setup_checkout_page")
class TestCheckout(BaseTest):

    def test_01_validate_empty_first_name(self):
        self.checkout_page.fill_user_info(config.EMPTY_FIRST_NAME, config.VALID_LAST_NAME, config.VALID_POST_CODE)
        self.checkout_page.continue_checkout()
        assert self.checkout_page.get_error_message() == self.checkout_page.EXPECTED_ERROR_EMPTY_FN

    def test_02_validate_empty_last_name(self):
        self.checkout_page.cancel_checkout()
        self.cart_page.checkout()
        self.checkout_page.fill_user_info(config.VALID_FIRST_NAME, config.EMPTY_LAST_NAME, config.VALID_POST_CODE)
        self.checkout_page.continue_checkout()
        assert self.checkout_page.get_error_message() == self.checkout_page.EXPECTED_ERROR_EMPTY_LN

    def test_03_validate_empty_post_code(self):
        self.checkout_page.cancel_checkout()
        self.cart_page.checkout()
        self.checkout_page.fill_user_info(config.VALID_FIRST_NAME, config.VALID_LAST_NAME, config.EMPTY_POST_CODE)
        self.checkout_page.continue_checkout()
        assert self.checkout_page.get_error_message() == self.checkout_page.EXPECTED_ERROR_EMPTY_PC

    def test_04_cancel_checkout(self):
        self.checkout_page.cancel_checkout()
        self.cart_page.checkout()
        self.checkout_page.fill_user_info(config.VALID_FIRST_NAME, config.VALID_LAST_NAME, config.VALID_POST_CODE)
        self.checkout_page.continue_checkout()
        self.checkout_page.cancel_checkout()
        assert self.inventory_page.is_open()