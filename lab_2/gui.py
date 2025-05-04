from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit,
    QFileDialog, QMessageBox
)


from file_processing import *


class App(QWidget):
    def __init__(self):
        """
        Class initialisation
        """
        super().__init__()
        self.initUI()

    
    def initUI(self):
        """
        Add windiw elements
        """
        self.setWindowTitle("Sequence tests")

        self.layout = QVBoxLayout()

        self.load_button = QPushButton("Load tests data")
        self.load_button.clicked.connect(self.load_data)

        self.run_button = QPushButton("Run tests")
        self.run_button.clicked.connect(self.run_tests)

        self.results_text_edit = QTextEdit()
        self.results_text_edit.setReadOnly(True)

        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.run_button)
        self.layout.addWidget(self.results_text_edit)

        self.setLayout(self.layout)
        self.show()


    def load_data(self):
        """
        Load data to class
        """
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Load JSON data",
                                                   "", "JSON Files (*.json);;All Files (*)", 
                                                   options = options)
        if file_path:
            try:
                self.settings = load_json_data(file_path)
                self.results_text_edit.append(f"Loaded settings from {file_path}.\n")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))


    def run_tests(self):
        """
        Run tests in class
        """
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Load sequence data",
                                                   "", "JSON Files (*.json);;All Files (*)", 
                                                   options = options)
        if file_path:
            try:
                sequences = read_sequence(file_path)
                results = run_tests(sequences)
                self.results_text_edit.append("\n".join(results) + "\n")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))