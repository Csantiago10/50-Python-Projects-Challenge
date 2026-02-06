def obtener_lista_numeros() -> str:
    numeros_desordenador = input(
        "Ingrese una lista de números desordenador y mezclado separador por comas: "
    )

    lista_numeros = numeros_desordenador.split(",")
    return lista_numeros


def obtener_listas_par_impar(lista_numeros: list) -> list:

    lista_pares = []
    lista_impares = []
    for item in lista_numeros:

        try:
            num = int(item)
            if num % 2 == 0:
                lista_pares.append(num)
            else:
                lista_impares.append(num)
        except ValueError:
            print("Dato incorrecto ingresado en la lista de numeros: {item}")
            continue
    lista_pares.sort()
    lista_impares.sort()

    return lista_pares, lista_impares


def main():
    lista_numeros = obtener_lista_numeros()

    lista_pares, lista_impares = obtener_listas_par_impar(lista_numeros)

    print(f"Los numeros pares son: {lista_pares}")
    print(f"Los numeros impares son: {lista_impares}")
