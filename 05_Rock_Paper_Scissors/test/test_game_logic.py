import unittest
import sys
import os
from unittest.mock import patch

# Search for the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.game_logic import (winner, turn_user)

class TestGameLogic(unittest.TestCase):

    # 1. Test win user
    def test_user_win(self):
        
        """
        Test that user wins the round when user chooses "piedra" and cpu chooses "tijera".
        """
        self.assertEqual(winner("piedra", "tijera"), "user")

    # 2. Test win cpu
    def test_cpu_win(self):
        
        """Test that cpu wins the round."""
        self.assertEqual(winner("papel", "tijera"), "cpu")

    # 3. Test tie
    def test_tie(self):
        
        """Test a tie between user and cpu."""
        self.assertEqual(winner("piedra", "piedra"), "tie")

    # 4. Test user input
    @patch('builtins.input', side_effect=["roca", "piedra"])
    def test_user_input(self, mock_input):
        """Test that user input is valid."""
        result = turn_user()
        self.assertEqual(result, "piedra")
        
        

