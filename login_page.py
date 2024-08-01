# coding=utf-8
from PyQt5.QtWidgets import (QMessageBox, QPushButton, QWidget, QVBoxLayout, QLineEdit, QLabel)
import psycopg2
import bcrypt
import re

conn = psycopg2.connect(
    dbname="expenses_db",
    user="postgres",
    password="admin123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# cursor
def validate_password(password):
    """

    :param password: checks match pattern for password
    :return: returns True if password is valid, else returns False
    """
    # Password must be at least 8 characters long
    if len(password) < 8:
        return False
    # Password must contain at least one uppercase letter, one lowercase letter, one digit, and
    # one special character
    #if not re.search(r"[A-Z]", password):
     #   return False
    #if not re.search(r"[a-z]", password):
     #   return False
    #if not re.search(r"[0-9]", password):
     #   return False
    #if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
     #   return False
    #return True


class LoginWindow(QWidget):
    """
    input: Username and Password
    output: Redirect to dashboard if login is successful
    """
    def __init__(self, app, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.app = app
        self.setWindowTitle("Login")

        layout = QVBoxLayout()

        self.user_name = QLineEdit()
        self.user_name.setPlaceholderText("Username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")
        self.signup_btn = QPushButton("Sign Up")

        self.login_btn.clicked.connect(self.login)
        self.signup_btn.clicked.connect(self.signup)

        layout.addWidget(QLabel("Login"))
        layout.addWidget(self.user_name)
        layout.addWidget(self.password)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.signup_btn)

        self.setLayout(layout)

    def login(self):
        username = self.user_name.text()
        password = self.password.text()
        # Authentication logic
        cursor.execute("SELECT password FROM users WHERE user_name=%s", (self.user_name.text(),))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password.encode(), user[0].encode('utf-8')):
            cursor.execute("SELECT id FROM users WHERE user_name=%s", (self.user_name.text(),))
            user_id = cursor.fetchone()[0]
            self.app.show_main_window(user_id)
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials")

    def signup(self):
        user_name = self.user_name.text()
        password = self.password.text()
        # Registration logic
        if not validate_password(password):
            QMessageBox.warning(self, "Error",
                                "Password must be at least 8 characters long, contain at least one uppercase letter, "
                                "one lowercase letter, one digit, and one special character.")
            return

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        try:
            cursor.execute("INSERT INTO users (user_name, password) VALUES (%s, %s)", (user_name, hashed_password))
            conn.commit()
            QMessageBox.information(self, "Success", "User registered successfully")
        except psycopg2.errors.UniqueViolation:
            conn.rollback()
            QMessageBox.warning(self, "Error", "Username already exists")
