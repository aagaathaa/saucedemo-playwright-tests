from pages import InventoryPage
from pages import LoginPage


class BaseTest:
    login_page: LoginPage
    inventory_page: InventoryPage