import json
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.locators import CART, ITEM_NAME, ITEM_PRICE, ITEMS, LOGIN_BTN, PASS, USER

ROOT = Path(__file__).resolve().parents[1]
TIMEOUT = 10


def cargar_datos():
    with open(ROOT / "datos" / "credenciales.json", encoding="utf-8") as f:
        return json.load(f)


def crear_driver():
    opts = Options()
    opts.add_argument("--start-maximized")
    return webdriver.Chrome(options=opts)


def esperar_visible(driver, locator, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def esperar_clickable(driver, locator, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def login(driver, usuario=None, password=None):
    datos = cargar_datos()
    driver.get(datos["url"])
    esperar_visible(driver, USER).send_keys(usuario or datos["usuario"])
    esperar_visible(driver, PASS).send_keys(password or datos["password"])
    esperar_clickable(driver, LOGIN_BTN).click()
    WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/inventory.html"))


def primer_producto(driver):
    esperar_visible(driver, ITEMS)
    nombre = driver.find_element(*ITEM_NAME).text
    precio = driver.find_element(*ITEM_PRICE).text
    return nombre, precio


def ir_al_carrito(driver):
    esperar_clickable(driver, CART).click()
    WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/cart.html"))
