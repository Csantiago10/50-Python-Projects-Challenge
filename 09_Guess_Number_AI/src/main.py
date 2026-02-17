import game


def panel():

    print("=" * 50)
    print("                     Juego de Adivinanza")
    print("=" * 50)
    print("* Piensa un número entre 1 y 100")
    print("* Lo adivinaré en menos de 7 intentos")
    print("* Responde a mis suposiciones con: ")
    print("     'A' -> Si TU número es más ALTO que mi suposición.")
    print("     'B' -> Si TU número es más BAJO que mi suposición.")
    print("     'C' -> Si mi suposición es CORRECTA.")
    print("=" * 50)

    # Initialize state variables
    limite_inferior = game.LIMITE_INFERIOR
    limite_superior = game.LIMITE_SUPERIOR
    attempts = 0

    while True:
        # 1. Verify trap (impossible range)
        if game.check_trap(limite_inferior, limite_superior):
            print("\n[!] Error: ¡Estás haciendo trampa! El rango es imposible.")
            break

        # 2. Calculate prediction
        prediction = game.number_estimate(limite_inferior, limite_superior)
        attempts += 1

        # 3. Interaction
        print(f"\n>> Intento #{attempts}: ¿Es {prediction} tu número?")
        respuesta = input("   Tu respuesta (A/B/C): ").upper().strip()

        # 4. Update logic
        if respuesta == "C":
            print(f"\n¡Genial! He adivinado tu número en {attempts} intentos.")
            break
        elif respuesta == "A":
            limite_inferior = game.upper_estimate(prediction)
        elif respuesta == "B":
            limite_superior = game.lower_estimate(prediction)
        else:
            print("   [!] Opción no válida. Usa A, B o C.")
            attempts -= 1


if __name__ == "__main__":
    panel()
