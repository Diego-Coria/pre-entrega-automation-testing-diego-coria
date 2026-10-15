from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import login
from utils.locators import LOGO, TITLE


def test_login_exitoso(driver):
    login(driver)
    assert "/inventory.html" in driver.current_url
    titulo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TITLE))
    logo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGO))
    assert titulo.text == "Products"
    assert "Swag Labs" in logo.text
