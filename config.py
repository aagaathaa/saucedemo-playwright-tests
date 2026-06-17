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
CANCEL_BTN = "#cancel"

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