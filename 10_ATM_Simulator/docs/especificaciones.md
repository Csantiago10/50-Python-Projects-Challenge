# Especificaciones: Simulador de Cajero Automático (Proyecto 10)

## 1. Descripción
Aplicación de consola que simula el funcionamiento de un Cajero Automático (ATM). El sistema permite la gestión de usuarios (registro, autenticación, recuperación de claves) y la realización de operaciones financieras básicas (consultas, depósitos y retiros), garantizando la persistencia de datos y la seguridad mediante hashing de contraseñas.

**Autor:** Ingeniero Santiago Noreña
**Fecha:** 19/02/2026
**Estado:** ✅ Terminado

## 2. Requerimientos Funcionales
- **Gestión de Sesión:**
    - **Login:** Validación de credenciales (Usuario y PIN). Bloqueo de cuenta tras 3 intentos fallidos.
    - **Registro:** Creación de nuevos usuarios con DNI y PIN de 4 dígitos. Generación automática de número de cuenta.
    - **Recuperación:** Restablecimiento de PIN validando Usuario y DNI.
- **Operaciones Financieras:**
    - **Consultar Saldo:** Visualización del saldo actual formateado (formato moneda).
    - **Depositar:** Ingreso de dinero (validación de montos positivos).
    - **Retirar:** Extracción de dinero con validación de fondos suficientes.
- **Generación de Comprobantes:**
    - Al realizar un retiro, el sistema debe generar automáticamente un archivo de texto (`.txt`) con los detalles de la transacción (Fecha, Usuario, Monto, Saldo restante).
- **Persistencia:**
    - Todos los cambios (saldos, nuevos usuarios, bloqueos) deben guardarse automáticamente en una base de datos local (JSON).

## 3. Requerimientos Técnicos
- **Arquitectura Modular:**
    - `src/main.py`: Orquestador del flujo principal y menús de usuario.
    - `src/auth.py`: Gestión de base de datos (JSON), autenticación y seguridad (Hashing).
    - `src/operations.py`: Lógica de transacciones financieras y generación de recibos.
- **Seguridad:**
    - **Hashing:** Los PINs no se guardan en texto plano. Se utiliza el algoritmo **SHA-256** (librería `hashlib`) para almacenarlos de forma segura.
- **Manejo de Datos:**
    - Base de datos en formato JSON (`docs/users.json`).
    - Referencias en memoria: Manipulación de diccionarios para actualizar el estado del usuario en tiempo real sin recargas innecesarias.
- **Validaciones:**
    - Control de tipos de datos (enteros para montos y DNI).
    - Verificación de existencia de usuario antes del registro (evitar duplicados).

## 4. Lógica del Algoritmo
### Autenticación y Bloqueo
1.  **Carga:** Se lee el archivo JSON en una lista de diccionarios.
2.  **Verificación:**
    *   Si `intentos_fallidos >= 3` $\rightarrow$ Denegar acceso (Cuenta Bloqueada).
    *   Si `hash(input_pin) == user_pin_hash` $\rightarrow$ Acceso concedido y resetear contador a 0.
    *   Si no coincide $\rightarrow$ Incrementar contador y guardar en JSON.

### Transacción de Retiro
1.  **Validación:** `Monto > 0` Y `Monto <= Saldo`.
2.  **Ejecución:** `Saldo_Nuevo = Saldo_Actual - Monto`.
3.  **Persistencia:** Actualizar objeto usuario y sobreescribir JSON.
4.  **Auditoría:** Crear archivo `recibo_{usuario}.txt` con fecha, monto y saldo restante.

## 5. Casos de Prueba (QA)
| Escenario | Acción | Entrada | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| **Registro** | Crear Usuario | User: "Test", PIN: "1234" | Usuario creado, N° Cuenta generado aleatoriamente. |
| **Login Exitoso** | Iniciar Sesión | Credenciales correctas | Acceso al menú de operaciones. |
| **Seguridad** | Login Fallido | PIN incorrecto (3 veces) | Mensaje "CUENTA BLOQUEADA". |
| **Fondos** | Retirar | Monto > Saldo | Error: "No tienes fondos suficientes". |
| **Persistencia** | Depositar | $500 | Saldo se actualiza en JSON y se mantiene al reiniciar el programa. |
| **Recuperación** | Reset PIN | User + DNI correctos | PIN actualizado y contador de bloqueos reseteado a 0. |
| **Recibo** | Retirar | $100 | Se crea archivo `docs/recibo_Test.txt`. |