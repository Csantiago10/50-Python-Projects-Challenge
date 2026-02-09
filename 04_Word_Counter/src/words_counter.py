import string


def clean_text(text : str) -> list:
    """
    Docstring for clean_text
    
    :param text: Description
    :type text: str
    :return: Description
    :rtype: list
    """

    # 1. Clean the text
    text =text.lower()
    # 2. Remove punctuation
    table_to_remove_punctuation = str.maketrans('', '', string.punctuation)
    # 3. Split the text
    return text.translate(table_to_remove_punctuation).split()

def word_counter(text : str) -> int:
    """
    Docstring for word_counter
    
    :param text: Description
    :type text: str
    :return: Description
    :rtype: int
    """

    # 1. Clean the text
    words = clean_text(text)
    return len(words)  


def frequency_counter(text : str) -> dict:
    """
    Docstring for frequency_counter
    
    :param text: Description
    :type text: str
    :return: Description
    :rtype: dict
    """

    # 1. Clean the text
    words = clean_text(text)
    
    frequency = {}
    # 2. Count the frequency
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

def frequency_sorter(frequency : dict) -> list:
    """
    Docstring for frequency_sorter
    
    :param frequency: Description
    :type frequency: dict
    :return: Description
    :rtype: list
    """
    list_frequency = []
    # 1. Transform the dictionary into a list
    for key, value in frequency.items():
        list_frequency.append((key, value))
    # 2. Sort the list
    list_frequency.sort(reverse=True, key=lambda x: x[1])
    

    return list_frequency[:3]


