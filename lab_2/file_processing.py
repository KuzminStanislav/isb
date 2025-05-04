import json
import os


from task_2.tests import NISTTests
    

def load_json_data(path: str) -> tuple[dict, list]:
    """
    Load data from JSON file
    :param path: Path to file
    :return: settings from JSON file
    """
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            constants = data.get("PI_I", [])
            return data, constants
    except FileNotFoundError:
        print(f"File {path} not found!")
        return {}, []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {path}!")
        return {}, []
    

def read_sequence(path: str) -> list:
    """
    Read sequences frow text files
    :param path: Path to text file
    :return: List of sequences
    """
    try:
        with open(path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        raise Exception(f"File {path} not found.")
    except IOError as e:
        raise Exception(f"Error while reading file: {e}")
    

def run_tests(seq: list[str], PI_I: list) -> list:
    """
    Run tests and return results
    :param seq: List of binary sequences
    :param PI_I: Probabilities 
    :return: List of results
    """
    results = []
    nist = NISTTests(seq[0])
    freq_test_result = nist.frequency_bit_test()
    results.append(f"Result of frequency bit test: {freq_test_result}")
    run_same_result = nist.run_same_bits_test()
    results.append(f"Result of run same bit test: {run_same_result}")
    longest_one_result = nist.longest_ones_seq_test(PI_I)
    results.append(f"Result of longest one sequency test: {longest_one_result}")
    return results


def write_results(path: str, cpp_results: list, java_results: list) -> None:
    """
    Write results in file
    :param path: Path to text file
    :param cpp_results: Results C++ tests
    :param java_results: Results JAVA tests
    """
    try:
        with open(path, "w") as file:
            file.write("C++ results:\n")
            for results in cpp_results:
                file.write(results + "\n")

            file.write("JAVA results:\n")
            for results in java_results:
                file.write(results + "\n")
    except IOError as e:
        raise Exception(f"Error while writing to file: {e}")