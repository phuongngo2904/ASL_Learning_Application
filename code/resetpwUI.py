from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
from images import res

class Ui_UI_rspw(object):
    def setupUi(self, UI_rspw):
        UI_rspw.setObjectName("UI_rspw")
        UI_rspw.resize(1047, 810)
        UI_rspw.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        UI_rspw.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(UI_rspw)
        self.widget.setGeometry(QtCore.QRect(30, 10, 971, 771))
        self.widget.setStyleSheet("QPushButton#Login_button{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85,98,112,226));\n"
"    color: rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#Login_button:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton#Login_button:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 470, 650))
        self.label.setStyleSheet("border-image: url(images/3.jpg);\n"
"background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(479, 30, 441, 650))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(650, 40, 121, 131))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-image: url(images/1.jpg);\n"
"background-color: rgba(0,0,0,0);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/1.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.submit_button = QtWidgets.QPushButton(self.widget)
        self.submit_button.setGeometry(QtCore.QRect(650, 500, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("QPushButton#submit_button{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85,98,112,226));\n"
"    color: rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#submit_button:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton#submit_button:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}")
        self.submit_button.setObjectName("submit_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(560, 580, 295, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fb_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.fb_button.setFont(font)
        self.fb_button.setStyleSheet("QPushButton#fb_button{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgba(85,98,112,255);\n"
"}\n"
"QPushButton#fb_button:hover{\n"
"    color: rgba(131,96,53,255);\n"
"}\n"
"QPushButton#fb_button:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"   color: rgba(91,88,53,255);\n"
"}")
        self.fb_button.setObjectName("fb_button")
        self.horizontalLayout.addWidget(self.fb_button)
        self.linkedin_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.linkedin_button.setFont(font)
        self.linkedin_button.setStyleSheet("QPushButton#linkedin_button{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgba(85,98,112,255);\n"
"}\n"
"QPushButton#linkedin_button:hover{\n"
"    color: rgba(131,96,53,255);\n"
"}\n"
"QPushButton#linkedin_button:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"   color: rgba(91,88,53,255);\n"
"}")
        self.linkedin_button.setObjectName("linkedin_button")
        self.horizontalLayout.addWidget(self.linkedin_button)
        self.git_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(20)
        self.git_button.setFont(font)
        self.git_button.setStyleSheet("QPushButton#git_button{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgba(85,98,112,255);\n"
"}\n"
"QPushButton#git_button:hover{\n"
"    color: rgba(131,96,53,255);\n"
"}\n"
"QPushButton#git_button:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"   color: rgba(91,88,53,255);\n"
"}")
        self.git_button.setObjectName("git_button")
        self.horizontalLayout.addWidget(self.git_button)
        self.minimize_button = QtWidgets.QPushButton(self.widget)
        self.minimize_button.setGeometry(QtCore.QRect(860, 40, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.minimize_button.setFont(font)
        self.minimize_button.setStyleSheet("QPushButton#minimize_button\n"
"{\n"
"font-family:\"Webdings\";\n"
"text-align:top;\n"
"background:#6DDF6D;border-radius:5px;\n"
"border:none;\n"
"font-size:13px;\n"
"}\n"
"QPushButton#minimize_button:hover{background:green;}")
        self.minimize_button.setObjectName("minimize_button")
        self.exit_button = QtWidgets.QPushButton(self.widget)
        self.exit_button.setGeometry(QtCore.QRect(890, 40, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("QPushButton#exit_button\n"
"{\n"
"font-family:\"Webdings\";\n"
"background:#F76677;border-radius:5px;\n"
"border:none;\n"
"font-size:13px;\n"
"}\n"
"QPushButton#exit_button:hover{background:red;}")
        self.exit_button.setObjectName("exit_button")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(510, 190, 371, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username_lineedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(15)
        self.username_lineedit.setFont(font)
        self.username_lineedit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.username_lineedit.setObjectName("username_lineedit")
        self.verticalLayout.addWidget(self.username_lineedit)
        self.pw_lineedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(15)
        self.pw_lineedit.setFont(font)
        self.pw_lineedit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.pw_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_lineedit.setObjectName("pw_lineedit")
        self.verticalLayout.addWidget(self.pw_lineedit)
        self.confirmpw_lineedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(15)
        self.confirmpw_lineedit.setFont(font)
        self.confirmpw_lineedit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.confirmpw_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpw_lineedit.setObjectName("confirmpw_lineedit")
        self.verticalLayout.addWidget(self.confirmpw_lineedit)

        self.retranslateUi(UI_rspw)
        QtCore.QMetaObject.connectSlotsByName(UI_rspw)
        ## set up button
        self.minimize_button.clicked.connect(UI_rspw.showMinimized)
        self.exit_button.clicked.connect(UI_rspw.close)
        self.git_button.clicked.connect(lambda: webbrowser.open('https://github.com/phuongngo2904'))
        self.linkedin_button.clicked.connect(lambda: webbrowser.open('https://linkedin.com/in/phuong-ngo-2904'))
        self.fb_button.clicked.connect(lambda: webbrowser.open('https://facebook.com/phuong.ngole.3'))

    def retranslateUi(self, UI_rspw):
        _translate = QtCore.QCoreApplication.translate
        UI_rspw.setWindowTitle(_translate("UI_rspw", "Reset Password"))
        self.submit_button.setText(_translate("UI_rspw", "Submit"))
        self.fb_button.setText(_translate("UI_rspw", "E"))
        self.linkedin_button.setText(_translate("UI_rspw", "h"))
        self.git_button.setText(_translate("UI_rspw", ")"))
        self.minimize_button.setText(_translate("UI_rspw", "0"))
        self.exit_button.setText(_translate("UI_rspw", "r"))
        self.username_lineedit.setPlaceholderText(_translate("UI_rspw", "User Name"))
        self.pw_lineedit.setPlaceholderText(_translate("UI_rspw", "New Password"))
        self.confirmpw_lineedit.setPlaceholderText(_translate("UI_rspw", "Confirm Password"))
