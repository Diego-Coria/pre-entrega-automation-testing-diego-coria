from utils.helpers import primer_producto
from utils.locators import FILTER, ITEMS, MENU, TITLE


def test_titulo_inventario(driver_logueado):
    assert driver_logueado.find_element(*TITLE).text == "Products"


def test_productos_visibles(driver_logueado):
    items = driver_logueado.find_elements(*ITEMS)
    assert len(items) >= 1
    nombre, precio = primer_producto(driver_logueado)
    assert nombre != ""
    assert "$" in precio
    print("Primer producto:", nombre, precio)


def test_elementos_ui(driver_logueado):
    assert driver_logueado.find_element(*MENU).is_displayed()
    assert driver_logueado.find_element(*FILTER).is_displayed()
