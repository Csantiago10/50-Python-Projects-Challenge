# Especificaciones: Piedra, Papel o Tijera (Proyecto 05)

## 1. Descripción
Juego de consola interactivo contra la CPU implementando la lógica clásica de "Piedra, Papel o Tijera". El sistema utiliza una modalidad "Mejor de 3" (Best of 3), donde el juego continúa hasta que uno de los dos contrincantes alcanza 2 victorias.

**Autor:** Ingeniero Santiago Noreña
**Fecha:** 11/02/2026
**Estado:** ✅ Terminado

## 2. Requerimientos Funcionales
- **Sistema de Rondas:** El juego debe iterar indefinidamente hasta que haya un ganador definitivo.
- **Validación de Entrada:** El usuario solo puede ingresar: 'piedra', 'papel' o 'tijera' (insensible a mayúsculas).
- **Inteligencia Artificial (RNG):** La CPU debe elegir aleatoriamente en cada turno.
- **Marcador en Vivo:** Al final de cada ronda, se debe mostrar el puntaje actual (Ej: "Santiago 1 - 0 CPU").
- **Condición de Victoria:** El primero en llegar a **2 puntos** gana la partida y el programa termina.

## 3. Requerimientos Técnicos
- **Modularidad:**
    - `src/game_logic.py`: Lógica de determinación del ganador y reglas.
    - `src/main.py`: Bucle del juego, inputs y control de estado (puntajes).
- **Estructuras de Datos:** Uso de un **Diccionario de Reglas** para determinar al ganador, evitando el uso excesivo de `if/elif` anidados.
- **Limpieza de Inputs:** Normalización de la entrada del usuario (`.lower()`, `.strip()`).

## 4. Lógica del Negocio (Matriz de Decisiones)
En lugar de múltiples condicionales, se usará un diccionario de "Quién gana a quién":

```python
REGLAS = {
    "piedra": "tijera",  # Piedra gana a Tijera
    "papel": "piedra",   # Papel gana a Piedra
    "tijera": "papel"    # Tijera gana a Papel
}

## 5. Casos de Prueba (QA)
El objetivo de esta sección es validar la lógica principal del juego y el manejo de errores en la entrada de datos.

| Jugador | CPU | Resultado Esperado | Marcador (Ejemplo) |
| :--- | :--- | :--- | :--- |
| Piedra | Tijera | Gana Jugador | 1 - 0 |
| Papel | Tijera | Gana CPU | 0 - 1 |
| Papel | Papel | Empate | 0 - 0 |
| Roca | (Cualquiera) | **Error:** Opción inválida | N/A |