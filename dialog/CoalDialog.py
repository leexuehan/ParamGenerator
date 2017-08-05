from PyQt5.QtWidgets import QDialog

from dialog.calendarDialog import CalendarDialog
from ui.coal import Ui_Coal_Dialog
from utils.ConfigFileUtils import ConfigFileUtils


class CoalDialog(QDialog):
    def __init__(self, parent=None):
        super(CoalDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Coal_Dialog()
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

    def on_purchase_compute_way_selected(self, item):
        compute_way = self.compute_ways[item]
        self.purchase_price_compute_way_selected = compute_way

    def on_sell_compute_way_selected(self, item):
        compute_way = self.compute_ways[item]
        self.sell_price_compute_way_selected = compute_way

    def on_add_new_coal_date_selected(self):
        calendarDialog = CalendarDialog()
        calendarDialog.show()
        if calendarDialog.exec_():
            date = calendarDialog.date_time
            print("value get from calendar window is:" + date.strftime('%Y/%m/%d'))
            self.ui.date_value_display.setPlainText(date.strftime('%Y/%m/%d'))
            self.coal_add_date = date.strftime('%Y/%m/%d')
        calendarDialog.destroy()

    def on_add_new_coal_finished(self):
        coal_name = self.ui.coal_name_content.toPlainText()
        coal_purchase_price = self.ui.coal_purchase_price_content.toPlainText()
        coal_sell_price = self.ui.coal_sell_price_content.toPlainText()
        print("add new ticket info (添加日期，煤种名称，进价，进价计费方式，售价，售价计费方式):",
              (self.coal_add_date, coal_name, coal_purchase_price, self.purchase_price_compute_way_selected
               , coal_sell_price, self.sell_price_compute_way_selected))
        # SqlUtils().add_ticket_record(self.ticket_add_date, ticket_name, ticket_purchase_price,
        #                              self.purchase_price_compute_way_selected, ticket_sell_price,
        #                              self.sell_price_compute_way_selected)
        self.accept()
