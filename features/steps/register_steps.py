from features.steps.common_steps import *
from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('el usuario debe ver el mensaje de "Successful registration!"')
def step_validate_registration(context):
    success_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Successful registration!')]"))
    )
    assert success_message is not None, "Error: No se encontró el mensaje de éxito"
    context.driver.quit()