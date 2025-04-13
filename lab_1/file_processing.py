import json


def load_json_data(filename: str) -> dict:
    """
    Load data from JSON-file
    :param filename: JSON-file name
    :return: Dict with JSON data
    """
    try:
        with open(filename, 'r', encoding = "utf-8") as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Can't find file: {filename}") from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON data in: {filename}") from e
    

def write_json_data(dict: dict, filename: str) -> None:
    """
    Write data to JSON-file
    :param dict: Dictionary of frequencies
    :param filename: JSON-file name
    """
    try: 
        with open(filename, 'w', encoding = "utf-8") as file:
            json.dump(dict, file, ensure_ascii = False)
    except OSError as e:
        raise OSError(f"Error while writting data to JSON-file: {e}")
    except Exception as e:
        raise RuntimeError(f"Error while processing data: {e}")


def read_text(filename: str) -> str:
    """
    Read text from file
    :param filename: Name of file
    :return: Data from file
    """
    try:
        with open(filename, 'r', encoding = "utf-8") as file:
            return file.read().strip()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Can't find file: {filename}") from e


def write_to_file(filename: str, content: str) -> None:
    """
    Write data to file
    :param filename: Name of file
    :param content: Content to writting
    """
    try:
        with open(filename, 'w', encoding = "utf-8") as file:
            file.write(content)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Can't write in file: {filename}") from e
