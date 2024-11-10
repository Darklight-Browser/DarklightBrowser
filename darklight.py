# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import QUrl, Signal
from PySide6.QtWebEngineWidgets import QWebEngineView  # Import the correct module
from bookmarks import bookmarks

class darklight(QMainWindow):
    # Sends bookmark signal upon request, used later on down the script.
    bookmarksRequested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Windows, webviews, and homepages oh my!
        self.setWindowTitle("Darklight")
        self.textBrowser = QWebEngineView()
        self.textBrowser.setUrl(QUrl("https://duckduckgo.com"))

        # Establishes the buttons to be used in the browser.
        self.addressBar = QLineEdit()
        self.forwardButton = QPushButton("→")
        self.backwardButton = QPushButton("←")
        self.refreshButton = QPushButton("↺")
        self.bookmarksButton = QPushButton("☆")

        self.forwardButton.clicked.connect(self.textBrowser.forward)
        self.backwardButton.clicked.connect(self.textBrowser.back)
        self.addressBar.returnPressed.connect(self.loadUrlFromAddressBar)
        self.refreshButton.clicked.connect(self.refreshWebPage)
        self.bookmarksButton.clicked.connect(self.loadBookmarks)

        # Assembles the buttons to be put into the toolbar layout!
        toolbarLayout = QHBoxLayout()
        toolbarLayout.addWidget(self.backwardButton)
        toolbarLayout.addWidget(self.forwardButton)
        toolbarLayout.addWidget(self.addressBar)
        toolbarLayout.addWidget(self.refreshButton)
        toolbarLayout.addWidget(self.bookmarksButton)

        # Assembles the vertical layout with toolbar above, webview below.
        mainLayout = QVBoxLayout() # The toolbar goes on top, webview below it.
        mainLayout.addLayout(toolbarLayout) # Toolbar layout containing all the buttons is applied to the window at the top.
        mainLayout.addWidget(self.textBrowser) # This is where the webview comes into play!

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    # Loads URL from user input into the address bar.
    def loadUrlFromAddressBar(self):
        enteredUrl = QUrl.fromUserInput(self.addressBar.text())
        self.textBrowser.setUrl(enteredUrl)

   # Refreshes the webpage from what's already in the address bar.
    def refreshWebPage(self):
        enteredUrl = self.addressBar.text()
        refreshedUrl = QUrl.fromUserInput(enteredUrl)
        self.textBrowser.setUrl(refreshedUrl)

   # Loads bookmarks window.
    def loadBookmarks(self):
        self.bookmarksRequested.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    darklight = darklight()
    bookmarksWin = bookmarks()
    darklight.bookmarksRequested.connect(bookmarksWin.open)
    darklight.show()
    sys.exit(app.exec())
