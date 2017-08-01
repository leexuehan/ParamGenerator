# -*- coding: utf-8 -*-
from app import Ui_MainWindow
from ticketDialog import TicketDialog

__author__ = 'leexuehan@github.com'

import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from excelOps import ExcelOps


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # init param table
        self.excelOps = ExcelOps()
        self.excelOps.generate_param_table()

        # init ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # init input
        self.beginDate = None
        self.endDate = None
        self.price = None
        self.coalSortsSelected = None

        # init comboBox
        self.sorts = []
        self.init_item_list()

    def init_item_list(self):
        self.ui.coalSorts.clear()
        with open('sortlist.txt', 'r', encoding='utf-8') as file:
            for line in file:
                self.sorts.append(line.strip())
            self.ui.coalSorts.addItems(self.sorts)
        self.coalSortsSelected = self.sorts[0]

    def onCoalSortSelected(self, item):
        # 获得条目
        coalSorts = self.sorts[item]
        print(coalSorts)
        if coalSorts == '添加煤种':
            print("开始添加新煤种.....")
        else:
            self.coalSortsSelected = coalSorts

    def getPrice(self):
        # 获得单价
        print(self.ui.priceInput.toPlainText())
        self.price = self.ui.priceInput.toPlainText()

    def exportTable(self, beginDate, endDate, price):
        # 导出每一次添加
        with open('添加备份.txt', 'a') as file:
            addtime = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
            content = str(self.beginDate) + '~' + str(
                self.endDate) + ',' + self.coalSortsSelected + ',' + self.price + '\n'
            file.write(str(addtime) + '添加了:' + content)

    def onAddFinished(self):
        # 校验输入是否完整
        if not self.verifyInput():
            return
        # 一次添加完成
        if not self.excelOps.update_param_table(self.coalSortsSelected, self.price, self.beginDate, self.endDate):
            QMessageBox.information(self, 'date select', '起始日期不能大于截止日期', QMessageBox.Yes)
            return
        # 导出此次添加到备份文件
        self.exportTable(self.beginDate, self.endDate, self.price)
        # 弹出成功消息框
        QMessageBox.information(self, 'add finished', '添加成功!此次添加的内容已经导出到本地备份文件中', QMessageBox.Yes)

    def beginDate(self):
        print(self.ui.startCalender.selectedDate().toPyDate())
        self.beginDate = str(self.ui.startCalender.selectedDate().toPyDate())

    def endDate(self):
        print(self.ui.endCalender.selectedDate().toPyDate())
        self.endDate = str(self.ui.endCalender.selectedDate().toPyDate())

    def verifyInput(self):
        if self.coalSortsSelected == None:
            QMessageBox.information(self, 'add finished', '没有选择种类', QMessageBox.Yes)
            return False
        elif self.beginDate == None:
            QMessageBox.information(self, 'add finished', '没有选择起始日期', QMessageBox.Yes)
            return False
        elif self.endDate == None:
            QMessageBox.information(self, 'add finished', '没有选择截止日期', QMessageBox.Yes)
            return False
        elif self.price == None:
            QMessageBox.information(self, 'add finished', '没有输入单价', QMessageBox.Yes)
            return False
        else:
            return True

    def invokeHelp(self):
        QMessageBox.information(self, 'invoke help', '帮助内容', QMessageBox.Yes)

    def invokeEdit(self):
        print('invoke edit')
        QMessageBox.information(self, 'invoke help', 'jj', QMessageBox.Yes)

    def manage_ticket(self):
        ticketDialog = TicketDialog()
        ticketDialog.show()
        ticketDialog.exec_()

    def exit(self):
        sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
