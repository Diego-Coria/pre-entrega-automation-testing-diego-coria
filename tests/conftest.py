from pathlib import Path

import pytest

from utils.helpers import crear_driver, login

REPORTS = Path(__file__).resolve().parents[1] / "reports"
REPORTS.mkdir(exist_ok=True)


@pytest.fixture
def driver():
    drv = crear_driver()
    yield drv
    drv.quit()


@pytest.fixture
def driver_logueado(driver):
    login(driver)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver") or item.funcargs.get("driver_logueado")
        if drv:
            drv.save_screenshot(str(REPORTS / f"{item.name}.png"))
