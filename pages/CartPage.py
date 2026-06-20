from playwright.sync_api import Page

from config import config
from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    def is_open(self):
        return self.page.url == config.CART_URL

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
        badge = self.page.locator(config.SHOPPING_CART_BADGE)
        count_badge = badge.count()
        if count_badge == 0:
            return 0
        return int(badge.inner_text())

    def remove_product(self, product_name):
        items = self.page.locator(config.CART_ITEM)

        self.click(config.SHOPPING_CART_CONTAINER)

        for index in range(items.count()):
            item = items.nth(index)

            title = item.locator(
                config.CART_ITEM_NAME
            ).inner_text()

            if title == product_name:
                item.locator(config.REMOVE_ITEM_BTN).click()

                return

        raise AssertionError(
            f"Product '{product_name}' not found"
        )

    def continue_shopping(self):
        self.click(config.CONTINUE_TO_SHOPPING_BTN)

    def checkout(self):
        self.click(config.CHECKOUT_BTN)

    def cancel_checkout(self):
        self.click(config.CANCEL_BTN_CHECKOUT)
