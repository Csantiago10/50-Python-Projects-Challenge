# 14_Django_ORM: Perfiles de Usuario

Este proyecto es una aplicación web simple desarrollada con Django que demuestra el uso del Mapeo Objeto-Relacional (ORM) de Django para gestionar y mostrar perfiles de usuario. La aplicación presenta tarjetas de perfil con una animación de volteo al pasar el mouse, mostrando las habilidades de cada usuario.

## Características

-   **Visualización Dinámica de Perfiles:** Los perfiles de usuario se obtienen de la base de datos y se muestran dinámicamente en la página.
-   **Tarjetas de Perfil Interactivas:** Las tarjetas de perfil tienen un efecto de volteo (flip) al pasar el mouse sobre ellas, revelando las habilidades del usuario.
-   **Gestión de Habilidades:** Las habilidades se almacenan como una cadena de texto separada por comas en la base de datos y se procesan en el modelo para mostrarlas como una lista.
-   **Uso del ORM de Django:** Toda la interacción con la base de datos se realiza a través del ORM de Django, lo que facilita la creación, lectura, actualización y eliminación de registros.
-   **Migraciones de Base de Datos:** El esquema de la base de datos se gestiona mediante el sistema de migraciones de Django, lo que permite un control de versiones del esquema de la base de datos.

## Tecnologías Utilizadas

-   **Python:** Lenguaje de programación principal.
-   **Django:** Framework de desarrollo web para la estructura y lógica del backend.
-   **HTML:** Lenguaje de marcado para la estructura de las páginas web.
-   **CSS:** Hojas de estilo para el diseño y la apariencia de la aplicación, incluyendo animaciones.
-   **SQLite:** Motor de base de datos ligero utilizado por defecto en Django para el desarrollo.

## Configuración e Instalación

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1.  **Clona el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd 14_Django_ORM
    ```

2.  **Crea y activa un entorno virtual:**
    - En Windows:
      ```bash
      python -m venv .venv
      .venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```

3.  **Instala las dependencias:**
    ```bash
    pip install Django
    ```

4.  **Aplica las migraciones:**
    ```bash
    python manage.py migrate
    ```
    Este comando creará la base de datos SQLite y las tablas necesarias según los modelos definidos.

5.  **Crea un superusuario (opcional):**
    Para acceder al panel de administración de Django, crea un superusuario:
    ```bash
    python manage.py createsuperuser
    ```
    Luego, sigue las instrucciones para crear tu cuenta de administrador. Puedes usar el panel de administración en `/admin/` para añadir perfiles.

6.  **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

7.  **Accede a la aplicación:**
    Abre tu navegador web y visita `http://127.0.0.1:8000/perfil/` para ver los perfiles de usuario.

## Estructura del Proyecto

El proyecto sigue una estructura estándar de Django:

```
14_Django_ORM/
├── config/           # Contenedor del proyecto Django.
│   ├── settings.py   # Configuración principal del proyecto.
│   └── urls.py       # Definición de las URLs principales.
├── core/             # Aplicación de Django para la lógica principal.
│   ├── migrations/   # Archivos de migración de la base de datos.
│   ├── static/       # Archivos estáticos (CSS, JavaScript, imágenes).
│   │   └── core/
│   │       ├── card.css
│   │       └── main.css
│   ├── templates/    # Plantillas HTML.
│   │   └── core/
│   │       └── profile.html
│   ├── models.py     # Definición de los modelos de la base de datos (ORM).
│   ├── views.py      # Lógica de las vistas que procesan las solicitudes.
│   └── admin.py      # Configuración del panel de administración.
└── manage.py         # Script de utilidad para la gestión del proyecto.
```

## Base de Datos

Este proyecto utiliza **SQLite** como motor de base de datos, que es ideal para desarrollo y aplicaciones pequeñas. El esquema de la base de datos está definido en `core/models.py` a través de la clase `Profile`.

El sistema de **migraciones de Django** se utiliza para versionar y aplicar los cambios en el esquema de la base de datos de manera controlada. Cada vez que se modifica el archivo `models.py`, se pueden generar nuevas migraciones con `python manage.py makemigrations` y aplicarlas con `python manage.py migrate`.
