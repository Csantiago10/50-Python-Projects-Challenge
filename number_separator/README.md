# 🔢 Proyecto: Clasificador de Números Pares e Impares

> **Estado:** Completado ✅
> **Autor:** Ingeniero Santiago Noreña
> **Stack:** Python 3.12, Unittest, Git

## 📋 Descripción
Este script de línea de comandos es una herramienta de procesamiento de datos numéricos diseñada bajo una arquitectura modular. Su objetivo es recibir una cadena de texto con números desordenados, realizar un "parsing" y conversión de tipos, y clasificar los valores en dos conjuntos distintos (Pares e Impares), presentándolos finalmente ordenados de forma ascendente.

Este proyecto demuestra la capacidad de manipular entradas de usuario no estructuradas, aplicar lógica algorítmica y separar responsabilidades en el código.

## 🚀 Características Técnicas
El desarrollo se rigió estrictamente por restricciones técnicas para asegurar el dominio de los fundamentos de Python:

* **Arquitectura Modular:** Separación de la lógica de negocio (`separador_par_impar.py`) del flujo de ejecución (`main.py`).
* **Manipulación de Cadenas (String Parsing):** Uso de métodos como `.split()` para procesar entradas de texto crudo.
* **Casting y Validación:** Conversión dinámica de tipos de datos (`String` a `Int`).
* **Lógica Aritmética:** Implementación del operador Módulo (`%`) para la determinación de paridad.
* **Algoritmos de Ordenamiento:** Uso eficiente de métodos nativos (`.sort()`).
* **QA Automatizado:** Incluye pruebas unitarias para validar la lógica de separación.

## 📂 Estructura del Proyecto

```text
number_separator/
├── docs/
│   └── especificaciones.md       # Requerimientos y restricciones técnicas
├── src/
│   ├── main.py                   # Orquestador (Punto de entrada del usuario)
│   └── separador_par_impar.py    # Lógica pura (Algoritmo de clasificación)
├── test/
│   └── test_separador.py         # Scripts de pruebas unitarias (QA)
├── .gitignore                    # Archivos excluidos del control de versiones
└── README.md                     # Documentación técnica