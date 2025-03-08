from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given("que el usuario ha iniciado sesión en la plataforma")
def step_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://test-qa.inlaze.com/auth/sign-in")
    context.driver.maximize_window()

    email_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='email']"))
    )
    password_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))
    )

    email_field.send_keys("demotionkronner@gmail.com")
    password_field.send_keys("Nicolas321.")

    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign in')]"))
    )
    sign_in_button.click()

    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/panel")
    )

@when("hace clic en el botón con su foto de perfil")
def step_click_profile_photo(context):
    profile_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(@class,'btn-circle avatar')]"))
    )
    profile_button.click()
    time.sleep(2)

@when('hace clic en el botón "Logout"')
def step_click_logout(context):
    logout_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ul[contains(@class, 'dropdown-content')]//a[contains(text(),'Logout')]"))
    )
    logout_button.click()
    time.sleep(2)

@then("el usuario es redirigido a la página de login")
def step_validate_redirect_login(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/auth/sign-in")
    )
    assert "/auth/sign-in" in context.driver.current_url, "El usuario no fue redirigido correctamente a la página de login"
