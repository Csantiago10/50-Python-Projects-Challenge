import game_logic as gc
def start_game():
    print("=" * 50)
    print("                 Papel, Piedra o Tijera")
    print("=" * 50)
    print("Reglas.")
    print("* El primero en llegar a 2 puntos gana.")
    print("-" * 50)

    points_user = 0
    points_cpu = 0
    points_victory = 2


    # 1. Start the game
    print("\nComienza el juego...")

    # 2. Play the game
    while True:
        try:
            user_option = gc.turn_user()
            cpu_option = gc.turn_cpu()

            print(f"El usuario eligio: {user_option}")
            print(f"La CPU eligio: {cpu_option}")

            winner = gc.winner(user_option, cpu_option)
            print(f"El ganador es: {winner}")

            if winner == "user":
                points_user += 1
            elif winner == "cpu":            
                points_cpu += 1


            print(f"Santiago: {points_user} - CPU: {points_cpu}")
            # 3. End the game
            if  points_user == points_victory:
                print("Santiago gana la partida")
                break
            elif points_cpu == points_victory:
                print("La CPU gana la partida")
                break
        except ValueError:
            print("Opcion no valida ingrese nuevamente...")

if __name__ == "__main__":
    start_game()
            


    
    

