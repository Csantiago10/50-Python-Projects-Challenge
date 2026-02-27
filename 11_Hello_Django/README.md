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

El app estará corriendo en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
