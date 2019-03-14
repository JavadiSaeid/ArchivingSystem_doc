import sys ,dpi ,os
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface_archive import Ui_MainWindow

class Baygan():
    def __init__(self):
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        # self.setupFirstVariable()
        self.ui.tab1_inputData.keyPressEvent = self.EnterToTab_1
        self.ui.tab2_SearchData.keyPressEvent = self.EnterToTab_2
        # self.ui.checkBox_daftar.keyPressEvent = self.loginPK
        self.ui.pushButton_sabt.clicked.connect(self.btn_sabt)
        self.ui.pushButton_search.clicked.connect(self.btn_search)
        self.ui.pushButton_new.clicked.connect(self.btn_New)
        self.ui.checkBox_daftar.stateChanged.connect(self.Daftar)
        self.ui.checkBox_daftar_2.stateChanged.connect(self.Daftar_2)

        self.setupFirstVariable()

        MainWindow.show()
        sys.exit(app.exec_())

    def setupFirstVariable(self):
        self.sangAsli_1 = ''
        self.sangFari_2 = ''
        self.daftarState = False
        self.daftarState_2 = False


    def EnterToTab_1(self, e):
        if e.key() == Qt.Key_Return:
            self.btn_sabt()
    def EnterToTab_2(self,e):
        if e.key() == Qt.Key_Return:
            print("tab Dovom enter shod")
            self.btn_search()

    def Daftar(self,state):
        if state == Qt.Checked:
            self.ui.lineEdit_sangFari.setEnabled(False)
        if state == Qt.Unchecked:
            self.ui.lineEdit_sangFari.setEnabled(True)
    def Daftar_2(self,state):
        if state == Qt.Checked:
            self.ui.lineEdit_sangFari_2.setEnabled(False)
        if state == Qt.Unchecked:
            self.ui.lineEdit_sangFari_2.setEnabled(True)

    def btn_sabt(self):
        self.sangAsli_1 = self.ui.lineEdit_sangAsli.text()
        self.sangFari_2 = self.ui.lineEdit_sangFari.text()
        if self.ui.checkBox_daftar.isChecked():
            self.daftarState = True
        else:
            self.daftarState = False
        print(self.sangAsli_1+"/"+self.sangFari_2)
        print(self.daftarState,self.daftarState_2)

    def btn_search(self):
        self.ui.pushButton_bazgashBygani.setEnabled(True)
        self.ui.pushButton_print.setEnabled(True)
        if self.ui.checkBox_daftar.isChecked():
            self.daftarState_2 = True
        else:
            self.daftarState_2 = False
        print(self.daftarState_2)

    def btn_New(self):
        self.ui.lineEdit_sangFari.setText('')
        self.ui.lineEdit_sangAsli.setText('')
        self.ui.textEdit_Tozihat.setText('')











if __name__ == '__main__':
    run = Baygan()



