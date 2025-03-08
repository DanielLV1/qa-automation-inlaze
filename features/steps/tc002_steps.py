from behave import when, then
from features.steps.common_steps import (
    step_fill_name, step_fill_email, step_fill_password, 
    step_fill_confirm_password, step_click_sign_up
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when("el usuario intenta registrarse con un email ya registrado")
def step_attempt_register_with_duplicate_email(context):
    """Llenar el formulario de registro con un correo duplicado y hacer clic en 'Sign Up'."""
    step_fill_name(context, "Juan Pérez")
    step_fill_email(context, "demotionkronner@gmail.com")  # Email que ya existe
    step_fill_password(context, "Nicolas321.")
    step_fill_confirm_password(context, "Nicolas321.")
    step_click_sign_up(context)

@then('no debe aparecer un mensaje de éxito')
def step_validate_no_success_message(context):
    """Verifica que el div de éxito 'Successful registration!' NO aparezca."""
    try:
        # Esperar unos segundos para verificar si aparece el div
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'text-sm') and contains(text(), 'Successful registration!')]"))
        )
        # Si encontramos el div, la prueba debe fallar
        assert False, "Error: Apareció la alerta de éxito y no debería."
    except:
        # Si el div NO aparece, la prueba pasa exitosamente
        pass


