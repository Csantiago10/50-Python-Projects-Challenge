# 📝 Proyecto 04: Contador de Palabras y Analizador de Texto

> **Estado:** Completado ✅
> **Autor:** Ingeniero Santiago Noreña
> **Stack:** Python 3.12, Unittest, Git

## 📋 Descripción
Este script es una herramienta de procesamiento de lenguaje natural (NLP) a nivel básico. Su función es recibir un bloque de texto (párrafo), realizar un proceso de "tokenización" (separación de elementos) y devolver métricas cuantitativas precisas, como el conteo total de palabras.

El proyecto simula el funcionamiento interno de las herramientas de análisis de texto que se encuentran en procesadores modernos, enfocándose en la limpieza y estructuración de datos no estructurados (strings).

## 🚀 Características Técnicas
Se implementaron algoritmos eficientes para la manipulación de cadenas de caracteres:

* **Tokenización (Parsing):** Algoritmo de separación de cadenas utilizando delimitadores de espacio (`.split()`).
* **Normalización de Datos:** Limpieza de espacios en blanco redundantes (`.strip()`) para evitar falsos positivos en el conteo.
* **Manejo de Cadenas:** Iteración y validación de texto vacío o nulo.
* **Arquitectura Modular:** Lógica de conteo (`words_counter.py`) desacoplada de la interfaz de usuario (`main.py`).
* **QA Automatizado:** Pruebas unitarias para validar casos borde (textos vacíos, espacios múltiples, caracteres especiales).

## 📂 Estructura del Proyecto

```text
word_counter/
├── docs/
│   └── especificaciones.md       # Requerimientos y casos de uso
├── src/
│   ├── main.py                   # Orquestador (Input/Output)
│   └── words_counter.py          # Motor de análisis de texto
├── tests/
│   └── test_words_counter.py           # Pruebas de validación (QA)
├── .gitignore
└── README.md                     # Documentación técnica