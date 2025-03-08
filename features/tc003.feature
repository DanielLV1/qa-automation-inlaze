Feature: Registro de Usuario
  Como usuario
  Quiero registrarme en la aplicación
  Para poder acceder a sus funcionalidades

  Scenario Outline: Validar que el nombre tenga al menos dos palabras
    Given que el usuario está en la página de registro
    When el usuario escribe su nombre completo "<nombre>"
    And completa los demás campos con datos válidos
    Then "<estado del botón>" debe ser el comportamiento observado

  Examples:
    | nombre           | estado del botón                              |
    | Juan            | El botón 'Sign Up' debe estar deshabilitado   |
    | Juan Pérez      | El botón 'Sign Up' debe estar habilitado      |
    | Juan Pérez López | El botón 'Sign Up' debe estar habilitado      |
