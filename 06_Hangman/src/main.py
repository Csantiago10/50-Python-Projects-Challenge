import hangman_logic as hl
import random


def start_game() -> None:

    print("=" * 50)
    print("            Bienvenido al juego del ahorcado!")
    print("=" * 50)

    # 1. Declare the variables for the game
    secret_word = random.choice(hl.BANK_WORDS)
    current_board = ["_"] * len(secret_word)
    lives = 6

    letter_used = set()

    while True:

        # 2. Show the board
        print(f" Progreso de la palabra: {current_board}")

        # 3. Get the letter from the user
        letter = input("Ingrese una letra: ").strip()

        if len(letter) != 1:
            print("Solo puedes ingresar una letra")
            continue

        if not letter.isalpha():
            print("Solo puedes ingresar letras")
            continue

        letter = letter.lower()

        # 4. check if the letter is used
        if letter in letter_used:
            print("Ya usaste esa letra, no pierdes vidas")
            continue

        # 5. if check letter no used add the letter to the set
        letter_used.add(letter)
        # 6. check if the letter is in the word
        board, found_new = hl.search_letter_in_word(letter, secret_word, current_board)
        # 7. update the board
        if found_new is True:
            print("Adivinaste una letra!")
            current_board = board
            print(f"Te quedan {lives} vidas")
        else:
            # 8. if the letter is not in the word, lose a life
            lives -= 1
            print(f"Te quedan {lives} vidas")

        # 9. check if the game is over
        if lives == 0:
            print(f"Perdiste la palabra era: {secret_word}")
            print("Game Over")
            break
        # 10. check if the game is won
        if "_" not in current_board:
            word_win = " ".join(current_board)
            print("-" * 50)
            print(f"\nAdivinaste la palabra: {secret_word}")
            print(f"Tu resultado es: {word_win}")
            print("Ganaste")
            print("-" * 50)
            break


if __name__ == "__main__":

    start_game()
