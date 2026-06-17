from playwright.sync_api import Page

import config
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # Errors
    EXPECTED_LOCKED_OUT_ERROR = \
        "Epic sadface: Sorry, this user has been locked out."
    EXPECTED_DONT_MATCH_ERROR = \
        "Epic sadface: Username and password do not match any user in this service"

    def password_field(self):
        self.fill_text(config.PASSWORD_FIELD, config.UNIQ_PASSWORD)

    def standard_user(self):
        self.fill_text(config.USERNAME_FIELD, config.STANDARD_USERNAME)
        self.password_field()
        self.click(config.LOGIN_BUTTON)

    def wrong_user(self):
        self.fill_text(config.USERNAME_FIELD, config.WRONG_USERNAME)
        self.password_field()
        self.click(config.LOGIN_BUTTON)

    def locked_out_user(self):
        self.fill_text(config.USERNAME_FIELD, config.LOCKED_OUT_USERNAME)
        self.password_field()
        self.click(config.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(config.ERROR_MESSAGE_LOGIN)
