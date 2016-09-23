# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(580, 420, 113, 32))
        self.exit.setObjectName("exit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(260, 370, 104, 41))
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 110, 59, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 240, 59, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 380, 59, 16))
        self.label_3.setObjectName("label_3")
        self.finishButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishButton.setGeometry(QtCore.QRect(580, 380, 113, 32))
        self.finishButton.setObjectName("finishButton")
        self.priceInput = QtWidgets.QTextEdit(self.centralwidget)
        self.priceInput.setGeometry(QtCore.QRect(260, 420, 104, 21))
        self.priceInput.setObjectName("priceInput")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 420, 59, 16))
        self.label_4.setObjectName("label_4")
        self.startCalender = QtWidgets.QCalendarWidget(self.centralwidget)
        self.startCalender.setGeometry(QtCore.QRect(250, 110, 296, 111))
        self.startCalender.setObjectName("startCalender")
        self.endCalender = QtWidgets.QCalendarWidget(self.centralwidget)
        self.endCalender.setGeometry(QtCore.QRect(250, 240, 296, 111))
        self.endCalender.setObjectName("endCalender")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.currentIndexChanged['int'].connect(MainWindow.itemlistSelected)
        self.exit.clicked.connect(MainWindow.exit)
        self.startCalender.clicked['QDate'].connect(MainWindow.beginDate)
        self.endCalender.clicked['QDate'].connect(MainWindow.endDate)
        self.priceInput.textChanged.connect(MainWindow.getPrice)
        self.finishButton.clicked.connect(MainWindow.onAddFinished)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "参数表生成器"))
        self.exit.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "起始日期"))
        self.label_2.setText(_translate("MainWindow", "截止日期"))
        self.label_3.setText(_translate("MainWindow", "选择种类"))
        self.finishButton.setText(_translate("MainWindow", "添加完成"))
        self.label_4.setText(_translate("MainWindow", "单价"))

