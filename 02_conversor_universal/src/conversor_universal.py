
def km_to_miles(km: float) -> float:
    """
    Docstring for km_to_miles
    
    :param km: Description
    :type km: float
    :return: Description
    :rtype: float
    """    
     
    return km * 0.621371

def miles_to_km(miles: float) -> float:
    """
    Docstring for miles_to_km
    
    :param miles: Description
    :type miles: float
    :return: Description
    :rtype: float
    """
    
    return miles * 1.60934

def kg_to_pounds(kg: float) -> float:
    """
    Docstring for kg_to_pounds
    
    :param kg: Description
    :type kg: float
    :return: Description
    :rtype: float
    """
    return kg * 2.20462

def pounds_to_kg(pounds: float) -> float:
    """
    Docstring for pounds_to_kg
    
    :param pounds: Description
    :type pounds: float
    :return: Description
    :rtype: float
    """
    return pounds * 0.453592

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Docstring for celsius_to_fahrenheit
    
    :param celsius: Description
    :type celsius: float
    :return: Description
    :rtype: float
    """
    return (celsius * 1.8) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Docstring for fahrenheit_to_celsius
    
    :param fahrenheit: Description
    :type fahrenheit: float
    :return: Description
    :rtype: float
    """
    return (fahrenheit - 32) / 1.8

def option_main():
    """
    Docstring for option_main
    
    :return: Description
    :rtype: str
    """
    while True:
        try:
            print("\n" + "=" * 50)
            print("Conversor de unidades")
            print("=" * 50)
            print("1. Kilometros a millas")
            print("2. Millas a kilometros")
            print("3. Kilogramos a libras")
            print("4. Libras a kilogramos")
            print("5. Celsius a Fahrenheit")
            print("6. Fahrenheit a Celsius")
            print("7. Salir")

            option = input("Seleccione una opcion: ")
        except ValueError:
            print("Opcion no valida ingrese nuevamente...")    

        return option

def execution_menu(option):
    """
    Docstring for ejecution_main
    
    :param option: Description
    """
    # 1. First check if the user wants to exit
    if option == "7":
        print("Saliendo...")
        return False
    # 2. Check if the option is valid
    if option not in ["1", "2", "3", "4", "5", "6"]:
        print("Opcion no valida ingrese nuevamente...")
        return True
    # 3. SAFE ZONE: ask for the value to convert
    try:
        value = float(input("Ingrese el valor a convertir: "))

        # 4. Check if the value is valid in mass and distance
        if option in ["1", "2", "3", "4"] and value < 0:
            print("Error: La distancia y la masa no pueden ser negativas")
            return True # RETURN to the menu without doing the calculation

        if option == "1":
            print("-" * 50)
            print("Kilometros a millas")
            print("-" * 50)
            print(f"{value} kilometros equivale a {km_to_miles(value):.2f} millas")
        elif option == "2":
            print("-" * 50)
            print("Millas a kilometros")
            print("-" * 50)
            print(f"{value} millas equivale a {miles_to_km(value):.2f} kilometros")
        elif option == "3":
            print("-" * 50)
            print("Kilogramos a libras")
            print("-" * 50)
            print(f"{value} kilogramos equivale a {kg_to_pounds(value):.2f} libras")
        elif option == "4":
            print("-" * 50)
            print("Libras a kilogramos")
            print("-" * 50)
            print(f"{value} libras equivale a {pounds_to_kg(value):.2f} kilogramos")
        elif option == "5":
            print("-" * 50)
            print("Celsius a Fahrenheit")
            print("-" * 50)
            print(f"{value} °C equivale a {celsius_to_fahrenheit(value):.2f} °F")
        elif option == "6":
            print("-" * 50)
            print("Fahrenheit a Celsius")
            print("-" * 50)
            print(f"{value} °F equivale a {fahrenheit_to_celsius(value):.2f} °C")
    except ValueError:
        print("¡Error! Ingrese un valor numerico válido (ej: 10 o 10.3)")
    
    return True
    


def main():
    while True:
        option = option_main()
        if not execution_menu(option):
            break