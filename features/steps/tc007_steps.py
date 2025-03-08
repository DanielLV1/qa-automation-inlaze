import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que el usuario está en la página de login')
def step_open_login_page(context):
    if not hasattr(context, "driver"):
        context.driver = webdriver.Chrome()
    
    context.driver.get("https://test-qa.inlaze.com/auth/sign-in")
    context.driver.maximize_window()

@when('hace clic en "Sign In"')
def step_click_sign_in(context):
    try:
        sign_in_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]"))
        )

        WebDriverWait(context.driver, 10).until(
            lambda driver: sign_in_button.is_enabled()
        )

        time.sleep(2)
        context.driver.execute_script("arguments[0].scrollIntoView();", sign_in_button)
        sign_in_button.click()
        time.sleep(3)

    except Exception:
        context.driver.execute_script("arguments[0].click();", sign_in_button)

@then('el usuario debe acceder al sistema y ver su nombre en la página principal')
def step_validate_successful_login(context):
    try:
        WebDriverWait(context.driver, 10).until(
            lambda driver: "/panel" in driver.current_url
        )

        time.sleep(2)

        user_name_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'font-bold')]"))
        )

        actual_text = user_name_element.text.strip()
        assert actual_text == "Daniel Labrador", f"Error: Se esperaba 'Daniel Labrador' pero se mostró '{actual_text}'"

    except Exception as e:
        assert False, f"Error: No se encontró el nombre del usuario en la página principal. Excepción: {e}"
