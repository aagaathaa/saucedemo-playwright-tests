import pytest

from config import config
from framework.base_test import BaseTest


@pytest.mark.usefixtures("setup_inventory_and_cart")
class TestCart(BaseTest):
    def test_01_add_to_cart(self):
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

    def test_04_remove_one_product_from_multiple(self):
        self.cart_page.remove_product("Sauce Labs Bolt T-Shirt")
        assert self.cart_page.count_badge() == 1
        self.cart_page.continue_shopping()
        assert self.cart_page.count_badge() == 1

    def test_05_cart_badge_updates(self):
        self.inventory_page.add_to_cart("Sauce Labs Bike Light")
        assert self.cart_page.count_badge() == 2
        self.inventory_page.add_to_cart("Sauce Labs Onesie")
        assert self.cart_page.count_badge() == 3
