Feature: Validación de contraseña en el registro
  Como usuario de la plataforma
  Quiero que la contraseña tenga validaciones de seguridad
  Para evitar registros con contraseñas débiles

  Scenario Outline: TC004 - Verificar que no se permita una contraseña débil
    Given que el usuario está en la página de registro
    When ingresa una contraseña débil "<password>"
    Then el botón "Sign Up" debe estar "deshabilitado"

    Examples:
      | password  |
      | 12345     |
      | abcdefgh  |
      | PASSWORD  |
      | pass1234  |