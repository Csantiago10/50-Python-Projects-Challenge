import random

RULES = {
    "piedra": "tijera",  # rock win to scissors 
    "papel": "piedra",   # paper win to rock
    "tijera": "papel"    # scissors win to paper
}
    
def winner(user : str, cpu : str) -> str:
    """
    Determine the winner of a round of Rock, Paper, Scissors.

    Parameters
    ----------
    user : str
        The user's choice.
    cpu : str
        The computer's choice.

    Returns
    -------
    str
        "tie" if the user and cpu have the same choice,
        "user" if the user wins, and "cpu" if the cpu wins.
    """
    if user == cpu:
        return "Empate"
    elif RULES[user] == cpu:
        return "user"
    else:
        return "cpu"
    
def turn_user():
    """
    Get the user's choice of rock, paper, or scissors.

    Returns
    -------
    str
        The user's choice of rock, paper, or scissors.
    """
    while True:
        user = input("Elige piedra, papel o tijera: ").lower().strip()
        if user in RULES.keys():
            return user
        print("Opción no válida. Por favor, elige piedra, papel o tijera.")



def turn_cpu():
    """
    Get the computer's choice of rock, paper, or scissors.

    Returns
    -------
    str
        The computer's choice of rock, paper, or scissors.
    """
    return random.choice(list(RULES.keys()))

    
