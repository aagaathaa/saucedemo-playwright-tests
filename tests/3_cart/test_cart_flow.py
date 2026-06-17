import pytest

import config
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_inventory_page")
class TestCartFlow(BaseTest):
    def test_01_add_to_cart(self):
        self.login_page.standard_user()
        self.inventory_page.add_to_cart("Sauce Labs Fleece Jacket")
        assert self.cart_page.count_badge() == 1

    def test_02_remove_from_cart(self):
        self.cart_page.remove_product("Sauce Labs Fleece Jacket")
        self.cart_page.continue_shopping()
        assert self.cart_page.count_badge() == 0

    def test_03_add_multiple_products(self):
        self.inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        self.inventory_page.add_to_cart("Sauce Labs Fleece Jacket")
        self.cart_page.open_cart()
        assert self.cart_page.is_product_in_cart("Sauce Labs Bolt T-Shirt")
        assert self.cart_page.is_product_in_cart("Sauce Labs Fleece Jacket")
        assert self.cart_page.count_badge() == 2

    def test_04_valid_checkout(self):
        self.cart_page.checkout()
        self.checkout_page.fill_user_info(config.VALID_FIRST_NAME, config.VALID_LAST_NAME, config.VALID_POST_CODE)
        self.checkout_page.continue_checkout()
        self.checkout_page.cancel_checkout()

    def test_05_empty_checkout(self):
        self.cart_page.open_cart()
        self.cart_page.checkout()
        self.checkout_page.fill_user_info(config.EMPTY_FIRST_NAME, config.VALID_LAST_NAME, config.VALID_POST_CODE)
        self.checkout_page.continue_checkout()
        assert self.checkout_page.get_error_message() == self.checkout_page.EXPECTED_ERROR_EMPTY_FN
