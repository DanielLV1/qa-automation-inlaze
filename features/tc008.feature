Feature: Validación del formulario de login

  Como usuario, quiero que el formulario de login no se envíe si hay campos vacíos
  para evitar errores en la autenticación.

  Scenario: Intentar iniciar sesión solo con email
    Given que el usuario está en la página de login
    When ingresa "test@example.com" en el campo "Email"
    Then el botón "Sign In" debe permanecer deshabilitado

  Scenario: Intentar iniciar sesión solo con contraseña
    Given que el usuario está en la página de login
    When ingresa "Password1!" en el campo "Password"
    Then el botón "Sign In" debe permanecer deshabilitado
