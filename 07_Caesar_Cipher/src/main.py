import cypher


def start_machine_caesar_cipher():
    print("🔐 --- MÁQUINA ENIGMA (CIFRADO CÉSAR) --- 🔐")

    while True:
        print("\n1. Encriptar mensaje")
        print("2. Desencriptar mensaje")
        print("3. Salir")

        option = input("Elija una opción: ")

        if option == "3":
            print("¡Hasta luego!")
            break

        if not option in ["1", "2"]:
            print("Opción no válida. Por favor, elija una opción válida.")
            continue

        message = input("Ingrese el mensaje a encriptar/desencriptar: ")

        try:
            shift = int(input("Ingrese el desplazamiento (número entero): "))
        except ValueError:
            print("El desplazamiento debe ser un número entero.")
            continue

        if shift < 1 or shift > 25:
            print("El desplazamiento debe estar entre 1 y 25.")
            continue

        if option == "1":
            message_encrypted = cypher.encrypt_message(message, shift)
            print(f"\n🔒 ENCRIPTADO: {message_encrypted}")
        elif option == "2":
            message_decrypted = cypher.decrypt_message(message, shift)
            print(f"\n🔓 DESENCRIPTADO: {message_decrypted}")


if __name__ == "__main__":
    start_machine_caesar_cipher()
