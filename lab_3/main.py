from file_module import FileProcessor
from hybrid_crypto import HybridCryptoSystem
from parser import *


if __name__ == "__main__":
    args = parse_arguments()
    mode = validate_mode(args)

    try:
        file_proc = FileProcessor()
        settings = file_proc.read_json("settings.json")
        private_path = settings["private_key"]
        public_path = settings["public_key"]
        symmetric_path = settings["symmetric_key"]
        plain_text = settings["plain_text"]
        encrypted_file = settings["encrypted_text"]
        decrypted_file = settings["decrypted_text"]

        crypto = HybridCryptoSystem(key_size = args.key_size)

        match mode:
            case "generate":
                private_key, public_key = crypto.generate_keys(
                    private_path,
                    public_path
                )
            case "encrypt":
                crypto.encrypt_file(
                    input_path = plain_text,
                    public_path = public_path,
                    encrypted_path = encrypted_file,
                    symmetric_path = symmetric_path
                )
            case "decrypt":
                decrypted_text = crypto.decrypt_file(
                    encrypted_path = encrypted_file,
                    private_path = private_path
                )
                file_proc.write_file(decrypted_file, decrypted_text)
    except Exception as e:
        print(f"Error: {e}")
