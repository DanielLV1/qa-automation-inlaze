from features.steps.common_steps import step_fill_name, step_fill_email, step_fill_password, step_fill_confirm_password
from behave import when
import time

@when('ingresa una contraseña débil "{password}"')
def step_fill_weak_password(context, password):
    step_fill_name(context, "Daniel Vargas")  # Usamos un nombre real
    step_fill_email(context, f"test{int(time.time())}@example.com")  # Generamos un correo único
    step_fill_password(context, password)  # Usamos la contraseña débil del test
    step_fill_confirm_password(context, password)  # Confirmamos con la misma contraseña
