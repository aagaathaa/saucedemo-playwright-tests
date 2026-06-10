from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.__page = page

    @property
    def page(self):
        return self.__page

    def fill_text(self, locator, text):
        self.page.locator(locator).highlight()
        self.page.locator(locator).fill(text)

    def click(self, locator):
        self.page.locator(locator).highlight()
        self.page.locator(locator).click()

    def select_option(self, locator, text):
        self.page.locator(locator).highlight()
        self.page.locator(locator).select_option(text)

    def get_text(self, locator):
        self.page.locator(locator).highlight()
        text = self.page.locator(locator).inner_text()
        return text

    def print_actual_exepected(self, actual_error, expected_error):
        print("\n===== Error Validation =====")
        print(f"Actual:   '{actual_error}'")
        print(f"Expected: '{expected_error}'")