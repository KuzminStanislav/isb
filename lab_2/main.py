import sys


from PyQt5.QtWidgets import QApplication


from gui import App
from file_processing import *
from task_2.tests import NISTTests


if __name__ == "__main__":
    settings_file = "settings.json"
    try:
        settings, PI_I = load_json_data(settings_file)
        cpp_file = settings.get("cpp_seq", "")
        java_file = settings.get("java_seq", "")
        output_path = settings.get("tests_results", "tests_results.txt")

        cpp_seq = read_sequence(cpp_file)
        java_seq = read_sequence(java_file)

        cpp_results = run_tests(cpp_seq, PI_I)
        java_results = run_tests(java_seq,PI_I)

        write_results(output_path, cpp_results, java_results)

    except Exception as e:
        print(f"Error while work: {e}")

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())