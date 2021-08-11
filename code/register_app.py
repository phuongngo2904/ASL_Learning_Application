import sqlite3
from PyQt5 import QtWidgets
from signupUI import Ui_NU_Form
from PyQt5.QtWidgets import QMessageBox
import sys

### Register Window
class register(QtWidgets.QWidget, Ui_NU_Form):
    def __init__(self):
        super(register, self).__init__()
        self.setupUi(self)
        self.signup_button.clicked.connect(self.sign_up_clicked)

    def sign_up_clicked(self):
        required_password_length = 8
        db = sqlite3.connect('database/users.db')
        cursor = db.cursor()
        cursor.execute("SELECT username from user_table WHERE username =(?)",
                       (self.username_lineedit.text(),))
        result = cursor.fetchall()

        if (len(result) == 0):
            if self.pw_lineedit.text() != self.confirmpw_lineedit.text():
                self.pw_lineedit.clear()
                self.confirmpw_lineedit.clear()
                message = QMessageBox()
                message.setIcon(QMessageBox.Critical)
                message.setWindowTitle("FAIL !")
                message.setText("The password you typed do not match. "
                                "Please retype the new password in both boxes")
                message.exec()
            elif len(self.pw_lineedit.text()) < required_password_length:
                self.pw_lineedit.clear()
                self.confirmpw_lineedit.clear()
                message = QMessageBox()
                message.setIcon(QMessageBox.Warning)
                message.setWindowTitle("Error !")
                message.setText("The password you typed is too short. "
                                "Your password must be longer than 8 characters")
                message.exec()
            elif len(self.pw_lineedit.text()) > required_password_length:
                query = "INSERT INTO user_table(username, email,fname,minit,lname,password) VALUES(?,?,?,?,?,?);"
                cursor.execute(query, (
                    self.username_lineedit.text(),
                    self.email_lineedit.text(),
                    self.fname_lineedit.text(),
                    self.midname_lineedit.text(),
                    self.lname_lineedit.text(),
                    self.pw_lineedit.text()
                ))
                cursor.fetchall()
                db.commit()
                db.close()
                message = QMessageBox()
                message.setIcon(QMessageBox.Information)
                message.setWindowTitle("Complete")
                message.setText("User has been created")
                message.exec()
                self.username_lineedit.clear()
                self.email_lineedit.clear()
                self.fname_lineedit.clear()
                self.midname_lineedit.clear()
                self.lname_lineedit.clear()
                self.pw_lineedit.clear()
                self.confirmpw_lineedit.clear()
        else:
            self.username_lineedit.clear()
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setWindowTitle("FAIL !")
            message.setText("User name already exists")
            message.exec()