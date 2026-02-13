# Especificaciones: Cifrado César (Proyecto 07)

## 1. Descripción
Herramienta de criptografía clásica que implementa el "Cifrado César", una técnica de sustitución simple donde cada letra de un texto es reemplazada por otra que se encuentra un número fijo de posiciones más adelante en el alfabeto. Este proyecto permite tanto encriptar como desencriptar mensajes respetando mayúsculas, minúsculas y caracteres especiales.

**Autor:** Ingeniero Santiago Noreña
**Fecha:** 13/02/2026
**Estado:** ✅ Terminado

## 2. Requerimientos Funcionales
- **Menú Interactivo:** El sistema debe ofrecer las opciones de:
    1. Encriptar mensaje.
    2. Desencriptar mensaje.
    3. Salir.
- **Entrada de Datos:**
    - **Mensaje:** Texto alfanumérico (se deben respetar espacios y símbolos, solo se cifran letras).
    - **Desplazamiento (Shift):** Número entero que define cuántas posiciones mover la letra.
- **Validación de Entrada:**
    - El desplazamiento debe ser estrictamente un número entero.
    - El rango del desplazamiento debe estar entre **1 y 25** para evitar rotaciones redundantes (ya que el alfabeto inglés tiene 26 letras).
- **Preservación de Formato:** Las mayúsculas deben mantenerse como mayúsculas, las minúsculas como minúsculas, y los caracteres no alfabéticos (números, signos de puntuación) deben quedar intactos.

## 3. Requerimientos Técnicos
- **Modularidad:**
    - `src/cypher.py`: Contiene la lógica pura de transformación de caracteres (Algoritmo `encrypt` y `decrypt`).
    - `src/main.py`: Maneja la interfaz de usuario (CLI), el bucle principal y las validaciones de entrada (`try-except`).
- **Manejo de ASCII:** Uso de las funciones nativas de Python `ord()` (caracter a entero) y `chr()` (entero a caracter).
- **Aritmética Modular:** Implementación del operador módulo `%` para manejar el desbordamiento del alfabeto (ej: Z + 1 = A).
- **Reutilización de Código:** La función de desencriptado reutiliza la lógica de encriptado invirtiendo el signo del desplazamiento ($Shift_{decrypt} = -Shift_{encrypt}$), reduciendo la duplicidad de código.

## 4. Lógica del Algoritmo (Matemática Modular)
El núcleo del proyecto se basa en la aritmética modular sobre los índices del alfabeto inglés (26 letras).

### Fórmulas
Para una letra $x$ y un desplazamiento $n$:

1.  **Normalización:** Convertir el valor ASCII a un índice base 0 (0-25).
    *   $Indice = ASCII(x) - Base$
    *   *Base = 65 ('A') para mayúsculas, 97 ('a') para minúsculas.*
2.  **Rotación (Cifrado):**
    *   $NuevoIndice = (Indice + n) \pmod{26}$
    *   *El operador módulo (%) asegura que si el índice pasa de 25, vuelva a empezar desde 0.*
3.  **Recuperación:**
    *   $CaracterCifrado = chr(NuevoIndice + Base)$

### Rangos ASCII Utilizados
| Tipo | Rango ASCII | Base |
| :--- | :--- | :--- |
| Mayúsculas | 65 - 90 | 65 |
| Minúsculas | 97 - 122 | 97 |

## 5. Casos de Prueba (QA)
| Operación | Mensaje de Entrada | Shift | Resultado Esperado | Notas |
| :--- | :--- | :--- | :--- | :--- |
| **Encriptar** | `HOLA` | `1` | `IPMB` | Desplazamiento simple (+1). |
| **Encriptar** | `Z` | `1` | `A` | Vuelta al inicio (Wrap-around). |
| **Desencriptar** | `IPMB` | `1` | `HOLA` | Inverso correcto. |
| **Mixto** | `Python 3.12` | `2` | `Ravjqp 3.12` | Ignora números y espacios. |
