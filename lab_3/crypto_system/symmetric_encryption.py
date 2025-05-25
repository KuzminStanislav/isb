import os
import secrets


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


from file_module import FileProcessor
from serialization import KeyProcessor


class SymmetricEncryption:
    def __init__(self, key_size: int):
        """
        Class initialization
        """
        self.file_proc = FileProcessor
        self.settings = self.file_proc.read_json("settings.json")
        if key_size not in self.settings["key_size"]:
            raise ValueError("Key length must be 128, 192 or 256!")
        self.key_size: int = key_size // 8


    def generate_key(self) -> bytes:
        """
        Generate symmetric key
        :return: symmetric key
        """
        return secrets.token_bytes(self.key_size)
    

    def encrypt(self, plain_text: bytes, key: bytes) -> bytes:
        """
        Encrypt plain text with symmetric key
        :param plain_text: plain text
        :param key: symmetric key
        """
        iv = os.urandom(16)
        cipher = Cipher(
            algorithms.AES(key),
            modes.CFB(iv),
            backend = default_backend() 
        )
        encryptor = cipher.encryptor()
        cipher_text = iv + encryptor.update(plain_text) + encryptor.finalize()
        return cipher_text
    

    def decrypt(self, cipher_text: bytes, key: bytes) -> bytes:
        """
        Decrypt cipher text with symmetric key
        :param cipher_text: encrypted text
        :param key: symmetric key
        """
        iv = cipher_text[:16]
        cipher = Cipher(
            algorithms.AES(key),
            modes.CFB(iv),
            backend = default_backend()
        )
        decryptor = cipher.decryptor()
        plain_text = decryptor.update(cipher_text[16:]) + decryptor.finalize()
        return plain_text