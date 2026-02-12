# 😵 Proyecto 06: Juego del Ahorcado (Hangman)

> **Estado:** Completado ✅
> **Autor:** Ingeniero Santiago Noreña
> **Stack:** Python 3.12, Unittest, Git

## 📋 Descripción
Este proyecto es una implementación clásica del juego de mesa "El Ahorcado" en una interfaz de línea de comandos (CLI). El objetivo es adivinar una palabra oculta seleccionada aleatoriamente antes de que se agoten las 6 vidas disponibles.

El sistema destaca por su optimización en el manejo de estructuras de datos, utilizando conjuntos (`sets`) para el historial de intentos y listas mutables para la renderización del tablero, asegurando un rendimiento eficiente.

## 🚀 Características Técnicas
Se aplicaron conceptos intermedios de manipulación de datos y arquitectura limpia:

*   **Estructuras de Datos Eficientes:** Uso de `set()` para almacenar letras usadas, garantizando búsquedas de complejidad O(1) y evitando ciclos innecesarios al verificar repetidos.
*   **Manipulación de Listas:** El tablero se gestiona como una lista mutable para actualizar caracteres específicos por índice sin regenerar strings constantemente.
*   **Validación de Entradas:** Sanitización de inputs (eliminación de espacios, conversión a minúsculas) y control de caracteres no alfabéticos.
*   **Arquitectura Modular:** Separación de responsabilidades entre la lógica del juego (`hangman_logic.py`) y la interfaz de usuario (`main.py`).
*   **QA Automatizado:** Pruebas unitarias exhaustivas para validar la lógica de aciertos, fallos y condiciones de victoria/derrota.

## 📂 Estructura del Proyecto

```text
06_Hangman/
├── docs/
│   ├── especificaciones.md       # Reglas de negocio y requerimientos
│   └── pseudocodigo.txt          # Lógica algorítmica planificada
├── src/
│   ├── main.py                   # Orquestador (Bucle del juego e interacción)
│   └── hangman_logic.py          # Lógica pura de búsqueda y actualización
├── test/
│   └── test_hangman_logic.py     # Pruebas unitarias (QA)
├── .gitignore
└── README.md                     # Documentación técnica
```