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

        self.results_text_edit = QTextEdit()
        self.results_text_edit.setReadOnly(True)

        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.results_text_edit)

        self.setLayout(self.layout)
        self.show()


    def load_data(self):
        """
        Load data to class
        """
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Load text data",
                                                   "", "text Files (*.txt);;All Files (*)", 
                                                   options = options)
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.results_text_edit.setPlainText(content)
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))