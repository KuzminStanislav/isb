from cryptography.hazmat.primitives import serialization


from file_module import *


def serialize_private(private_key, key_path: str) -> None:
    """
    Serialize and save private key
    :param private_key: private key
    :param key_path: path to private key
    """
    content = private_key.private_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PrivateFormat.TraditionalOpenSSL)
    write_file(key_path, content)


def serialize_public(public_key, key_path: str) -> None:
    """
    Serialize and save public key
    :param public_key: public key
    :param key_path: path to public key
    """
    content = public_key.public_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PublicFormat.SubjectPublicKeyInfo)
    write_file(key_path, content)


def load_private_key(key_path: str):
    """
    Load private key from file
    :param key_path: path to private key
    """
    content = read_file(key_path)
    return serialization.load_pem_private_key(
        content, password = None)


def load_public_key(key_path: str):
    """
    Load public key from file
    :param key_path: path to public key
    """
    content = read_file(key_path)
    return serialization.load_pem_public_key(content)