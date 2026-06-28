from playwright.sync_api import Page

from config import config
from pages.BasePage import BasePage


class HeaderComp(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def logo(self):
        self.get_text(".app_logo")

    def menu_btn(self):
        self.click("#react-burger-menu-btn")

    def cart_btn(self):
        self.click(".shopping_cart_link")