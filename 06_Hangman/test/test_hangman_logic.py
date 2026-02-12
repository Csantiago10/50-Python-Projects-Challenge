import unittest
import sys
import os

# Path for the folder 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import hangman_logic as hl


class TestHangmanLogic(unittest.TestCase):
    def test_change_first_position_of_board(self):
        """
        Test that the function search_letter_in_word changes the first position of the board when the letter is found.

        Args:
            letter (str): The letter to search
            secret_word (str): The secret word
            current_board (list): The current board

        Returns:
            tuple: (current_board, found) where current_board is the updated board and found is a boolean indicating if the letter was found
        """
        letter = "P"
        secret_word = "Python"
        current_board = ["_"] * len(secret_word)
        current_board, found = hl.search_letter_in_word(
            letter, secret_word, current_board
        )
        self.assertEqual(current_board, ["P", "_", "_", "_", "_", "_"])
        self.assertTrue(found)

    def test_error_rest_lifes(self):
        """
        Test that the function search_letter_in_word doesn't change the board when the letter is not found.

        Args:
            letter (str): The letter to search
            secret_word (str): The secret word
            current_board (list): The current board

        Returns:
            tuple: (current_board, found) where current_board is the updated board and found is a boolean indicating if the letter was found
        """
        letter = "z"
        secret_word = "Python"
        lives = 6
        current_board = ["_"] * len(secret_word)
        current_board, found = hl.search_letter_in_word(
            letter, secret_word, current_board
        )

        if not found:
            lives -= 1

        self.assertEqual(current_board, ["_"] * len(secret_word))
        self.assertFalse(found)
        self.assertEqual(lives, 5)

    def test_letter_used(self):
        """
        Docstring for test_letter_used

        :param self: Description
        """
        letter = "P"
        letter_used = set()
        letter_used.add(letter)
        self.assertTrue(letter in letter_used)

    def test_double_hit_in_word(self):
        """
        Test that the function search_letter_in_word correctly handles cases where the letter is found more than once in the word.

        Args:
            letter (str): The letter to search
            secret_word (str): The secret word
            current_board (list): The current board

        Returns:
            tuple: (current_board, found) where current_board is the updated board and found is a boolean indicating if the letter was found
        """
        letter = "A"
        secret_word = "AJA"
        current_board = ["_"] * len(secret_word)
        current_board, found = hl.search_letter_in_word(
            letter, secret_word, current_board
        )
        self.assertEqual(current_board, ["A", "_", "A"])
        self.assertTrue(found)

    def test_win_game(self):
        """
        Test the user win the game when the secret word 'SOL' is guessed.

        :param self: Description
        """
        secret_word = "SOL"
        current_board = ["_"] * len(secret_word)

        for letter in secret_word:
            current_board, found = hl.search_letter_in_word(
                letter, secret_word, current_board
            )

        self.assertEqual(current_board, ["S", "O", "L"])
        self.assertTrue(found)

    def test_lose_game(self):
        """
        Test that the user loses the game after 6 incorrect attempts.
        """
        secret_word = "PYTHON"
        current_board = ["_"] * len(secret_word)
        lives = 6
        wrong_letters = ["A", "B", "C", "D", "E", "F"]

        for letter in wrong_letters:
            current_board, found = hl.search_letter_in_word(
                letter, secret_word, current_board
            )
            if not found:
                lives -= 1

        self.assertEqual(lives, 0)


if __name__ == "__main__":
    unittest.main()
