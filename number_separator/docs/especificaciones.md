# Especificaciones del Proyecto: Clasificador de Pares e Impares

## 1. Descripción General
Script de línea de comandos diseñado para procesar una entrada de texto con números desordenados, clasificarlos según su paridad (pares vs. impares) y presentarlos de manera ordenada ascendente.

**Autor:** Ingeniero Santiago Noreña
**Fecha:** 06/02/2026
**Estado:** ✅ Terminado

## 2. Requerimientos Funcionales

### 2.1 Entrada (Input)
* El sistema solicitará al usuario una lista de números ingresados en una sola línea.
* **Formato esperado:** Números separados por caracteres (comas o espacios).
* *Ejemplo:* `1, 4, 5, 20, 33`

### 2.2 Procesamiento
* Convertir la entrada de texto en datos numéricos.
* Validar la paridad de cada número utilizando el operador módulo.
* Ordenar ambas listas resultantes de menor a mayor.

### 2.3 Salida (Output)
* El sistema debe imprimir en consola dos líneas separadas:
    1.  Lista de números **Pares** (Ordenados).
    2.  Lista de números **Impares** (Ordenados).

## 3. Restricciones Técnicas (Stack Tecnológico)
Para fines de aprendizaje y cumplimiento del ejercicio, el código fuente (`src`) debe implementar estrictamente los siguientes conceptos:
* **Entrada de datos:** Función `input()`.
* **Manipulación de Strings:** Método `.split()`.
* **Conversión de Tipos:** Casting con `int()`.
* **Lógica Matemática:** Operador Módulo (`%`) para determinar paridad.
* **Estructuras de Datos:** Listas y métodos `.append()` y `.sort()`.
* **Control de Flujo:** Bucles `for` para iterar los datos.

## 4. Casos de Prueba (Test Cases)

| Entrada Usuario | Salida Esperada: Pares | Salida Esperada: Impares |
| :--- | :--- | :--- |
| `1, 4, 5, 20, 33` | `[4, 20]` | `[1, 5, 33]` |
| `10, 2, 8, 5, 3` | `[2, 8, 10]` | `[3, 5]` |
| `7, 7, 1` | `[]` (Lista vacía) | `[1, 7, 7]` |

## 5. Pseudocódigo (Diseño Lógico)

INICIO
    1. IMPRIMIR "Ingrese números separados por coma:"
    2. entrada_usuario = RECIBIR input()
    
    3. lista_strings = SEPARAR entrada_usuario usando split()
    
    4. INICIALIZAR lista_pares vacía
    5. INICIALIZAR lista_impares vacía
    
    6. PARA CADA "num_str" EN lista_strings:
        a. numero = CONVERTIR num_str A Entero (int)
        
        b. SI (numero % 2 == 0) ENTONCES:
            AGREGAR numero A lista_pares
           SINO:
            AGREGAR numero A lista_impares
            
    7. ORDENAR lista_pares (ascendente)
    8. ORDENAR lista_impares (ascendente)
    
    9. IMPRIMIR "Pares: " + lista_pares
   10. IMPRIMIR "Impares: " + lista_impares
FIN