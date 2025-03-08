# Automatización de Pruebas con Selenium y Behave para la plataforma Inlaze

Este proyecto contiene pruebas automatizadas para validar el formulario de registro e inicio de sesión en la plataforma **Inlaze**, utilizando **Python**, **Selenium** y **Behave**.

---

## Casos de Prueba incluidos

### Registro de Usuarios
- Registro con datos válidos.
-  Validación del campo nombre con mínimo 2 palabras.
- Validación del formato estándar y unicidad del email.
- Validación de requisitos de contraseña (mínimo 8 caracteres, letras, números y caracteres especiales).
- Validación de contraseñas coincidentes.
- Validación de campos obligatorios antes del registro.
- Mensaje de error al intentar registrar un email ya existente.

### Casos para Inicio de Sesión
- Validación del botón deshabilitado al faltar campos.
- Validación del mensaje de error para credenciales incorrectas.
- Validación de sesión correcta.
- Validación de cierre de sesión exitoso.

---

## Requisitos del sistema

- **Python 3.9+**

- ChromeDriver (gestionado automáticamente por `webdriver-manager`)

---

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/DanielLV1/qa-automation-inlaze.git
```

### 2. Crear y activar entorno virtual (opcional pero recomendado)

**Windows:**
```powershell
python -m venv env
.\env\Scripts\activate
```


### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar pruebas automatizadas

```bash
behave
```

o individualmente por archivo:

```bash
behave features/nombre_archivo.feature
```

---

##  Requisitos técnicos
- Navegador Google Chrome actualizado.
- Python 3.9 o superior.
- Librerías indicadas en `requirements.txt`.

---

##  Estructura del Proyecto
```bash
📂 features
 ├── steps
 │   ├── common_steps.py
 │   └── tc001_steps.py, tc002_steps.py, ...
 ├── tc001.feature
 ├── ...
 └── tc010.feature

requirements.txt
README.md
.gitignore
```


## Notas adicionales
- Asegúrate de actualizar los controladores web si experimentas problemas de compatibilidad.
- Las pruebas asumen un entorno de desarrollo local con acceso a internet para acceder al sitio web de pruebas.

---

## Enlaces útiles
- [Documentación de Selenium](https://selenium-python.readthedocs.io/)
- [Behave Documentation](https://behave.readthedocs.io/)

