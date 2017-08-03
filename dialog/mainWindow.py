# -*- coding: utf-8 -*-
from dialog.calendarDialog import CalendarDialog
from dialog.ticketDialog import TicketDialog
from ui.app import Ui_MainWindow

__author__ = 'leexuehan@github.com'

import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from utils.excelOps import ExcelOps


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
        self.coal_sorts = []
        self.load_coal_sorts()
        self.ticket_sorts = []
        self.load_ticket_sorts()

    def load_coal_sorts(self):
        self.ui.coal_sorts.clear()
        with open('sortlist.txt', 'r', encoding='utf-8') as file:
            for line in file:
                self.coal_sorts.append(line.strip())
            self.ui.coal_sorts.addItems(self.coal_sorts)
        self.coalSortsSelected = self.coal_sorts[0]

    def load_ticket_sorts(self):
        self.ui.ticket_sorts.clear()
        with open('ticketlist.txt', 'r', encoding='utf-8') as file:
            for line in file:
                self.ticket_sorts.append(line.strip())
            self.ui.ticket_sorts.addItems(self.ticket_sorts)

    def onCoalSortSelected(self, item):
        # 获得条目
        coalSorts = self.coal_sorts[item]
        self.coalSortsSelected = coalSorts

    def getPrice(self):
        # 获得单价
        pass

    def exportTable(self, beginDate, endDate, price):
        # 导出每一次添加
        with open('添加备份.txt', 'a') as file:
            addtime = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
            content = str(self.beginDate) + '~' + str(
                self.endDate) + ',' + self.coalSortsSelected + ',' + self.price + '\n'
            file.write(str(addtime) + '添加了:' + content)

    def onAddFinished(self):
        # 校验输入是否完整
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

    def on_date_selected(self):
        calendarDialog = CalendarDialog()
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.date_value_display.setPlainText(date.strftime('%Y/%m/%d'))
        calendarDialog.destroy()

    def on_name_input(self):
        print("input name is", self.ui.usernmae_content.text())

    def on_input_car_id(self):
        print("input car id is", self.ui.car_id_content.text())

    def on_weight_value_input(self):
        print("input weight value is", self.ui.weight_value.text())
        print("input weight value2 is", self.ui.weight_value_2.text())

    def exit(self):
        sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
