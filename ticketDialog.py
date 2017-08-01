from PyQt5.QtWidgets import QDialog

from ticket import Ui_Dialog


class TicketDialog(QDialog):
    def __init__(self, parent=None):
        super(TicketDialog, self).__init__(parent)
        # init ui
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
