import unittest
import sys
import os

# Add the 'src' directory to the system path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.cypher import encrypt_message, decrypt_message


class TestCaesarCipher(unittest.TestCase):
    """
    Unit tests for the Caesar Cipher logic (Project 07).
    These tests cover the scenarios defined in 'docs/especificaciones.md'.
    """

    def test_encrypt_basic_shift(self):
        """
        Test Case 1: Basic Encryption.
        Input: 'HOLA', Shift: 1
        Expected Output: 'IPMB'
        Description: Simple shift of +1 for uppercase letters.
        """
        message = "HOLA"
        shift = 1
        expected_result = "IPMB"
        self.assertEqual(encrypt_message(message, shift), expected_result)

    def test_encrypt_wrap_around(self):
        """
        Test Case 2: Wrap-around Encryption.
        Input: 'Z', Shift: 1
        Expected Output: 'A'
        Description: Verifies that the cipher correctly wraps from Z back to A.
        """
        message = "Z"
        shift = 1
        expected_result = "A"
        self.assertEqual(encrypt_message(message, shift), expected_result)

    def test_decrypt_basic_shift(self):
        """
        Test Case 3: Basic Decryption.
        Input: 'IPMB', Shift: 1
        Expected Output: 'HOLA'
        Description: Verifies that decrypting returns the original message (Inverse operation).
        """
        encrypted_message = "IPMB"
        shift = 1
        expected_result = "HOLA"
        self.assertEqual(decrypt_message(encrypted_message, shift), expected_result)

    def test_encrypt_mixed_content(self):
        """
        Test Case 4: Mixed Content (Special characters and numbers).
        Input: 'Python 3.12', Shift: 2
        Expected Output: 'Ravjqp 3.12'
        Description: Verifies that numbers, spaces, and punctuation are ignored, while case is preserved.
        """
        message = "Python 3.12"
        shift = 2
        expected_result = "Ravjqp 3.12"
        self.assertEqual(encrypt_message(message, shift), expected_result)


if __name__ == "__main__":
    unittest.main()
