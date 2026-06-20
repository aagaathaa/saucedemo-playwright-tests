# =========================
# General
# =========================

BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
CART_URL = "https://www.saucedemo.com/cart.html"
CHECKOUT_URL = "https://www.saucedemo.com/checkout-step-one.html"
OVERVIEW_URL = "https://www.saucedemo.com/checkout-step-two.html"
ORDER_COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"

# =========================
# Users data
# =========================

UNIQ_PASSWORD = "secret_sauce"
STANDARD_USERNAME = "standard_user"
WRONG_USERNAME = "standart_usr"
LOCKED_OUT_USERNAME = "locked_out_user"


# =========================
# Login Page
# =========================

USERNAME_FIELD = "#user-name"
PASSWORD_FIELD = "#password"
LOGIN_BUTTON = "#login-button"
ERROR_MESSAGE_LOGIN = ".error-message-container"


# =========================
# Inventory Page
# =========================

INVENTORY_ITEM = ".inventory_item"
INVENTORY_ITEM_NAME = ".inventory_item_name"
ADD_TO_CART_BTN = ".btn_inventory"

SHOPPING_CART_CONTAINER = "#shopping_cart_container"
SHOPPING_CART_BADGE = ".shopping_cart_badge"

DEFAULT_PRODUCT = "Sauce Labs Backpack"
EXPECTED_TOTAL_PRICE = "$32.39"
DESC_DEFAULT_PRODUCT = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."

SECOND_PRODUCT = "Sauce Labs Bolt T-Shirt"
THIRD_PRODUCT = "Sauce Labs Fleece Jacket"

# =========================
# Cart Page
# =========================

CART_ITEM = ".cart_item"
CART_QUANTITY = ".cart_quantity"
CART_ITEM_NAME = ".inventory_item_name"

REMOVE_ITEM_BTN = ".btn_secondary.cart_button"
CHECKOUT_BTN = "#checkout"
CONTINUE_TO_SHOPPING_BTN = "#continue-shopping"


# =========================
# Checkout Page
# =========================

FIRST_NAME_FIELD = "#first-name"
LAST_NAME_FIELD = "#last-name"
POST_CODE_FIELD = "#postal-code"
CONTINUE_BTN = "#continue"
CANCEL_BTN_CHECKOUT = "#cancel"

VALID_FIRST_NAME = "Agatha"
VALID_LAST_NAME = "Cohen"
VALID_POST_CODE = "2345652"

EMPTY_FIRST_NAME = ""
EMPTY_LAST_NAME = ""
EMPTY_POST_CODE = ""

LONG_FIRST_NAME = "A" * 100
LONG_LAST_NAME = "B" * 100
LONG_POST_CODE = "1" * 100

SPECIAL_FIRST_NAME = "@@@"
SPECIAL_LAST_NAME = "###"
SPECIAL_POST_CODE = "!@#$%"

NUMERIC_FIRST_NAME = "12345"
NUMERIC_LAST_NAME = "67890"

UNICODE_FIRST_NAME = "Агата"
UNICODE_LAST_NAME = "כהן"

ERROR_MESSAGE_CHECKOUT = "[data-test='error']"


# =========================
# Checkout Overview Page
# =========================

CANCEL_BTN_OVERVIEW = "#cancel"
FINISH_BTN = "#finish"

CART_LIST = ".cart_list"
CART_ITEM = ".cart_item"
CART_QUANTITY_OVERVIEW = ".cart_quantity"
CART_LABEL = ".cart_item_label"
DESC_PRODUCT = ".inventory_item_desc"
# INVENTORY_ITEM_NAME = ".inventory_item_name"
# INVENTORY_ITEM_DESC = ".inventory_item_desc"
# INVENTORY_ITEM_PRICE = ".inventory_item_price"

SUMMARY_INFO = ".summary_info"
LABEL_PAYMENT_INFO = "[data-test='payment-info-label']"
PAYMENT_INFO_VALUE = "[data-test='payment-info-value']"
LABEL_SHIPPING_INFO = "[data-test='shipping-info-label']"
SHIPPING_INFO_VALUE = "[data-test='shipping-info-value']"
LABEL_PRICE_TOTAL = "[data-test='total-info-label']"
SUB_TOTAL = "[data-test='subtotal-label']"
TAX_TOTAL = "[data-test='tax-label']"
SUMMARY_TOTAL = "[data-test='total-label']"

EXPECTED_PAYMENT_LABEL = "Payment Information:"
EXPECTED_SHIPPING_LABEL = "Shipping Information:"
EXPECTED_PRICE_LABEL = "Price Total"

# =========================
# Order Complete Page
# =========================

BACK_HOME_BTN = "#back-to-products"
COMPLETE_HEADER = ".complete-header"
EXPECTED_HEADER = "Thank you for your order!"
COMPLETE_TEXT = ".complete-text"
EXPECTED_COMPLETE_TEXT = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
