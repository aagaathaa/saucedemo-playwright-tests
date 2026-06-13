import pytest

from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_inventory_page")
class TestInventory(BaseTest):
    def test_01_add_to_cart(self):
        self.login_page.standard_user()
        self.inventory_page.add_to_cart("Sauce Labs Fleece Jacket")
        assert self.cart_page.count_badge() == 1

    def test_02_check_product_in_cart(self):
        self.login_page.standard_user()
        self.inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        self.cart_page.open_cart()
        self.cart_page.is_product_in_cart("Sauce Labs Bolt T-Shirt")