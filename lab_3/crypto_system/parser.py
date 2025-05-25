import argparse


def parse_arguments() -> tuple:
    """
    Parsing arguments
    :return: tuple of parsed arguments
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen', '--generation', 
                       action='store_true', 
                       help='Started mode of key generation')
    group.add_argument('-enc', '--encryption', 
                       action='store_true', 
                       help='Started encryption mode')
    group.add_argument('-dec', '--decryption', 
                       action='store_true', 
                       help='Started decryption mode')
    parser.add_argument('-k', '--key_size', 
                        type = int, 
                        required = True, 
                        help='Length of key: 128, 192, 256')
    return parser.parse_args()


def validate_mode(args: tuple) -> str:
    """
    Cheking parser mode
    :param args: tuple of arguments
    :return: chosen mode
    """
    match args:
        case _ if args.generation:
            return "generate"
        case _ if args.encryption:
            return "encrypt"
        case _ if args.decryption:
            return "decrypt"
        case _:
            raise ValueError("Unknown mode!")