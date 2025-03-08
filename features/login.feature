Feature: Registro de usuario en la plataforma

  Scenario: Registro exitoso con datos válidos
    Given que el usuario está en la página de registro
    When ingresa un nombre válido
    And ingresa un email válido y único
    And ingresa una contraseña válida
    And confirma la contraseña
    And hace clic en "Sign Up"
    Then el usuario debe ver el mensaje de "Successful registration!"
