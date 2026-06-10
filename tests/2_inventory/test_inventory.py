import pytest

from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_inventory_page")
class TestInventory(BaseTest):
    def test_01_add_to_cart(self):
        self.login_page.standard_user()
        self.inventory_page.add_to_cart("Sauce Labs Fleece Jacket")