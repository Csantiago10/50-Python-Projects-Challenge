# 🔐 Proyecto 03: Generador de Contraseñas Seguras

> **Estado:** Completado ✅
> **Autor:** Ingeniero Santiago Noreña
> **Stack:** Python 3.12, Unittest, Git

## 📋 Descripción
Este proyecto es una herramienta de automatización enfocada en la seguridad informática. Su función principal es generar cadenas de texto aleatorias (contraseñas) con alta entropía, permitiendo al usuario personalizar la longitud y la complejidad (inclusión de mayúsculas, números y símbolos).

El objetivo es solucionar el problema de las contraseñas débiles o repetidas mediante un algoritmo de selección pseudoaleatoria robusto.

## 🚀 Características Técnicas
Se implementaron prácticas de desarrollo limpio y uso eficiente de la librería estándar de Python:

* **Manejo de Librerías Estándar:** Uso intensivo de los módulos `random` y `string` para la generación de caracteres.
* **Validación de Entradas:** Control de excepciones para asegurar que la longitud solicitada sea un número entero válido y positivo.
* **Arquitectura Modular:** Separación de la lógica de generación (`generator.py`) de la interfaz de consola (`main.py`).
* **Lógica de Selección:** Algoritmos para garantizar que la contraseña resultante cumpla con los criterios seleccionados por el usuario.
* **QA Automatizado:** Pruebas unitarias para verificar la longitud y composición de las contraseñas generadas.

## 📂 Estructura del Proyecto

```text
password_generator/
├── docs/
│   └── especificaciones.md       # Reglas de negocio y requerimientos
├── src/
│   ├── main.py                   # Orquestador (Interacción con el usuario)
│   └── generator.py              # Algoritmo de generación de contraseñas
├── tests/
│   └── test_generator.py         # Pruebas de longitud y contenido (QA)
├── .gitignore
└── README.md                     # Documentación técnica