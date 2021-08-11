import webbrowser
from images import res
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NU_Form(object):
    def setupUi(self, NU_Form):
        NU_Form.setObjectName("NU_Form")
        NU_Form.resize(1052, 802)
        NU_Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        NU_Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(NU_Form)
        self.widget.setGeometry(QtCore.QRect(20, 10, 971, 771))
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
        self.label.setStyleSheet("border-image: url(images/2.jpg);\n"
"background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(479, 30, 441, 650))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(640, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgba(0,0,0,255);")
        self.label_3.setObjectName("label_3")
        self.signup_button = QtWidgets.QPushButton(self.widget)
        self.signup_button.setGeometry(QtCore.QRect(640, 540, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("QPushButton#signup_button{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85,98,112,226));\n"
"    color: rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#signup_button:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton#signup_button:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}")
        self.signup_button.setObjectName("signup_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(560, 590, 295, 80))
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
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(200, 70, 151, 51))
        self.label_5.setStyleSheet("font: 18pt \"Segoe Print\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(500, 90, 391, 431))
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
        self.fname_lineedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(15)
        self.fname_lineedit.setFont(font)
        self.fname_lineedit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.fname_lineedit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.fname_lineedit.setObjectName("fname_lineedit")
        self.verticalLayout.addWidget(self.fname_lineedit)
        self.midname_lineedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(15)
        self.midname_lineedit.setFont(font)
        self.midname_lineedit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.midname_lineedit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.midname_lineedit.setObjectName("midname_lineedit")
        self.verticalLayout.addWidget(self.midname_lineedit)
        self.lname_lineedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(15)
        self.lname_lineedit.setFont(font)
        self.lname_lineedit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lname_lineedit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lname_lineedit.setObjectName("lname_lineedit")
        self.verticalLayout.addWidget(self.lname_lineedit)
        self.email_lineedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(15)
        self.email_lineedit.setFont(font)
        self.email_lineedit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.email_lineedit.setObjectName("email_lineedit")
        self.verticalLayout.addWidget(self.email_lineedit)
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
        self.confirmpw_lineedit.setObjectName("confirmpw_lineedi")
        self.verticalLayout.addWidget(self.confirmpw_lineedit)

        self.retranslateUi(NU_Form)
        QtCore.QMetaObject.connectSlotsByName(NU_Form)
        ## set up button
        self.minimize_button.clicked.connect(NU_Form.showMinimized)
        self.exit_button.clicked.connect(NU_Form.close)
        self.git_button.clicked.connect(lambda: webbrowser.open('https://github.com/phuongngo2904'))
        self.linkedin_button.clicked.connect(lambda: webbrowser.open('https://linkedin.com/in/phuong-ngo-2904'))
        self.fb_button.clicked.connect(lambda: webbrowser.open('https://facebook.com/phuong.ngole.3'))
    def retranslateUi(self, NU_Form):
        _translate = QtCore.QCoreApplication.translate
        NU_Form.setWindowTitle(_translate("NU_Form", "Register"))
        self.label_3.setText(_translate("NU_Form", "Register"))
        self.signup_button.setText(_translate("NU_Form", "Sign Up"))
        self.fb_button.setText(_translate("NU_Form", "E"))
        self.linkedin_button.setText(_translate("NU_Form", "h"))
        self.git_button.setText(_translate("NU_Form", ")"))
        self.minimize_button.setText(_translate("NU_Form", "0"))
        self.exit_button.setText(_translate("NU_Form", "r"))
        self.label_5.setText(_translate("NU_Form", "New User"))
        self.username_lineedit.setPlaceholderText(_translate("NU_Form", "User Name"))
        self.fname_lineedit.setPlaceholderText(_translate("NU_Form", "First Name"))
        self.midname_lineedit.setPlaceholderText(_translate("NU_Form", "Middle Name"))
        self.lname_lineedit.setPlaceholderText(_translate("NU_Form", "Last Name"))
        self.email_lineedit.setPlaceholderText(_translate("NU_Form", "Email Address"))
        self.pw_lineedit.setPlaceholderText(_translate("NU_Form", "Password"))
        self.confirmpw_lineedit.setPlaceholderText(_translate("NU_Form", "Confirm Password"))