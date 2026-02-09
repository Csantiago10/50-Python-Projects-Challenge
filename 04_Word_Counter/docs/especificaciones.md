# Especificaciones: Analizador de Texto (Proyecto 04)

## 1. Descripción
Herramienta de análisis de texto diseñada para procesar párrafos extensos, extraer estadísticas clave y determinar la densidad de palabras. Su objetivo es identificar patrones de repetición ignorando "ruido" gramatical (mayúsculas, puntuación).

**Autor:** Ingeniero Santiago Noreña
**Fecha:** 09/02/2026
**Estado:** ✅ Terminado

## 2. Requerimientos Funcionales
- **Entrada de Datos:** Permitir al usuario ingresar un texto largo o párrafo completo.
- **Análisis Estadístico:**
    - Calcular el **Total de Palabras** (excluyendo signos de puntuación).
    - Identificar las **3 palabras más frecuentes** (Top 3 Ranking).
- **Normalización:** El sistema debe tratar "Hola", "hola" y "hola." como la misma palabra.

## 3. Requerimientos Técnicos
- **Modularidad:** Separación de lógica de análisis e interfaz de usuario.
- **Arquitectura de Archivos:**
    - `src/words_counter.py`: Funciones puras de limpieza y conteo.
    - `src/main.py`: Captura de input y visualización de resultados.
    - `test/test_words_counter.py`: Pruebas de limpieza y frecuencia.
- **Estructuras de Datos:** Uso obligatorio de **Diccionarios (`dict`)** para el conteo de frecuencias `{palabra: cantidad}`.
- **Manipulación de Strings:** Uso de métodos como `.lower()`, `.maketrans()`, `.translate()` o `.strip()` para la limpieza.

## 4. Lógica del Negocio / Algoritmos

### A. Algoritmo de Limpieza (Normalización)
1. Recibir texto crudo.
2. Convertir todo a **minúsculas** (`.lower()`) para evitar duplicados por capitalización.
3. Eliminar signos de puntuación (.,;:¡!¿?) reemplazándolos por espacios o vacío.
4. Dividir el texto en una lista de palabras (`.split()`).

### B. Algoritmo de Conteo (Frecuencia)
1. Inicializar un diccionario vacío.
2. Iterar sobre la lista de palabras limpias.
3. Si la palabra existe en el diccionario $\rightarrow$ Sumar +1 al valor.
4. Si NO existe $\rightarrow$ Crear la llave con valor 1.

### C. Algoritmo de Ranking (Top 3)
1. Convertir el diccionario en una lista de tuplas `[(palabra, cantidad), ...]`.
2. Ordenar la lista de forma descendente basándose en la cantidad.
3. Retornar los primeros 3 elementos.

## 5. Casos de Prueba (QA)
| Escenario | Entrada | Salida Esperada | Comportamiento |
| :--- | :--- | :--- | :--- |
| **Básico** | `"Hola mundo"` | `Total: 2`, `Top: [('hola', 1), ('mundo', 1)]` | Conteo simple. |
| **Normalización** | `"Hola, hola."` | `Total: 2`, `Top: [('hola', 2)]` | Ignora comas, puntos y mayúsculas. |
| **Ranking** | `"a a a b b c"` | `Top: [('a', 3), ('b', 2), ('c', 1)]` | Orden correcto por frecuencia. |
| **Texto Vacío** | `""` | `Total: 0`, `Top: []` | Manejo de input vacío. |