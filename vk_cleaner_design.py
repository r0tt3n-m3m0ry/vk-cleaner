# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\vk_cleaner_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vk_cleaner(object):
    def setupUi(self, vk_cleaner):
        vk_cleaner.setObjectName("vk_cleaner")
        vk_cleaner.resize(703, 490)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        vk_cleaner.setFont(font)
        self.centralwidget = QtWidgets.QWidget(vk_cleaner)
        self.centralwidget.setObjectName("centralwidget")
        self.checkbox_clear_wall = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_clear_wall.setGeometry(QtCore.QRect(40, 70, 111, 31))
        self.checkbox_clear_wall.setObjectName("checkbox_clear_wall")
        self.checkbox_clear_friends = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_clear_friends.setGeometry(QtCore.QRect(40, 120, 121, 31))
        self.checkbox_clear_friends.setObjectName("checkbox_clear_friends")
        self.checkbox_clear_subscriptions = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_clear_subscriptions.setGeometry(QtCore.QRect(40, 220, 151, 31))
        self.checkbox_clear_subscriptions.setObjectName("checkbox_clear_subscriptions")
        self.checkbox_clear_groups = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_clear_groups.setGeometry(QtCore.QRect(40, 170, 121, 31))
        self.checkbox_clear_groups.setObjectName("checkbox_clear_groups")
        self.checkbox_clear_messages = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_clear_messages.setGeometry(QtCore.QRect(40, 270, 181, 31))
        self.checkbox_clear_messages.setObjectName("checkbox_clear_messages")
        self.checkbox_clear_photos = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_clear_photos.setGeometry(QtCore.QRect(40, 320, 181, 31))
        self.checkbox_clear_photos.setObjectName("checkbox_clear_photos")
        self.vk_clear = QtWidgets.QPushButton(self.centralwidget)
        self.vk_clear.setGeometry(QtCore.QRect(40, 370, 171, 51))
        self.vk_clear.setObjectName("vk_clear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 171, 31))
        self.label.setObjectName("label")
        self.log_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.log_browser.setGeometry(QtCore.QRect(270, 20, 401, 401))
        self.log_browser.setObjectName("log_browser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 440, 641, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        vk_cleaner.setCentralWidget(self.centralwidget)

        self.retranslateUi(vk_cleaner)
        QtCore.QMetaObject.connectSlotsByName(vk_cleaner)

    def retranslateUi(self, vk_cleaner):
        _translate = QtCore.QCoreApplication.translate
        vk_cleaner.setWindowTitle(_translate("vk_cleaner", "MainWindow"))
        self.checkbox_clear_wall.setText(_translate("vk_cleaner", "Стена"))
        self.checkbox_clear_friends.setText(_translate("vk_cleaner", "Друзья"))
        self.checkbox_clear_subscriptions.setText(_translate("vk_cleaner", "Подписки"))
        self.checkbox_clear_groups.setText(_translate("vk_cleaner", "Группы"))
        self.checkbox_clear_messages.setText(_translate("vk_cleaner", "Сообщения"))
        self.checkbox_clear_photos.setText(_translate("vk_cleaner", "Фотографии"))
        self.vk_clear.setText(_translate("vk_cleaner", "Очиситить!"))
        self.label.setText(_translate("vk_cleaner", "Что чистим?"))
        self.log_browser.setPlaceholderText(_translate("vk_cleaner", "Логи будут выводиться сюда"))
        self.label_2.setText(_translate("vk_cleaner", "Vk Cleaner by r0tt3n-m3m0ry v1.0"))
