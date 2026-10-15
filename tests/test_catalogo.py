"""Catálogo: título, productos visibles y UI principal."""
from utils.helpers import primer_producto
from utils.locators import FILTER, ITEMS, MENU, TITLE


def test_titulo_inventario(driver_logueado):
    assert driver_logueado.find_element(*TITLE).text == "Products"


def test_productos_visibles(driver_logueado, capsys):
    items = driver_logueado.find_elements(*ITEMS)
    assert len(items) >= 1
    nombre, precio = primer_producto(driver_logueado)
    assert nombre
    assert precio.startswith("$")
    print(f"Primer producto: {nombre} - {precio}")


def test_elementos_ui(driver_logueado):
    assert driver_logueado.find_element(*MENU).is_displayed()
    assert driver_logueado.find_element(*FILTER).is_displayed()
