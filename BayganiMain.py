import sys ,dpi ,sqlite3,getpass
from time import sleep

from PyQt5.QtCore import QRegExp, Qt, QThread, pyqtSignal
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel
from pytz import timezone
from jdatetime import datetime as dt
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from interface_archive import Ui_MainWindow
from PyQt5 import QtWidgets
from about import Ui_Form

class Baygan():
    def __init__(self):
        app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.dateTime()
        # self.dbPath = r'\\10.120.112.70\baygan-data\ArchivesData.db'
        self.dbPath = r'Backup\ArchivesData.db'
        self.onlyInt = QIntValidator()              ## just int get in LineEdir , int Value in QlineEdit
        self.ui.lineEdit_dateYear.setText(self.nowYear)
        self.ui.lineEdit_dateYear.setValidator((QIntValidator(1,9999)))
        self.ui.lineEdit_dateMonth.setText(self.nowMonth)
        self.ui.lineEdit_dateMonth.setValidator((QIntValidator(1,12)))
        self.ui.lineEdit_dateDay.setText(self.nowDay)
        self.ui.lineEdit_dateDay.setValidator((QIntValidator(1,31)))
        self.ui.lineEdit_sangAsli.setValidator(QIntValidator(1,999))
        # self.ui.lineEdit_sangAsli_2.setValidator(QIntValidator(1,999))
        self.ui.lineEdit_sangAsli_2.setMaxLength(3)
        # regex=QRegExp("^\*$|[0-9]+")
        regex=QRegExp("[0-9]+")
        validator = QRegExpValidator(regex)
        self.ui.lineEdit_sangAsli_2.setValidator(validator)
        self.ui.lineEdit_sangFari.setValidator(self.onlyInt)
        self.ui.lineEdit_sangFari_2.setValidator(validator)

        self.ui.tab1_inputData.keyPressEvent = self.EnterToTab_1
        self.ui.tab2_SearchData.keyPressEvent = self.EnterToTab_2
        self.ui.pushButton_sabt.clicked.connect(self.btn_sbt)
        self.ui.pushButton_search.clicked.connect(self.btn_search)
        self.ui.pushButton_new.clicked.connect(self.btn_New)
        self.ui.checkBox_daftar.stateChanged.connect(self.Daftar)
        self.ui.checkBox_viaDate.stateChanged.connect(self.advance)
        self.ui.checkBox_allDontReturn.stateChanged.connect(self.allDontReturn)
        self.ui.checkBox_daftar_2.stateChanged.connect(self.Daftar_2)
        self.ui.pushButton_bazgashBygani.clicked.connect(self.btn_return)
        self.ui.action_about.triggered.connect(self.RunAbout)
        self.MainWindow.setWindowFlags(Qt.WindowStaysOnTopHint)

        MainWindowGetSize = self.MainWindow.frameGeometry()
        DesktopCenter = QDesktopWidget().availableGeometry().center()
        MainWindowGetSize.moveCenter(DesktopCenter)
        self.MainWindow.move(MainWindowGetSize.topLeft())
        self.MainWindow.show()
        sys.exit(app.exec_())

    def RunAbout(self):
        self.Form = QtWidgets.QWidget()
        self.uiForm = Ui_Form()
        self.uiForm.setupUi(self.Form)
        self.Form.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.Form.setWindowFlags(self.Form.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        MainWindowGetSize = self.Form.frameGeometry()
        DesktopCenter = QDesktopWidget().availableGeometry().center()
        MainWindowGetSize.moveCenter(DesktopCenter)
        self.Form.move(MainWindowGetSize.topLeft())
        self.Form.keyPressEvent      = self.CustomClose

        self.Form.show()
    def CustomClose(self,e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.Form.close()


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
        if self.ui.checkBox_viaDate.isChecked():
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
            self.ui.checkBox_viaDate.setEnabled(False)
            self.ui.lineEdit_sangAsli_2.setEnabled(False)
            self.ui.lineEdit_sangAsli_2.setText('')
            self.ui.lineEdit_sangFari_2.setEnabled(False)
            self.ui.lineEdit_sangFari_2.setText('')
            self.ui.radioButton_bakhsh25_2.setEnabled(False)
            self.ui.radioButton_bakhsh26_2.setEnabled(False)
            self.ui.checkBox_daftar_2.setEnabled(False)
        else:
            self.ui.checkBox_daftar_2.setEnabled(True)
            self.ui.checkBox_viaDate.setEnabled(True)
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

    def insertdb(self,TR,SA,HR,TG,ER,SF='',BH='',TT='',BT='',BS = ''):
        with sqlite3.connect(self.dbPath) as database:
            IT_BAYGAN = "CREATE TABLE IF NOT EXISTS IT_BAYGAN (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,th VARCHAR(50),st VARCHAR(50),tr VARCHAR(50) ," \
                    "sn VARCHAR(60),bh VARCHAR (10),hr varchar (60),tg VARCHAR (50),er varchar (50),tt TEXT,bt varchar (30),bs varchar (30),us VARCHAR (72),sn_bh VARCHAR(50) REFERENCES STATUS_BAYGAN(sn_bh))"
            STATUS_BAYGAN = "CREATE TABLE IF NOT EXISTS STATUS_BAYGAN(sn_bh VARCHAR(50) NOT NULL UNIQUE PRIMARY KEY, ss VARCHAR(60))"
            USERS_BAYGAN = "CREATE TABLE IF NOT EXISTS USERS_BAYGAN(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,us varchar (60) NOT NULL UNIQUE, pw VARCHAR(60) NOT NULL)"

            database.execute(STATUS_BAYGAN)
            database.execute(IT_BAYGAN)
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
            insert = "INSERT INTO IT_BAYGAN(th,st,tr,sn,bh,hr,tg,er,tt,bt,bs,sn_bh,us) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
                .format(TH, ST, TR, SN, BH, HR, TG, ER, TT, BT,BS, SNBH,getpass.getuser())
            instatus = "INSERT OR REPLACE INTO STATUS_BAYGAN(sn_bh, ss) VALUES ('{}', 'Exit')".format(SNBH,SNBH)
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

    def dbToTableView(self,commandSQL):
        QApplication.processEvents()
        if QSqlDatabase.contains("qt_sql_default_connection"):
            db = QSqlDatabase.database("qt_sql_default_connection")
        else:
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(self.dbPath)
            db.open()
        projectModel = QSqlQueryModel()
        projectModel.setQuery(commandSQL, db)
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
        projectModel.setHeaderData(10, Qt.Horizontal, 'ساعت بازگشت')
        self.ui.tableView_result.setModel(projectModel)
        # self.ui.tableView_result.show()
        self.rowCount = projectModel.rowCount()
        db.close()

    def getStatus(self,SNBH):
        with sqlite3.connect(self.dbPath) as database:
            getStatus = "SELECT ss FROM STATUS_BAYGAN WHERE sn_bh = '{}'".format(SNBH)
            GetSTATUS = database.execute(getStatus)
            for row in GetSTATUS:
                Status = row[0]
                break
        return Status

    def btn_search(self):
        self.searcherVariable()
        if self.ui.checkBox_daftar_2.isChecked():
            SNBH = self.sangAsli_2
        else:
            SNBH = self.sangAsli_2 + "/" + self.sangFari_2+ "-" + self.bakhsh_2
            SN2  = self.sangAsli_2 + "/" + self.sangFari_2
            BH2  = self.bakhsh_2
        if self.ui.checkBox_allDontReturn.isChecked():
            self.dbToTableView(commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN INNER JOIN STATUS_BAYGAN ON IT_BAYGAN.sn_bh = STATUS_BAYGAN.sn_bh WHERE ss='Exit'")
        elif self.ui.checkBox_viaDate.isChecked():
            day = self.ui.lineEdit_dateDay.text()
            month = self.ui.lineEdit_dateMonth.text()
            year = self.ui.lineEdit_dateYear.text()
            searchDate = year+"/"+month+"/"+day
            searchType = self.ui.comboBox_searchType.currentText()
            if self.ui.checkBox_daftar_2.isChecked():
                if self.sangAsli_2 == '':  ## namayesh tamaie savabeq mojod dafater dar tarikh khas
                    if searchType == 'تمام سوابق موجود':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN WHERE tr = 'دفتر' AND (th='{}' OR bt = '{}')".format(searchDate,searchDate))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage(
                                "برای تاریخ {} سابقه ای موجود نیست".format(searchDate))
                    elif searchType == 'بازگشت داده نشده':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN INNER JOIN STATUS_BAYGAN ON IT_BAYGAN.sn_bh = STATUS_BAYGAN.sn_bh WHERE ss='Exit' AND tr = 'دفتر' AND th='{}' AND bt = ''".format(searchDate))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage(
                                "برای تاریخ {} سابقه ای موجود نیست".format(searchDate))
                    elif searchType == 'بازگشت داده شده':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN WHERE tr = 'دفتر'  AND  bt = '{}' ".format(searchDate))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage("در تاریخ {} سابقه ای موجود نیست".format(searchDate))
                else:   ## jostojo Baray Ye Daftar
                    if searchType == 'تمام سوابق موجود':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN WHERE sn_bh ='{}' AND (th='{}' OR bt = '{}')".format(SNBH,searchDate,searchDate))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage(
                                "در تاریخ {} برای دفتر {} سابقه ای موجود نیست".format(searchDate, SNBH))
                    elif searchType == 'بازگشت داده نشده':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN INNER JOIN STATUS_BAYGAN ON IT_BAYGAN.sn_bh = STATUS_BAYGAN.sn_bh  WHERE ss='Exit' AND th='{}' AND sn='{}' AND bt = ''".format(searchDate,SNBH))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage(
                                "در تاریخ {} برای دفتر {} سابقه ای موجود نیست".format(searchDate, SNBH))
                        else:
                            self.ARBTN()
                    elif searchType == 'بازگشت داده شده':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN WHERE sn_bh ='{}' AND  bt = '{}' ".format(SNBH,searchDate))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage( "در تاریخ {} برای دفتر {} سابقه ای موجود نیست".format(searchDate,SNBH))
            else:
                if self.sangAsli_2 == '' and self.sangFari_2 == '': ## search ba '' va koli
                    if searchType == 'تمام سوابق موجود':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN WHERE tr = 'پرونده' AND (th='{}' OR bt = '{}')".format(
                                searchDate, searchDate))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage(
                                "برای تاریخ {} سابقه ای موجود نیست".format(searchDate))
                    elif searchType == 'بازگشت داده نشده':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN INNER JOIN STATUS_BAYGAN ON IT_BAYGAN.sn_bh = STATUS_BAYGAN.sn_bh WHERE ss='Exit' AND tr = 'پرونده' AND th='{}' AND bt = ''".format(
                                searchDate))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage(
                                "برای تاریخ {} سابقه ای موجود نیست".format(searchDate))
                    elif searchType == 'بازگشت داده شده':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN WHERE tr = 'پرونده'  AND  bt = '{}' ".format(
                                searchDate))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage(
                                "در تاریخ {} سابقه ای موجود نیست".format(searchDate))

                elif self.sangAsli_2 != '' and self.sangFari_2 != '':
                    if searchType == 'تمام سوابق موجود':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN WHERE sn_bh ='{}' AND (th='{}' OR bt = '{}')".format(
                                SNBH, searchDate, searchDate))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage(
                                "در تاریخ {} برای دفتر {} سابقه ای موجود نیست".format(searchDate, SNBH))
                    elif searchType == 'بازگشت داده نشده':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN INNER JOIN STATUS_BAYGAN ON IT_BAYGAN.sn_bh = STATUS_BAYGAN.sn_bh  WHERE ss='Exit' AND th='{}' AND sn='{}' AND bh='{}' AND bt = ''".format(
                                searchDate,SN2,BH2))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage(
                                "در تاریخ {} برای دفتر {} سابقه ای موجود نیست".format(searchDate, SNBH))
                        else:
                            self.ARBTN()
                    elif searchType == 'بازگشت داده شده':
                        self.dbToTableView(
                            commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN WHERE sn_bh ='{}' AND  bt = '{}' ".format(
                                SNBH, searchDate))
                        if self.rowCount <= 0:
                            self.ui.statusbar.showMessage(
                                "در تاریخ {} برای دفتر {} سابقه ای موجود نیست".format(searchDate, SNBH))
                else:
                    self.errorM('شماره پلاک به درستی وارد نشده است\n برای بازیابی کلیه پلاک ها باید هردو فیلد سنگ اصلی و فرعی خالی باشند و یا پلاک را بطور کامل وارد کنید.')

        else:
            if self.ui.checkBox_daftar_2.isChecked():
                if self.sangAsli_2 == '':
                    self.dbToTableView(commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN WHERE tr='دفتر' ")
                else:
                    self.dbToTableView(commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN WHERE sn='{}' ".format(self.sangAsli_2))
                    if self.rowCount > 0:
                        if self.getStatus(SNBH) == 'Exit':
                            self.ARBTN()
                    else:
                        self.ui.statusbar.showMessage("برای دفتر {} سابقه ای موجود نیست".format(self.sangAsli_2))
            else:
                if self.sangAsli_2 == '' and self.sangFari_2 == '':
                    self.dbToTableView(commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN WHERE tr='پرونده'")
                elif self.sangAsli_2 != '' and self.sangFari_2 != '' :
                    self.dbToTableView(commandSQL="SELECT sn,bh,tr,hr,tg,er,tt,th,st,bt,bs FROM IT_BAYGAN where sn_bh='{}'".format(SNBH))
                    if self.rowCount > 0:
                        if self.getStatus(SNBH) == 'Exit':
                            self.ARBTN()
                    else:
                        self.ui.statusbar.showMessage("برای پلاک {} بخش {} سابقه ای موجود نیست".format(self.sangAsli_2+"/"+self.sangFari_2,self.bakhsh_2))
                else:
                    self.errorM('شماره پلاک به درستی وارد نشده است\n برای بازیابی کلیه پلاک ها باید هردو فیلد سنگ اصلی و فرعی خالی باشند و یا پلاک را بطور کامل وارد کنید.')

    def btn_return(self):
        if self.ui.checkBox_daftar_2.isChecked():
            SNBH = self.sangAsli_2
        else:
            SNBH = self.sangAsli_2 + "/" + self.sangFari_2+ "-" + self.bakhsh_2
        with sqlite3.connect(self.dbPath) as database:
            update_status = "UPDATE STATUS_BAYGAN SET ss='Returned' WHERE sn_bh = '{}'".format( SNBH)
            self.dateTime()
            TR = self.TimeSabt.strftime("%Y/%m/%d")
            SR = self.TimeSabt.strftime("%H:%M")
            update_Baygan = "UPDATE IT_BAYGAN SET bt='{}' , bs ='{}' WHERE sn_bh = '{}' AND id = (SELECT MAX(id) FROM IT_BAYGAN WHERE sn_bh = '{}')".format(TR,SR,SNBH,SNBH)
            database.execute(update_status)
            database.execute(update_Baygan)
            database.commit()
            self.btn_search()
            self.ui.pushButton_bazgashBygani.setEnabled(False)
            self.ui.statusbar.showMessage('تاریخ بازگشت با موفقیت ثبت شد')
            # self.ui.lineEdit_sangAsli_2.setText('')
            # self.ui.lineEdit_sangFari_2.setText('')

    def ARBTN(self):
        self.ui.pushButton_bazgashBygani.setEnabled(True)
        self.ui.pushButton_print.setEnabled(True)

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
        box.setWindowFlags(box.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        box.exec_()





if __name__ == '__main__':
    run = Baygan()



