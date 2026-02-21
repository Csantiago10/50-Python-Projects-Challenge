import auth
import operations
import random


def user_session_loop(user, list_users):
    """Bucle of user session."""
    print(f"\n¡Bienvenido, {user['username']}!")

    while True:
        print("=" * 50)
        print(f"Cuenta N°: {user['n_account']} ")
        print("=" * 50)
        print("1. Ver saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        print("=" * 50)

        op_user = input("Seleccione una opción: ").strip()

        if op_user == "1":
            print(f"\nTu saldo actual es: {operations.check_balance(user)}")
        elif op_user == "2":
            try:
                deposit = int(input("Ingrese la cantidad a depositar: "))
                result = operations.deposit_money(user, deposit)
                if result:
                    # user es una referencia al dict dentro de list_users,
                    # así que solo necesitamos guardar la DB.
                    auth.save_database(list_users)
                    print("\n¡Depósito realizado con éxito!")
                    print(f"Nuevo saldo: {operations.check_balance(user)}")
            except ValueError:
                print("\n[!] Error: Ingrese un monto numérico válido.")
        elif op_user == "3":
            try:
                withdraw = int(input("Ingrese la cantidad a retirar: "))
                result = operations.withdraw_money(user, withdraw)
                if result:
                    auth.save_database(list_users)
                    print("\n¡Retiro realizado con éxito!")
                    print(f"Nuevo saldo: {operations.check_balance(user)}")
            except ValueError:
                print("\n[!] Error: Ingrese un monto numérico válido.")
        elif op_user == "4":
            print("\nCerrando sesión...")
            break
        else:
            print("\n[!] Opción no válida. Intente nuevamente.")


def main_panel():
    """Main panel."""
    list_users = auth.load_database()

    while True:
        print("=" * 50)
        print("      Bienvenido al Simulador de Cajero Automático      ")
        print("=" * 50)
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Recuperar PIN")
        print("4. Salir")
        print("=" * 50)

        option = input("Seleccione una opción: ").strip()

        if option == "1":
            # --- Lógic of Login ---
            print("\n--- Iniciar Sesión ---")
            username = input("Usuario: ").strip()

            # 1. Buscamos al usuario primero para verificar bloqueos
            user = auth.get_user_by_username(list_users, username)

            if user and user.get("failed_attempts", 0) >= 3:
                print(f"\n[!] CUENTA BLOQUEADA. Ha excedido el número de intentos.")
                print(
                    "Por favor, utilice la opción 'Recuperar PIN' para desbloquearla."
                )
                continue

            pin = input("PIN: ").strip()

            # Validamos que el PIN sea un número
            if not pin.isdigit():
                print("\n[!] Error: El PIN debe ser numérico.")
                continue

            # 2. Verificamos credenciales
            if user and auth.check_pin(user, pin):
                # Resetear intentos fallidos al ingresar correctamente
                if user.get("failed_attempts", 0) > 0:
                    user["failed_attempts"] = 0
                    auth.save_database(list_users)

                # Delegamos la sesión a la nueva función
                user_session_loop(user, list_users)

            else:
                # Manejo de error y bloqueo
                if user:
                    attempts = user.get("failed_attempts", 0) + 1
                    user["failed_attempts"] = attempts
                    auth.save_database(list_users)
                    print(f"\n[!] PIN incorrecto. Intentos fallidos: {attempts}/3")
                else:
                    print("\n[!] Usuario o PIN incorrecto.")
        elif option == "2":
            # --- Lógica de Registro ---
            print("\n--- Registro de Nuevo Usuario ---")
            username = input("Crea un nombre de usuario: ").strip()
            try:
                dni = int(input("DNI: "))
            except ValueError:
                print("\n[!] Error: El DNI debe ser numérico.")
                continue
            if auth.verify_user(list_users, username, dni):
                print("\n[!] Error: Ya existe un usuario con ese nombre o DNI.")
                continue

            pin = input("Crea un PIN de 4 dígitos: ").strip()
            if not pin.isdigit() or len(pin) != 4:
                print("\n[!] Error: El PIN debe ser una cadena numérica de 4 dígitos.")
                continue

            n_account = random.randint(100000, 999999)
            auth.register_user(
                list_users, username, dni, pin, n_account, saldo=0
            )  # Pasamos el PIN como string
            auth.save_database(list_users)
            print(f"\n¡Usuario '{username}' registrado con éxito!")
            print(f"Tu número de cuenta es: {n_account}")

        elif option == "3":
            # --- Lógica de Recuperación de PIN ---
            print("\n--- Recuperación de PIN ---")
            username = input("Ingrese su usuario: ").strip()
            try:
                dni = int(input("Ingrese su DNI: "))
            except ValueError:
                print("\n[!] Error: El DNI debe ser numérico.")
                continue

            print("\n[!] Recuerde que el PIN debe ser numérico de 4 dígitos.")

            new_pin = input("Ingrese su nuevo PIN (4 dígitos): ").strip()
            if not new_pin.isdigit() or len(new_pin) != 4:
                print("\n[!] Error: El PIN debe ser numérico de 4 dígitos.")
                continue

            if auth.reset_pin(list_users, username, dni, new_pin):
                auth.save_database(list_users)
                print("\n¡PIN actualizado con éxito! Ahora puede iniciar sesión.")
            else:
                print(
                    "\n[!] Error: Usuario o DNI incorrectos. No se pudo restablecer el PIN."
                )

        elif option == "4":
            print("¡Hasta luego!")
            break
        else:
            print("\n[!] Opción no válida. Por favor, elija una opción del menú.")


if __name__ == "__main__":
    main_panel()
