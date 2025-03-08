from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('el mensaje "Passwords do not match" debe mostrarse en la página')
def step_validate_error_message(context):
    try:
        error_label = WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'label-text-alt text-error')]"))
        )
        assert error_label.text.strip() == "Passwords do not match", f"Error: Se esperaba 'Passwords do not match' pero se mostró '{error_label.text.strip()}'"

    except Exception as e:
        assert False, f"Error: No se encontró el mensaje 'Passwords do not match'. Excepción: {e}"
