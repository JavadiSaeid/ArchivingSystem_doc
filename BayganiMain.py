import sys ,dpi ,os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface_archive import Ui_MainWindow

class Baygan():
    def __init__(self):
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.tab1_inputData.keyPressEvent = self.EnterToTab_1
        self.ui.tab2_SearchData.keyPressEvent = self.EnterToTab_2
        # self.ui.checkBox_daftar.keyPressEvent = self.loginPK
        self.ui.pushButton_sabt.clicked.connect(self.btn_sabt)
        self.ui.pushButton_search.clicked.connect(self.btn_search)

        MainWindow.show()
        sys.exit(app.exec_())

    def EnterToTab_1(self, e):
        if e.key() == Qt.Key_Return:
            self.btn_sabt()
    def EnterToTab_2(self,e):
        if e.key() == Qt.Key_Return:
            print("tab Dovom enter shod")
            self.btn_search()

    def btn_sabt(self):
        sangAsli_1 = self.ui.lineEdit_sangAsli.text()
        sangFari_2 = self.ui.lineEdit_sangFari.text()
        print(sangAsli_1+"/"+sangFari_2)

    def btn_search(self):
        self.ui.pushButton_bazgashBygani.setEnabled(True)
        self.ui.pushButton_print.setEnabled(True)


if __name__ == '__main__':
    run = Baygan()



