from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage


class BaseTest:
    login_page: LoginPage
    inventory_page: InventoryPage
    cart_page: CartPage
    checkout_page: CheckoutPage
