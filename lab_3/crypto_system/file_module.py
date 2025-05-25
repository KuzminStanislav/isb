import json


class FileProcessor:
    def __init__(self, path: str = " "):
        """
        Class initialization
        """
        self.path = path

    def read_json(self) -> dict:
        """
        Read data from JSON file
        :return: JSON data
        """
        with open(self.path, "r") as file:
            return json.load(file)
        

    def write_json(self, data: dict) -> None:
        """
        Write data to JSON file
        :param data: JSON data
        """
        with open(self.path, "w") as file:
            json.dump(data, file, indent = 4)



    def read_file(self) -> bytes:
        """
        Read file data
        :return: bytes of data
        """
        with open(self.path, "rb") as file:
            content = file.read()
        return content


    def write_file(self, content: bytes) -> None:
        """
        Write data to file
        :param content: data that is written to file
        """
        with open(self.path, "wb") as file:
            file.write(content)