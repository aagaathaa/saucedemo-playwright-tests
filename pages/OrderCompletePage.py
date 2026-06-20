from playwright.sync_api import Page

from config import config
from pages.BasePage import BasePage


class OrderCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def is_open(self):
        return self.page.url == config.ORDER_COMPLETE_URL

    def get_complete_header(self):
        return self.get_text(config.COMPLETE_HEADER)

    def get_complete_text(self):
        return self.get_text(config.COMPLETE_TEXT)

    def back_home(self):
        self.click(config.BACK_HOME_BTN)