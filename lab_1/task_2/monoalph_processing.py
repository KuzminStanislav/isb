from collections import Counter


def calculate_frequencies(cipher_text: str) -> dict[str, float]:
    """
    Count frequency of any symbol
    :param cipher_text: Decrypted text
    :return: Frequency dictionary
    """
    try:
        freqs = {}
        cipher_text = cipher_text.replace(" ", "")
        for char in cipher_text:
            match char in freqs:
                case True:
                    freqs[char] += 1
                case False:
                    freqs[char] = 1
        total_lenght = sum(freqs.values())
        for char in freqs:
            freqs[char] /= total_lenght
        return freqs
    except Exception as e:
        raise ValueError(f"Error while counting frequencies: {e}")
    

def sort_dict(dict: dict[str, float], reverse: bool) -> dict:
    """
    Sort dictionary
    :param dict: Dictionary
    :param reverse: Order flag of reversing
    :return: Sorted dictionary
    """
    return sorted(dict.items(), key = lambda item: item[1], reverse = reverse)


def compare_freq(encrypted_freq: dict[str, float], ru_freq: dict[str, float]) -> dict:
    """
    Compare frequencies from encrypted and etalon russian dictionaries
    :param encrypted_freq: Dictionary with encrypted frequencies
    :param ru_freq: Dictionary with etalon russian frequencies
    :return: Dictionary of mappings of symbol changes 
    """
    try:
        sort_encrypted = sort_dict(encrypted_freq, reverse = True)
        sort_etalon = sort_dict(ru_freq, reverse = True)
        mappings = {}
        for encrypted_char, _ in sort_encrypted[:len(sort_etalon)]:
            mappings[encrypted_char] = sort_etalon[len(mappings)][0]
        return mappings
    except Exception as e:
        raise RuntimeError(f"Error while comparing: {e}")
    

def apply_mappings(text: str, mappings: dict[str, str]) -> str:
    """
    Apply mappings of symbol changes in text
    :param text: Encrypted Text
    :param mappings_path: Path to JSON-file 
    :return: Decrypted text
    """
    try:
        translation_table = str.maketrans(mappings)
        return text.translate(translation_table)
    except Exception as e:
        raise RuntimeError(f"Error while changes: {e}")