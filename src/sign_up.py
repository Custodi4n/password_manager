from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_create_user(object):
    def setupUi(self, create_user):
        create_user.setObjectName("create_user")
        create_user.resize(400, 308)
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(16)
        create_user.setFont(font)
        create_user.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.lineEdit = QtWidgets.QLineEdit(parent=create_user)
        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-style: solid;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-color: white;\n"
"border-radius: 10% 10%;\n"
"text-align: center;\n"
"text-color: white;")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=create_user)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 130, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-style: solid;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-color: white;\n"
"border-radius: 10% 10%;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=create_user)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 190, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-style: solid;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-color: white;\n"
"border-radius: 10% 10%;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(parent=create_user)
        self.label.setGeometry(QtCore.QRect(66, 70, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=create_user)
        self.label_2.setGeometry(QtCore.QRect(33, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=create_user)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=create_user)
        self.pushButton.setGeometry(QtCore.QRect(158, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: white;\n"
"border-radius: 10% 10%;\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(create_user)
        QtCore.QMetaObject.connectSlotsByName(create_user)

    def retranslateUi(self, create_user):
        _translate = QtCore.QCoreApplication.translate
        create_user.setWindowTitle(_translate("create_user", "PassGuard"))
        self.label.setText(_translate("create_user", "Login"))
        self.label_2.setText(_translate("create_user", "Password"))
        self.label_3.setText(_translate("create_user", "Master-pass"))
        self.pushButton.setText(_translate("create_user", "Sign up"))