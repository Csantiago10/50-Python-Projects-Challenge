# Especificaciones: El Conversor Universal (Proyecto 02)

## 1. Descripción
Herramienta de consola interactiva diseñada para realizar conversiones precisas entre unidades de medida (Longitud, Masa y Temperatura). El sistema implementa un ciclo de vida continuo, permitiendo al usuario realizar múltiples operaciones en una sola sesión sin necesidad de reiniciar el programa.

**Autor:** Ingeniero Santiago Noreña
**Fecha:** 06/02/2026
**Estado:** ✅ Terminado


## 2. Requerimientos Funcionales
- **Menú Interactivo:** Desplegar un menú claro con 7 opciones (6 de conversión y 1 de salida).
- **Ciclo de Ejecución:** El programa debe mantenerse activo (`while True`) hasta que el usuario seleccione explícitamente la opción **"7. Salir"**.
- **Formato de Salida:** Los resultados deben mostrarse con **2 decimales** de precisión usando `f-strings` (ej: `10.00 Km son 6.21 Millas`).
- **Validación de Entrada (UX):**
    - Detectar la intención de salir **antes** de solicitar valores numéricos.
    - Manejar errores de tipo (texto en lugar de números) mediante `try-except`.
    - **Validación Física:** Impedir valores negativos en conversiones de Masa y Longitud, permitiéndolos solo en Temperatura.

## 3. Requerimientos Técnicos
- **Modularidad:** Separación de la lógica de negocio y la interfaz.
- **Arquitectura de Archivos:**
    - `src/conversor_universal.py`: Módulo con funciones puras para los cálculos matemáticos.
    - `src/main.py`: Control de flujo, menú y manejo de excepciones.
    - `test/test_conversor_universal.py`: Pruebas unitarias de las fórmulas.
- **Manejo de Errores:** Uso de bloques `try-except` para evitar el cierre inesperado de la aplicación (`ValueError`).

## 4. Definiciones Matemáticas (Lógica)
Las funciones deben implementar las siguientes fórmulas de conversión:

### Longitud
- **Km a Millas:** $Millas = Km \times 0.621371$
- **Millas a Km:** $Km = Millas \times 1.60934$

### Masa
- **Kg a Libras:** $Libras = Kg \times 2.20462$
- **Libras a Kg:** $Kg = Libras \times 0.453592$

### Temperatura
- **Celsius a Fahrenheit:** $F = (C \times 1.8) + 32$
- **Fahrenheit a Celsius:** $C = \frac{F - 32}{1.8}$

## 5. Casos de Prueba (QA)
| Opción | Entrada (Valor) | Salida Esperada | Comportamiento |
| :--- | :--- | :--- | :--- |
| **1** | `10` | `6.21 Millas` | Cálculo correcto. |
| **5** | `-10` | `14.00 °F` | Permite negativos (Temperatura). |
| **3** | `-5` | `Error: No negativos` | Bloquea negativos (Masa). |
| **-** | `hola` | `Error: Dato inválido` | `try-except` atrapa el error. |
| **7** | `(vacio)` | `Saliendo...` | Cierra el programa limpiamente. |