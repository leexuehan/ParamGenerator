# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticket.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ticket_Dialog(object):
    def setupUi(self, Ticket_Dialog):
        Ticket_Dialog.setObjectName("Ticket_Dialog")
        Ticket_Dialog.resize(400, 300)
        self.ticket_name_label = QtWidgets.QLabel(Ticket_Dialog)
        self.ticket_name_label.setGeometry(QtCore.QRect(80, 60, 91, 16))
        self.ticket_name_label.setObjectName("ticket_name_label")
        self.ticket_name_content = QtWidgets.QTextEdit(Ticket_Dialog)
        self.ticket_name_content.setGeometry(QtCore.QRect(170, 50, 71, 31))
        self.ticket_name_content.setObjectName("ticket_name_content")
        self.ticket_price_label = QtWidgets.QLabel(Ticket_Dialog)
        self.ticket_price_label.setGeometry(QtCore.QRect(80, 110, 91, 16))
        self.ticket_price_label.setObjectName("ticket_price_label")
        self.ticket_price_content = QtWidgets.QTextEdit(Ticket_Dialog)
        self.ticket_price_content.setGeometry(QtCore.QRect(170, 100, 71, 31))
        self.ticket_price_content.setObjectName("ticket_price_content")
        self.confirm = QtWidgets.QPushButton(Ticket_Dialog)
        self.confirm.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(Ticket_Dialog)
        self.cancel.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(Ticket_Dialog)
        self.cancel.clicked.connect(Ticket_Dialog.reject)
        self.confirm.clicked.connect(Ticket_Dialog.on_ok)
        QtCore.QMetaObject.connectSlotsByName(Ticket_Dialog)

    def retranslateUi(self, Ticket_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Ticket_Dialog.setWindowTitle(_translate("Ticket_Dialog", "Dialog"))
        self.ticket_name_label.setText(_translate("Ticket_Dialog", "输入票种名称"))
        self.ticket_price_label.setText(_translate("Ticket_Dialog", "输入票种价格"))
        self.confirm.setText(_translate("Ticket_Dialog", "确定"))
        self.cancel.setText(_translate("Ticket_Dialog", "取消"))

