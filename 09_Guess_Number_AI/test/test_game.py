import unittest
import sys
import os

# Adjust path to import src module from tests folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from game import (
    number_estimate,
    upper_estimate,
    lower_estimate,
    check_trap,
)


class TestBinarySearch(unittest.TestCase):

    def test_initial_prediction(self):
        """Initial test: Range 1-100 -> Prediction 50"""
        # Test case: Game start
        # Specification: PC Prediction = 50
        prediction = number_estimate(1, 100)
        self.assertEqual(prediction, 50, "Initial prediction should be 50")

    def test_response_high(self):
        """Test response 'A' (High): Lower limit adjustment"""
        # Test case: User says "A" (High) to prediction 50
        # Specification: New Range [51, 100] -> low = 50 + 1
        prediction = 50
        new_lower = upper_estimate(prediction)
        self.assertEqual(new_lower, 51, "New lower limit should be 51")

    def test_response_low(self):
        """Test response 'B' (Low): Upper limit adjustment"""
        # Test case: User says "B" (Low) to prediction 50
        # Specification: New Range [1, 49] -> high = 50 - 1
        prediction = 50
        new_upper = lower_estimate(prediction)
        self.assertEqual(new_upper, 49, "New upper limit should be 49")

    def test_next_prediction_after_high(self):
        """Test next prediction after 'High' (Range 51-100)"""
        # Test case: Searching for 75. Current range [51, 100]
        # Specification: Prediction = (51 + 100) // 2 = 75
        prediction = number_estimate(51, 100)
        self.assertEqual(prediction, 75, "Prediction for range 51-100 should be 75")

    def test_check_trap_valid(self):
        """Test trap detection: Valid range"""
        # Case: Lower limit <= Upper limit
        is_trap = check_trap(1, 100)
        self.assertFalse(is_trap, "Should not detect trap in valid range (1, 100)")

    def test_check_trap_invalid(self):
        """Test trap detection: Invalid range"""
        # Case: Lower limit > Upper limit (Ex: 51 > 50)
        is_trap = check_trap(51, 50)
        self.assertTrue(is_trap, "Should detect trap when lower > upper")


if __name__ == "__main__":
    unittest.main()
