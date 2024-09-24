import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow, QTableWidgetItem
from login_form import Ui_login_form
from create_db import login_user, create_user, view_all_data, check_master_password, add_password, delete_data
from main_window import Ui_Main_menu
from sites_window import Ui_Sites_window
from sign_up import Ui_create_user
from check_window import Ui_Dialog
import pandas as pd
import webbrowser

user_id = 1

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login_form()
        self.ui.setupUi(self)
        self.ui.enter_button.clicked.connect(self.authenticate)
        self.ui.enter_button_2.clicked.connect((self.open_sign_up_window))
        self.show()

    def authenticate(self):
        enter_login = self.ui.login_password.text()
        enter_password = self.ui.line_password.text()
        if login_user(enter_login, enter_password) == False:
            QMessageBox.critical(self, 'Error', "Неверный логин или пароль!")
        else:
            user_id = login_user(enter_login, enter_password)
            QMessageBox.information(self, 'Success', "Успешный вход!")
            self.open_main_window()
            return user_id
        
    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def open_sign_up_window(self):
        self.sign_up_window = Sign_Up()
        self.sign_up_window.show()
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main_menu()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton_2.clicked.connect(self.open_sites_window)
        self.ui.pushButton_3.clicked.connect(self.github_link)
        self.ui.pushButton_4.clicked.connect(self.youtube_link)
        self.ui.pushButton_5.clicked.connect(self.discord_link)
        self.ui.pushButton_6.clicked.connect(self.vk_link)
        self.ui.pushButton_7.clicked.connect(self.gmail_link)
        self.ui.pushButton_8.clicked.connect(self.telegram_link)

    def open_sites_window(self):
        self.sites_window = SitesWindow()
        self.sites_window.show()
        self.close()

    def github_link(self):
        webbrowser.open_new('https://github.com/login')

    def youtube_link(self):
        webbrowser.open_new('https://www.youtube.com/')

    def discord_link(self):
        webbrowser.open_new('https://discord.com/')

    def vk_link(self):
        webbrowser.open_new('https://vk.com/feed')

    def gmail_link(self):
        webbrowser.open_new('https://mail.google.com/mail/u/0/#inbox')

    def telegram_link(self):
        webbrowser.open_new('https://telegram.org/')

class SitesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Sites_window()
        self.ui.setupUi(self)
        self.show()
        self.ui.Home_button.clicked.connect(self.open_main_window)
        self.ui.pushButton_3.clicked.connect(self.view_all_data)
        self.ui.pushButton_4.clicked.connect(self.add_data)
        self.ui.pushButton_5.clicked.connect(self.del_data)

    def view_all_data(self):
        print(user_id)
        if check_master_password(user_id, self.ui.lineEdit_3.text()):
            data = pd.DataFrame(view_all_data(user_id), columns=['website', 'username', 'password'])
            print(data)
            for i in range(0, data.shape[0]):
                print(data.shape[0])
                print(i)
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(data.iloc[i][0]))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(data.iloc[i][1]))
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(data.iloc[i][2]))
                i += 1

    def add_data(self):
        enter_website = self.ui.login_password.text()
        enter_username = self.ui.line_password.text()
        enter_password = self.ui.line_password_2.text()
        add_password(user_id, enter_website, enter_username, enter_password)

    def del_data(self):
        enter_id_line = self.ui.login_password_2.text()
        delete_data(user_id, enter_id_line)

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class Sign_Up(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_create_user()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton.clicked.connect(self.reg)

    def reg(self):
        enter_login = self.ui.lineEdit.text()
        enter_password = self.ui.lineEdit_2.text()
        enter_master_pass = self.ui.lineEdit_3.text()
        if create_user(enter_login, enter_password, enter_master_pass):
            user_id = create_user(enter_login, enter_password, enter_master_pass)
            QMessageBox.information(self, 'Success', "Успешный вход!")
            self.open_main_window()
            return user_id
        else:
            QMessageBox.critical(self, 'Error', "Введены некорректные данные!")

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    sys.exit(app.exec())