from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow, QWidget, QLineEdit


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        MainWindow.setStyleSheet("background-color: #fffff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.confirmpasswd = QtWidgets.QLabel(self.centralwidget)
        self.confirmpasswd.setGeometry(QtCore.QRect(70, 359, 111, 21))
        self.confirmpasswd.setStyleSheet("""
        {
            color: #2e7d32;
            background-color: #fef4f6;
            padding-right: 3px;
            text-align: Justify;
            padding-top: 2px;
            padding-bottom: 2px;
        }
        """
    )
        self.confirmpasswd.setObjectName("confirmpasswd")
        self.emailfield = QtWidgets.QLineEdit(self.centralwidget)
        self.emailfield.setGeometry(QtCore.QRect(190, 250, 191, 22))
        self.emailfield.setStyleSheet("background-color: white;\n"
"border: 1px solid #A5D6A7;")
        self.emailfield.setObjectName("emailfield")
        self.passwdfield = QtWidgets.QLineEdit(self.centralwidget)
        self.passwdfield.setGeometry(QtCore.QRect(190, 300, 191, 22))
        self.passwdfield.setStyleSheet("background-color: white;\n"
"border: 1px solid #A5D6A7;")
        self.passwdfield.setText("")
        self.passwdfield.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwdfield.setObjectName("passwdfield")
        self.confpasswdfield = QLineEdit(self.centralwidget)
        self.confpasswdfield.setGeometry(QtCore.QRect(190, 357, 191, 22))
        self.confpasswdfield.setStyleSheet("background-color: white;\n"
"border: 1px solid #A5D6A7;")
        self.confpasswdfield.setText("")
        self.confpasswdfield.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confpasswdfield.setObjectName("confpasswdfield")
        self.signupframe = QtWidgets.QFrame(self.centralwidget)
        self.signupframe.setGeometry(QtCore.QRect(20, 70, 391, 421))
        self.signupframe.setStyleSheet("background-color: #A5D6A7;\n"
"vertical-align: center;\n"
"")
        self.signupframe.setFrameShape(QFrame.StyledPanel)
        self.signupframe.setFrameShadow(QFrame.Raised)
        self.signupframe.setObjectName("signupframe")
        self.namefield = QLineEdit(self.signupframe)
        self.namefield.setGeometry(QtCore.QRect(170, 130, 191, 22))
        self.namefield.setStyleSheet("background-color: white;\n"
"border: 1px solid #A5D6A7;")
        self.namefield.setObjectName("namefield")
        self.name = QtWidgets.QLabel(self.signupframe)
        self.name.setGeometry(QtCore.QRect(50, 131, 49, 20))
        self.name.setStyleSheet("color: #2e7d32;\n"
"background-color: #fef4f6;\n"
"padding-right: 3px;\n"
"text-align: Justify;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;")
        self.name.setObjectName("name")
        self.email = QtWidgets.QLabel(self.signupframe)
        self.email.setGeometry(QtCore.QRect(50, 180, 49, 21))
        self.email.setStyleSheet("color: #2e7d32;\n"
"background-color: #fef4f6;\n"
"padding-right: 3px;\n"
"text-align: Justify;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLabel(self.signupframe)
        self.password.setGeometry(QtCore.QRect(50, 230, 61, 21))
        self.password.setStyleSheet("color: #2e7d32;\n"
"background-color: #fef4f6;\n"
"padding-right: 4px;\n"
"text-align: Justify;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"")
        self.password.setObjectName("password")
        self.exitinguser = QtWidgets.QLabel(self.signupframe)
        self.exitinguser.setGeometry(QtCore.QRect(50, 380, 81, 21))
        self.exitinguser.setStyleSheet("color: #2e7d32;\n"
"background-color: #fef4f6;\n"
"padding-right: 3px;\n"
"text-align: Justify;\n"
"padding-top: 2px;\n"
"padding-bottom: 2px;\n"
"")
        self.exitinguser.setObjectName("exitinguser")
        self.signinbutton = QtWidgets.QPushButton(self.signupframe)
        self.signinbutton.setGeometry(QtCore.QRect(150, 380, 75, 24))
        self.signinbutton.setStyleSheet("text-align: center;\n"
"background-color: #f1f7f4;\n"
"border-radius: 5px;\n"
"border: 1px solid #ffffff;\n"
"color: #2e7d32;\n"
"font-weight: 500px;")
        self.signinbutton.setObjectName("signinbutton")
        self.signupbutton = QtWidgets.QPushButton(self.signupframe)
        self.signupbutton.setGeometry(QtCore.QRect(280, 340, 75, 24))
        self.signupbutton.setStyleSheet("text-align: center;\n"
"background-color: #2e7d32;\n"
"border-radius: 2px;\n"
"border: 1px solid #ffffff;\n"
"color: #ffffff;\n"
"font-weight: Bold;")
        self.signupbutton.setObjectName("signupbutton")
        self.label = QtWidgets.QLabel(self.signupframe)
        self.label.setGeometry(QtCore.QRect(150, 30, 81, 31))
        self.label.setStyleSheet("font: \"Futura Bk BT\";\n"
"font-size: 12.5pt ;\n"
"color: #2e7d32;\n"
"background-color: #ffffff;\n"
"font-weight: BOLD;\n"
"border: 1px solid #f6fef3;\n"
"border-radius: 5px;\n"
"padding: 3px 2px;\n"
"align: center;\n"
"")
        self.label.setObjectName("label")
        self.signupframe.raise_()
        self.confirmpasswd.raise_()
        self.emailfield.raise_()
        self.passwdfield.raise_()
        self.confpasswdfield.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Expense Tracker"))
        self.confirmpasswd.setText(_translate("MainWindow", "Confirm Password"))
        self.emailfield.setPlaceholderText(_translate("MainWindow", "example@name.com"))
        self.passwdfield.setPlaceholderText(_translate("MainWindow", "password"))
        self.confpasswdfield.setPlaceholderText(_translate("MainWindow", "confirm password"))
        self.namefield.setPlaceholderText(_translate("MainWindow", "Firstname, Lastname"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.email.setText(_translate("MainWindow", "Email"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.exitinguser.setText(_translate("MainWindow", "Existing user?"))
        self.signinbutton.setText(_translate("MainWindow", "Sign in"))
        self.signupbutton.setText(_translate("MainWindow", "Sign up"))
        self.label.setText(_translate("MainWindow", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
 