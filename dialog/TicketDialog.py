# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog

from dialog.calendarDialog import CalendarDialog
from ui.ticket import Ui_Ticket_Dialog
from utils.ConfigFileUtils import ConfigFileUtils
from utils.SqlUtils import SqlUtils


class TicketDialog(QDialog):
    def __init__(self, parent=None):
        super(TicketDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Ticket_Dialog()
        self.ui.setupUi(self)

        # init compute ways
        self.load_compute_ways()

    def load_compute_ways(self):
        self.ui.purchase_compute_way.clear()
        self.compute_ways = []
        ways = ConfigFileUtils.read_sort_list('compute_ways')
        for way in ways:
            self.compute_ways.append(way.strip())
        self.ui.purchase_compute_way.addItems(self.compute_ways)
        self.ui.sell_compute_way.addItems(self.compute_ways)

    def on_purchase_price_compute_way_selected(self, item):
        compute_way = self.compute_ways[item]
        self.purchase_price_compute_way_selected = compute_way

    def on_sell_price_compute_way_selected(self, item):
        compute_way = self.compute_ways[item]
        self.sell_price_compute_way_selected = compute_way

    def on_ticket_add_date_selected(self):
        calendarDialog = CalendarDialog()
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.date_value_display.setPlainText(date.strftime('%Y/%m/%d'))
            self.ticket_add_date = date.strftime('%Y/%m/%d')
        calendarDialog.destroy()

    def on_ok(self):
        ticket_name = self.ui.ticket_name_content.toPlainText()
        ticket_purchase_price = self.ui.ticket_purchase_price_content.toPlainText()
        ticket_sell_price = self.ui.ticket_sell_price_content.toPlainText()
        print("add new ticket info (添加日期，票名，进价，进价计费方式，售价，售价计费方式):",
              (self.ticket_add_date, ticket_name, ticket_purchase_price, self.purchase_price_compute_way_selected
               , ticket_sell_price, self.sell_price_compute_way_selected))
        SqlUtils().add_ticket_record(self.ticket_add_date, ticket_name, ticket_purchase_price,
                                     self.purchase_price_compute_way_selected, ticket_sell_price,
                                     self.sell_price_compute_way_selected)
        self.accept()
