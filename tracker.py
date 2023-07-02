# Needed for access to command line arguements
# I probably won't use this but I want it just in case
import sys

# Need to be able to use SQL commands in the background
import sqlite3

# Now we are going to get stuff from PyQT6
# Have to tell it what we want because they offer a lot of stuff
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget, QToolBar, QStatusBar, QLineEdit, QGridLayout
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
        # Inserting an image of what I want my text to look like. 
        textImage = QPixmap('homeScreenText.jpg')
        textImageLabel = QLabel()
        textImageLabel.setPixmap(textImage)
        textImageLabel.setScaledContents(True)

        self.setCentralWidget(textImageLabel)

    def clickedOnSearchIcon(self):
        print("Sam needs to insert search code.")

    def clickedOnPlusIcon(self):

        plusLayout = QGridLayout()
        
        # Getting input from the user about the items that need added to the inventory
        # Got a bit crazy
        
        # Getting primary key information
        self.getPrimaryKey = QLineEdit()
        # Setting a mak length for the primary key
        self.getPrimaryKey.setMaxLength(5)
        # Tells user what to put in box. 
        self.getPrimaryKey.setPlaceholderText("Enter item number: ")
        # Add it to the grid to show up on screen
        plusLayout.addWidget(self.getPrimaryKey, 0, 0)
        # What to do once enter has been submitted
        self.getPrimaryKey.returnPressed.connect(self.pkReturnPressed)

        # Creating a line to show when the user has pressed enter to submit the information
        # For primary key
        self.pkReady = QLineEdit(text="Not Ready")
        # Add it to the layout
        plusLayout.addWidget(self.pkReady, 0, 1)

        # Follows same logic as the primary key information
        self.getMake = QLineEdit()
        self.getMake.setMaxLength(20)
        self.getMake.setPlaceholderText("Enter item make: ")
        plusLayout.addWidget(self.getMake, 1, 0)
        self.getMake.returnPressed.connect(self.maReturnPressed)

        # Follows same logic as pkReady line
        # For make 
        self.maReady = QLineEdit(text="Not Ready")
        plusLayout.addWidget(self.maReady, 1, 1)

        # Follows same logic as the primary key information
        self.getModel = QLineEdit()
        self.getModel.setMaxLength(20)
        self.getModel.setPlaceholderText("Enter item model: ")
        plusLayout.addWidget(self.getModel, 2, 0)
        self.getModel.returnPressed.connect(self.moReturnPressed)

        # Follows same logic as pkReady line
        # For model
        self.moReady = QLineEdit(text="Not Ready")
        plusLayout.addWidget(self.moReady, 2, 1)        

        # Follows same logic as the primary key information
        self.getItemType = QLineEdit()
        self.getItemType.setMaxLength(50)
        self.getItemType.setPlaceholderText("Enter item type: ")
        plusLayout.addWidget(self.getItemType, 3, 0)
        self.getItemType.returnPressed.connect(self.itReturnPressed)

        # Follows same logic as pkReady line
        # For item type
        self.itReady = QLineEdit(text="Not Ready")
        plusLayout.addWidget(self.itReady, 3, 1)

        # Follows same logic as the primary key information
        self.getPurchasedDate = QLineEdit()
        self.getPurchasedDate.setMaxLength(10)
        self.getPurchasedDate.setPlaceholderText("Enter item purchased date: ")
        plusLayout.addWidget(self.getPurchasedDate, 4, 0)
        self.getPurchasedDate.returnPressed.connect(self.pdReturnPressed)

        # Follows same logic as pkReady line
        # For purchased date
        self.pdReady = QLineEdit(text="Not Ready")
        plusLayout.addWidget(self.pdReady, 4, 1)

        # Follows same logic as the primary key information
        self.getName = QLineEdit()
        self.getName.setMaxLength(5) 
        self.getName.setPlaceholderText("Enter item name: ")
        plusLayout.addWidget(self.getName, 5, 0)
        self.getName.returnPressed.connect(self.naReturnPressed)

        # Follows same logic as pkReady line
        # For name
        self.naReady = QLineEdit(text="Not Ready")
        plusLayout.addWidget(self.naReady, 5, 1)

        # Follows same logic as the primary key information
        self.getAssignedBranch = QLineEdit()
        self.getAssignedBranch.setMaxLength(20)
        self.getAssignedBranch.setPlaceholderText("Enter item branch: ")
        plusLayout.addWidget(self.getAssignedBranch, 6, 0)
        self.getAssignedBranch.returnPressed.connect(self.abReturnPressed)

        # Follows same logic as pkReady line
        # For assigned branch 
        self.abReady = QLineEdit(text="Not Ready")
        plusLayout.addWidget(self.abReady, 6, 1)

        # Created a submit button
        self.addSubmitBtn = QPushButton(text="Submit")
        # Add it to the grid
        plusLayout.addWidget(self.addSubmitBtn, 3, 2)
        # Tells what happens when the button is clicked on
        self.addSubmitBtn.clicked.connect(self.sBtnClicked)

        widget = QWidget()
        widget.setLayout(plusLayout)
        self.setCentralWidget(widget)

    def pkReturnPressed(self):
        self.pkReady.setText("Ready!")
        self.primaryKey = self.getPrimaryKey.text()
        return self.primaryKey

    def maReturnPressed(self):
        self.maReady.setText("Ready!")
        self.make = self.getMake.text()
        return self.make
        
    def moReturnPressed(self):
        self.moReady.setText("Ready!")
        self.model = self.getModel.text()
        return self.model

    def itReturnPressed(self):
        self.itReady.setText("Ready!")
        self.itemType = self.getItemType.text()
        return self.itemType

    def pdReturnPressed(self):
        self.pdReady.setText("Ready!")
        self.purchasedDate = self.getPurchasedDate.text()
        return self.purchasedDate

    def naReturnPressed(self):
        self.naReady.setText("Ready!")
        self.name = self.getName.text()
        return self.name

    def abReturnPressed(self):
        self.abReady.setText("Ready!")
        self.assignedBranch = self.getAssignedBranch.text()
        return self.assignedBranch

    def sBtnClicked(self):
        self.addCommand()
        self.addSubmitBtn.setText("Completed!")

    def addCommand(self):
        # Connecting with the database to work with the information stored there
        con = sqlite3.connect('inventory.db')
        # Creating the cursor method to use the execute method
        cur = con.cursor()

        cur.execute("INSERT INTO computer VALUES (?, ?, ?, ?, ?, ?, ?)", (self.primaryKey, self.make, self.model, self.itemType, self.purchasedDate, self.name, self.assignedBranch))

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
                    (number INTEGER NOT NULL PRIMARY KEY, make, model, itemType, purchasedDate, name, assignedBranch)''')
        
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