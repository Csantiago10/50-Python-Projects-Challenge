# Blog API

API RESTful construida con Django y Django REST Framework para gestionar las publicaciones de un blog.

## ✨ Características

- Creación, lectura, actualización y eliminación (CRUD) de publicaciones del blog.
- Serialización de datos para convertir objetos complejos en tipos de datos nativos de Python.
- Endpoints de API para interactuar con los datos del blog.

## 🚀 Tecnologías Utilizadas

- **Backend:**
  - Python
  - Django
  - Django REST Framework

## 📋 Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (sistema de control de versiones)

## 🔧 Instalación y Configuración

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/Csantiago10/50-Python-Projects-Challenge.git
    cd 21_Blog_API
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # Para Windows
    python -m venv .venv
    .venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Si no existe un archivo `requirements.txt`, necesitarás instalar Django y Django REST Framework manualmente: `pip install django djangorestframework`)*

4.  **Aplica las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    La API estará disponible en `http://127.0.0.1:8000/`.

## 🎮 Uso

Una vez que el servidor está en funcionamiento, puedes usar un cliente de API como [Postman](https://www.postman.com/) o `curl` para interactuar con los siguientes endpoints.

### Endpoints de la API

-   `GET /api/posts/`: Obtiene una lista de todas las publicaciones.
-   `POST /api/posts/`: Crea una nueva publicación.
-   `GET /api/posts/<id>/`: Obtiene los detalles de una publicación específica.
-   `PUT /api/posts/<id>/`: Actualiza una publicación existente.
-   `DELETE /api/posts/<id>/`: Elimina una publicación.

*(Nota: Las rutas exactas de los endpoints pueden variar. Consulta el archivo `core/urls.py` o `blog_backend/urls.py` para confirmar las URL correctas).*
