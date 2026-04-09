# 🚀 50 Projects Challenge: Python Core to Pro
**Por: Santiago | Ingeniero Informático**

Este repositorio contiene mi progreso en el reto de los 50 proyectos de Python, diseñados para fortalecer la lógica de programación, el desarrollo backend y la arquitectura de software.

---

## 📊 Estado del Reto
![Progress](https://geps.dev/progress/46)
*(46% completado - 23 de 50)*

## 📂 Estructura de cada Proyecto
Cada carpeta dentro de este repositorio sigue el estándar de **Src Layout**:
* `src/`: Lógica principal del programa.
* `test/`: Pruebas unitarias con `unittest`.
* `docs/`: Especificaciones técnicas y pseudocódigo.

---

## 🛠️ Fase 1: Lógica Pura & Python Core (1-10)
El objetivo de esta fase es dominar algoritmos sin librerías externas.

| ID | Proyecto | Conceptos Clave | Estado | Link |
| :--- | :--- | :--- | :--- | :--- |
| 01 | **Number Separator** | `input`, `split`, `sort`, `try/except` | ✅ Terminado | [Ver Proyecto](./number_separator) |
| 02 | **Conversor Universal** | Funciones, `if/elif/else`, `f-strings` | ✅ Terminado | [Ver Proyecto](./02_conversor_universal) |
| 03 | **Password Generator** | Funciones `random`, `string constants`, `shuffle` | ✅ Terminado | [Ver Proyecto](./03_Password_Generator) |
| 04 | **Word Counter** | Funciones `string`, `lower`, `maketrans`, `translate`, `list`, `dict`, `sort`, `reverse`  | ✅ Terminado | [Ver Proyecto](./04_Word_Counter) |
| 05 | **Rock, Paper, Scissors** | `while True`, lógica booleana | ✅ Terminado | [Ver Proyecto](./05_Rock_Paper_Scissors) |
| 06 | **Hangman** | `set`, `list` (mutable), `input`, `unittest` | ✅ Terminado | [Ver Proyecto](./06_Hangman) |
| 07 | **César Cipher** | Código ASCII (`ord`, `chr`), módulos | ✅ Terminado | [Ver Proyecto](./07_Caesar_Cipher) |
| 08 | **To-Do CLI** | File I/O (`.txt`), Persistence | ✅ Terminado | [Ver Proyecto](./08_todoList_CLI) |
| 09 | **Guess the Number** | Búsqueda Binaria (Binary Search) | ✅ Terminado | [Ver Proyecto](./09_Guess_Number_AI) |
| 10 | **ATM Simulator** | Hashing (SHA-256), Persistencia de Datos (JSON), y Generación de Archivos (.txt) | ✅ Terminado | [Ver Proyecto](./10_ATM_Simulator) |

---

## 🚀 FASE 2: EL BACKEND JUNIOR (Django & Web)
En esta fase, dejamos la consola y construimos aplicaciones web completas usando el patrón MVT (Model-View-Template) y bases de datos relacionales.

| ID | Proyecto | Conceptos Clave | Django | Estado | Link |
| :-- | :--- | :--- | :--- | :--- | :--- |
| 11 | **Hello Django (The Monolith)** | `Configuración de entorno`, `settings.py`, `Rutas (urls)`, `Vistas (views)`, `JSON Response`, `Templates,Django`, `HTTP` | Django HTTP | ✅ Terminado | [Ver Proyecto](./11_Hello_Django) |
| 12 | **Motor de Plantillas (MVT)** | `Renderizado de HTML`, `Jinja Syntax ({% %})`, `Context Data, Herencia de Plantillas` | Django, HTML | ✅ Terminado | [Ver Proyecto](./11_Hello_Django) |
| 13 | **Archivos Estáticos & CSS** | `Manejo de static files`, `carga de CSS/JS/Imágenes`, `Diseño básico` | Django, CSS | ✅ Terminado | [Ver Proyecto](./11_Hello_Django) |
| 14 | **Modelos y Bases de Datos (ORM)** | `models.py`, `Migraciones (makemigrations)`, `SQLite`, `Manipulación de datos sin SQL.` | Django ORM, SQL | ✅ Terminado | [Ver Proyecto](./14_Django_ORM) |
| 15 | **El Panel de Administración** | `admin.py`, `Superusuario`, `Gestión de datos visual`, `Personalización del Admin`. | Django Admin | ✅ Terminado | [Ver Proyecto](./14_Django_ORM) |
| 16 | **Formularios y Peticiones POST** | `forms.py`, `Validación de datos`, `CSRF Token`, `Seguridad en inputs`, `HTTP Verbs.` | Django Forms | ✅ Terminado | [Ver Proyecto](./14_Django_ORM) |
| 17 | **CRUD Web I: Read & Create** | `Creación de una "App de Notas".` `Listar datos de la DB`  `crear nuevos registros desde la web` | Django CRUD | ✅ Terminado | [Ver Proyecto](./14_Django_ORM) |
| 18 | **CRUD Web II: Update & Delete** | `Rutas dinámicas (<int:id>)`, `get_object_or_404`, `Edición y Borrado seguro` | Django CRUD | ✅ Terminado | [Ver Proyecto](./14_Django_ORM) |
| 19 | **Sistema de Autenticación** | `Login`, `Logout`, `Registro de Usuarios`, `Decoradores (@login_required)`, `Sesiones`| Django Auth | ✅ Terminado | [Ver Proyecto](./14_Django_ORM) |
| 20 | **Deploy a Producción (La Nube)** | `Gunicorn (Servidor WSGI)`, `WhiteNoise (archivos estáticos)`, `Variables de entorno`, `DEBUG=False` | Cloud, CI/CD | ✅ Terminado | [Ver Proyecto](./14_Django_ORM) |


## 🚀 FASE 3: EL ARQUITECTO API (Django REST Framework Mastery)
En esta fase  tu herramienta principal será Django REST Framework (DRF). Vas a construir los "motores invisibles" que alimentan aplicaciones móviles y webs. Y sí, cada proyecto será una aplicación completa y funcional (Un MVP real).

| ID | Proyecto | Conceptos Clave | Estado | Link |
| :--- | :--- | :--- | :--- | :--- |
| 21 | **Headless Blog API** | `Intro a DRF`, `Serializers`, `APIViews`, `Endpoints CRUD en formato JSON` | ✅ Terminado | [Ver Proyecto](./21_Blog_API) |
| 22 | **Auth Service (JWT)** | `JSON Web Tokens (SimpleJWT)`, `Login/Register API`, `Permisos (IsAuthenticated)` | ✅ Terminado | [Ver Proyecto](./22_Auth_Service_JWT). |
| 23 | **E-commerce Inventory API** |	`Bases de datos relacionales (One-to-Many, Many-to-Many)`, `Filtros y Búsquedas complejas` |	✅ Terminado | [Ver Proyecto](./23_Ecommerce_API) |
| 24 | **News Aggregator API** |	`Web Scraping (BeautifulSoup)`, `integraciones externas`, `guardar datos extraídos en DB` |	⏳ Pendiente | ... |
| 25 | **Instagram-lite Backend** |	`Manejo de subida de archivos (Multipart/form-data)`, `procesamiento de imágenes (Pillow)` |	⏳ Pendiente |... |
| 26 | **Weather & Crypto Proxy API** |	`Consumo de APIs externas con requests`, `manejo de Caché para no saturar límites` |	⏳ Pendiente | ... |
| 27 | **Booking System API (Citas)** |	`Lógica de Fechas y Horas (datetime)`, `validación de superposición de turnos` |	⏳ Pendiente | ... |
| 28 | **Twitter Clone Backend** |	`Lógica de Seguidores (Followers/Following)`, `Feeds personalizados`, `permisos a nivel de objeto` |	⏳ Pendiente | ... |
| 29 | **Stripe Webhooks Simulator** |	`Recibir peticiones de terceros (Webhooks)`, `actualizar estados de pago de forma segura` |	⏳ Pendiente | ... |
| 30 | **URL Shortener Micro-SaaS** |	`Proyecto Full-Stack API` `Redirecciones HTTP`, `analítica de clics`, `Deploy en PostgreSQL`	|⏳ Pendiente | ... |


---

## ⚙️ Cómo ejecutar los proyectos

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Csantiago10/50-Python-Projects-Challenge.git