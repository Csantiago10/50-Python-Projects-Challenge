# 14_Django_ORM: Perfiles de Usuario

Este proyecto es una aplicación web simple desarrollada con Django que demuestra el uso del Mapeo Objeto-Relacional (ORM) de Django para gestionar y mostrar perfiles de usuario. La aplicación presenta tarjetas de perfil con una animación de volteo al pasar el mouse, mostrando las habilidades de cada usuario.

## Características

-   **Visualización Dinámica de Perfiles:** Los perfiles de usuario se obtienen de la base de datos y se muestran dinámicamente en la página.
-   **Tarjetas de Perfil Interactivas:** Las tarjetas de perfil tienen un efecto de volteo (flip) al pasar el mouse sobre ellas, revelando las habilidades del usuario.
-   **Gestión de Habilidades:** Las habilidades se almacenan como una cadena de texto separada por comas en la base de datos y se procesan en el modelo para mostrarlas como una lista.
-   **Uso del ORM de Django:** Toda la interacción con la base de datos se realiza a través del ORM de Django, lo que facilita la creación, lectura, actualización y eliminación de registros.
-   **Migraciones de Base de Datos:** El esquema de la base de datos se gestiona mediante el sistema de migraciones de Django, lo que permite un control de versiones del esquema de la base de datos.

## Proyecto 14: Creación de la Base de Datos y Migraciones

En el proyecto 14, se estableció la base de datos inicial utilizando **SQLite**. Se definió el modelo `Profile` en `core/models.py` para representar la tabla de perfiles de usuario en la base de datos.

Los siguientes pasos se llevaron a cabo:

1.  **Definición del Modelo:** Se creó el modelo `Profile` con campos como `name`, `description`, `skills`, etc.
2.  **Generación de Migraciones:** Se ejecutó `python manage.py makemigrations` para crear el archivo de migración inicial (`0001_initial.py`), que traduce el modelo de Python a un esquema de base de datos.
3.  **Aplicación de Migraciones:** Con `python manage.py migrate`, se aplicó la migración a la base de datos SQLite, creando así la tabla `core_profile`.

## Proyecto 15: Superusuario y Panel de Administración

En el proyecto 15, se extendió la funcionalidad para interactuar con la base de datos a través del panel de administración de Django.

Las principales tareas realizadas fueron:

1.  **Creación de un Superusuario:** Se utilizó el comando `python manage.py createsuperuser` para crear un administrador con acceso al panel de Django.
2.  **Registro de Modelos en el Admin:** El modelo `Profile` se registró en `core/admin.py` para que fuera visible y gestionable desde el panel de administración.
3.  **Personalización del Panel de Administración:**
    -   **Filtros:** Se añadió un `list_filter` en `core/admin.py` para permitir filtrar los perfiles por campos como `created` o `updated`.
    -   **Barra de Búsqueda:** Se implementó una `search_fields` para facilitar la búsqueda de perfiles por nombre o descripción.
    -   **Visualización de Campos:** Se configuró `list_display` para personalizar las columnas que se muestran en la lista de perfiles.
4.  **Adición de Registros:** Se añadió un nuevo perfil a la base de datos directamente desde el panel de administración, demostrando la facilidad de gestión de datos que ofrece Django.

## Proyecto 16: Formulario de Creación de Perfiles

En el proyecto 16, se implementó la funcionalidad para que los usuarios puedan crear nuevos perfiles directamente desde la interfaz web.

Los cambios clave fueron:

1.  **Botón de Crear Perfil:** En la vista principal (`profile.html`), se añadió un botón con el texto "Crear Perfil".
2.  **Ruta y Vista para el Formulario:** Se creó una nueva ruta y su vista correspondiente que renderiza un formulario de creación de perfiles. El botón mencionado anteriormente redirige a esta página.
3.  **Procesamiento del Formulario:** La vista del formulario maneja tanto las solicitudes `GET` (para mostrar el formulario vacío) como las `POST` (para procesar los datos enviados).
4.  **Guardado y Redirección:** Al enviar el formulario con datos válidos, la vista guarda la información en la base de datos, creando un nuevo registro en la tabla `Profile`. Inmediatamente después, redirige al usuario de vuelta a la página principal de perfiles (`profile.html`), donde ahora se puede ver el nuevo perfil añadido.

## Proyecto 17: Funcionalidad de Edición y Eliminación de Perfiles

En el proyecto 17, se mejoró la interacción del usuario con los perfiles al añadir la capacidad de **editar** y **eliminar** perfiles directamente desde la vista principal.

Los cambios implementados fueron:

1.  **Botones de Acción en Cada Tarjeta:** Se agregaron los botones "Editar" y "Eliminar" en la parte inferior de cada tarjeta de perfil.
2.  **Rutas y Vistas para Edición:**
    -   Se creó una nueva ruta `(profile_update)` que captura el ID del perfil a editar.
    -   La vista correspondiente maneja la lógica para obtener los datos del perfil existente, presentarlos en un formulario y procesar los cambios enviados mediante una solicitud `POST`.
3.  **Rutas y Vistas para Eliminación:**
    -   Se definió una ruta `(profile_delete)` que también captura el ID del perfil.
    -   La vista de eliminación presenta una página de confirmación para asegurar que el usuario realmente desea eliminar el perfil.
    -   Al confirmar, el perfil se elimina de la base de datos y se redirige al usuario a la página principal.
4.  **Ajustes de Estilos:** Se realizaron ajustes en los archivos CSS (`card.css` y `buttons.css`) para integrar los nuevos botones de manera estética y funcional dentro de cada tarjeta, asegurando que el diseño se mantenga coherente y adaptable.

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
