# Especificaciones: Adivina el Número (Búsqueda Binaria) (Proyecto 09)

## 1. Descripción
Juego interactivo de consola donde los roles se invierten: el usuario piensa un número secreto (del 1 al 100) y la computadora debe adivinarlo. Para garantizar la eficiencia, el sistema utiliza el algoritmo de **Búsqueda Binaria**, asegurando encontrar el número en un máximo de 7 intentos ($log_2(100) \approx 6.64$), en lugar de adivinar al azar.

**Autor:** Ingeniero Santiago Noreña
**Fecha:** 16/02/2026
**Estado:** ✅ Terminado

## 2. Requerimientos Funcionales
- **Interacción Inversa:** El usuario mantiene el número en su mente; la PC propone números.
- **Sistema de Feedback:** El usuario debe responder a cada predicción con:
    - `"A"` (Alto): El número secreto es mayor que la predicción mostrada.
    - `"B"` (Bajo): El número secreto es menor que la predicción mostrada.
    - `"C"` (Correcto): La computadora ha acertado.
- **Eficiencia Algorítmica:** La computadora debe calcular el punto medio del rango posible en cada turno.
- **Detección de Trampas:** Si el usuario da respuestas contradictorias que hacen que el rango de búsqueda sea imposible (ej: límite inferior > límite superior), el sistema debe lanzar un error y terminar el juego.

## 3. Requerimientos Técnicos
- **Algoritmo:** Implementación estricta de Búsqueda Binaria.
- **Variables de Estado:**
    - `limite_inferior`: Inicio del rango de búsqueda (Inicia en 1).
    - `limite_superior`: Fin del rango de búsqueda (Inicia en 100).
    - `prediccion`: Valor calculado por la PC.
- **Fórmula Matemática:** `prediccion = (limite_inferior + limite_superior) // 2` (División entera).
- **Ciclo de Control:** Bucle `while` que se mantiene activo hasta que el usuario confirme con "C" o se detecte trampa.

## 4. Lógica del Algoritmo (Pseudocódigo)
El núcleo del proyecto se basa en reducir el espacio de búsqueda a la mitad en cada iteración.

1.  **Inicialización:**
    *   Definir `limite_inferior = 1`
    *   Definir `limite_superior = 100`
    *   Definir `respuesta_usuario = ""`
2.  **Bucle Principal:**
    *   Mientras `respuesta_usuario != "C"`:
        *   **Validación de Trampa:** Si `limite_inferior > limite_superior`, imprimir "¡Estás haciendo trampa!" y romper ciclo.
        *   **Cálculo:** `prediccion = (limite_inferior + limite_superior) // 2`
        *   **Interacción:** Preguntar "¿Es {prediccion} tu número? (A/B/C): "
        *   **Lógica de Actualización:**
            *   Si `respuesta == "A"` (Es más Alto):
                *   El número está arriba. Nuevo `limite_inferior = prediccion + 1`
            *   Si `respuesta == "B"` (Es más Bajo):
                *   El número está abajo. Nuevo `limite_superior = prediccion - 1`
            *   Si `respuesta == "C"`:
                *   Imprimir "¡Sabía que lo lograría!"

## 5. Casos de Prueba (QA)
| Número Mental | Predicción PC | Respuesta Usuario | Acción del Algoritmo | Nuevo Rango |
| :--- | :--- | :--- | :--- | :--- |
| **75** | 50 | "A" (Alto) | `low = 50 + 1` | [51, 100] |
| **75** | 75 | "C" (Correcto)| Terminar Juego | N/A |
| **25** | 50 | "B" (Bajo) | `high = 50 - 1` | [1, 49] |
| **Trampa** | 50 | "A" (Dice > 50)| `low = 51` | [51, 100] |
| **Trampa** | ... | "B" (Dice < 51)| `high = 50` | [51, 50] |
| **Trampa** | ... | ... | Detectar `low > high` | **Error** |