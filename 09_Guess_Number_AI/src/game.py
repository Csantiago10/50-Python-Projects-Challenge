# --------------------------------------
# Global variables
# --------------------------------------
LIMITE_INFERIOR = 1
LIMITE_SUPERIOR = 100


# --------------------------------------
# Functions
# --------------------------------------
def number_estimate(limite_inferior: int, limite_superior: int) -> int:
    """Calculates the midpoint of the current range."""
    prediction = (limite_inferior + limite_superior) // 2
    return prediction


def upper_estimate(prediction: int) -> int:
    """If 'High' (A), the number is greater. Returns the new lower limit."""
    return prediction + 1


def lower_estimate(prediction: int) -> int:
    """If 'Low' (B), the number is smaller. Returns the new upper limit."""
    return prediction - 1


def check_trap(limite_inferior: int, limite_superior: int) -> bool:
    """Checks if the range is invalid (cheating)."""
    return limite_inferior > limite_superior
