# Pre-entrega Automatización QA — Sauce Demo

Automatización de flujos básicos en [saucedemo.com](https://www.saucedemo.com) con Selenium WebDriver y Pytest (login, catálogo y carrito).

## Tecnologías

- Python 3
- Pytest
- Selenium WebDriver
- pytest-html (reporte)

## Estructura

```
tests/     casos de prueba
utils/     driver, esperas y locators
datos/     credenciales JSON
reports/   HTML y capturas ante fallo
```

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Chrome instalado (Selenium Manager descarga el driver).

## Ejecutar pruebas

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

También: `pytest tests/ -v`

## Casos

1. Login `standard_user` / `secret_sauce` → `/inventory.html`, Products y Swag Labs.
2. Título, al menos un producto (nombre/precio), menú y filtros.
3. Agregar primer producto, badge = 1, ítem en el carrito.

Cada test usa su propio navegador (independientes). Si un test falla se guarda `reports/<nombre>.png`.
