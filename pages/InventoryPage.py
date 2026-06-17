from playwright.sync_api import Page

import config
from pages.BasePage import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def add_to_cart(self, product_name):
        items = self.page.locator(config.INVENTORY_ITEM)

        for index in range(items.count()):
            item = items.nth(index)

            title = item.locator(
                config.INVENTORY_ITEM_NAME
            ).inner_text()

            # print(title)

            if title == product_name:
                item.locator(
                    config.ADD_TO_CART_BTN
                ).click()

                return

        raise AssertionError(
            f"Product '{product_name}' not found"
        )
