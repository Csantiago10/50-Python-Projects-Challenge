# 🏦 Proyecto 10: Simulador de Cajero Automático (ATM)

> **Estado:** Completado ✅
> **Autor:** Ingeniero Santiago Noreña
> **Stack:** Python 3.12, JSON, Hashlib

## 📋 Descripción
Aplicación de consola que simula las operaciones de un Cajero Automático (ATM). Permite a los usuarios registrarse, iniciar sesión, consultar su saldo, depositar, retirar dinero y recuperar su PIN. La seguridad de las credenciales se garantiza mediante el hashing de los PINs, y la persistencia de los datos se gestiona a través de un archivo JSON.

## 🚀 Características Técnicas
*   **Gestión de Usuarios:** Sistema completo de registro, autenticación y recuperación de PIN.
*   **Seguridad:** Implementación de hashing con **SHA-256** para proteger los PINs de los usuarios, evitando el almacenamiento en texto plano.
*   **Persistencia de Datos:** Uso de un archivo JSON como base de datos para guardar la información de los usuarios, saldos y estados de las cuentas.
*   **Operaciones Financieras:** Funcionalidades para consultar saldo, realizar depósitos y retiros, con validaciones de fondos.
*   **Generación de Recibos:** Creación automática de un archivo `.txt` como comprobante después de cada retiro.
*   **Mecanismo de Bloqueo:** La cuenta se bloquea automáticamente después de 3 intentos de inicio de sesión fallidos para prevenir ataques de fuerza bruta.

## 📂 Estructura
```text
10_ATM_Simulator/
├── docs/
│   ├── especificaciones.md
│   └── users.json
├── src/
│   ├── main.py          # Orquestador principal y menús
│   ├── app.py           # Lógica de la aplicación
│   ├── auth.py          # Autenticación y hashing
│   ├── operations.py    # Operaciones financieras
│   └── views/           # Módulos de la interfaz de usuario
├── test/
│   └── test_atm.py      # Pruebas unitarias
└── README.md
```