import pytest

from config import config
from framework.base_test import BaseTest

@pytest.mark.usefixtures("setup_overview_page")
class TestOverview(BaseTest):
    def test_01_validate_product(self):
        product_name = self.overview_page.get_product_name()
        product_desc = self.overview_page.get_desc_product()
        product_qty = self.overview_page.quantity()

        print(f"\nProduct name: {product_name}")
        print(f"\nDescription: {product_desc}")
        print(f"\nQuantity: {product_qty}")

        assert self.overview_page.is_product_in_overview(config.DEFAULT_PRODUCT)
        assert product_desc == config.DESC_DEFAULT_PRODUCT
        assert product_qty == "1"

    def test_02_validate_payment_info(self):
        payment_label = self.overview_page.payment_info_label()
        payment_info = self.overview_page.get_payment_info()

        print(f"\nPayment Info: {payment_info}")

        assert payment_info == "SauceCard #31337"
        assert payment_label == config.EXPECTED_PAYMENT_LABEL

    def test_03_validate_shipping_info(self):
        shipping_label = self.overview_page.shipping_info_label()
        shipping_info = self.overview_page.get_shipping_info()
        print(f"\nShipping Info: {shipping_info}")
        assert shipping_info == "Free Pony Express Delivery!"
        assert shipping_label == config.EXPECTED_SHIPPING_LABEL

    def test_04_validate_total_price(self):
        price_label = self.overview_page.price_total_label()
        total_price = self.overview_page.get_summary_total()
        print(f"\nTotal Price: {total_price}")
        assert total_price == config.EXPECTED_TOTAL_PRICE
        assert price_label == config.EXPECTED_PRICE_LABEL

    def test_05_validate_correct_price(self):
        item_total = self.overview_page.extract_price(
            self.overview_page.get_item_total()
        )

        tax = self.overview_page.extract_price(
            self.overview_page.get_tax_total()
        )

        total = self.overview_page.extract_price(
            self.overview_page.get_summary_total()
        )
        print(f"\nItem Total: {item_total}")
        print(f"Tax: {tax}")
        print(f"Expected Total: {item_total + tax}")
        print(f"Actual Total: {total}")

        assert round(item_total + tax, 2) == total

    def test_06_cancel_order(self):
        self.overview_page.cancel_order()
        assert self.inventory_page.is_open()

@pytest.mark.usefixtures("setup_overview_page")
class TestOverviewFinish(BaseTest):
    def test_07_finish_order(self):
        self.overview_page.finish_order()
        assert self.order_complete_page.is_open()