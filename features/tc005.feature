Feature: Validación del formulario de registro
  Como usuario, quiero validar el formulario de registro
  para asegurarme de que los errores se manejan correctamente

  Scenario: Intentar registrarse solo con nombre y contraseña
    Given que el usuario está en la página de registro
    When ingresa los datos "Daniel Vargas", "", "12345", "12345"
    Then el botón "Sign Up" debe estar "deshabilitado"

  Scenario: Intentar registrarse solo con email y contraseña
    Given que el usuario está en la página de registro
    When ingresa los datos "", "test@example.com", "12345", "12345"
    Then el botón "Sign Up" debe estar "deshabilitado"
