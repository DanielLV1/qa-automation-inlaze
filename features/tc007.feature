Feature: Iniciar sesión en la plataforma

  Como usuario registrado,
  quiero iniciar sesión con mis credenciales válidas,
  para poder acceder al sistema.

  Scenario: Iniciar sesión con credenciales correctas
    Given que el usuario está en la página de login
    When ingresa "demotionkronner@gmail.com" en el campo "Email"
    And ingresa "Nicolas321." en el campo "Password"
    And hace clic en "Sign In"
    Then el usuario debe acceder al sistema y ver su nombre en la página principal
