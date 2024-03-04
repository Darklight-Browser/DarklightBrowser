# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel

class bookmarks(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Sets window tile.
        self.setWindowTitle("Bookmarks - Darklight")

        # Establishes the bookmarks window layout and assigns a label to it.
        bookWinLayout = QVBoxLayout()
        bookWinLayout.addWidget(QLabel("This is where bookmarks will be stored, configured, and managed. Will complete later."))
        self.setLayout(bookWinLayout)
