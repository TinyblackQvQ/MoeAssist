import PyQt5.QtWidgets as qtWidgets


class MainWindow(qtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("MoeAssist")
