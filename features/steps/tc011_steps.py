from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@when("ingresa un email incorrecto y una contraseña incorrecta")
def step_fill_invalid_credentials(context):
    """Ingresa credenciales incorrectas en el formulario de login."""
    email_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='email']"))
    )
    password_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='password']//input"))
    )

    email_field.clear()
    email_field.send_keys("gdanielfeslipe@gmail.com")

    password_field.clear()
    password_field.send_keys("Incorrecta123")

@then('debe visualizar un mensaje de error indicando "{mensaje_error}"')
def step_validate_error_message(context, mensaje_error):
    try:
        print("Esperando mensaje de error...")
        error_message_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(@class, "flex") and contains(., "{mensaje_error}")]'))
        )
        assert error_message_element.is_displayed(), f"El mensaje '{mensaje_error}' no está visible."
    except Exception as e:
        context.driver.save_screenshot("error_message_not_found.png")
        raise AssertionError(f"Error: No se encontró el mensaje '{mensaje_error}'. Excepción: {str(e)}")