Feature: Validación de email duplicado en el registro

  Scenario: TC002 - Intentar registro con email duplicado
    Given que el usuario está en la página de registro
    When el usuario intenta registrarse con un email ya registrado
    Then debe aparecer un mensaje de error indicando "Este correo ya está registrado"