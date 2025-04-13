from file_processing import *
from task_1.vigenere import encrypt_vigenere, decrypt_vigenere
from task_2.monoalph_processing import calculate_frequencies, compare_freq, apply_mappings


def task1(utils_data: dict) -> None:
    """
    Encrypting and decrypting by vigenere cipher
    :param utils_data: Dictionary with pathes to files
    """
    try:
        alph_path = utils_data["alphabet"]["path"]
        key_path = utils_data["key"]["path"]
        input_path = utils_data["plain_text"]["path"]
        output_path = utils_data["encrypted_text"]["path"]

        alphabet = load_json_data(alph_path)["alphabet"]
        key = load_json_data(key_path)["key"]

        plain_text = read_text(input_path)
        encrypted_text = encrypt_vigenere(plain_text, key, alphabet)
        write_to_file(output_path, encrypted_text)
        decrypted_text = decrypt_vigenere(encrypted_text, key, alphabet)

        if plain_text != decrypted_text:
            raise ValueError("Decripted text not equal plain text")
        
    except FileNotFoundError as e:
        print(f"Error: file didn't found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error while processing JSON: {e}")
    except OSError as e:
        print(f"Error while file-working: {e}")
    except Exception as e:
        print(f"Error: {e}")
        

def task2(utils_data: dict) -> None:
    """
    Encrypting and decrypting by monoalph_processing
    :param utils_data: Dictionary with pathes to files
    """
    try:
        encrypt_path = utils_data["encrypted_text"]["path"]
        decrypt_path = utils_data["decrypted_text"]["path"]
        ru_freq_path = utils_data["ru_freq"]["path"]
        encrypted_freq_path = utils_data["encrypted_freq"]["path"]
        mappings_path = utils_data["mappings"]["path"]

        ru_freq = load_json_data(ru_freq_path)["ru_freq"]

        encrypted_text = read_text(encrypt_path)
        encrypted_freq = calculate_frequencies(encrypted_text)
        write_json_data(encrypted_freq, encrypted_freq_path)
        mappings = compare_freq(encrypted_freq, ru_freq)
        write_json_data(mappings, mappings_path)
        decrypted_text = apply_mappings(encrypted_text, mappings)
        write_to_file(decrypt_path, decrypted_text)
                
    except FileNotFoundError as e:
        print(f"Error: file didn't found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error while processing JSON: {e}")
    except OSError as e:
        print(f"Error while file-working: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        utils_data1 = load_json_data("utils.json").get("task_1")
        task1(utils_data1)
        utils_data2 = load_json_data("utils.json").get("task_2")
        task2(utils_data2)
                
    except FileNotFoundError as e:
        print(f"Error: file didn't found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error while processing JSON: {e}")
    except OSError as e:
        print(f"Error while file-working: {e}")
    except Exception as e:
        print(f"Error: {e}")