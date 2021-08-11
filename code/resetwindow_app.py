from PyQt5 import QtWidgets
from resetpwUI import Ui_UI_rspw
from PyQt5.QtWidgets import QMessageBox
import sqlite3

### Reset password Window
class reset_password(QtWidgets.QWidget, Ui_UI_rspw):
    def __init__(self):
        super(reset_password, self).__init__()
        self.setupUi(self)
        self.submit_button.clicked.connect(self.submit_clicked)
    def submit_clicked(self):
        db = sqlite3.connect('database/users.db')
        cursor = db.cursor()
        cursor.execute("Select username from user_table where username=(?)",
                       (self.username_lineedit.text(),))
        result = cursor.fetchall()
        if len(result) == 0:
            self.username_lineedit.clear()
            self.pw_lineedit.clear()
            message = QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setWindowTitle("FAIL !")
            message.setText("User not found !!")
            message.exec()
        else:
            required_password_length = 8
            name=[x[0] for x in result]
            #print(name[0])
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
                cursor.execute("UPDATE user_table SET password=(?) WHERE username =(?)",
                               (self.pw_lineedit.text(), name[0]))
                db.commit()
                db.close()
                self.pw_lineedit.clear()
                self.confirmpw_lineedit.clear()
                message = QMessageBox()
                message.setIcon(QMessageBox.Information)
                message.setWindowTitle("Success !")
                message.setText("Your password has been updated.")
                message.exec()


