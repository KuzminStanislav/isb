from cryptography.hazmat.primitives import serialization


from file_module import FileProcessor


class KeyProcessor:
    def __init__(self, file_proc: FileProcessor):
        """
        Class initialization
        """
        self.file_proc = file_proc


    def serialize_private(self, private_key, key_path: str) -> None:
        """
        Serialize and save private key
        :param private_key: private key
        :param key_path: path to private key
        """
        content = private_key.private_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
            )
        self.file_proc.write_file(key_path, content)


    def serialize_public(self, public_key, key_path: str) -> None:
        """
        Serialize and save public key
        :param public_key: public key
        :param key_path: path to public key
        """
        content = public_key.public_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo
            )
        self.file_proc.write_file(key_path, content)


    def load_private_key(self, key_path: str):
        """
        Load private key from file
        :param key_path: path to private key
        """
        content = self.file_proc.read_file(key_path)
        return serialization.load_pem_private_key(
            content, password = None)


    def load_public_key(self, key_path: str):
        """
        Load public key from file
        :param key_path: path to public key
        """
        content = self.file_proc.read_file(key_path)
        return serialization.load_pem_public_key(content)