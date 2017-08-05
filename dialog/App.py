# -*- coding: utf-8 -*-
from dialog.CoalDialog import CoalDialog
from dialog.calendarDialog import CalendarDialog
from dialog.TicketDialog import TicketDialog
from ui.main_window import Ui_MainWindow
from utils.ConfigFileUtils import ConfigFileUtils
from utils.SqlUtils import SqlUtils

__author__ = 'leexuehan@github.com'

import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # init ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # init comboBox
        self.coal_sorts = []
        self.load_coal_sorts_from_db()
        self.ticket_sorts = []
        self.load_ticket_sorts_from_db()

        # init param table
        # self.excelOps = ExcelOps()
        # self.excelOps.generate_param_table()

        # init input
        self.select_date = None
        self.beginDate = None
        self.endDate = None
        self.price = None
        self.coal_sorts_selected = None

    def load_coal_sorts_from_db(self):
        self.ui.coal_sorts.clear()
        coal_list = SqlUtils().query_all_tickets_name()
        for coal in coal_list:
            self.coal_sorts.append(coal[0])
        # coal_list = ConfigFileUtils.read_sort_list('coals')
        # for coal in coal_list:
        #     self.coal_sorts.append(coal.strip())
        self.ui.coal_sorts.addItems(self.coal_sorts)
        self.coal_sorts_selected = self.coal_sorts[0]

    def load_ticket_sorts_from_db(self):
        self.ui.ticket_sorts.clear()
        ticket_list = ConfigFileUtils.read_sort_list('tickets')
        for ticket in ticket_list:
            self.ticket_sorts.append(ticket.strip())
        self.ui.ticket_sorts.addItems(self.ticket_sorts)

    def onCoalSortSelected(self, item):
        # 获得条目
        coalSorts = self.coal_sorts[item]
        self.coal_sorts_selected = coalSorts

    def on_ticket_selected(self, item):
        ticket_name = self.ticket_sorts[item]
        self.ticket_selected = ticket_name

    def exportTable(self, beginDate, endDate, price):
        # 导出每一次添加
        with open('添加备份.txt', 'a') as file:
            addtime = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
            content = str(self.beginDate) + '~' + str(
                self.endDate) + ',' + self.coal_sorts_selected + ',' + self.price + '\n'
            file.write(str(addtime) + '添加了:' + content)

    # 添加记录“逐车明细”
    def on_record_add(self):
        print("ready to add record!!!!!!!!!!!111")
        # 校验输入是否完整
        # 数据库存一份，excel 存一份
        print(self.select_date, type(self.select_date))
        SqlUtils().add_record_by_car_detail(self.select_date, self.person_name, self.car_id,
                                            self.coal_sorts_selected,
                                            self.weight_value, self.ticket_selected)
        QMessageBox.information(self, 'add finished', '添加成功!此次添加的内容已经导出到本地备份文件中', QMessageBox.Yes)

    def verifyInput(self):
        if self.coal_sorts_selected == None:
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

    def on_add_new_ticket(self):
        ticketDialog = TicketDialog()
        ticketDialog.show()
        ticketDialog.exec_()

    def on_add_new_coal(self):
        coalDialog = CoalDialog()
        coalDialog.show()
        coalDialog.exec_()

    def on_date_selected(self):
        calendarDialog = CalendarDialog()
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.date_value_display.setPlainText(date.strftime('%Y/%m/%d'))
            self.select_date = date.strftime('%Y/%m/%d')
        calendarDialog.destroy()

    def on_name_input(self):
        print("input name is", self.ui.usernmae_content.text())
        self.person_name = self.ui.usernmae_content.text()

    def on_input_car_id(self):
        print("input car id is", self.ui.car_id_content.text())
        self.car_id = self.ui.car_id_content.text()

    def on_weight_value_input(self):
        print("input weight value is", self.ui.weight_value.text())
        self.weight_value = self.ui.weight_value.text()

    def exit(self):
        sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())