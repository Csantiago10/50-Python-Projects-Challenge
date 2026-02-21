import json
import os
import hashlib

# Define la ruta absoluta al archivo de la base de datos
DB_PATH = os.path.join(os.path.dirname(__file__), "../docs/users.json")


def _hash_pin(pin: str) -> str:
    """Hashea un PIN usando SHA-256 para almacenamiento seguro."""
    pin_bytes = pin.encode("utf-8")
    return hashlib.sha256(pin_bytes).hexdigest()


def format_balance(amount: int) -> str:
    """Formatea un monto numérico a formato moneda (Latam)."""
    standard_format = "{:,.2f}".format(amount)
    latam_format = standard_format.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"${latam_format}"


def load_database():
    """
    Docstring for load_database
    Loads the database from a JSON file
    """
    try:
        with open(DB_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(
            f"\n[!] Advertencia: El archivo de base de datos está corrupto o tiene un formato inválido."
        )
        print("[!] Se iniciará con una base de datos vacía para evitar errores.")
        return []


def verify_user(list_users: list, username: str, dni: int) -> bool:
    for user in list_users:
        if user["DNI"] == dni or user["username"] == username:
            return True
    return False


def register_user(
    list_users: list, username: str, dni: int, pin: str, n_account: int, saldo: int
) -> dict:
    """Crea un nuevo usuario y lo añade a la lista."""
    new_user = {
        "username": username,
        "DNI": dni,
        "pin": _hash_pin(pin),  # Guardamos el PIN hasheado
        "n_account": n_account,
        "saldo": saldo,
        "saldo_str": format_balance(saldo),
        "failed_attempts": 0,
    }
    list_users.append(new_user)

    return new_user


def login_user(list_users, username: str, pin: str) -> dict:
    """Busca un usuario por nombre y PIN, y lo devuelve si lo encuentra."""
    hashed_pin_attempt = _hash_pin(pin)
    for user in list_users:
        if user["username"] == username and user["pin"] == hashed_pin_attempt:
            return user
    return None


def get_user_by_username(list_users: list, username: str) -> dict | None:
    """Busca y devuelve un usuario por su nombre de usuario."""
    for user in list_users:
        if user["username"] == username:
            return user
    return None


def check_pin(user: dict, pin: str) -> bool:
    """Verifica si el PIN ingresado coincide con el del usuario."""
    return user["pin"] == _hash_pin(pin)


def reset_pin(list_users: list, username: str, dni: int, new_pin: str) -> bool:
    """Busca un usuario por nombre y DNI, y actualiza su PIN."""
    for user in list_users:
        if user["username"] == username and user["DNI"] == dni:
            user["pin"] = _hash_pin(new_pin)
            user["failed_attempts"] = 0
            return True
    return False


def save_database(list_users):
    """Guarda la lista completa de usuarios en el archivo JSON."""
    # Aseguramos que el directorio exista antes de guardar
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with open(DB_PATH, "w") as file:
        json.dump(list_users, file, indent=4)
