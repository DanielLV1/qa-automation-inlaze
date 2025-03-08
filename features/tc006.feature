Feature: Validación de la confirmación de contraseña en el formulario de registro

  Como usuario, quiero validar que la confirmación de contraseña coincida con la ingresada
  para asegurarme de que los errores se manejen correctamente.

  Scenario Outline: Validar coincidencia de contraseñas en el registro
    Given que el usuario está en la página de registro
    When ingresa "<Full Name>" en el campo "Full Name"
    And ingresa "<Email>" en el campo "Email"
    And ingresa "<Password>" en el campo "Password"
    And ingresa "<Repeat Password>" en el campo "Confirm Password"
    Then el mensaje "Passwords do not match" debe mostrarse en la página

  Examples:
    | Full Name   | Email             | Password  | Repeat Password |
    | Juan Pérez | test@example.com  | Password1! | Password2!      |
