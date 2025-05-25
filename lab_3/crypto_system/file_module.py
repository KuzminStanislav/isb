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
        try:
            with open(self.path, "r") as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Can't find file: {filename}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON data in: {filename}") from e
        except Exception as e:
            print(f"Error: {e}")
        

    def write_json(self, data: dict) -> None:
        """
        Write data to JSON file
        :param data: JSON data
        """
        try:
            with open(self.path, "w") as file:
                json.dump(data, file, indent = 4)
        except OSError as e:
            raise OSError(f"Error while writting data to JSON-file: {e}")
        except Exception as e:
            raise RuntimeError(f"Error while processing data: {e}")
        except Exception as e:
            print(f"Error: {e}")


    def read_file(self) -> bytes:
        """
        Read file data
        :return: bytes of data
        """
        try:
            with open(self.path, "rb") as file:
                content = file.read()
            return content
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Can't find file: {filename}") from e
        except Exception as e:
            print(f"Error: {e}")


    def write_file(self, content: bytes) -> None:
        """
        Write data to file
        :param content: data that is written to file
        """
        try:
            with open(self.path, "wb") as file:
                file.write(content)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Can't write in file: {filename}") from e
        except Exception as e:
            print(f"Error: {e}")