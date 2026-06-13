# In case you want to open browser before each class
import pytest

from pages.CartPage import CartPage
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage

# Old fixture, disabled for now
# @pytest.fixture(scope="class", autouse=True)
# def setup_page_class(request, browser):
#     request.cls.page = browser.new_page()
#     request.cls.page.goto("https://www.saucedemo.com/")
#     request.cls.login_page = LoginPage(request.cls.page)
#     yield
#     request.cls.page.close()
#     browser.close()


@pytest.fixture
def setup_login_page(request, browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")

    request.cls.page = page
    request.cls.login_page = LoginPage(page)

    yield

    page.close()

@pytest.fixture
def setup_inventory_page(request, browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")

    request.cls.page = page
    request.cls.login_page = LoginPage(page)
    request.cls.inventory_page = InventoryPage(page)
    request.cls.cart_page = CartPage(page)

    yield
    page.close()