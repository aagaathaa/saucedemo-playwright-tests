import allure

from playwright.sync_api import Page

from config import config
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def is_open(self):
        return self.page.url == config.BASE_URL

    # Errors
    EXPECTED_LOCKED_OUT_ERROR = \
        "Epic sadface: Sorry, this user has been locked out."
    EXPECTED_DONT_MATCH_ERROR = \
        "Epic sadface: Username and password do not match any user in this service"

    @allure.step("Enter password")
    def password_field(self):
        self.fill_text(config.PASSWORD_FIELD, config.UNIQ_PASSWORD)

    @allure.step("Log in as standard user")
    def standard_user(self):
        self.fill_text(config.USERNAME_FIELD, config.STANDARD_USERNAME)
        self.password_field()
        self.click(config.LOGIN_BUTTON)

    @allure.step("Log in with invalid credentials")
    def wrong_user(self):
        self.fill_text(config.USERNAME_FIELD, config.WRONG_USERNAME)
        self.password_field()
        self.click(config.LOGIN_BUTTON)

    @allure.step("Log in as locked out user")
    def locked_out_user(self):
        self.fill_text(config.USERNAME_FIELD, config.LOCKED_OUT_USERNAME)
        self.password_field()
        self.click(config.LOGIN_BUTTON)

    @allure.step("Get login error message")
    def get_error_message(self):
        return self.get_text(config.ERROR_MESSAGE_LOGIN)