def shift_char_encrypt(char: str, shift: int, alphabet: str) -> str:
    """
    Shift symbol while encrypting
    :param char: Shifting symbol
    :param shift: Shifting value
    :param alphabet: Alphabet to encrypting
    :return: New symbol after shifting
    """
    if not char.isalpha():
        return char
    
    char_upper = char.upper()
    if char_upper not in alphabet:
        raise ValueError(f"Character '{char}' not found in alphabet.")
    position = alphabet.index(char_upper)
    new_position = (position + shift) % len(alphabet)
    encrypted_char = alphabet[new_position]
    return encrypted_char if char.isupper() else encrypted_char.lower()


def encrypt_vigenere(plain_text: str, key: str, alphabet: str) -> str:
    """
    Vigenere encrypting
    :param plain_text: Plain text
    :param key: Key for encrypting
    :param alphabet: Alphabet to encrypting
    :return: Encrypted text
    """
    cipher_text = []
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            key_char = key[key_index % len(key)].upper()
            shift = alphabet.index(key_char)
            new_position = (alphabet.index(char.upper()) + shift) % len(alphabet)
            cipher_text.append(alphabet[new_position] if char.isupper() else alphabet[new_position].lower())
            key_index += 1
        else:
            cipher_text.append(char)
    return ''.join(cipher_text)


def shift_char_decrypt(char: str, shift: int, alphabet: str) -> str:
    """
    Shift symbol while decrypting
    :param char: Shifting symbol
    :param shift: Shifting value
    :param alphabet: Alphabet to decrypting
    :return: New symbol after shifting
    """
    if not char.isalpha():
        return char
    
    char_upper = char.upper()
    if char_upper not in alphabet:
        raise ValueError(f"Character '{char}' not found in alphabet.")
    position = alphabet.index(char_upper)
    new_position = (position - shift + len(alphabet)) % len(alphabet)
    decrypted_char = alphabet[new_position]
    return decrypted_char if char.isupper() else decrypted_char.lower()


def decrypt_vigenere(cipher_text: str, key: str, alphabet: str) -> str:
    """
    Vigenere decrypting
    :param cipher_text: Text after encrypting
    :param key: Key for decrypting
    :param alphabet: Alphabet to decrypting
    :return: Decrypted text
    """
    plain_text = []
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            key_char = key[key_index % len(key)].upper()
            shift = alphabet.index(key_char)
            new_position = (alphabet.index(char.upper()) - shift) % len(alphabet)
            plain_text.append(alphabet[new_position] if char.isupper() else alphabet[new_position].lower())
            key_index += 1
        else:
            plain_text.append(char)
    return ''.join(plain_text)