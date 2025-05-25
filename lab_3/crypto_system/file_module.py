import json


class FileProcessor:
    def read_json(self, path: str) -> dict:
        """
        Read data from JSON file
        :param path: path to file
        :return: JSON data
        """
        try:
            with open(path, "r") as file:
                return json.load(file)
        except Exception as e:
            print(f"Error while loading JSON-data: {e}")
        

    def write_json(self, path: str, data: dict) -> None:
        """
        Write data to JSON file
        :param path: path to file
        :param data: JSON data
        """
        try:
            with open(path, "w") as file:
                json.dump(data, file, indent = 4)
        except OSError as e:
            raise OSError(f"Error while writting data to JSON-file: {e}")
        except Exception as e:
            raise RuntimeError(f"Error while processing data: {e}")
        except Exception as e:
            print(f"Error: {e}")


    def read_file(self, path: str) -> bytes:
        """
        Read file data
        :param path: path to file
        :return: bytes of data
        """
        try:
            with open(path, "rb") as file:
                content = file.read()
            return content
        except Exception as e:
            print(f"Error while reading file: {e}")


    def write_file(self, path: str, content: bytes) -> None:
        """
        Write data to file
        :param path: path to file
        :param content: data that is written to file
        """
        try:
            with open(path, "wb") as file:
                file.write(content)
        except Exception as e:
            print(f"Error while writting data to file: {e}")