import sys ,dpi ,os
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface_archive import Ui_MainWindow

class Baygan():
    def __init__(self):
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.ui.pushButton_sabt.clicked.connect(self.btn_sabt)
        self.ui.pushButton_sabt.setFocus()

        MainWindow.show()
        sys.exit(app.exec_())

    def btn_sabt(self):
        sangAsli_1 = self.ui.lineEdit_sangAsli.text()
        sangFari_2 = self.ui.lineEdit_sangFari.text()
        print(sangAsli_1+"/"+sangFari_2)


if __name__ == '__main__':
    run = Baygan()


