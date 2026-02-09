import words_counter

def start_program():
    """
    Docstring for start_program
    """
    # 1. Type the text
    text = input("Ingrese un texto: ")
    # 2. Clean the text
    cant_words = words_counter.word_counter(text)
    # 3. Count the frequency
    frequency_words = words_counter.frequency_counter(text)
    # 4. Sort the frequency
    top3_words = words_counter.frequency_sorter(frequency_words)

    print("=" * 50)
    print("                 RESULTADOS ")
    print("=" * 50)

    print("\n" +"-" * 50)
    print(" Cantidad de palabras. ")
    print("-" * 50)
    print(cant_words) 

    print("\n" +"-" * 50)
    print(" Frecuencia de palabras. ")
    print("-" * 50)
    print(frequency_words)

    print("\n" +"-" * 50)
    print(" Palabras con mas frecuencia. ")
    print("-" * 50)
    for word, count in top3_words:
        print(f"{word}: {count}")
    


if __name__ == '__main__':
    start_program()