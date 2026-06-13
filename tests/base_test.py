from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage


class BaseTest:
    login_page: LoginPage
    inventory_page: InventoryPage
    cart_page: CartPage