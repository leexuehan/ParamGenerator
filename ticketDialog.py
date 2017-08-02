# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog

from ticket import Ui_Ticket_Dialog


class TicketDialog(QDialog):
    def __init__(self, parent=None):
        super(TicketDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Ticket_Dialog()
        self.ui.setupUi(self)

    def on_ok(self):
        ticket_name = self.ui.ticket_name_content.toPlainText()
        ticket_price = self.ui.ticket_price_content.toPlainText()
        print("exec add new coal,name is " + ticket_name + ",price is " + ticket_price)
        self.accept()


