from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given("que el usuario está en la página de registro")
def step_open_register_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://test-qa.inlaze.com/auth/sign-up")
    context.driver.maximize_window()

@when('ingresa "{nombre}" en el campo "Full Name"')
def step_fill_name(context, nombre):
    name_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='full-name']"))
    )
    name_field.clear()
    name_field.send_keys(nombre)
    time.sleep(1)

@when('ingresa "{email}" en el campo "Email"')
def step_fill_email(context, email):
    email_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='email']"))
    )
    email_field.clear()
    if email.strip():
        email_field.send_keys(email)

@when('ingresa "{password}" en el campo "Password"')
def step_fill_password(context, password):
    password_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='password']//input"))
    )
    password_field.clear()
    if password.strip():
        password_field.send_keys(password)
    else:
        print("DEBUG: Se dejó vacío el campo Password.")

    # Esperar hasta que el campo sea visible y esté habilitado
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='password']"))
    )

    # Asegurar que no haya otro elemento superpuesto
    context.driver.execute_script("arguments[0].scrollIntoView();", password_field)

    # Intentar limpiar el campo de forma segura
    try:
        password_field.clear()
    except Exception:
        context.driver.execute_script("arguments[0].value = '';", password_field)

    # Intentar escribir la contraseña
    if password.strip():
        try:
            password_field.send_keys(password)
        except Exception:
            context.driver.execute_script("arguments[0].value = arguments[1];", password_field, password)
    else:
        print("DEBUG: Se dejó vacío el campo Password.")
        
@when('ingresa "{password}" en el campo "Confirm Password"')
def step_fill_confirm_password(context, password):
    confirm_password_field = context.driver.find_element(By.XPATH, "//*[@id='confirm-password']//input")
    confirm_password_field.clear()
    if password:
        confirm_password_field.send_keys(password)

@when('hace clic en "Sign Up"')
def step_click_sign_up(context):
    try:
        sign_up_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign up')]"))
        )
        WebDriverWait(context.driver, 10).until(lambda driver: sign_up_button.is_enabled())
        context.driver.execute_script("arguments[0].scrollIntoView();", sign_up_button)
        sign_up_button.click()
    except Exception as e:
        print(f"Error al hacer clic en Sign Up: {e}")
        context.driver.save_screenshot("error_sign_up.png")

@then('el botón "Sign Up" debe estar "{estado_boton}"')
def step_validate_button(context, estado_boton):
    sign_up_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign up')]"))
    )
    time.sleep(2)
    is_disabled = sign_up_button.get_attribute("disabled") is not None

    print(f"DEBUG: Estado actual del botón -> {'Deshabilitado' if is_disabled else 'Habilitado'}")
    if estado_boton == "deshabilitado":
        assert is_disabled, "Error: El botón debería estar deshabilitado, pero está habilitado."
    else:
        assert not is_disabled, "Error: El botón debería estar habilitado, pero está deshabilitado."
