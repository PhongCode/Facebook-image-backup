# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'theme.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class LoginClass(object):
    def setupUi(self, Login_page):
        Login_page.setObjectName("Login_page")
        Login_page.resize(503, 358)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login_page.setWindowIcon(icon)
        Login_page.setStyleSheet("QMainWindow {\n"
"    border: solid white 5px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Login_page)
        self.centralwidget.setStyleSheet("QWidget#centralwidget {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.00568182 rgba(170, 85, 127, 255), stop:0.988636 rgba(109, 25, 27, 255), stop:1 rgba(66, 164, 255, 255));\n"
"}\n"
"  \n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.Cookie = QtWidgets.QGroupBox(self.centralwidget)
        self.Cookie.setGeometry(QtCore.QRect(30, 60, 441, 231))
        self.Cookie.setStyleSheet("QGroupBox {\n"
"    background-color: #FFF;\n"
"    border: none;\n"
"}\n"
"  \n"
"")
        self.Cookie.setTitle("")
        self.Cookie.setObjectName("Cookie")
        self.Browser = QtWidgets.QPushButton(self.Cookie)
        self.Browser.setGeometry(QtCore.QRect(190, 110, 38, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Browser.setFont(font)
        self.Browser.setStyleSheet("QPushButton#Browser:hover:!pressed\n"
"{\n"
"      background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(64, 64, 64, 255));\n"
"}\n"
"QPushButton#Browser {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.00568182 rgba(170, 85, 127, 255), stop:0.988636 rgba(109, 25, 27, 255), stop:1 rgba(66, 164, 255, 255));\n"
"    border: none; \n"
"    color: white;\n"
"    border-bottom-left-radius : 10px;\n"
"    border-top-left-radius : 10px;\n"
"}\n"
"\n"
"QPushButton#Browser:disabled {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(64, 64, 64, 255));\n"
"}")
        self.Browser.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("static/folder-open-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Browser.setIcon(icon1)
        self.Browser.setIconSize(QtCore.QSize(20, 20))
        self.Browser.setObjectName("Browser")
        self.Filename = QtWidgets.QLabel(self.Cookie)
        self.Filename.setGeometry(QtCore.QRect(190, 110, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Filename.setFont(font)
        self.Filename.setStyleSheet("QLabel#Filename {\n"
"      background-color:  #ddd;\n"
"      border: none; \n"
"    color: #000;\n"
"    border-radius: 10px;\n"
"}")
        self.Filename.setScaledContents(False)
        self.Filename.setWordWrap(False)
        self.Filename.setIndent(50)
        self.Filename.setObjectName("Filename")
        self.label = QtWidgets.QLabel(self.Cookie)
        self.label.setGeometry(QtCore.QRect(160, 20, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.LoginImage = QtWidgets.QLabel(self.Cookie)
        self.LoginImage.setGeometry(QtCore.QRect(0, 0, 161, 231))
        self.LoginImage.setText("")
        self.LoginImage.setPixmap(QtGui.QPixmap("static/login-background.jpg"))
        self.LoginImage.setScaledContents(True)
        self.LoginImage.setObjectName("LoginImage")
        self.Notes = QtWidgets.QLabel(self.Cookie)
        self.Notes.setGeometry(QtCore.QRect(160, 210, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.Notes.setFont(font)
        self.Notes.setAcceptDrops(False)
        self.Notes.setStyleSheet("QLabel#Author {\n"
"    color: #fff;\n"
"}")
        self.Notes.setScaledContents(False)
        self.Notes.setAlignment(QtCore.Qt.AlignCenter)
        self.Notes.setObjectName("Notes")
        self.Login = QtWidgets.QPushButton(self.Cookie)
        self.Login.setGeometry(QtCore.QRect(190, 150, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Login.setFont(font)
        self.Login.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"      \n"
"      background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(64, 64, 64, 255));\n"
"}\n"
"QPushButton {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.00568182 rgba(170, 85, 127, 255), stop:0.988636 rgba(109, 25, 27, 255), stop:1 rgba(66, 164, 255, 255));\n"
"    border: none; \n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    \n"
"      background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(64, 64, 64, 255));\n"
"}")
        self.Login.setIconSize(QtCore.QSize(24, 24))
        self.Login.setObjectName("Login")
        self.Filename.raise_()
        self.Browser.raise_()
        self.label.raise_()
        self.LoginImage.raise_()
        self.Notes.raise_()
        self.Login.raise_()
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(20, 330, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setStyleSheet("QLabel#Title {\n"
"    color: #fff;\n"
"}")
        self.Title.setScaledContents(True)
        self.Title.setWordWrap(False)
        self.Title.setIndent(0)
        self.Title.setObjectName("Title")
        self.Icon = QtWidgets.QLabel(self.centralwidget)
        self.Icon.setGeometry(QtCore.QRect(-5, 333, 21, 21))
        self.Icon.setText("")
        self.Icon.setPixmap(QtGui.QPixmap("static/logo.png"))
        self.Icon.setScaledContents(True)
        self.Icon.setObjectName("Icon")
        self.Description = QtWidgets.QLabel(self.centralwidget)
        self.Description.setGeometry(QtCore.QRect(20, 343, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(4)
        font.setBold(False)
        font.setWeight(50)
        self.Description.setFont(font)
        self.Description.setStyleSheet("QLabel#Description {\n"
"    color: #fff;\n"
"}")
        self.Description.setObjectName("Description")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 43, 20))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: none;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Mini = QtWidgets.QPushButton(self.groupBox)
        self.Mini.setGeometry(QtCore.QRect(23, 2, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Mini.setFont(font)
        self.Mini.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"    background-color: rgb(72, 72, 72);\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(131, 131, 131);\n"
"    border-radius: 8px;\n"
"}")
        self.Mini.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("static/minimum-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Mini.setIcon(icon2)
        self.Mini.setIconSize(QtCore.QSize(12, 12))
        self.Mini.setObjectName("Mini")
        self.Exit = QtWidgets.QPushButton(self.groupBox)
        self.Exit.setGeometry(QtCore.QRect(3, 2, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Exit.setFont(font)
        self.Exit.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"    background-color: rgb(107, 0, 0);\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(170, 85, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.Exit.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("static/times-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit.setIcon(icon3)
        self.Exit.setIconSize(QtCore.QSize(12, 12))
        self.Exit.setObjectName("Exit")
        self.Author = QtWidgets.QLabel(self.centralwidget)
        self.Author.setGeometry(QtCore.QRect(390, 340, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.Author.setFont(font)
        self.Author.setAcceptDrops(False)
        self.Author.setStyleSheet("QLabel#Author {\n"
"    color: #FFF;\n"
"}")
        self.Author.setScaledContents(False)
        self.Author.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Author.setObjectName("Author")
        Login_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_page)
        QtCore.QMetaObject.connectSlotsByName(Login_page)

    def retranslateUi(self, Login_page):
        _translate = QtCore.QCoreApplication.translate
        Login_page.setWindowTitle(_translate("Login_page", "Facekup - Download everything"))
        self.Filename.setText(_translate("Login_page", "Browse your cookie.json"))
        self.label.setText(_translate("Login_page", "IMPORT COOKIE"))
        self.Notes.setText(_translate("Login_page", "Facekup use J2Team cookie extension to create login session"))
        self.Login.setText(_translate("Login_page", "Log In"))
        self.Title.setText(_translate("Login_page", "Facekup"))
        self.Description.setText(_translate("Login_page", "Facebook image backup version 1.0.19"))
        self.Author.setText(_translate("Login_page", "www.nguyentrieuphong.com "))