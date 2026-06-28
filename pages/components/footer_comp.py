from playwright.sync_api import Page

from pages.BasePage import BasePage
from config import config


class FooterComp(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def twitter_btn(self):
        self.click(".social_twitter")
        return self.page.url == config.TWITTER_LINK

    def facebook_btn(self):
        self.click(".social_facebook")
        return self.page.url == config.FACEBOOK_LINK

    def linkedin_btn(self):
        self.click(".social_linkedin")
        return self.page.url == config.LINKDIN_LINK

    def copyright_text(self):
        self.get_text(".footer_copy")

