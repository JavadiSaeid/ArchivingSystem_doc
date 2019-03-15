import sys ,dpi ,os
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface_archive import Ui_MainWindow

class Baygan():
    def __init__(self):
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.onlyInt = QIntValidator()              ## just int get in LineEdir , int Value in QlineEdit
        self.onlyIntAsli = QIntValidator(1,999)
        self.ui.lineEdit_sangAsli.setValidator(self.onlyIntAsli)
        self.ui.lineEdit_sangAsli_2.setValidator(self.onlyIntAsli)
        self.ui.lineEdit_sangFari.setValidator(self.onlyInt)
        self.ui.lineEdit_sangFari_2.setValidator(self.onlyInt)
        self.ui.tab1_inputData.keyPressEvent = self.EnterToTab_1
        self.ui.tab2_SearchData.keyPressEvent = self.EnterToTab_2
        self.ui.pushButton_sabt.clicked.connect(self.btn_sabt)
        self.ui.pushButton_search.clicked.connect(self.btn_search)
        self.ui.pushButton_new.clicked.connect(self.btn_New)
        self.ui.checkBox_daftar.stateChanged.connect(self.Daftar)
        self.ui.checkBox_daftar_2.stateChanged.connect(self.Daftar_2)


        MainWindow.show()
        sys.exit(app.exec_())


    def EnterToTab_1(self, e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter :
            self.btn_sabt()
    def EnterToTab_2(self,e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            print("tab Dovom enter shod")
            self.btn_search()

    def Daftar(self,state):
        if state == Qt.Checked:
            self.ui.lineEdit_sangFari.setEnabled(False)
            self.ui.radioButton_bakhsh25_1.setEnabled(False)
            self.ui.radioButton_bakhsh26_1.setEnabled(False)

        if state == Qt.Unchecked:
            self.ui.lineEdit_sangFari.setEnabled(True)
            self.ui.radioButton_bakhsh25_1.setEnabled(True)
            self.ui.radioButton_bakhsh26_1.setEnabled(True)
    def Daftar_2(self,state):
        if state == Qt.Checked:
            self.ui.lineEdit_sangFari_2.setEnabled(False)
            self.ui.radioButton_bakhsh25_2.setEnabled(False)
            self.ui.radioButton_bakhsh26_2.setEnabled(False)
        if state == Qt.Unchecked:
            self.ui.lineEdit_sangFari_2.setEnabled(True)
            self.ui.radioButton_bakhsh25_2.setEnabled(True)
            self.ui.radioButton_bakhsh26_2.setEnabled(True)

    def getUpdateVriable(self):
        self.sangAsli_1 = self.ui.lineEdit_sangAsli.text()
        self.sangFari_1 = self.ui.lineEdit_sangFari.text()
        if self.ui.checkBox_daftar.isChecked():
            self.daftarState_1 = True
        else:
            self.daftarState_1 = False
        if self.ui.radioButton_bakhsh26_1.isChecked():
            self.bakhsh = 26
        else:
            self.bakhsh = 25
        self.hamkarCB = self.ui.comboBox_Hamkaran.currentText()
        if self.ui.radioButton_arbabRojo.isChecked():
            self.dariaftKonande = 'ارباب رجوع'
        else:
            self.dariaftKonande = 'همکار'
        if self.ui.radioButton_edary.isChecked():
            self.elatDarkhast = 'اداری'
        elif self.ui.radioButton_estelam.isChecked():
            self.elatDarkhast = 'استعلام'
        elif self.ui.radioButton_tafkik.isChecked():
            self.elatDarkhast = 'تفکیک'
        elif self.ui.radioButton_tajmii.isChecked():
            self.elatDarkhast = 'تجمیعی'
        elif self.ui.radioButton_nameEdarat.isChecked():
            self.elatDarkhast = 'نامه ادارات'
        elif self.ui.radioButton_darKhastSanad.isChecked():
            self.elatDarkhast = 'درخواست سند'
        elif self.ui.radioButton_Jari.isChecked():
            self.elatDarkhast = 'جاری'
        elif self.ui.radioButton_Baresi.isChecked():
            self.elatDarkhast = 'بررسی'
        elif self.ui.radioButton_sayer.isChecked():
            self.elatDarkhast = 'سایر'
        self.tozihat = self.ui.textEdit_Tozihat.toPlainText()


    def btn_sabt(self):
        self.getUpdateVriable()

        print(self.sangAsli_1+"/"+self.sangFari_1)
        print ("Daftar=",self.daftarState_1)
        print(self.bakhsh)
        print(self.hamkarCB)
        print(self.dariaftKonande)
        print(self.elatDarkhast)
        print(self.tozihat)

        self.btn_New()

    def btn_search(self):
        self.sangAsli_2 = self.ui.lineEdit_sangAsli_2.text()
        self.sangFari_2 = self.ui.lineEdit_sangFari_2.text()
        if self.ui.radioButton_bakhsh26_2.isChecked():
            self.bakhsh_2 = 26
        else:
            self.bakhsh_2 = 25
        self.ui.pushButton_bazgashBygani.setEnabled(True)
        self.ui.pushButton_print.setEnabled(True)
        if self.ui.checkBox_daftar.isChecked():
            self.daftarState_2 = True
        else:
            self.daftarState_2 = False
        self.ui.lineEdit_sangAsli_2.setText('')
        self.ui.lineEdit_sangFari_2.setText('')

        print(self.sangAsli_2+"/"+self.sangFari_2)
        print(self.bakhsh_2)
        print(self.daftarState_2)

    def btn_New(self):
        self.ui.lineEdit_sangFari.setText('')
        self.ui.lineEdit_sangAsli.setText('')
        self.ui.textEdit_Tozihat.setText('')











if __name__ == '__main__':
    run = Baygan()



