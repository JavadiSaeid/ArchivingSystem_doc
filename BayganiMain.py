import sys ,dpi ,sqlite3

from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from pytz import timezone
from jdatetime import datetime as dt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interface_archive import Ui_MainWindow

class Baygan():
    def __init__(self):
        app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.dateTime()
        self.onlyInt = QIntValidator()              ## just int get in LineEdir , int Value in QlineEdit
        self.ui.lineEdit_dateYear.setText(self.nowYear)
        self.ui.lineEdit_dateYear.setValidator((QIntValidator(1,9999)))
        self.ui.lineEdit_dateMonth.setText(self.nowMonth)
        self.ui.lineEdit_dateMonth.setValidator((QIntValidator(1,12)))
        self.ui.lineEdit_dateDay.setText(self.nowDay)
        self.ui.lineEdit_dateDay.setValidator((QIntValidator(1,31)))
        self.ui.lineEdit_sangAsli.setValidator(QIntValidator(1,999))
        self.ui.lineEdit_sangAsli_2.setValidator(QIntValidator(1,999))
        self.ui.lineEdit_sangFari.setValidator(self.onlyInt)
        self.ui.lineEdit_sangFari_2.setValidator(self.onlyInt)
        self.ui.tab1_inputData.keyPressEvent = self.EnterToTab_1
        self.ui.tab2_SearchData.keyPressEvent = self.EnterToTab_2
        self.ui.pushButton_sabt.clicked.connect(self.btn_sbt)
        self.ui.pushButton_search.clicked.connect(self.btn_search)
        self.ui.pushButton_new.clicked.connect(self.btn_New)
        self.ui.checkBox_daftar.stateChanged.connect(self.Daftar)
        self.ui.checkBox_advanceSearch.stateChanged.connect(self.advance)
        self.ui.checkBox_allDontReturn.stateChanged.connect(self.allDontReturn)
        self.ui.checkBox_daftar_2.stateChanged.connect(self.Daftar_2)
        self.MainWindow.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.MainWindow.show()
        sys.exit(app.exec_())

    def dateTime(self):
        self.tz = timezone('Asia/Tehran')
        self.TimeSabt = dt.now(self.tz)
        self.nowYear = self.TimeSabt.strftime("%Y")
        self.nowMonth = self.TimeSabt.strftime("%m")
        self.nowDay = self.TimeSabt.strftime("%d")
        self.nowHour = self.TimeSabt.strftime("%H")
        self.nowMinute = self.TimeSabt.strftime("%M")
    def EnterToTab_1(self, e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter :
            self.btn_sbt()
    def EnterToTab_2(self,e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            print("tab Dovom enter shod")
            self.btn_search()

    def Daftar(self,state):
        if state == Qt.Checked:
            self.ui.lineEdit_sangFari.setText('')
            self.ui.lineEdit_sangFari.setEnabled(False)
            self.ui.radioButton_bakhsh25_1.setEnabled(False)
            self.ui.radioButton_bakhsh26_1.setEnabled(False)
        if state == Qt.Unchecked:
            self.ui.lineEdit_sangFari.setEnabled(True)
            self.ui.radioButton_bakhsh25_1.setEnabled(True)
            self.ui.radioButton_bakhsh26_1.setEnabled(True)
    def Daftar_2(self,state):
        if state == Qt.Checked:
            if not self.ui.checkBox_allDontReturn.isChecked():
                self.ui.lineEdit_sangFari_2.setText('')
                self.ui.lineEdit_sangFari_2.setEnabled(False)
                self.ui.radioButton_bakhsh25_2.setEnabled(False)
                self.ui.radioButton_bakhsh26_2.setEnabled(False)
        if state == Qt.Unchecked:
            if not self.ui.checkBox_allDontReturn.isChecked():
                self.ui.lineEdit_sangFari_2.setEnabled(True)
                self.ui.radioButton_bakhsh25_2.setEnabled(True)
                self.ui.radioButton_bakhsh26_2.setEnabled(True)
    def advance(self):
        if self.ui.checkBox_advanceSearch.isChecked():
            self.ui.lineEdit_dateDay.setEnabled(True)
            self.ui.lineEdit_dateMonth.setEnabled(True)
            self.ui.lineEdit_dateYear.setEnabled(True)
            self.ui.comboBox_searchType.setEnabled(True)
            self.ui.checkBox_allDontReturn.setEnabled(False)
        else:
            self.ui.checkBox_allDontReturn.setEnabled(True)
            self.ui.lineEdit_dateDay.setEnabled(False)
            self.ui.lineEdit_dateMonth.setEnabled(False)
            self.ui.lineEdit_dateYear.setEnabled(False)
            self.ui.comboBox_searchType.setEnabled(False)
    def allDontReturn(self):
        if self.ui.checkBox_allDontReturn.isChecked():
            self.ui.checkBox_advanceSearch.setEnabled(False)
            self.ui.lineEdit_sangAsli_2.setEnabled(False)
            self.ui.lineEdit_sangAsli_2.setText('')
            self.ui.lineEdit_sangFari_2.setEnabled(False)
            self.ui.lineEdit_sangFari_2.setText('')
            self.ui.radioButton_bakhsh25_2.setEnabled(False)
            self.ui.radioButton_bakhsh26_2.setEnabled(False)
        else:
            self.ui.checkBox_advanceSearch.setEnabled(True)
            self.ui.lineEdit_sangAsli_2.setEnabled(True)
            if not self.ui.checkBox_daftar_2.isChecked():
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
        if self.daftarState_1:
            self.TypeReq = "دفتر"
        else:
            self.TypeReq = "پرونده"
        if self.ui.radioButton_bakhsh26_1.isChecked():
            self.bakhsh = '26'
        else:
            self.bakhsh = '25'
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

    def insertdb(self,TR,SA,HR,TG,ER,SF='',BH='',TT='',BT=''):
        # with sqlite3.connect(r'Backup\ArchivesData.db') as database:
        with sqlite3.connect(r'\\10.120.112.70\baygan-data\ArchivesData.db') as database:
            IT_BAYGAN = "CREATE TABLE IF NOT EXISTS IT_BAYGAN (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,th VARCHAR(50),st VARCHAR(50),tr VARCHAR(50) ," \
                    "sn VARCHAR(60),bh VARCHAR (10),hr varchar (60),tg VARCHAR (50),er varchar (50),tt TEXT,bt varchar (50))"
            STATUS_BAYGAN = "CREATE TABLE IF NOT EXISTS STATUS_BAYGAN(sn_bh VARCHAR(50) NOT NULL UNIQUE PRIMARY KEY, ss VARCHAR(60))"
            USERS_BAYGAN = "CREATE TABLE IF NOT EXISTS USERS_BAYGAN(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,us varchar (60) NOT NULL UNIQUE, pw VARCHAR(60) NOT NULL)"
            database.execute(IT_BAYGAN)
            database.execute(STATUS_BAYGAN)
            database.execute(USERS_BAYGAN)
            TH = self.TimeSabt.strftime("%Y/%m/%d")
            ST = self.TimeSabt.strftime("%H:%M")
            if TR == 'پرونده':
                SN = SA+"/"+SF
                SNBH = SA+"/"+SF+"-"+BH
            else:
                BH = ''
                SN = SA
                SNBH = SN
            insert = "INSERT INTO IT_BAYGAN(th,st,tr,sn,bh,hr,tg,er,tt,bt) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
                .format(TH, ST, TR, SN, BH, HR, TG, ER, TT, BT)
            instatus = "INSERT OR REPLACE INTO STATUS_BAYGAN(sn_bh, ss) VALUES ('{}', 'Exit')".format(SNBH)
            database.execute(insert)
            database.execute(instatus)
            database.commit()

    def btn_sbt(self):
        self.getUpdateVriable()
        self.dateTime()
        try:
            if self.ui.checkBox_daftar.isChecked():
                if self.sangAsli_1 != '':
                    self.insertdb(TR=self.TypeReq, SA=self.sangAsli_1, SF=self.sangFari_1, BH=self.bakhsh,
                                  HR=self.hamkarCB, TG=self.dariaftKonande, ER=self.elatDarkhast, TT=self.tozihat)
                    self.ui.statusbar.showMessage('با موفقیت ثبت شد')
                    self.btn_New()
                else:
                    self.ui.statusbar.showMessage('خطا')
                    self.errorM(errorText='شماره سنگ اصلی دفتر باید وارد شود')
            else:
                if self.sangAsli_1 != '':
                    if self.sangFari_1 != '':
                        self.insertdb(TR=self.TypeReq, SA=self.sangAsli_1, SF=self.sangFari_1, BH=self.bakhsh,
                                      HR=self.hamkarCB, TG=self.dariaftKonande, ER=self.elatDarkhast, TT=self.tozihat)
                        self.ui.statusbar.showMessage('با موفقیت ثبت شد')
                        self.btn_New()
                    else:
                        self.errorM('شماره سنگ فرعی باید وارد شود')
                else:
                    self.errorM('شماره سنگ اصلی باید وارد شود')
        except:
            self.ui.statusbar.showMessage('خطا در ثبت اطلاعات')
            self.errorM(' خطایی در ثبت اطلاعات بوجود امده است \n این خطا را به مدیر سیستم اطلاع دهید')
            pass


    def searcherVariable(self):
        self.sangAsli_2 = self.ui.lineEdit_sangAsli_2.text()
        self.sangFari_2 = self.ui.lineEdit_sangFari_2.text()
        if self.ui.radioButton_bakhsh26_2.isChecked():
            self.bakhsh_2 = '26'
        else:
            self.bakhsh_2 = '25'
        if self.ui.checkBox_daftar_2.isChecked():
            self.daftarState_2 = True
        else:
            self.daftarState_2 = False
    def btn_search(self):
        self.searcherVariable()
        if self.ui.checkBox_allDontReturn.isChecked():
            # with sqlite3.connect(r'Backup\ArchivesData.db') as database:
            # with sqlite3.connect(r'\\10.120.112.70\baygan-data\ArchivesData.db') as database:
                # selectALL = "SELECT * FROM IT_BAYGAN"
                # curser = database.execute(selectALL)
                # self.ui.tableView_result.setItem
                # for row in curser:
                #     print (row)
                #     print("ID =", row[0])
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(r'\\10.120.112.70\baygan-data\ArchivesData.db')
            db.open()
            projectModel = QSqlQueryModel()
            projectModel.setQuery("SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt FROM IT_BAYGAN", db)
            projectModel.setHeaderData(0, Qt.Horizontal, 'پلاک')
            projectModel.setHeaderData(1, Qt.Horizontal, 'بخش')
            projectModel.setHeaderData(2, Qt.Horizontal, 'نوع')
            projectModel.setHeaderData(3, Qt.Horizontal, 'همکار تقاضا کننده')
            projectModel.setHeaderData(4, Qt.Horizontal, 'تحویل گیرنده')
            projectModel.setHeaderData(5, Qt.Horizontal, 'علت درخواست')
            projectModel.setHeaderData(6, Qt.Horizontal, 'توضیحات')
            projectModel.setHeaderData(7, Qt.Horizontal, 'تاریخ تحویل')
            projectModel.setHeaderData(8, Qt.Horizontal, 'ساعت تحویل')
            projectModel.setHeaderData(9, Qt.Horizontal, 'تاریخ بازگشت')
            self.ui.tableView_result.setModel(projectModel)
            self.ui.tableView_result.show()
            db.close()

        else:
            pass
        self.ui.pushButton_bazgashBygani.setEnabled(True)
        self.ui.pushButton_print.setEnabled(True)
        # self.ui.lineEdit_sangAsli_2.setText('')
        # self.ui.lineEdit_sangFari_2.setText('')

        # print(self.sangAsli_2+"/"+self.sangFari_2)
        # print(self.bakhsh_2)
        # print(self.daftarState_2)

    def btn_New(self):
        self.ui.lineEdit_sangFari.setText('')
        self.ui.lineEdit_sangAsli.setText('')
        self.ui.textEdit_Tozihat.setText('')


    def errorM(self,errorText='مشکلی پیش آمده است !!!'):
        box = QMessageBox()
        box.setIcon(QMessageBox.Warning)
        box.setWindowTitle('ارور')
        box.setText(errorText)
        box.setStandardButtons(QMessageBox.Yes)
        buttonY = box.button(QMessageBox.Yes)

        buttonY.setText('       تایید       ')
        box.setStyleSheet("QMessageBox{\n"
                          "background-color:    #d9c9a3    ;\n"
                          "border: 3px solid   #ff0000  ;\n"
                          "border-radius:5px;\n"
                          "}\n"
                          "QLabel{\n"
                          "color:   #ff0000  ;\n"
                          "font: 13pt \"A Arsoo\";\n"
                          "font-weight: bold;\n"
                          "border:no;\n"
                          "}\n"
                          "\n"
                          "QPushButton:hover:!pressed\n"
                          "{\n"
                          "  border: 2px dashed rgb(255, 85, 255);\n"
                          "    background-color:  #e4e7bb ;\n"
                          "    color:  #9804ff ;\n"
                          "}\n"
                          "QPushButton{\n"
                          "background-color:  #a2fdc1 ;\n"
                          "font: 12pt \"A Arsoo\";\n"
                          "font-weight: bold;\n"
                          "    color:  #ff0000 ;\n"
                          "border: 2px solid  #8b00ff ;\n"
                          "border-radius: 8px;\n"
                          "}")
        box.setWindowFlags(box.windowFlags() | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        # box.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        box.exec_()








if __name__ == '__main__':
    run = Baygan()



