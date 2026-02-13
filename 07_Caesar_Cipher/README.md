# 🔐 Proyecto 07: Cifrado César (Caesar Cipher)

> **Estado:** Completado ✅
> **Autor:** Ingeniero Santiago Noreña
> **Stack:** Python 3.12, Unittest, Git

## 📋 Descripción
Este proyecto es una implementación de la herramienta de criptografía clásica conocida como "Cifrado César". Es una técnica de sustitución simple donde cada letra de un texto es reemplazada por otra que se encuentra un número fijo de posiciones más adelante en el alfabeto.

El sistema permite tanto encriptar como desencriptar mensajes, destacando por su capacidad de respetar el formato original (mayúsculas, minúsculas y caracteres especiales) mediante el uso de aritmética modular y manipulación de códigos ASCII.

## 🚀 Características Técnicas
El desarrollo se centró en la lógica matemática y la manipulación de caracteres a bajo nivel:

*   **Aritmética Modular:** Implementación del operador módulo (`%`) para manejar el desbordamiento del alfabeto (ej: Z + 1 = A), asegurando una rotación cíclica correcta.
*   **Manipulación ASCII:** Uso de las funciones nativas `ord()` y `chr()` para la conversión precisa entre caracteres y sus valores enteros.
*   **Reutilización de Lógica:** El algoritmo de desencriptado aprovecha la función de encriptado invirtiendo matemáticamente el desplazamiento ($Shift_{decrypt} = -Shift_{encrypt}$), evitando duplicidad de código.
*   **Validación de Entradas:** Control estricto del rango de desplazamiento (1-25) y manejo de excepciones para asegurar la integridad de la ejecución.
*   **Arquitectura Modular:** Separación de responsabilidades entre la lógica de transformación (`cypher.py`) y la interfaz de usuario (`main.py`).

## 📂 Estructura del Proyecto

```text
07_Caesar_Cipher/
├── docs/
│   ├── especificaciones.md       # Reglas matemáticas y requerimientos
│   └── pseudocodigo.txt          # Lógica algorítmica planificada
├── src/
│   ├── main.py                   # Orquestador (Interfaz CLI y validaciones)
│   └── cypher.py                 # Lógica pura de transformación (Algoritmo)
├── tests/
│   └── test_cypher.py            # Pruebas unitarias de encriptado/desencriptado
├── .gitignore
└── README.md                     # Documentación técnica
```