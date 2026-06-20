import pytest

from config import config
from framework.base_test import BaseTest

@pytest.mark.usefixtures("setup_order_complete_page")
class TestOrderComplete(BaseTest):
    def test_01_validate_header(self):
        complete_header = self.order_complete_page.get_complete_header()

        print(f"\nComplete Header: {complete_header}")

        assert complete_header == config.EXPECTED_HEADER

    def test_02_validate_complete_text(self):
        complete_text = self.order_complete_page.get_complete_text()

        print(f"\nComplete Text: {complete_text}")

        assert complete_text == config.EXPECTED_COMPLETE_TEXT

    def test_03_validate_back_home_button(self):
        self.order_complete_page.back_home()
        assert self.inventory_page.is_open()