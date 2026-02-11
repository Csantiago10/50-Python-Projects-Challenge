# 🎮 Proyecto 05: Piedra, Papel o Tijera (Optimizado)

> **Estado:** Completado ✅
> **Autor:** Ingeniero Santiago Noreña
> **Stack:** Python 3.12, Unittest, Git

## 📋 Descripción
Este proyecto es una implementación robusta y modular del clásico juego de simulación de decisiones (Piedra, Papel o Tijera). A diferencia de las implementaciones básicas que utilizan múltiples condicionales anidados, este software utiliza una arquitectura basada en datos (**Data-Driven Logic**) para determinar el ganador de manera eficiente.

El objetivo técnico fue eliminar la complejidad ciclomática mediante el uso de tablas de búsqueda (Diccionarios), permitiendo una escalabilidad sencilla y un código limpio.

## 🚀 Características Técnicas
El desarrollo se enfocó en la optimización algorítmica y la calidad del código:

* **Lógica Basada en Diccionarios:** Implementación de Hash Maps (`Rules Dictionary`) para determinar el estado de victoria en tiempo constante O(1), reemplazando largas cadenas de `if/elif`.
* **Arquitectura Modular:** Separación estricta entre la capa de presentación (`main.py`) y la lógica de negocio (`game_logic.py`).
* **Manejo de Errores (Robustez):** Validación de entradas del usuario con recuperación automática ante inputs inválidos (ej. "Roca" en lugar de "Piedra").
* **Testing Avanzado (QA):** Uso de `unittest` y técnicas de **Mocking** para simular el comportamiento aleatorio de la CPU y las entradas del usuario durante las pruebas.
* **Aleatoriedad Controlada:** Uso del módulo `random` para la toma de decisiones de la IA.

## 📂 Estructura del Proyecto

```text
rock_paper_scissors/
├── docs/
│   └── especificaciones.md       # Reglas del juego y lógica de victoria
├── src/
│   ├── main.py                   # Orquestador (Ciclo del juego y Score)
│   └── game_logic.py             # Motor de decisiones (Diccionario de Reglas)
├── tests/
│   └── test_game_logic.py        # Pruebas unitarias con Mocks (QA)
├── .gitignore
└── README.md                     # Documentación técnica