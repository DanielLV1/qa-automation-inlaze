Feature: Validación del mensaje de error al ingresar credenciales incorrectas

  Scenario: Intentar iniciar sesión con credenciales inválidas
    Given que el usuario está en la página de login
    When ingresa un email incorrecto y una contraseña incorrecta
    And hace clic en "Sign In"
    Then debe visualizar un mensaje de error indicando "Password doesn't match"
