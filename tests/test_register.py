import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://test-qa.inlaze.com/auth/sign-up")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_register_user(setup):
    driver = setup

    # Esperar hasta que la página de registro cargue completamente
    wait = WebDriverWait(driver, 10)

    # Ubicar los elementos del formulario con el nuevo XPath
    name_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='full-name']")))
    email_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='email']")))
    password_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']//input")))
    confirm_password_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='confirm-password']//input")))

    # Ingresar datos de prueba
    name_field.send_keys("Juan Pérez")
    email_field.send_keys(f"juan{int(time.time())}@example.com")  # Email único
    password_field.send_keys("Password1!")
    confirm_password_field.send_keys("Password1!")

    # Verificar si el botón está habilitado antes de hacer clic
    sign_up_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign up')]")))

    # Hacer clic en el botón de registro
    sign_up_button.click()

    # Esperar a que aparezca un mensaje de éxito (ajusta este XPath según la página)
    success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ml-3 text-sm font-normal') and contains(text(), 'Successful registration!')]")))
                                                                    
    assert success_message is not None, "Error: No se encontró el mensaje de éxito"

