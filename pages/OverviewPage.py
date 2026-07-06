import allure
import re

from playwright.sync_api import Page

from config import config
from pages.BasePage import BasePage


class OverviewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def is_open(self):
        return self.page.url == config.OVERVIEW_URL

    @allure.step("Complete the order")
    def finish_order(self):
        self.click(config.FINISH_BTN)

    @allure.step("Cancel the order")
    def cancel_order(self):
        self.click(config.CANCEL_BTN_OVERVIEW)

    @allure.step("Get payment information label")
    def payment_info_label(self):
        return self.get_text(config.LABEL_PAYMENT_INFO)

    @allure.step("Get payment information")
    def get_payment_info(self):
        return self.get_text(config.PAYMENT_INFO_VALUE)

    @allure.step("Get shipping information label")
    def shipping_info_label(self):
        return self.get_text(config.LABEL_SHIPPING_INFO)

    @allure.step("Get shipping information")
    def get_shipping_info(self):
        return self.get_text(config.SHIPPING_INFO_VALUE)

    @allure.step("Get total price label")
    def price_total_label(self):
        return self.get_text(config.LABEL_PRICE_TOTAL)

    @allure.step("Get order total")
    def get_summary_total(self):
        total = self.get_text(config.SUMMARY_TOTAL)
        return total.replace("Total: ", "")

    @allure.step("Get item total")
    def get_item_total(self):
        item_total = self.get_text(config.SUB_TOTAL)
        return item_total.replace("Item total: ", "")

    @allure.step("Get tax amount")
    def get_tax_total(self):
        tax = self.get_text(config.TAX_TOTAL)
        return tax.replace("Tax: ", "")

    @allure.step("Verify product '{product_name}' is displayed in the order overview")
    def is_product_in_overview(self, product_name):
        label_item = self.locator(config.CART_ITEM)

        for index in range(label_item.count()):
            item = label_item.nth(index)

            item_name = item.locator(config.CART_ITEM_NAME).inner_text()

            if item_name == product_name:
                return True

        raise AssertionError(
            f"Product '{product_name}' not found"
        )

    @allure.step("Get product name")
    def get_product_name(self):
        return self.get_text(config.CART_ITEM_NAME)

    @allure.step("Extract price from text")
    def extract_price(self, text):
        return float(re.search(r"\d+\.\d+", text).group())

    @allure.step("Get product description")
    def get_desc_product(self):
        return self.get_text(config.DESC_PRODUCT)

    @allure.step("Get product quantity")
    def quantity(self):
        return self.get_text(config.CART_QUANTITY)