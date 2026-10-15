"""Selectores de Sauce Demo."""
from selenium.webdriver.common.by import By

# Login
USER = (By.ID, "user-name")
PASS = (By.ID, "password")
LOGIN_BTN = (By.ID, "login-button")

# Inventario
TITLE = (By.CLASS_NAME, "title")
LOGO = (By.CLASS_NAME, "app_logo")
MENU = (By.ID, "react-burger-menu-btn")
FILTER = (By.CLASS_NAME, "product_sort_container")
CART = (By.CLASS_NAME, "shopping_cart_link")
CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
ITEMS = (By.CLASS_NAME, "inventory_item")
ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
ADD_FIRST = (By.CSS_SELECTOR, ".inventory_item:first-child button")

# Carrito
CART_ITEM = (By.CLASS_NAME, "cart_item")
CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
