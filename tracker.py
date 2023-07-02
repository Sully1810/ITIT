# Needed for access to command line arguements
# I probably won't use this but I want it just in case
import sys

# Now we are going to get stuff from PyQT6
# Have to tell it what we want because they offer a lot of stuff
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QPushButton, QStackedLayout, QVBoxLayout, QWidget
from PyQt6.QtGui import QPalette, QColor, QAction, QIcon

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

        # Setting up the interface layout using to several different types
        # Page layout will work vertically
        pagelayout = QVBoxLayout()
        # The buttons need to be laid out horizontally
        button_layout = QHBoxLayout()
        # I need the pages to be stacked according to what button is pushed
        # The stacklayout allows that
        self.stacklayout = QStackedLayout()

        # Have to pass my button_layout and my self.stacklayout through our page layout to help it align
        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        # Creating my Home Button
        btn = QPushButton("Home")
        # Telling the program what needs to happen when the button is pushed
        # In this case, it needs to activate_tab_1 which will hold everything on the home page
        btn.pressed.connect(self.activate_tab_1)
        # Adding the button to our layout
        button_layout.addWidget(btn)
        # Making it red so you can see the changes from switching screens
        self.stacklayout.addWidget(Color("red"))

        # Followed the "Home" button logic
        # Creating my Search Inventory Button
        btn = QPushButton("Search Inventory")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("green"))

        # Followed the "Home" button logic
        # Creating my Add Items Button        
        btn = QPushButton("Add Items")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("yellow"))

        # Followed the "Home" button logic
        # Creating my Update Items Button
        btn = QPushButton("Update Items")
        btn.pressed.connect(self.activate_tab_4)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("blue"))

        # Followed the "Home" button logic
        # Creating my Delete Items Button
        btn = QPushButton("Delete Items")
        btn.pressed.connect(self.activate_tab_5)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("purple"))

        # Creates blank widgets that our buttons go into
        # Allows the "stacking" to happen
        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    # Defines what to do if home button is pushed
    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    # Defines what to do if search inventory button is pushed
    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    # Defines what to do if add items button is pushed
    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)

    # Defines what to do if update items button is pushed
    def activate_tab_4(self):
        self.stacklayout.setCurrentIndex(3)

    # Defines what to do if delete button is pushed
    def activate_tab_5(self):
        self.stacklayout.setCurrentIndex(4)

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