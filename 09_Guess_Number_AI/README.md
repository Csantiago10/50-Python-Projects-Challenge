# 🧠 Proyecto 09: Adivina el Número (IA)

> **Estado:** Completado ✅
> **Autor:** Ingeniero Santiago Noreña
> **Stack:** Python 3.12, Búsqueda Binaria, Unittest

## 📋 Descripción
En este proyecto invertimos los roles: el usuario piensa un número y la computadora debe adivinarlo. Implementamos el algoritmo de **Búsqueda Binaria** para garantizar que la IA encuentre el número en un máximo de 7 intentos ($log_2(100)$), demostrando la eficiencia algorítmica frente a la fuerza bruta.

## 🚀 Características Técnicas
*   **Algoritmo Eficiente:** Uso de división y conquista para reducir el rango de búsqueda a la mitad en cada paso.
*   **Detección de Trampas:** El sistema identifica si el usuario da respuestas contradictorias (ej: decir que es mayor a 50 y luego menor a 51).
*   **Interacción CLI:** Interfaz de consola clara para guiar al usuario.
*   **Calidad de Código:** Funciones y pruebas documentadas en inglés (Docstrings) siguiendo buenas prácticas.

## 📂 Estructura
```text
09_Guess_Number_AI/
├── docs/
│   ├── especificaciones.md
│   └── pseudocodigo.txt
├── src/
│   ├── main.py      # Interfaz y bucle de juego
│   └── game.py      # Lógica de búsqueda binaria
├── test_game.py     # Pruebas unitarias (QA)
└── README.md
```