
def encrypt_message(message: str , shift: int) -> str:
    """
    Encrypt message with the method of the caesar cipher
        
    :param message: Description
    :param shift: Description
    :return: Description
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha(): # check if the value is a letter
            if char.isupper(): # check if the value is in mayus
                # A = 65 and Z = 90 for ASCII values in mayus 
                encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                # a = 97 and z = 122 for ASCII values in minus
                encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # value is not a letter and should not be encrypted
            encrypted_message += char

    return encrypted_message

def decrypt_message(message: str , shift: int) -> str:
    """
    Decrypt message with the method of the caesar cipher
        
    :param message: Description
    :param shift: Description
    :return: Description
    """
    return encrypt_message(message, -shift)
    
