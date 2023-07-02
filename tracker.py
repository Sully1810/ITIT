# Needed for access to command line arguements
# I probably won't use this but I want it just in case
import sys

# Need to be able to use SQL commands in the background
import sqlite3

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

        # Called to create the inventory DB
        # Only used on first time
        #self.createDatabase()

        # Called to create the tables for the DB
        # Only used on first time
        #self.createTables()

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        # Creating my home icon
        homeIcon = QAction(QIcon("home.png"), "Home", self)
        # Tells people what to do if they hover over it
        homeIcon.setStatusTip("Click to return to home screen.")
        # Tells what happens if someone presses the home icon
        homeIcon.triggered.connect(self.clickedOnHomeIcon)
        # Adds the icon to the toolbar
        toolbar.addAction(homeIcon)

        # Follows the same logic as the home icon
        # Creating the search icon
        searchIcon = QAction(QIcon("search.png"), "Search", self)
        searchIcon.setStatusTip("Click to search inventory list.")
        searchIcon.triggered.connect(self.clickedOnSearchIcon)
        toolbar.addAction(searchIcon)

        # Follows the same logic as the home icon
        # Creating the add items icon
        plusIcon = QAction(QIcon("plus.png"), "Add Items", self)
        plusIcon.setStatusTip("Click to add items to the inventory list.")
        plusIcon.triggered.connect(self.clickedOnPlusIcon)
        toolbar.addAction(plusIcon)

        # Follows the same logic as the home icon
        # Creating the update items icon
        updateIcon = QAction(QIcon("upArrow.png"), "Update Items", self)
        updateIcon.setStatusTip("Click to update an item's information.")
        updateIcon.triggered.connect(self.clickedOnUpdateIcon)
        toolbar.addAction(updateIcon)

        # Follows the same logic as the home icon
        # Creating the delete icon
        deleteIcon = QAction(QIcon("delete.png"), "Delete Items", self)
        deleteIcon.setStatusTip("Click to delete items from the inventory list.")
        deleteIcon.triggered.connect(self.clickedOnDeleteIcon)
        toolbar.addAction(deleteIcon)

        self.setStatusBar(QStatusBar(self))

    def clickedOnHomeIcon(self):
  
        textImage = QPixmap('homeScreenText.jpg')
        textImageLabel = QLabel()
        textImageLabel.setPixmap(textImage)
        textImageLabel.setScaledContents(True)

        self.setCentralWidget(textImageLabel)

    def clickedOnSearchIcon(self):
        print("Sam needs to insert search code.")

    def clickedOnPlusIcon(self):
        print("Sam needs to insert add code.")

    def clickedOnUpdateIcon(self):
        print("Sam needs to insert update code.")

    def clickedOnDeleteIcon(self):
        print("Sam needs to insert delete code.")

    def createDatabase(self):
        # Connecting with the database to work with the information stored there
        con = sqlite3.connect('inventory.db')
        # Creating the cursor method to use the execute method
        cur = con.cursor()

    def createTables(self):

        # Connecting with the database to work with the information stored there
        con = sqlite3.connect('inventory.db')
        # Creating the cursor method to use the execute method
        cur = con.cursor()

        # Creating my first table using the execute method
        # Then the rows are listed as well
        # First column is primary key by making it an INTEGER NOT NULL PRIMARY KEY
        cur.execute(''' CREATE TABLE computer
                    (number INTEGER NOT NULL PRIMARY KEY, make, model, purchasedDate, name, assignedBranch)''')
    
        

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