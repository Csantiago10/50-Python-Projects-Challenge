# Especificaciones: Generador de Contraseñas (Proyecto 03)

## 1. Descripción del Proyecto
Herramienta de línea de comandos (CLI) diseñada para generar contraseñas seguras y aleatorias. El sistema permite al usuario personalizar la complejidad de la contraseña seleccionando qué tipos de caracteres incluir, garantizando una alta entropía (aleatoriedad) para mejorar la seguridad digital.

**Autor:** Ingeniero Santiago Noreña
**Fecha:** 07/02/2026
**Estado:** ✅ Terminado

## 2. Requerimientos Funcionales
- **Entrada de Longitud:** El usuario debe definir la longitud de la contraseña ($N$).
- **Configuración de Complejidad:** El sistema debe realizar tres preguntas de configuración (S/N):
    1. ¿Incluir letras mayúsculas?
    2. ¿Incluir números?
    3. ¿Incluir símbolos?
- **Validación de Selección:**
    - Por defecto, siempre se incluyen letras minúsculas para evitar un conjunto vacío.
    - Si el usuario selecciona "N" en todo, la contraseña será solo de minúsculas.
- **Ciclo de Ejecución:** El programa debe mantenerse en un bucle (`while True`) permitiendo generar múltiples contraseñas hasta que el usuario elija salir.

## 3. Requerimientos Técnicos
- **Librerías:** Uso de `random` (o `secrets` para mayor seguridad) y la librería `string` para obtener los mapas de caracteres.
- **Arquitectura de Archivos:**
    - `src/generador.py`: Módulo con la lógica pura de construcción de contraseñas.
    - `src/main.py`: Módulo de interfaz (inputs, prints y bucle principal).
    - `test/test_generador.py`: Pruebas unitarias de las contraseñas.
    - `docs/especificaciones.md`: Documentación técnica del proyecto.
- **Estrategia de Código (Refactorización):**
    - En lugar de crear 8 condicionales (`if/elif`) para cada combinación posible, se debe usar un **Algoritmo de Construcción Dinámica**.
    - Se inicia con un "pool" base y se le concatenan los grupos de caracteres seleccionados.
- **Manejo de Errores:**
    - Bloques `try-except` para validar que la longitud sea un número entero.
    - Validación de que la longitud sea mayor a 0.

## 4. Lógica del Algoritmo (Flujo Optimizado)
Para evitar la explosión combinatoria de `if/else`, se implementará la siguiente lógica:

1.  **Definir Alfabeto Base:** `caracteres = string.ascii_lowercase` (a-z).
2.  **Evaluación Secuencial:**
    * Si `mayus == "S"` $\rightarrow$ `caracteres += string.ascii_uppercase`
    * Si `nums == "S"` $\rightarrow$ `caracteres += string.digits`
    * Si `simb == "S"` $\rightarrow$ `caracteres += string.punctuation`
3.  **Generación:**
    * Crear un bucle que se repita $N$ veces (longitud solicitada).
    * En cada vuelta, elegir un caracter al azar del string `caracteres`.
    * Concatenar el resultado.
4.  **Salida:** Mostrar la contraseña final.

## 5. Casos de Prueba (QA)
| Escenario | Configuración (Mayús/Num/Simb) | Entrada Longitud | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| **Máxima Seguridad** | S / S / S | `15` | String mixto (Ej: `A#3f_9kL...`) |
| **Alfanumérico** | S / S / N | `8` | Solo letras y números (Ej: `A3k9Lp12`) |
| **Solo Texto** | S / N / N | `10` | Solo letras (Ej: `AbCdEfGhIj`) |
| **Error de Usuario** | - | `texto` | Mensaje: "Error, ingrese un número." |
| **Longitud Inválida** | - | `-5` | Mensaje: "La longitud debe ser positiva." |