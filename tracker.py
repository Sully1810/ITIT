# Needed for access to command line arguements
# I probably won't use this but I want it just in case
import sys

# Now we are going to get stuff from PyQT6
# Have to tell it what we want because they offer a lot of stuff
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QPushButton, QStackedLayout, QVBoxLayout, QWidget, QToolBar, QStatusBar
from PyQt6.QtGui import QPalette, QColor, QAction, QIcon, QPixmap

# Creating the color class to customize our interface layout
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

# Creating a subclass to customize our application's main window
# This will also create our window that a user interfaces with
class MainWindow(QMainWindow):
    def __init__(self):
        # Since I subclassed a Qtclass, I have to call the super__init__ function to setup my object
        super().__init__()

        # Giving my app a title window. 
        self.setWindowTitle("ITIT")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        homeIcon = QAction(QIcon("home.png"), "Home", self)
        homeIcon.setStatusTip("Click to return to home screen.")
        homeIcon.triggered.connect(self.clickedOnHomeIcon)
        homeIcon.setCheckable(True)
        toolbar.addAction(homeIcon)

        self.setStatusBar(QStatusBar(self))

    def clickedOnHomeIcon(self):
  
        textImage = QPixmap('homeScreenText.jpg')
        textImageLabel = QLabel()
        textImageLabel.setPixmap(textImage)
        textImageLabel.setScaledContents(True)

        self.setCentralWidget(textImageLabel)

# Creating the application
# Passing in sys.argv to allow command line arguements
# Applications handle our event loop
app = QApplication(sys.argv)

# Creating a Qt Widget which will be our window
window = MainWindow()
# IMPORTANT!!! Show the window
# Default is to hide the window
window.show()

# Start the event loop
app.exec()