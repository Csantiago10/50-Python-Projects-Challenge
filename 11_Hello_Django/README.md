# 11_Hello_Django

Proyecto simple para aprender las bases de Django.

## Levantamiento

1.  Crear un entorno virtual

    ```bash
    python -m venv .venv
    ```

2.  Activar el entorno virtual

    -   En Windows
        ```bash
        .venv\Scripts\activate
        ```
    -   En Linux/Mac
        ```bash
        source .venv/bin/activate
        ```

3.  Instalar las dependencias

    ```bash
    pip install -r requirements.txt
    ```

4.  Correr las migraciones

    ```bash
    python manage.py migrate
    ```

5.  Levantar el servidor de desarrollo

    ```bash
    python manage.py runserver
    ```

# Proyecto 12

En este proyecto, hemos añadido una plantilla HTML (`profile.html`) que utiliza el sistema de plantillas de Django. Este sistema es muy similar a Jinja2 y nos permite generar contenido HTML de forma dinámica.

En el archivo `profile.html`, puedes ver cómo utilizamos:
-   Variables como `{{ name }}` y `{{ role }}` para mostrar datos que vienen desde el backend.
-   Estructuras de control como `{% for skill in skills %}` para iterar sobre una lista de habilidades y mostrarlas en la página.

Esto nos permite crear páginas web dinámicas y personalizadas con Django.

# Proyecto 13

Para mejorar la apariencia de nuestro perfil de usuario, hemos introducido el manejo de archivos estáticos en Django.

1.  **Creación de la carpeta `static/core`**: Dentro de nuestra aplicación `core`, creamos la estructura de carpetas `static/core` para almacenar nuestros archivos CSS. Django buscará automáticamente en las carpetas `static` de cada aplicación.

2.  **Estilos para la Tarjeta**: Hemos añadido dos archivos CSS:
    *   `main.css`: Para estilos generales.
    *   `card.css`: Contiene los estilos específicos para la tarjeta de perfil, incluyendo un efecto de volteo en 3D que se activa al pasar el ratón por encima.

3.  **Carga en la Plantilla**: En `profile.html`, cargamos estos estilos utilizando la etiqueta `{% static %}` de Django, asegurando que las rutas a los archivos se generen correctamente.




El app estará corriendo en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
