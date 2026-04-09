# Ecommerce API con Django REST Framework

Este proyecto implementa una API RESTful para un sistema de E-commerce básico, utilizando Django y Django REST Framework (DRF). La API gestiona dos modelos principales: `Category` y `Product`, estableciendo una relación jerárquica entre ellos.

## Características Principales

- **Django REST Framework:** Construido sobre DRF, aprovechando sus robustas funcionalidades para el desarrollo rápido de APIs.
- **Modelo de Datos Relacional:**
    - **Category:** Modelo principal que define las categorías de los productos.
    - **Product:** Modelo que hereda de `Category`, representando los productos individuales, cada uno asociado a una categoría específica.
- **CRUD Completo y Eficiente:**
    - Se utiliza `ModelViewSet` de DRF para las vistas (`views`).
    - Esto proporciona automáticamente un conjunto completo de operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para los modelos `Category` y `Product` sin necesidad de implementar cada método manualmente.
- **Serialización de Datos:** Se emplean `Serializers` para convertir los modelos de Django (`querysets` y `model instances`) en tipos de datos nativos de Python, que luego pueden ser fácilmente renderizados en JSON para las respuestas de la API.

## Estructura del Proyecto

El proyecto sigue una estructura estándar de Django, con una aplicación principal (`ecommerce_products`) que gestiona la configuración y el enrutamiento a nivel de proyecto, y una aplicación dedicada (`products`) que contiene la lógica de negocio de la API.

```
.
├── ecommerce_products/   # App de configuración del proyecto
└── products/           # App para la lógica del E-commerce
    ├── models.py       # Define los modelos Category y Product
    ├── serializers.py  # Define los serializadores para los modelos
    ├── views.py        # Implementa los ViewSets para la API
    └── urls.py         # Define las rutas de la API para esta app
```

## Vistas con ModelViewSet

El uso de `ModelViewSet` simplifica enormemente la creación de las vistas. Un único `ViewSet` puede reemplazar la necesidad de escribir múltiples vistas para las operaciones estándar de un modelo. Por ejemplo, para el modelo `Product`, el `ProductViewSet` gestiona:

- **Listar todos los productos:** `GET /api/products/`
- **Crear un nuevo producto:** `POST /api/products/`
- **Obtener un producto específico:** `GET /api/products/{id}/`
- **Actualizar un producto:** `PUT /api/products/{id}/`
- **Actualizar parcialmente un producto:** `PATCH /api/products/{id}/`
- **Eliminar un producto:** `DELETE /api/products/{id}/`

Esta implementación asegura un desarrollo rápido, limpio y mantenible, siguiendo las mejores prácticas de DRF.
