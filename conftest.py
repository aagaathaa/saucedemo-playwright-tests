# In case you want to open browser before each class
import pytest

from config.config import (
    BASE_URL,
    DEFAULT_PRODUCT,
    VALID_FIRST_NAME,
    VALID_LAST_NAME,
    VALID_POST_CODE,
    VIEWPORT,
    VIDEO_OPTIONS,
)
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from pages.OrderCompletePage import OrderCompletePage
from pages.OverviewPage import OverviewPage

@pytest.fixture
def setup_login_page(request, browser):
    context = browser.new_context(
        viewport=VIEWPORT,
        **VIDEO_OPTIONS
    )

    page = context.new_page()
    page.goto(BASE_URL)

    request.cls.page = page
    request.cls.login_page = LoginPage(page)

    yield

    context.close()


@pytest.fixture(scope="class")
def setup_inventory_and_cart(request, browser):
    context = browser.new_context(
    viewport=VIEWPORT,
    **VIDEO_OPTIONS
)

    page = context.new_page()
    page.goto(BASE_URL)

    request.cls.page = page
    request.cls.login_page = LoginPage(page)
    request.cls.inventory_page = InventoryPage(page)
    request.cls.cart_page = CartPage(page)
    request.cls.checkout_page = CheckoutPage(page)

    # Prepare checkout state
    request.cls.login_page.standard_user()

    yield
    context.close()

@pytest.fixture(scope="class")
def setup_checkout_page(request, browser):
    context = browser.new_context(
    viewport=VIEWPORT,
    **VIDEO_OPTIONS
)

    page = context.new_page()
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

    context.close()

@pytest.fixture(scope="class")
def setup_overview_page(request, browser):
    context = browser.new_context(
    viewport=VIEWPORT,
    **VIDEO_OPTIONS
)

    page = context.new_page()
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

    context.close()

@pytest.fixture(scope="class")
def setup_order_complete_page(request, browser):
    context = browser.new_context(
    viewport=VIEWPORT,
    **VIDEO_OPTIONS
)

    page = context.new_page()
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

    context.close()