from features.steps.common_steps import step_fill_name, step_fill_email, step_fill_password, step_fill_confirm_password, step_validate_button
from behave import when, then
import time

@when('el usuario escribe su nombre completo "{nombre}"')
def step_fill_name_tc003(context, nombre):
    step_fill_name(context, nombre)
    time.sleep(1)  # Pequeña espera para asegurar que el campo de nombre se llene antes de seguir

@when("completa los demás campos con datos válidos")
def step_fill_valid_data(context):
    step_fill_email(context, f"test{int(time.time())}@example.com")  # Genera un email único
    step_fill_password(context, "Password123!")
    step_fill_confirm_password(context, "Password123!")

@then(u'"El botón \'Sign Up\' debe estar deshabilitado" debe ser el comportamiento observado')
def step_validate_button_disabled(context):
    step_validate_button(context, "deshabilitado")

@then(u'"El botón \'Sign Up\' debe estar habilitado" debe ser el comportamiento observado')
def step_validate_button_enabled(context):
    step_validate_button(context, "habilitado")
