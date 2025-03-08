Feature: Validación del cierre de sesión

  Scenario: Validar cierre de sesión correctamente
    Given que el usuario ha iniciado sesión en la plataforma
    When hace clic en el botón con su foto de perfil
    And hace clic en el botón "Logout"
    Then el usuario es redirigido a la página de login
