from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@then('el botón "Sign In" debe permanecer deshabilitado')
def step_validate_sign_in_button_disabled(context):
    time.sleep(2)  # Espera 2 segundos antes de la verificación

    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
    )
    is_disabled = not sign_in_button.is_enabled()
    assert is_disabled, "Error: El botón 'Sign In' debería estar deshabilitado, pero está habilitado."
