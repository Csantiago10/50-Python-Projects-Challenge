# Servicio de Autenticación con JWT en Django

Este proyecto es una API RESTful desarrollada con Django y Django REST Framework que implementa un sistema de autenticación seguro basado en JSON Web Tokens (JWT).

## Descripción

El proyecto expone endpoints para la gestión de un modelo simple (`Computer`) y asegura estos endpoints mediante autenticación por JWT. Los usuarios deben obtener un token de acceso para poder interactuar con los datos, garantizando que solo las solicitudes autorizadas sean procesadas.

## Características

-   **Autenticación JWT**: Utiliza `djangorestframework-simplejwt` para la generación y validación de tokens.
-   **Endpoints Seguros**: Todas las rutas de la API que gestionan datos están protegidas y requieren un token de acceso válido.
-   **Operaciones CRUD**: Soporte completo para Crear, Leer, Actualizar y Eliminar (CRUD) sobre el modelo `Computer`.
-   **Obtención y Refresco de Tokens**: Endpoints dedicados para que los usuarios obtengan (`/api/token/`) y refresquen (`/api/token/refresh/`) sus tokens de acceso.

## Tecnologías Utilizadas

-   Python 3
-   Django
-   Django REST Framework
-   Django REST Framework Simple JWT

## Instalación

Sigue estos pasos para configurar el entorno de desarrollo:

1.  **Clonar el repositorio**
    ```bash
    git clone https://github.com/Csantiago10/50-Python-Projects-Challenge.git
    cd 22_Auth_Service_JWT
    ```

2.  **Crear y activar un entorno virtual**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
    ```

3.  **Instalar dependencias**
    Asegúrate de tener el archivo `requirements.txt` en el directorio del proyecto.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar migraciones**
    Esto creará la base de datos SQLite y las tablas necesarias.
    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario**
    Necesitarás un usuario para poder obtener un token de autenticación.
    ```bash
    python manage.py createsuperuser
    ```

6.  **Iniciar el servidor de desarrollo**
    ```bash
    python manage.py runserver
    ```
    La API estará disponible en `http://127.0.0.1:8000/`.

## Uso de la API

Todos los endpoints de datos requieren un token JWT en la cabecera `Authorization` como `Bearer <token>`.

### Autenticación

1.  **Obtener Token de Acceso**

    Realiza una petición `POST` a `/api/token/` con tu nombre de usuario y contraseña para obtener un token de acceso y uno de refresco.

    **Request:**
    ```http
    POST /api/token/ HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json

    {
        "username": "tu_usuario",
        "password": "tu_contraseña"
    }
    ```

    **Response:**
    ```json
    {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```

2.  **Refrescar Token de Acceso**

    Si tu token de acceso expira, puedes obtener uno nuevo enviando tu token de refresco a `/api/token/refresh/`.

    **Request:**
    ```http
    POST /api/token/refresh/ HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json

    {
        "refresh": "tu_token_de_refresco"
    }
    ```

    **Response:**
    ```json
    {
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```

### Endpoints Protegidos

#### Computadoras (`/api/computers/`)

-   `GET`: Lista todas las computadoras.
-   `POST`: Crea una nueva computadora.

    **Ejemplo de `POST`:**
    ```http
    POST /api/computers/ HTTP/1.1
    Host: 127.0.0.1:8000
    Authorization: Bearer <tu_token_de_acceso>
    Content-Type: application/json

    {
        "brand": "Marca Ejemplo",
        "model": "Modelo 2024",
        "price": 1500.00
    }
    ```

#### Detalle de Computadora (`/api/computers/<id>/`)

-   `GET`: Obtiene los detalles de una computadora específica.
-   `PUT`: Actualiza los datos de una computadora.
-   `DELETE`: Elimina una computadora.
