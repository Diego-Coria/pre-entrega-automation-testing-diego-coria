from utils.helpers import ir_al_carrito, primer_producto
from utils.locators import ADD_FIRST, CART_BADGE, CART_ITEM, CART_ITEM_NAME


def test_agregar_primer_producto_al_carrito(driver_logueado):
    nombre, precio = primer_producto(driver_logueado)
    driver_logueado.find_element(*ADD_FIRST).click()
    badge = driver_logueado.find_element(*CART_BADGE)
    assert badge.text == "1"
    ir_al_carrito(driver_logueado)
    items = driver_logueado.find_elements(*CART_ITEM)
    assert len(items) == 1
    assert driver_logueado.find_element(*CART_ITEM_NAME).text == nombre
