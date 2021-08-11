import sqlite3
from PyQt5 import QtWidgets
from mainwindow_UI import Ui_mainWindow
from register_app import register
from resetwindow_app import reset_password
from PyQt5.QtWidgets import QMessageBox
import sys

### Main Window
class ASL_app(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(ASL_app, self).__init__()
        self.setupUi(self)
        self.Login_button.clicked.connect(self.login_clicked)
        self.new_user_button.clicked.connect(self.newuser_clicked)
        self.reset_button.clicked.connect(self.reset_clicked)

    def login_clicked(self):
        db = sqlite3.connect('database/users.db')
        cursor = db.cursor()
        cursor.execute("Select username, password from user_table where username=(?)",
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
            for x in result:
                name = x[0]
                pw = x[1]
            if self.username_lineedit.text() == name and self.pw_lineedit.text() == pw:
                print("Successful")
                # open a new window
            elif self.username_lineedit.text() == name and self.pw_lineedit.text() != pw:
                message = QMessageBox()
                message.setIcon(QMessageBox.Warning)
                message.setWindowTitle("FAIL !")
                message.setText("Incorrect password.")
                message.exec()
                self.pw_lineedit.clear()
        db.commit()
        db.close()
    def newuser_clicked(self):
        self.r = register()
        self.r.show()
        if self.r.isVisible():
            self.showMinimized()

    def reset_clicked(self):
        self.res_pw = reset_password()
        self.res_pw.show()
        if self.res_pw.isVisible():
            self.showMinimized()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = ASL_app()
    Form.show()
    sys.exit(app.exec_())
