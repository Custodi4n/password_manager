from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_login_form(object):
    def setupUi(self, login_form):
        login_form.setObjectName("login_form")
        login_form.resize(406, 308)
        login_form.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.login_text = QtWidgets.QLabel(parent=login_form)
        self.login_text.setGeometry(QtCore.QRect(63, 88, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(14)
        self.login_text.setFont(font)
        self.login_text.setStyleSheet("color: white;")
        self.login_text.setObjectName("login_text")
        self.password_text = QtWidgets.QLabel(parent=login_form)
        self.password_text.setGeometry(QtCore.QRect(30, 147, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(14)
        self.password_text.setFont(font)
        self.password_text.setStyleSheet("color: white;")
        self.password_text.setObjectName("password_text")
        self.login_password = QtWidgets.QLineEdit(parent=login_form)
        self.login_password.setGeometry(QtCore.QRect(130, 83, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(10)
        self.login_password.setFont(font)
        self.login_password.setStyleSheet("border-style: solid;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-color: white;\n"
"border-radius: 10% 10%;\n"
"text-align: center;\n"
"text-color: white;")
        self.login_password.setText("")
        self.login_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.login_password.setObjectName("login_password")
        self.line_password = QtWidgets.QLineEdit(parent=login_form)
        self.line_password.setGeometry(QtCore.QRect(130, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(10)
        self.line_password.setFont(font)
        self.line_password.setStyleSheet("border-style: solid;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-color: white;\n"
"border-radius: 10% 10%;\n"
"text-align: center;\n"
"text-color: white;")
        self.line_password.setText("")
        self.line_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_password.setObjectName("line_password")
        self.enter_button = QtWidgets.QPushButton(parent=login_form)
        self.enter_button.setGeometry(QtCore.QRect(130, 192, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(14)
        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet("color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: white;\n"
"border-radius: 10% 10%;\n"
"")
        self.enter_button.setObjectName("enter_button")
        self.enter_button_2 = QtWidgets.QPushButton(parent=login_form)
        self.enter_button_2.setGeometry(QtCore.QRect(220, 192, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(14)
        self.enter_button_2.setFont(font)
        self.enter_button_2.setStyleSheet("color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: white;\n"
"border-radius: 10% 10%;\n"
"")
        self.enter_button_2.setObjectName("enter_button_2")

        self.retranslateUi(login_form)
        QtCore.QMetaObject.connectSlotsByName(login_form)

    def retranslateUi(self, login_form):
        _translate = QtCore.QCoreApplication.translate
        login_form.setWindowTitle(_translate("login_form", "PassGuard"))
        self.login_text.setText(_translate("login_form", "Login"))
        self.password_text.setText(_translate("login_form", "Password"))
        self.enter_button.setText(_translate("login_form", "Sign in"))
        self.enter_button_2.setText(_translate("login_form", "Sign up"))