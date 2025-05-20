from asymmetric_encryption import AsymmetricEncryption
from file_module import *
from symmetric_encryption import SymmetricEncryption


class HybridCryptoSystem:
    def __init__(self, key_size: int):
        """
        Class initialization
        """
        self.asym_encryptor = AsymmetricEncryption()
        self.sym_encryptor = SymmetricEncryption(key_size)


    def generate_keys(self, private_path: str, public_path: str) -> tuple:
        """
        Generate keys and save them
        :param private_path: path to private key
        :param public_path: path to public key
        :return: tuple of serialized keys
        """
        private_key, public_key = self.asym_encryptor.generate_keys()
        self.asym_encryptor.serialize_private_key(private_key, private_path)
        self.asym_encryptor.serialize_public_key(public_key, public_path)
        return private_key, public_key
    

    def encrypt_file(self, input_path: str,
                    public_path: str, encrypted_path: str) -> None:
        """
        Encrypt file and save it
        :param input_path: path to plain text
        :param public_path: path to public key
        :param encrypted_path: path to encrypted text
        """
        symmetric_key = self.sym_encryptor.generate_key()
        encrypted_key = self.asym_encryptor.encrypt(symmetric_key, public_path)

        plain_text = read_file(input_path)
        cipher_text = self.sym_encryptor.encrypt(plain_text, symmetric_key)

        write_file(encrypted_path, encrypted_key + cipher_text)


    def decrypt_file(self, encrypted_path: str,
                    private_path: str) -> bytes:
        """
        Decrypt encrypted file
        :param encrypted_path: path to encrypted text
        :param private_path: path to private key
        :return: data of encrypted file
        """
        data = read_file(encrypted_path)

        encrypted_key = data[:256]
        cipher_text = data[256:]

        symmetric_key = self.asym_encryptor.decrypt(encrypted_key, private_path)
        decrypted_text = self.sym_encryptor.decrypt(cipher_text, symmetric_key)
        return decrypted_text