import webbrowser
from images import res
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1068, 841)
        mainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        mainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(29, 10, 971, 771))
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
        self.label.setStyleSheet("border-image: url(:/images/4.jpg);\n"
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
        self.label_3.setGeometry(QtCore.QRect(660, 160, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgba(0,0,0,255);")
        self.label_3.setObjectName("label_3")
        self.username_lineedit = QtWidgets.QLineEdit(self.widget)
        self.username_lineedit.setGeometry(QtCore.QRect(530, 240, 341, 41))
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
        self.pw_lineedit = QtWidgets.QLineEdit(self.widget)
        self.pw_lineedit.setGeometry(QtCore.QRect(530, 310, 341, 41))
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
        self.Login_button = QtWidgets.QPushButton(self.widget)
        self.Login_button.setGeometry(QtCore.QRect(580, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Login_button.setFont(font)
        self.Login_button.setStyleSheet("QPushButton#Login_button{\n"
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
        self.Login_button.setObjectName("Login_button")
        self.reset_button = QtWidgets.QPushButton(self.widget)
        self.reset_button.setGeometry(QtCore.QRect(660, 500, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.reset_button.setFont(font)
        self.reset_button.setStyleSheet("QPushButton#reset_button{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85,98,112,226));\n"
"    color: rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#reset_button:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton#reset_button:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}")
        self.reset_button.setObjectName("reset_button")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(590, 470, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgba(0,0,0,210);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(560, 570, 295, 80))
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
        self.new_user_button = QtWidgets.QPushButton(self.widget)
        self.new_user_button.setGeometry(QtCore.QRect(720, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_user_button.setFont(font)
        self.new_user_button.setStyleSheet("QPushButton#new_user_button{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85,98,112,226));\n"
"    color: rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#new_user_button:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton#new_user_button:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}")
        self.new_user_button.setObjectName("new_user_button")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(70, 390, 391, 51))
        self.label_5.setStyleSheet("font: 18pt \"Segoe Print\";")
        self.label_5.setObjectName("label_5")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        ## set up button
        self.minimize_button.clicked.connect(mainWindow.showMinimized)
        self.exit_button.clicked.connect(mainWindow.close)
        self.git_button.clicked.connect(lambda: webbrowser.open('https://github.com/phuongngo2904'))
        self.linkedin_button.clicked.connect(lambda: webbrowser.open('https://linkedin.com/in/phuong-ngo-2904'))
        self.fb_button.clicked.connect(lambda: webbrowser.open('https://facebook.com/phuong.ngole.3'))

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "ASL Learning Application"))
        self.label_3.setText(_translate("mainWindow", "Log In"))
        self.username_lineedit.setPlaceholderText(_translate("mainWindow", "User Name"))
        self.pw_lineedit.setPlaceholderText(_translate("mainWindow", "Password"))
        self.Login_button.setText(_translate("mainWindow", "Log In"))
        self.reset_button.setText(_translate("mainWindow", "Reset"))
        self.label_4.setText(_translate("mainWindow", "Forgor Username or Password ?"))
        self.fb_button.setText(_translate("mainWindow", "E"))
        self.linkedin_button.setText(_translate("mainWindow", "h"))
        self.git_button.setText(_translate("mainWindow", ")"))
        self.minimize_button.setText(_translate("mainWindow", "0"))
        self.exit_button.setText(_translate("mainWindow", "r"))
        self.new_user_button.setText(_translate("mainWindow", "New User"))
        self.label_5.setText(_translate("mainWindow", "ASL Learning Application"))