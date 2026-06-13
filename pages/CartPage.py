from playwright.sync_api import Page

import config
from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_cart(self):
        self.page.locator(config.SHOPPING_CART_CONTAINER).click()

    def is_product_in_cart(self, product_name):
        items = self.page.locator(config.CART_ITEM)

        for index in range(items.count()):
            title = items.nth(index).locator(config.CART_ITEM_NAME).inner_text()

            if title == product_name:
                return True

        return False

    def count_badge(self):
        return int(self.page.locator(config.SHOPPING_CART_BADGE).inner_text())
