# Especificaciones: El Ahorcado (Hangman) (Proyecto 06)

## 1. Descripción
Juego de consola interactivo donde el usuario debe adivinar una palabra secreta letra por letra antes de que se agoten sus intentos. El sistema implementa manipulación avanzada de listas para la visualización del progreso y conjuntos (sets) para la optimización de búsquedas.

**Autor:** Ingeniero Santiago Noreña
**Fecha:** 12/02/2026
**Estado:** ✅ Terminado

## 2. Requerimientos Funcionales
- **Banco de Palabras:** El sistema debe seleccionar aleatoriamente una palabra secreta de una lista predefinida (Ej: "python", "backend").
- **Visualización del Tablero:** Mostrar el progreso de la palabra oculta usando guiones bajos y actualizar las letras acertadas en su posición correcta (Ej: `P _ T _ O N`).
- **Control de Vidas:** El jugador inicia con **6 vidas**. Cada error resta 1 vida. Si llega a 0, el juego termina (Game Over).
- **Validación de Repetidos:** Si el usuario ingresa una letra que ya había intentado antes, el sistema debe avisarle sin penalizarle vidas.
- **Condición de Victoria:** El juego termina cuando no quedan guiones bajos `_` en el tablero.

## 3. Requerimientos Técnicos (Arquitectura)
- **Modularidad:**
    - `src/hangman_logic.py`: Funciones puras para buscar letras y actualizar el estado.
    - `src/main.py`: Bucle principal `While`, manejo de inputs y renderizado.
- **Estructuras de Datos (Clave):**
    - **Tablero Mutable:** NO usar strings para el tablero. Usar una **Lista** (`["_", "_", "_"]`) para permitir modificaciones por índice.
    - **Optimización de Búsqueda:** Usar un **Set** (`set()`) para almacenar el historial de letras usadas (`letras_usadas`), garantizando búsquedas O(1).
- **Limpieza de Inputs:** Normalización de la entrada del usuario (`.lower()`, `.strip()`) para evitar errores por mayúsculas o espacios.

## 4. Lógica del Negocio (Algoritmo de Actualización)
A diferencia de un diccionario simple, aquí la lógica requiere iteración posicional.

> **Pseudocódigo de Actualización:**
> Al recibir una letra correcta, no basta con saber que "existe". Se debe recorrer la palabra secreta índice por índice:
> `Si palabra_secreta[i] == letra_usuario -> tablero[i] = letra_usuario`

## 5. Casos de Prueba (QA)
Matriz para validar la lógica de vidas, detección de repetidos y condiciones de fin de juego.

| Palabra Secreta | Input Usuario | Estado Tablero (Visual) | Vidas | Resultado Esperado |
| :--- | :---: | :--- | :---: | :--- |
| PYTHON | P | `P _ _ _ _ _` | 6 | Acierto (Actualiza posición 0) |
| PYTHON | Z | `_ _ _ _ _ _` | 5 | Error (Resta vida) |
| PYTHON | P | `P _ _ _ _ _` | 6 | Aviso: "Letra repetida" (No resta vida) |
| AJA | A | `A _ A` | 6 | Acierto Múltiple (Actualiza pos 0 y 2) |
| SOL | (Completa) | `S O L` | N/A | **Victoria** (Rompe el bucle) |
| SOL | (Falla 6 veces)| `_ _ _` | 0 | **Game Over** |