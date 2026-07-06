import allure
import pytest

from config import config
from framework.base_test import BaseTest


@allure.feature("Order Complete")
@pytest.mark.usefixtures("setup_order_complete_page")
class TestOrderComplete(BaseTest):

    @allure.story("Order Confirmation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify order completion header is displayed")
    def test_01_validate_header(self):
        complete_header = self.order_complete_page.get_complete_header()

        print(f"\nComplete Header: {complete_header}")

        assert complete_header == config.EXPECTED_HEADER

    @allure.story("Order Confirmation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify order completion message is displayed")
    def test_02_validate_complete_text(self):
        complete_text = self.order_complete_page.get_complete_text()

        print(f"\nComplete Text: {complete_text}")

        assert complete_text == config.EXPECTED_COMPLETE_TEXT

    @allure.story("Navigation")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Verify Back Home button returns to the inventory page")
    def test_03_validate_back_home_button(self):
        self.order_complete_page.back_home()

        assert self.inventory_page.is_open()