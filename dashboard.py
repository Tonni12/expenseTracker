# coding=utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QMenu, QMenuBar, QHBoxLayout, QMainWindow, QApplication

class MainDashboard(QMainWindow):
    def __init__(self):
        super(MainDashboard, self).__init__()
        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)

        self.setLabel()

        # Create the main layout
        self.main_layout = QHBoxLayout(self.centralWidget)

        # Create the sidebar layout
        self.side_menu = QtWidgets.QWidget()
        self.sidebar_layout = QVBoxLayout(self.side_menu)

        # Add some buttons to the sidebar
        self.main_page = QtWidgets.QPushButton("Dashboard")
        self.edit_exp = QtWidgets.QPushButton("Edit Expenses")
        self.view_summary = QtWidgets.QPushButton("View Expenses")
        self.setting = QtWidgets.QPushButton("Settings")
        self.terminate = QtWidgets.QPushButton("Logout")

        self.side_menu.addWidget(self.main_page)
        self.side_menu.addWidget(self.edit_exp)
        self.side_menu.addWidget(self.view_summary)
        self.side_menu.addWidget(self.setting)
        self.side_menu.addWidget(self.terminate)

        # Add a spacer to push the buttons to the top
        self.sidebar_layout.addStretch()

        # Add the sidebar layout to the main layout
        self.main_layout.addLayout(self.sidebar_layout)

        # Add a main content area
        self.content_area = QtWidgets.QTextEdit()
        self.main_layout.addWidget(self.content_area)

        # Set the main window properties
        self.setWindowTitle("MainWindow with Sidebar")
        self.resize(800, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    app.exec()
