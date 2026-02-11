# 🔄 Proyecto: Conversor Universal de Unidades

> **Estado:** Completado ✅
> **Autor:** Ingeniero Santiago Noreña
> **Stack:** Python 3.12, Unittest, Git

## 📋 Descripción
Este aplicativo de línea de comandos (CLI) es una herramienta matemática diseñada para realizar conversiones precisas entre diferentes sistemas de medidas (Métrico e Imperial). El sistema permite transformar valores en categorías fundamentales como **Longitud, Peso, Temperatura**, entre otras.

El proyecto destaca por su arquitectura modular y el uso de estructuras de datos eficientes para gestionar múltiples factores de conversión sin saturar el código con condicionales excesivos.

## 🚀 Características Técnicas
El desarrollo se enfocó en la escalabilidad y la precisión aritmética:

* **Arquitectura Modular:** Separación clara entre la interfaz de usuario (`main.py`) y el motor de cálculo (`conversor_universal.py`).
* **Diccionarios (Hash Maps):** Implementación de diccionarios anidados para almacenar factores de conversión, permitiendo una búsqueda de complejidad O(1).
* **Manejo de Excepciones:** Sistema robusto (`try/except`) para validar entradas numéricas y evitar cierres inesperados.
* **Aritmética de Precisión:** Manejo de conversiones lineales (multiplicación simple) y no lineales (fórmulas de temperatura).
* **Limpieza de Datos:** Normalización de inputs (insensibilidad a mayúsculas/minúsculas).

## 📂 Estructura del Proyecto

```text
universal_converter/
├── docs/
│   └── especificaciones.md           # Requerimientos y fórmulas de conversión
├── src/
│   ├── main.py                       # Orquestador (Interacción con el usuario)
│   └── conversor_universal.py        # Lógica de negocio (Fórmulas y Diccionarios)
├── tests/
│   └── test_conversor_universal.py   # Pruebas unitarias de precisión (QA)
├── .gitignore                        # Archivos de sistema ignorados
└── README.md                         # Documentación técnica