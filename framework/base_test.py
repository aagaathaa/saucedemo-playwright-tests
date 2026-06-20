from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from pages.OrderCompletePage import OrderCompletePage
from pages.OverviewPage import OverviewPage


class BaseTest:
    login_page: LoginPage
    inventory_page: InventoryPage
    cart_page: CartPage
    checkout_page: CheckoutPage
    overview_page: OverviewPage
    order_complete_page: OrderCompletePage
