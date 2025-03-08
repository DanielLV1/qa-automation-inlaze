from behave import when
from features.steps.common_steps import step_fill_name, step_fill_email, step_fill_password, step_validate_button

@when('ingresa los datos "Daniel Vargas", "", "12345", "12345"')
def step_fill_name_and_password(context):
    step_fill_name(context, "Daniel Vargas")
    step_fill_password(context, "12345")
    step_validate_button(context, "deshabilitado")

@when('ingresa los datos "", "test@example.com", "12345", "12345"')
def step_fill_email_and_password(context):
    step_fill_email(context, "test@example.com")
    step_fill_password(context, "12345")
    step_validate_button(context, "deshabilitado")
