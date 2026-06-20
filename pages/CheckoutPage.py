from playwright.sync_api import Page

from config import config
from pages.BasePage import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def is_open(self):
        return self.page.url == config.CHECKOUT_URL

    # Errors
    EXPECTED_ERROR_EMPTY_FN = \
        "Error: First Name is required"
    EXPECTED_ERROR_EMPTY_LN = \
        "Error: Last Name is required"
    EXPECTED_ERROR_EMPTY_PC = \
        "Error: Postal Code is required"

    def fill_user_info(self, first_name, last_name, post_code):
        self.fill_text(
            config.FIRST_NAME_FIELD,
            first_name
        )

        self.fill_text(
            config.LAST_NAME_FIELD,
            last_name
        )

        self.fill_text(
            config.POST_CODE_FIELD,
            post_code
        )

    def continue_checkout(self):
        self.click(config.CONTINUE_BTN)

    def cancel_checkout(self):
        self.click(config.CANCEL_BTN_CHECKOUT)

    def get_error_message(self):
        return self.get_text(config.ERROR_MESSAGE_CHECKOUT)

    def reopen_checkout(self):
        self.checkout_page.cancel_checkout()
        self.cart_page.checkout()
