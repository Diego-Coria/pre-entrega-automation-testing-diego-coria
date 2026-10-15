# Pre-entrega automation testing

Tests automaticos de saucedemo.com con Python, Selenium y Pytest.

## Tecnologias

- Python
- Pytest
- Selenium WebDriver
- pytest-html

## Estructura

- tests/ : casos de prueba
- utils/ : funciones auxiliares
- datos/ : usuario y password
- reports/ : reporte html

## Instalacion

```
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

En Windows (PowerShell): `.venv\Scripts\activate`

## Como correr los tests

```
pytest -v --html=reports/reporte.html --self-contained-html
```

## Tests

- Login con standard_user / secret_sauce
- Catalogo (titulo, productos, menu y filtro)
- Agregar un producto al carrito
