import json


def read_json(path: str) -> dict:
    """
    Read data from JSON file
    :param path: path to JSON file
    :return: JSON data
    """
    with open(path, "r") as file:
        return json.load(file)
    

def write_json(path: str, data: dict) -> None:
    """
    Write data to JSON file
    :param path: path to JSON file
    :param data: JSON data
    """
    with open(path, "w") as file:
        json.dump(data, file, indent = 4)



def read_file(path: str) -> bytes:
    """
    Read file data
    :param path: path to file
    :return: bytes of data
    """
    with open(path, "rb") as file:
        content = file.read()
    return content


def write_file(path: str, content: bytes) -> None:
    """
    Write data to file
    :param path: path to file
    :param content: data that is written to file
    """
    with open(path, "wb") as file:
        file.write(content)