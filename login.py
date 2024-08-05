
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys

from PyQt5.QtWidgets import QFrame


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(11)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signupframe = QtWidgets.QFrame(self.centralwidget)
        self.signupframe.setGeometry(QtCore.QRect(60, 70, 435, 421))
        self.signupframe.setStyleSheet("background-color: #A5D6A7;\n"
            "")
        self.signupframe.setFrameStyle(QFrame.StyledPanel)
        self.signupframe.setFrameShadow(QFrame.Raised)
        self.signupframe.setObjectName("signupframe")
        self.email = QtWidgets.QLabel(self.signupframe)
        self.email.setGeometry(QtCore.QRect(50, 140, 49, 21))
        self.email.setStyleSheet("color: #2e7d32;\n"
            "background-color: #fef4f6;\n"
            "padding-right: 3px;\n"
            "text-align: Justify;\n"
            "padding-top: 2px;\n"
            "padding-bottom: 2px;")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLabel(self.signupframe)
        self.password.setGeometry(QtCore.QRect(50, 190, 61, 21))
        self.password.setStyleSheet("color: #2e7d32;\n"
            "background-color: #fef4f6;\n"
            "padding-right: 4px;\n"
            "text-align: Justify;\n"
            "padding-top: 2px;\n"
            "padding-bottom: 2px;\n"
            "")
        self.password.setObjectName("password")
        self.signupbutton = QtWidgets.QPushButton(self.signupframe)
        self.signupbutton.setGeometry(QtCore.QRect(160, 270, 75, 24))
        self.signupbutton.setStyleSheet("text-align: center;\n"
            "background-color: #2e7d32;\n"
            "border-radius: 2px;\n"
            "border: 1px solid #ffffff;\n"
            "color: #ffffff;\n"
            "font-weight: Bold;")
        self.signupbutton.setObjectName("signupbutton")
        self.signinfield = QtWidgets.QLabel(self.signupframe)
        self.signinfield.setGeometry(QtCore.QRect(170, 40, 81, 31))
        self.signinfield.setStyleSheet("font: \"Futura Bk BT\";\n"
            "font-size: 12.5pt ;\n"
            "color: #2e7d32;\n"
            "background-color: #ffffff;\n"
            "font-weight: BOLD;\n"
            "border: 1px solid #f6fef3;\n"
            "border-radius: 5px;\n"
            "padding: 3px 2px;\n"
            "align: center;\n"
            "")
        self.signinfield.setObjectName("signinfield")
        self.passwdfield = QtWidgets.QLineEdit(self.signupframe)
        self.passwdfield.setGeometry(QtCore.QRect(140, 189, 191, 22))
        self.passwdfield.setStyleSheet("background-color: white;\n"
            "border: 1px solid #A5D6A7;")
        self.passwdfield.setText("")
        self.passwdfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwdfield.setObjectName("passwdfield")
        self.emailfield = QtWidgets.QLineEdit(self.signupframe)
        self.emailfield.setGeometry(QtCore.QRect(140, 140, 191, 22))
        self.emailfield.setStyleSheet("background-color: white;\n"
            "border: 1px solid #A5D6A7;")
        self.emailfield.setObjectName("emailfield")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Expense Tracker"))
        self.email.setText(_translate("MainWindow", "Email"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.signupbutton.setText(_translate("MainWindow", "Login"))
        self.signinfield.setText(_translate("MainWindow", "Sign In"))
        self.passwdfield.setPlaceholderText(_translate("MainWindow", "password"))
        self.emailfield.setPlaceholderText(_translate("MainWindow", "example@name.com"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())
