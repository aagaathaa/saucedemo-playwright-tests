# In case you want to open browser before each class
import pytest

from config.config import BASE_URL, DEFAULT_PRODUCT, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_POST_CODE
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from pages.OrderCompletePage import OrderCompletePage
from pages.OverviewPage import OverviewPage


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
    page.goto(BASE_URL)

    request.cls.page = page
    request.cls.login_page = LoginPage(page)

    yield

    page.close()


@pytest.fixture(scope="class")
def setup_inventory_and_cart(request, browser):
    page = browser.new_page()
    page.goto(BASE_URL)

    request.cls.page = page
    request.cls.login_page = LoginPage(page)
    request.cls.inventory_page = InventoryPage(page)
    request.cls.cart_page = CartPage(page)
    request.cls.checkout_page = CheckoutPage(page)

    # Prepare checkout state
    request.cls.login_page.standard_user()

    yield
    page.close()

@pytest.fixture(scope="class")
def setup_checkout_page(request, browser):
    page = browser.new_page()
    page.goto(BASE_URL)

    request.cls.page = page
    request.cls.login_page = LoginPage(page)
    request.cls.inventory_page = InventoryPage(page)
    request.cls.cart_page = CartPage(page)
    request.cls.checkout_page = CheckoutPage(page)

    # Prepare checkout state
    request.cls.login_page.standard_user()
    request.cls.inventory_page.add_to_cart(DEFAULT_PRODUCT)
    request.cls.cart_page.open_cart()
    request.cls.cart_page.checkout()

    yield

    page.close()

@pytest.fixture(scope="class")
def setup_overview_page(request, browser):
    page = browser.new_page()
    page.goto(BASE_URL)

    request.cls.page = page
    request.cls.login_page = LoginPage(page)
    request.cls.inventory_page = InventoryPage(page)
    request.cls.cart_page = CartPage(page)
    request.cls.checkout_page = CheckoutPage(page)
    request.cls.overview_page = OverviewPage(page)
    request.cls.order_complete_page = OrderCompletePage(page)

    # Navigate user to Overview Page
    request.cls.login_page.standard_user()
    request.cls.inventory_page.add_to_cart(DEFAULT_PRODUCT)
    request.cls.cart_page.open_cart()
    request.cls.cart_page.checkout()
    request.cls.checkout_page.fill_user_info(VALID_FIRST_NAME, VALID_LAST_NAME, VALID_POST_CODE)
    request.cls.checkout_page.continue_checkout()


    yield

    page.close()

@pytest.fixture(scope="class")
def setup_order_complete_page(request, browser):
    page = browser.new_page()
    page.goto(BASE_URL)

    request.cls.page = page
    request.cls.login_page = LoginPage(page)
    request.cls.inventory_page = InventoryPage(page)
    request.cls.cart_page = CartPage(page)
    request.cls.checkout_page = CheckoutPage(page)
    request.cls.overview_page = OverviewPage(page)
    request.cls.order_complete_page = OrderCompletePage(page)

    # Navigate user to Overview Page
    request.cls.login_page.standard_user()
    request.cls.inventory_page.add_to_cart(DEFAULT_PRODUCT)
    request.cls.cart_page.open_cart()
    request.cls.cart_page.checkout()
    request.cls.checkout_page.fill_user_info(VALID_FIRST_NAME, VALID_LAST_NAME, VALID_POST_CODE)
    request.cls.checkout_page.continue_checkout()
    request.cls.overview_page.finish_order()

    yield

    page.close()