from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


from file_module import FileProcessor
from serialization import KeyProcessor


class AsymmetricEncryption:
    def __init__(self):
        """
        Class initialization
        """
        self.file_proc = FileProcessor()
        self.serializor = KeyProcessor(self.file_proc)
        self.settings = self.file_proc.read_json("settings.json")
        self.rsa_key_size: int = self.settings["rsa_key_size"]
        self.public_exponent: int = self.settings["public_exponent"]


    def generate_keys(self) -> tuple:
        """
        Generate RSA keys
        :return: tuple of pair RSA keys
        """
        private_key = rsa.generate_private_key(
            public_exponent = self.public_exponent,
            key_size = self.rsa_key_size,
            backend = default_backend())
        public_key = private_key.public_key()
        return private_key, public_key
    

    def serialize_private_key(self, private_key, key_path: str) -> None:
        """
        Serialization of private key
        :param private_key: private key
        :param key_path: path to private key
        """
        if not key_path or not isinstance(key_path, str):
            raise ValueError("Key path must not be empty string!")
        self.serializor.serialize_private(
            private_key, key_path)


    def serialize_public_key(self, public_key, key_path: str) -> None:
        """
        Serialization of public key
        :param public_key: public key
        :param key_path: path to public key
        """
        if not key_path or not isinstance(key_path, str):
            raise ValueError("Key path must not be empty string!")
        self.serializor.serialize_public(
            public_key, key_path)


    def encrypt(self, symmetric_key: bytes, key_path: str) -> bytes:
        """
        Encrypt symmetric key with public RSA
        :param symmetric_key: symmetric key
        :param key_path: path to public key
        :return: encrypted key
        """
        if not isinstance(symmetric_key, bytes) or len(symmetric_key) == 0:
            raise ValueError("Symmetric key must not be empty!")
        public_key = self.serializor.load_public_key(key_path)
        encrypted_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf = padding.MGF1(algorithm = hashes.SHA256()),
                algorithm = hashes.SHA256(),
                label = None)
        )
        return encrypted_key
    

    def decrypt(self, encrypted_key: bytes, key_path: str) -> bytes:
        """
        Decrypt symmetric key with private RSA
        :param encrypted_key: encrypted key
        :param key_path: path to private key
        :return: decrypted data
        """
        if not isinstance(encrypted_key, bytes) or len(encrypted_key) == 0:
            raise ValueError("Symmetric key must not be empty!")
        private_key = self.serializor.load_private_key(key_path)
        symmetric_key = private_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf = padding.MGF1(algorithm = hashes.SHA256()),
                algorithm = hashes.SHA256(),
                label = None)
        )
        return symmetric_key