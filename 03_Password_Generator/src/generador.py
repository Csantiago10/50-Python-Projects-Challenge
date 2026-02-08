import string
import random


def construir_pool(minis: str, mayus: str, nums: str, simb: str) -> str:
    """
    Construye el conjunto de caracteres permitidos.
    """
    # 1. Creamos un string vacío
    pool = ""

    # 2. Agregamos ingredientes según lo que pida el usuario
    if minis == "S":
        pool += string.ascii_lowercase
    if mayus == "S":
        pool += string.ascii_uppercase
    if nums == "S":
        pool += string.digits
    if simb == "S":
        pool += string.punctuation

    return pool


def generar_password(config: dict) -> str:
    """
    Recibe un diccionario con configuración y devuelve la contraseña.
    config = {'longitud': 10, 'pool': 'abc...'}
    """
    # 1. Sacamos los datos de la caja (diccionario)
    longitud = config["longitud"]
    pool = config["pool"]

    # 2. Validación de seguridad (por si la longitud es 0 o negativa)
    if longitud <= 0:
        return ""

    # 3. Generación OPTIMIZADA (List Comprehension)
    # Elegimos 'longitud' veces un caracter al azar del 'pool'
    lista_caracteres = random.choices(pool, k=longitud)

    # 4. Unimos la lista en un texto
    password = "".join(lista_caracteres)

    return password
