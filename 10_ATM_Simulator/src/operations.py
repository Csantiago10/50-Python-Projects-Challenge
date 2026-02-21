import auth
import datetime
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "../docs")


def save_receipt(user: dict, amount: int, type_op: str):
    """Genera un archivo de texto con el detalle de la operación."""
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"recibo_{user['username']}.txt"
    file_path = os.path.join(DOCS_DIR, filename)

    content = (
        f"=================================\n"
        f"       COMPROBANTE DE CAJERO     \n"
        f"=================================\n"
        f"Fecha:   {date}\n"
        f"Cliente: {user['username']}\n"
        f"Cuenta:  {user['n_account']}\n"
        f"---------------------------------\n"
        f"Tipo:    {type_op}\n"
        f"Monto:   {auth.format_balance(amount)}\n"
        f"Saldo:   {user['saldo_str']}\n"
        f"=================================\n"
    )

    os.makedirs(DOCS_DIR, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"\n[i] Recibo guardado en '{filename}'")


def check_balance(user: dict) -> str:
    """Formatea y devuelve el saldo del usuario."""
    return auth.format_balance(user["saldo"])


def deposit_money(user: dict, deposit: int) -> dict | bool:
    """
    Añade dinero al saldo de un usuario específico.
    Devuelve el usuario actualizado o False si el monto es inválido.
    """
    if deposit <= 0:
        print("\n[!] Error: El monto a depositar debe ser positivo.")
        return False

    user["saldo"] += deposit
    user["saldo_str"] = auth.format_balance(user["saldo"])
    return user


def withdraw_money(user: dict, withdraw: int) -> dict | bool:
    """
    Resta dinero del saldo de un usuario específico.
    Devuelve el usuario actualizado o False si no hay fondos suficientes.
    """
    if withdraw <= 0:
        print("\n[!] Error: El monto a retirar debe ser positivo.")
        return False
    if withdraw > user["saldo"]:
        print("\n[!] Error: No tienes fondos suficientes.")
        return False

    user["saldo"] -= withdraw
    user["saldo_str"] = auth.format_balance(user["saldo"])
    save_receipt(user, withdraw, "RETIRO")
    return user
