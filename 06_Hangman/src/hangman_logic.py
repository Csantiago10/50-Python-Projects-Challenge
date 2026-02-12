BANK_WORDS = [
    "python",
    "java",
    "kotlin",
    "javascript",
    "php" "c#",
    "c++",
    "c",
    "html",
    "css",
    "manzana",
    "pera",
    "platano",
    "manzana",
    "parque",
    "ciudad" "perro",
    "gato",
    "elefante",
    "jirafa",
    "mono" "computador",
    "teclado",
    "monitor",
    "raton",
    "mouse",
]


def search_letter_in_word(letter: str, secret_word: str, current_board: list) -> tuple:
    """function to search a letter in a word

    Args:
        letter (str): letter to search
        secret_word (str): secret word
        current_board (list): current board

    Returns:
        list: current board
        bool: True if the letter is in the word, False otherwise
    """
    found = False

    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            current_board[i] = letter
            found = True

    return current_board, found