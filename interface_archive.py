# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Baygani.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 629)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color: #5D5136;\n"
"}\n"
"QStatusBar{\n"
"background-color:#5D5136;\n"
"color: rgb(0, 255, 59);\n"
"border:1px solid rgbrgb(0, 148, 0);\n"
"border-radius:2px;\n"
"    font: 10pt \"A Arsoo\";\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab1_inputData = QtWidgets.QWidget()
        self.tab1_inputData.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tab1_inputData.setStyleSheet("QWidget{\n"
"background-color: #b8d5dd  ;\n"
"}\n"
"QGroupBox{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"A Arghavan\";\n"
"border-style: dashed;\n"
"border-bottom-width: 2px;\n"
"}\n"
"QRadioButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"A Arghavan\";\n"
"}\n"
"QLabel{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 17pt \"A Arsoo\";\n"
"}\n"
"QComboBox{\n"
"background-color: #eee1c5   ;\n"
"font: 75 10pt \"A Arsoo\";\n"
"color:#0A1F85;\n"
"border: 1px solid #096578  ;\n"
"border-radius: 3px;\n"
"}\n"
"QTextEdit{\n"
"background-color: #f9eff3 ;\n"
"font: 75 9pt \"A Arsoo\";\n"
"border: 1px solid  #fc9f47    ;\n"
"border-radius: 10px;\n"
"}\n"
"QCheckBox{\n"
"font: 75 12pt \"A Arsoo\";\n"
"}\n"
"QStatusBar{\n"
"background-color:rgb(33, 33, 33);\n"
"color: rgb(0, 255, 59);\n"
"border:1px solid rgbrgb(0, 148, 0);\n"
"border-radius:2px;\n"
"    font: 8pt \"Dast Nevis\";\n"
"}\n"
"")
        self.tab1_inputData.setObjectName("tab1_inputData")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab1_inputData)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_inputData = QtWidgets.QGroupBox(self.tab1_inputData)
        self.groupBox_inputData.setObjectName("groupBox_inputData")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_inputData)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_Tozihat = QtWidgets.QGroupBox(self.groupBox_inputData)
        self.groupBox_Tozihat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_Tozihat.setStyleSheet("QRadioButton{\n"
"font: 75 11pt \"A Arsoo\";\n"
"}")
        self.groupBox_Tozihat.setObjectName("groupBox_Tozihat")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_Tozihat)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textEdit_Tozihat = QtWidgets.QTextEdit(self.groupBox_Tozihat)
        self.textEdit_Tozihat.setEnabled(True)
        self.textEdit_Tozihat.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_Tozihat.setObjectName("textEdit_Tozihat")
        self.gridLayout_6.addWidget(self.textEdit_Tozihat, 3, 0, 1, 6)
        self.radioButton_sayer = QtWidgets.QRadioButton(self.groupBox_Tozihat)
        self.radioButton_sayer.setChecked(False)
        self.radioButton_sayer.setObjectName("radioButton_sayer")
        self.gridLayout_6.addWidget(self.radioButton_sayer, 1, 2, 1, 1)
        self.radioButton_darKhastSanad = QtWidgets.QRadioButton(self.groupBox_Tozihat)
        self.radioButton_darKhastSanad.setObjectName("radioButton_darKhastSanad")
        self.gridLayout_6.addWidget(self.radioButton_darKhastSanad, 0, 5, 1, 1)
        self.radioButton_nameEdarat = QtWidgets.QRadioButton(self.groupBox_Tozihat)
        self.radioButton_nameEdarat.setObjectName("radioButton_nameEdarat")
        self.gridLayout_6.addWidget(self.radioButton_nameEdarat, 0, 4, 1, 1)
        self.radioButton_tajmii = QtWidgets.QRadioButton(self.groupBox_Tozihat)
        self.radioButton_tajmii.setObjectName("radioButton_tajmii")
        self.gridLayout_6.addWidget(self.radioButton_tajmii, 0, 3, 1, 1)
        self.radioButton_tafkik = QtWidgets.QRadioButton(self.groupBox_Tozihat)
        self.radioButton_tafkik.setObjectName("radioButton_tafkik")
        self.gridLayout_6.addWidget(self.radioButton_tafkik, 0, 2, 1, 1)
        self.radioButton_estelam = QtWidgets.QRadioButton(self.groupBox_Tozihat)
        self.radioButton_estelam.setObjectName("radioButton_estelam")
        self.gridLayout_6.addWidget(self.radioButton_estelam, 0, 1, 1, 1)
        self.radioButton_edary = QtWidgets.QRadioButton(self.groupBox_Tozihat)
        self.radioButton_edary.setChecked(True)
        self.radioButton_edary.setObjectName("radioButton_edary")
        self.gridLayout_6.addWidget(self.radioButton_edary, 0, 0, 1, 1)
        self.radioButton_Jari = QtWidgets.QRadioButton(self.groupBox_Tozihat)
        self.radioButton_Jari.setObjectName("radioButton_Jari")
        self.gridLayout_6.addWidget(self.radioButton_Jari, 1, 0, 1, 1)
        self.radioButton_Baresi = QtWidgets.QRadioButton(self.groupBox_Tozihat)
        self.radioButton_Baresi.setObjectName("radioButton_Baresi")
        self.gridLayout_6.addWidget(self.radioButton_Baresi, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_Tozihat, 6, 0, 1, 1)
        self.horizontalLayout_Sang = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Sang.setObjectName("horizontalLayout_Sang")
        spacerItem = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Sang.addItem(spacerItem)
        self.lineEdit_sangFari = QtWidgets.QLineEdit(self.groupBox_inputData)
        self.lineEdit_sangFari.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("A Arghavan")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_sangFari.setFont(font)
        self.lineEdit_sangFari.setStyleSheet("")
        self.lineEdit_sangFari.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sangFari.setObjectName("lineEdit_sangFari")
        self.horizontalLayout_Sang.addWidget(self.lineEdit_sangFari)
        self.label = QtWidgets.QLabel(self.groupBox_inputData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_Sang.addWidget(self.label)
        self.lineEdit_sangAsli = QtWidgets.QLineEdit(self.groupBox_inputData)
        font = QtGui.QFont()
        font.setFamily("A Arghavan")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_sangAsli.setFont(font)
        self.lineEdit_sangAsli.setStyleSheet("")
        self.lineEdit_sangAsli.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_sangAsli.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_sangAsli.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sangAsli.setObjectName("lineEdit_sangAsli")
        self.horizontalLayout_Sang.addWidget(self.lineEdit_sangAsli)
        self.checkBox_daftar = QtWidgets.QCheckBox(self.groupBox_inputData)
        self.checkBox_daftar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_daftar.setTabletTracking(True)
        self.checkBox_daftar.setAutoFillBackground(False)
        self.checkBox_daftar.setObjectName("checkBox_daftar")
        self.horizontalLayout_Sang.addWidget(self.checkBox_daftar)
        spacerItem1 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Sang.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_Sang, 0, 0, 1, 1)
        self.horizontalLayout_QRadio = QtWidgets.QHBoxLayout()
        self.horizontalLayout_QRadio.setContentsMargins(10, 7, 10, 7)
        self.horizontalLayout_QRadio.setSpacing(30)
        self.horizontalLayout_QRadio.setObjectName("horizontalLayout_QRadio")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_QRadio.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_inputData)
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_QRadio.addWidget(self.label_2)
        self.radioButton_bakhsh26_1 = QtWidgets.QRadioButton(self.groupBox_inputData)
        self.radioButton_bakhsh26_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_bakhsh26_1.setChecked(True)
        self.radioButton_bakhsh26_1.setObjectName("radioButton_bakhsh26_1")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_bakhsh26_1)
        self.horizontalLayout_QRadio.addWidget(self.radioButton_bakhsh26_1)
        self.radioButton_bakhsh25_1 = QtWidgets.QRadioButton(self.groupBox_inputData)
        self.radioButton_bakhsh25_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_bakhsh25_1.setChecked(False)
        self.radioButton_bakhsh25_1.setObjectName("radioButton_bakhsh25_1")
        self.buttonGroup_2.addButton(self.radioButton_bakhsh25_1)
        self.horizontalLayout_QRadio.addWidget(self.radioButton_bakhsh25_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_QRadio.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_QRadio, 2, 0, 1, 1)
        self.horizontalLayout_DarkhastKonande = QtWidgets.QHBoxLayout()
        self.horizontalLayout_DarkhastKonande.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_DarkhastKonande.setSpacing(10)
        self.horizontalLayout_DarkhastKonande.setObjectName("horizontalLayout_DarkhastKonande")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_DarkhastKonande.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.groupBox_inputData)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_DarkhastKonande.addWidget(self.label_3)
        self.comboBox_Hamkaran = QtWidgets.QComboBox(self.groupBox_inputData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Hamkaran.sizePolicy().hasHeightForWidth())
        self.comboBox_Hamkaran.setSizePolicy(sizePolicy)
        self.comboBox_Hamkaran.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_Hamkaran.setEditable(False)
        self.comboBox_Hamkaran.setObjectName("comboBox_Hamkaran")
        self.comboBox_Hamkaran.addItem("")
        self.comboBox_Hamkaran.addItem("")
        self.comboBox_Hamkaran.addItem("")
        self.comboBox_Hamkaran.addItem("")
        self.comboBox_Hamkaran.addItem("")
        self.comboBox_Hamkaran.addItem("")
        self.comboBox_Hamkaran.addItem("")
        self.comboBox_Hamkaran.addItem("")
        self.comboBox_Hamkaran.addItem("")
        self.comboBox_Hamkaran.addItem("")
        self.comboBox_Hamkaran.addItem("")
        self.comboBox_Hamkaran.addItem("")
        self.horizontalLayout_DarkhastKonande.addWidget(self.comboBox_Hamkaran)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_DarkhastKonande.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.horizontalLayout_DarkhastKonande, 4, 0, 1, 1)
        self.horizontalLayout_TahvilGirande = QtWidgets.QHBoxLayout()
        self.horizontalLayout_TahvilGirande.setContentsMargins(10, 5, 10, 0)
        self.horizontalLayout_TahvilGirande.setSpacing(20)
        self.horizontalLayout_TahvilGirande.setObjectName("horizontalLayout_TahvilGirande")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_TahvilGirande.addItem(spacerItem6)
        self.label_4 = QtWidgets.QLabel(self.groupBox_inputData)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_TahvilGirande.addWidget(self.label_4)
        self.radioButton_arbabRojo = QtWidgets.QRadioButton(self.groupBox_inputData)
        self.radioButton_arbabRojo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_arbabRojo.setChecked(True)
        self.radioButton_arbabRojo.setObjectName("radioButton_arbabRojo")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_arbabRojo)
        self.horizontalLayout_TahvilGirande.addWidget(self.radioButton_arbabRojo)
        self.radioButton_hamkar = QtWidgets.QRadioButton(self.groupBox_inputData)
        self.radioButton_hamkar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_hamkar.setObjectName("radioButton_hamkar")
        self.buttonGroup_3.addButton(self.radioButton_hamkar)
        self.horizontalLayout_TahvilGirande.addWidget(self.radioButton_hamkar)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_TahvilGirande.addItem(spacerItem7)
        self.gridLayout_2.addLayout(self.horizontalLayout_TahvilGirande, 5, 0, 1, 1)
        self.horizontalLayout_sabtBtn = QtWidgets.QHBoxLayout()
        self.horizontalLayout_sabtBtn.setContentsMargins(20, 0, 20, 5)
        self.horizontalLayout_sabtBtn.setObjectName("horizontalLayout_sabtBtn")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_sabtBtn.addItem(spacerItem8)
        self.pushButton_sabt = QtWidgets.QPushButton(self.groupBox_inputData)
        self.pushButton_sabt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_sabt.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed rgb(255, 85, 0);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: #FF0000;\n"
"}\n"
"QPushButton{\n"
"background-color: #24470d  ;\n"
"font: 14pt \"A Arsoo\";\n"
"color: rgb(255, 255, 127);\n"
"border: 1px solid   #b2ff00  ;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_sabt.setAutoDefault(False)
        self.pushButton_sabt.setDefault(False)
        self.pushButton_sabt.setObjectName("pushButton_sabt")
        self.horizontalLayout_sabtBtn.addWidget(self.pushButton_sabt)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_sabtBtn.addItem(spacerItem9)
        self.gridLayout_2.addLayout(self.horizontalLayout_sabtBtn, 7, 0, 1, 1)
        self.horizontalLayout_btnNew = QtWidgets.QHBoxLayout()
        self.horizontalLayout_btnNew.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_btnNew.setObjectName("horizontalLayout_btnNew")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btnNew.addItem(spacerItem10)
        self.pushButton_new = QtWidgets.QPushButton(self.groupBox_inputData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_new.sizePolicy().hasHeightForWidth())
        self.pushButton_new.setSizePolicy(sizePolicy)
        self.pushButton_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_new.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed   #039cff  ;\n"
"    background-color:  #cddbab  ;\n"
"    color:   #d101ff  ;\n"
"}\n"
"QPushButton{\n"
"background-color:   #0087f1    ;\n"
"font: 14pt \"A Arsoo\";\n"
"color: rgb(255, 255, 127);\n"
"border: 1px solid   #2bff01 ;;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_new.setObjectName("pushButton_new")
        self.horizontalLayout_btnNew.addWidget(self.pushButton_new)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btnNew.addItem(spacerItem11)
        self.gridLayout_2.addLayout(self.horizontalLayout_btnNew, 8, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_inputData, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab1_inputData, "")
        self.tab2_SearchData = QtWidgets.QWidget()
        self.tab2_SearchData.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab2_SearchData.setStatusTip("")
        self.tab2_SearchData.setStyleSheet("QWidget{\n"
"background-color: #ece6f9  ;\n"
"}\n"
"QGroupBox{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"A Arghavan\";\n"
"border-style: dashed;\n"
"border-bottom-width: 2px;\n"
"}\n"
"QRadioButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"A Arghavan\";\n"
"}\n"
"QLabel{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 18pt \"A Arsoo\";\n"
"}\n"
"QComboBox{\n"
"background-color: #eee1c5   ;\n"
"}\n"
"QCheckBox{\n"
"font: 75 12pt \"A Arsoo\";\n"
"}\n"
"")
        self.tab2_SearchData.setObjectName("tab2_SearchData")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab2_SearchData)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab2_SearchData)
        self.groupBox.setEnabled(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, 10, 20, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_search.setEnabled(True)
        self.pushButton_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_search.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed rgb(255, 85, 0);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton{\n"
"background-color: #d3f97a   ;\n"
"font: 14pt \"A Arsoo\";\n"
"color:    #056608   ;\n"
"border: 1px solid   #003efe   ;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_search.setAutoDefault(False)
        self.pushButton_search.setDefault(False)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_2.addWidget(self.pushButton_search)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout_QRadio_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_QRadio_2.setContentsMargins(10, 7, 10, 7)
        self.horizontalLayout_QRadio_2.setSpacing(30)
        self.horizontalLayout_QRadio_2.setObjectName("horizontalLayout_QRadio_2")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_QRadio_2.addItem(spacerItem14)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_QRadio_2.addWidget(self.label_5)
        self.radioButton_bakhsh26_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_bakhsh26_2.setEnabled(True)
        self.radioButton_bakhsh26_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_bakhsh26_2.setChecked(True)
        self.radioButton_bakhsh26_2.setObjectName("radioButton_bakhsh26_2")
        self.horizontalLayout_QRadio_2.addWidget(self.radioButton_bakhsh26_2)
        self.radioButton_bakhsh25_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_bakhsh25_2.setEnabled(True)
        self.radioButton_bakhsh25_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_bakhsh25_2.setChecked(False)
        self.radioButton_bakhsh25_2.setObjectName("radioButton_bakhsh25_2")
        self.horizontalLayout_QRadio_2.addWidget(self.radioButton_bakhsh25_2)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_QRadio_2.addItem(spacerItem15)
        self.gridLayout_5.addLayout(self.horizontalLayout_QRadio_2, 1, 0, 1, 1)
        self.horizontalLayout_Sang_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Sang_2.setObjectName("horizontalLayout_Sang_2")
        spacerItem16 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Sang_2.addItem(spacerItem16)
        self.lineEdit_sangFari_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_sangFari_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("A Arghavan")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_sangFari_2.setFont(font)
        self.lineEdit_sangFari_2.setStyleSheet("")
        self.lineEdit_sangFari_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sangFari_2.setObjectName("lineEdit_sangFari_2")
        self.horizontalLayout_Sang_2.addWidget(self.lineEdit_sangFari_2)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_Sang_2.addWidget(self.label_6)
        self.lineEdit_sangAsli_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_sangAsli_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("A Arghavan")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_sangAsli_2.setFont(font)
        self.lineEdit_sangAsli_2.setStyleSheet("")
        self.lineEdit_sangAsli_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_sangAsli_2.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_sangAsli_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_sangAsli_2.setObjectName("lineEdit_sangAsli_2")
        self.horizontalLayout_Sang_2.addWidget(self.lineEdit_sangAsli_2)
        self.checkBox_daftar_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_daftar_2.setEnabled(True)
        self.checkBox_daftar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_daftar_2.setObjectName("checkBox_daftar_2")
        self.horizontalLayout_Sang_2.addWidget(self.checkBox_daftar_2)
        spacerItem17 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Sang_2.addItem(spacerItem17)
        self.gridLayout_5.addLayout(self.horizontalLayout_Sang_2, 0, 0, 1, 1)
        self.tableView_result = QtWidgets.QTableView(self.groupBox)
        self.tableView_result.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_result.sizePolicy().hasHeightForWidth())
        self.tableView_result.setSizePolicy(sizePolicy)
        self.tableView_result.setObjectName("tableView_result")
        self.gridLayout_5.addWidget(self.tableView_result, 5, 0, 1, 1)
        self.horizontalLayout_btnNew_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_btnNew_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_btnNew_2.setObjectName("horizontalLayout_btnNew_2")
        spacerItem18 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btnNew_2.addItem(spacerItem18)
        self.pushButton_bazgashBygani = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_bazgashBygani.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_bazgashBygani.sizePolicy().hasHeightForWidth())
        self.pushButton_bazgashBygani.setSizePolicy(sizePolicy)
        self.pushButton_bazgashBygani.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_bazgashBygani.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed   #039cff  ;\n"
"    background-color:  #cddbab  ;\n"
"    color:   #d101ff  ;\n"
"}\n"
"QPushButton{\n"
"background-color:#64A3F8;\n"
"font: 14pt \"A Arsoo\";\n"
"color: #EE2121;\n"
"border: 1px solid   #2bff01 ;;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_bazgashBygani.setObjectName("pushButton_bazgashBygani")
        self.horizontalLayout_btnNew_2.addWidget(self.pushButton_bazgashBygani)
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btnNew_2.addItem(spacerItem19)
        self.pushButton_print = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_print.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_print.sizePolicy().hasHeightForWidth())
        self.pushButton_print.setSizePolicy(sizePolicy)
        self.pushButton_print.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_print.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed  #FF87A6  ;\n"
"    background-color:  #5F8375  ;\n"
"    color:  #E0F354  ;\n"
"}\n"
"QPushButton{\n"
"background-color:  #96B9B9    ;\n"
"font: 14pt \"A Arsoo\";\n"
"color: #533F11;\n"
"border: 1px solid   #FE760C ;;\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_print.setObjectName("pushButton_print")
        self.horizontalLayout_btnNew_2.addWidget(self.pushButton_print)
        spacerItem20 = QtWidgets.QSpacerItem(100, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btnNew_2.addItem(spacerItem20)
        self.gridLayout_5.addLayout(self.horizontalLayout_btnNew_2, 6, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setStyleSheet("QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font: 75 12pt \"A Arghavan\";\n"
"border-style: solid;\n"
"border-bottom-width: 2px;\n"
"}\n"
"QCheckBox{\n"
"font: 75 8pt \"A Arsoo\";\n"
"}\n"
"QComboBox{\n"
"background-color: #eee1c5   ;\n"
"font: 75 10pt \"A Arsoo\";\n"
"color:#0A1F85;\n"
"border: 1px solid #096578  ;\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.checkBox_advanceSearch = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_advanceSearch.setObjectName("checkBox_advanceSearch")
        self.gridLayout_7.addWidget(self.checkBox_advanceSearch, 1, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem21, 1, 5, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_dateDay = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_dateDay.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_dateDay.sizePolicy().hasHeightForWidth())
        self.lineEdit_dateDay.setSizePolicy(sizePolicy)
        self.lineEdit_dateDay.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateDay.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateDay.setSizeIncrement(QtCore.QSize(20, 20))
        self.lineEdit_dateDay.setBaseSize(QtCore.QSize(20, 20))
        self.lineEdit_dateDay.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dateDay.setObjectName("lineEdit_dateDay")
        self.horizontalLayout.addWidget(self.lineEdit_dateDay)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(15, 46))
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.lineEdit_dateMonth = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_dateMonth.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_dateMonth.sizePolicy().hasHeightForWidth())
        self.lineEdit_dateMonth.setSizePolicy(sizePolicy)
        self.lineEdit_dateMonth.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth.setSizeIncrement(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth.setBaseSize(QtCore.QSize(20, 20))
        self.lineEdit_dateMonth.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dateMonth.setObjectName("lineEdit_dateMonth")
        self.horizontalLayout.addWidget(self.lineEdit_dateMonth)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(15, 46))
        self.label_8.setSizeIncrement(QtCore.QSize(15, 46))
        self.label_8.setBaseSize(QtCore.QSize(15, 46))
        font = QtGui.QFont()
        font.setFamily("A Arsoo")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEdit_dateYear = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_dateYear.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_dateYear.sizePolicy().hasHeightForWidth())
        self.lineEdit_dateYear.setSizePolicy(sizePolicy)
        self.lineEdit_dateYear.setMinimumSize(QtCore.QSize(35, 20))
        self.lineEdit_dateYear.setMaximumSize(QtCore.QSize(35, 20))
        self.lineEdit_dateYear.setSizeIncrement(QtCore.QSize(35, 20))
        self.lineEdit_dateYear.setBaseSize(QtCore.QSize(35, 20))
        self.lineEdit_dateYear.setMaxLength(32765)
        self.lineEdit_dateYear.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dateYear.setObjectName("lineEdit_dateYear")
        self.horizontalLayout.addWidget(self.lineEdit_dateYear)
        self.gridLayout_7.addLayout(self.horizontalLayout, 1, 4, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem22, 1, 7, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem23, 1, 3, 1, 1)
        self.comboBox_searchType = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_searchType.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_searchType.sizePolicy().hasHeightForWidth())
        self.comboBox_searchType.setSizePolicy(sizePolicy)
        self.comboBox_searchType.setMinimumSize(QtCore.QSize(220, 0))
        self.comboBox_searchType.setObjectName("comboBox_searchType")
        self.comboBox_searchType.addItem("")
        self.comboBox_searchType.addItem("")
        self.comboBox_searchType.addItem("")
        self.comboBox_searchType.addItem("")
        self.comboBox_searchType.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_searchType, 1, 6, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem24, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab2_SearchData, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_close = QtWidgets.QAction(MainWindow)
        self.action_close.setObjectName("action_close")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action_help)
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_about)
        self.menu.addSeparator()
        self.menu.addAction(self.action_close)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.action_close.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.lineEdit_sangAsli)
        MainWindow.setTabOrder(self.lineEdit_sangAsli, self.lineEdit_sangFari)
        MainWindow.setTabOrder(self.lineEdit_sangFari, self.checkBox_daftar)
        MainWindow.setTabOrder(self.checkBox_daftar, self.radioButton_bakhsh26_1)
        MainWindow.setTabOrder(self.radioButton_bakhsh26_1, self.radioButton_bakhsh25_1)
        MainWindow.setTabOrder(self.radioButton_bakhsh25_1, self.comboBox_Hamkaran)
        MainWindow.setTabOrder(self.comboBox_Hamkaran, self.radioButton_arbabRojo)
        MainWindow.setTabOrder(self.radioButton_arbabRojo, self.radioButton_hamkar)
        MainWindow.setTabOrder(self.radioButton_hamkar, self.radioButton_edary)
        MainWindow.setTabOrder(self.radioButton_edary, self.radioButton_estelam)
        MainWindow.setTabOrder(self.radioButton_estelam, self.radioButton_tafkik)
        MainWindow.setTabOrder(self.radioButton_tafkik, self.radioButton_tajmii)
        MainWindow.setTabOrder(self.radioButton_tajmii, self.radioButton_nameEdarat)
        MainWindow.setTabOrder(self.radioButton_nameEdarat, self.radioButton_darKhastSanad)
        MainWindow.setTabOrder(self.radioButton_darKhastSanad, self.radioButton_Jari)
        MainWindow.setTabOrder(self.radioButton_Jari, self.radioButton_Baresi)
        MainWindow.setTabOrder(self.radioButton_Baresi, self.radioButton_sayer)
        MainWindow.setTabOrder(self.radioButton_sayer, self.textEdit_Tozihat)
        MainWindow.setTabOrder(self.textEdit_Tozihat, self.pushButton_sabt)
        MainWindow.setTabOrder(self.pushButton_sabt, self.pushButton_new)
        MainWindow.setTabOrder(self.pushButton_new, self.lineEdit_sangAsli_2)
        MainWindow.setTabOrder(self.lineEdit_sangAsli_2, self.lineEdit_sangFari_2)
        MainWindow.setTabOrder(self.lineEdit_sangFari_2, self.checkBox_daftar_2)
        MainWindow.setTabOrder(self.checkBox_daftar_2, self.radioButton_bakhsh26_2)
        MainWindow.setTabOrder(self.radioButton_bakhsh26_2, self.radioButton_bakhsh25_2)
        MainWindow.setTabOrder(self.radioButton_bakhsh25_2, self.checkBox_advanceSearch)
        MainWindow.setTabOrder(self.checkBox_advanceSearch, self.lineEdit_dateDay)
        MainWindow.setTabOrder(self.lineEdit_dateDay, self.lineEdit_dateMonth)
        MainWindow.setTabOrder(self.lineEdit_dateMonth, self.comboBox_searchType)
        MainWindow.setTabOrder(self.comboBox_searchType, self.pushButton_search)
        MainWindow.setTabOrder(self.pushButton_search, self.pushButton_bazgashBygani)
        MainWindow.setTabOrder(self.pushButton_bazgashBygani, self.pushButton_print)
        MainWindow.setTabOrder(self.pushButton_print, self.tableView_result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "سامانه بایگانی ثبت ماسال"))
        self.tabWidget.setStatusTip(_translate("MainWindow", "  ثبت پرونده خارج شده از بایگانی"))
        self.groupBox_inputData.setTitle(_translate("MainWindow", "فرم ثبت خروج پرونده از بایگانی"))
        self.groupBox_Tozihat.setStatusTip(_translate("MainWindow", "  علت درخواست پرونده از بایگانی  "))
        self.groupBox_Tozihat.setTitle(_translate("MainWindow", "توضیحات"))
        self.textEdit_Tozihat.setStatusTip(_translate("MainWindow", "توضیحات خود را در این بخش بنویسید"))
        self.textEdit_Tozihat.setPlaceholderText(_translate("MainWindow", "توضیحات"))
        self.radioButton_sayer.setText(_translate("MainWindow", "سایر"))
        self.radioButton_darKhastSanad.setText(_translate("MainWindow", "درخواست سند"))
        self.radioButton_nameEdarat.setText(_translate("MainWindow", "نامه ادارات"))
        self.radioButton_tajmii.setText(_translate("MainWindow", "تجمیع"))
        self.radioButton_tafkik.setText(_translate("MainWindow", "تفکیک"))
        self.radioButton_estelam.setText(_translate("MainWindow", "استعلام"))
        self.radioButton_edary.setText(_translate("MainWindow", "اداری"))
        self.radioButton_Jari.setText(_translate("MainWindow", "جاری"))
        self.radioButton_Baresi.setText(_translate("MainWindow", "بررسی"))
        self.lineEdit_sangFari.setStatusTip(_translate("MainWindow", "سنگ فرعی را وارد کنید"))
        self.lineEdit_sangFari.setPlaceholderText(_translate("MainWindow", "سنگ فرعی"))
        self.label.setText(_translate("MainWindow", "/"))
        self.lineEdit_sangAsli.setStatusTip(_translate("MainWindow", "سنگ اصلی را وارد کنید"))
        self.lineEdit_sangAsli.setPlaceholderText(_translate("MainWindow", "سنگ اصلی"))
        self.checkBox_daftar.setStatusTip(_translate("MainWindow", "   درخواست دریافت دفتر از بایگانی  "))
        self.checkBox_daftar.setText(_translate("MainWindow", "دفتر"))
        self.label_2.setStatusTip(_translate("MainWindow", "بخش را انتخاب کنید"))
        self.label_2.setText(_translate("MainWindow", "بخش:"))
        self.radioButton_bakhsh26_1.setStatusTip(_translate("MainWindow", "بخش 26 گیلان"))
        self.radioButton_bakhsh26_1.setText(_translate("MainWindow", "26"))
        self.radioButton_bakhsh25_1.setStatusTip(_translate("MainWindow", "بخش 25 گیلان"))
        self.radioButton_bakhsh25_1.setText(_translate("MainWindow", "25"))
        self.label_3.setStatusTip(_translate("MainWindow", "همکار تقاضا کننده پرونده را مشخص کنید"))
        self.label_3.setText(_translate("MainWindow", "همکار تقاضا کننده:"))
        self.comboBox_Hamkaran.setStatusTip(_translate("MainWindow", "همکار تقاضا کننده پرونده را مشخص کنید"))
        self.comboBox_Hamkaran.setCurrentText(_translate("MainWindow", "کیوان حسنجانی"))
        self.comboBox_Hamkaran.setItemText(0, _translate("MainWindow", "کیوان حسنجانی"))
        self.comboBox_Hamkaran.setItemText(1, _translate("MainWindow", "صائمه امجدی"))
        self.comboBox_Hamkaran.setItemText(2, _translate("MainWindow", "سیدمحمد آتشی"))
        self.comboBox_Hamkaran.setItemText(3, _translate("MainWindow", "علی رحمانی"))
        self.comboBox_Hamkaran.setItemText(4, _translate("MainWindow", "آرمان کاظمی"))
        self.comboBox_Hamkaran.setItemText(5, _translate("MainWindow", "یداله شهبازی"))
        self.comboBox_Hamkaran.setItemText(6, _translate("MainWindow", "سیدرشید کاظمی"))
        self.comboBox_Hamkaran.setItemText(7, _translate("MainWindow", "سیدمحمد موسوی"))
        self.comboBox_Hamkaran.setItemText(8, _translate("MainWindow", "صدیقه روشن"))
        self.comboBox_Hamkaran.setItemText(9, _translate("MainWindow", "محسن مهرافشان"))
        self.comboBox_Hamkaran.setItemText(10, _translate("MainWindow", "علیرضا آزادی"))
        self.comboBox_Hamkaran.setItemText(11, _translate("MainWindow", "سایر"))
        self.label_4.setStatusTip(_translate("MainWindow", "تحویل گیرنده پرونده از بایگانی را انتخاب کنید"))
        self.label_4.setText(_translate("MainWindow", "تحویل گیرنده:"))
        self.radioButton_arbabRojo.setStatusTip(_translate("MainWindow", "تحویل گیرنده پرونده از بایگانی را انتخاب کنید"))
        self.radioButton_arbabRojo.setText(_translate("MainWindow", "ارباب رجوع"))
        self.radioButton_hamkar.setStatusTip(_translate("MainWindow", "تحویل گیرنده پرونده از بایگانی را انتخاب کنید"))
        self.radioButton_hamkar.setText(_translate("MainWindow", "همکار"))
        self.pushButton_sabt.setStatusTip(_translate("MainWindow", "برای ثبت کلیک کنید"))
        self.pushButton_sabt.setText(_translate("MainWindow", "ثبت"))
        self.pushButton_new.setStatusTip(_translate("MainWindow", "پاکسازی فرم برای ثبت اطلاعات جدید"))
        self.pushButton_new.setText(_translate("MainWindow", "   جدید   "))
        self.pushButton_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1_inputData), _translate("MainWindow", "ورود اطلاعات"))
        self.groupBox.setStatusTip(_translate("MainWindow", "   جستجوی سوابق پرونده خارج شده از بایگانی"))
        self.groupBox.setTitle(_translate("MainWindow", "فرم بازیابی اطلاعات ثبت شده"))
        self.pushButton_search.setStatusTip(_translate("MainWindow", "برای جستجو اطلاعات ذخیره شده کلیک کنید"))
        self.pushButton_search.setText(_translate("MainWindow", "جستجو"))
        self.pushButton_search.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.label_5.setStatusTip(_translate("MainWindow", "بخش را انتخاب کنید"))
        self.label_5.setText(_translate("MainWindow", "بخش:"))
        self.radioButton_bakhsh26_2.setText(_translate("MainWindow", "26"))
        self.radioButton_bakhsh25_2.setText(_translate("MainWindow", "25"))
        self.lineEdit_sangFari_2.setStatusTip(_translate("MainWindow", "سنگ فرعی را وارد کنید"))
        self.lineEdit_sangFari_2.setPlaceholderText(_translate("MainWindow", "سنگ فرعی"))
        self.label_6.setText(_translate("MainWindow", "/"))
        self.lineEdit_sangAsli_2.setStatusTip(_translate("MainWindow", "سنگ اصلی را وارد کنید"))
        self.lineEdit_sangAsli_2.setPlaceholderText(_translate("MainWindow", "سنگ اصلی"))
        self.checkBox_daftar_2.setStatusTip(_translate("MainWindow", "   بازیابی دفتر خارج شده از بایگانی   "))
        self.checkBox_daftar_2.setText(_translate("MainWindow", "دفتر"))
        self.pushButton_bazgashBygani.setStatusTip(_translate("MainWindow", "  ثبت پرونده بازگشت داده شده به بایگانی"))
        self.pushButton_bazgashBygani.setText(_translate("MainWindow", "بازگشت پرونده به بایگانی"))
        self.pushButton_print.setStatusTip(_translate("MainWindow", "پرینت اطلاعات بازیابی شده"))
        self.pushButton_print.setText(_translate("MainWindow", "     پرینت     "))
        self.groupBox_2.setTitle(_translate("MainWindow", "بازیابی پیشرفته"))
        self.checkBox_advanceSearch.setText(_translate("MainWindow", "بازیابی پیشرفته"))
        self.lineEdit_dateDay.setPlaceholderText(_translate("MainWindow", "روز"))
        self.label_7.setText(_translate("MainWindow", "/"))
        self.lineEdit_dateMonth.setPlaceholderText(_translate("MainWindow", "ماه"))
        self.label_8.setText(_translate("MainWindow", "/"))
        self.lineEdit_dateYear.setPlaceholderText(_translate("MainWindow", "سال"))
        self.comboBox_searchType.setItemText(0, _translate("MainWindow", "کلیه سوابق موجود"))
        self.comboBox_searchType.setItemText(1, _translate("MainWindow", "بازگشت داده نشده"))
        self.comboBox_searchType.setItemText(2, _translate("MainWindow", "بازگشت داده شده"))
        self.comboBox_searchType.setItemText(3, _translate("MainWindow", "کلیه پرونده های بازگشت داده نشده"))
        self.comboBox_searchType.setItemText(4, _translate("MainWindow", "کلیه پرونده های بازگشت داده شده"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2_SearchData), _translate("MainWindow", "بازیابی اطلاعات"))
        self.menu.setTitle(_translate("MainWindow", "فایل"))
        self.action_help.setText(_translate("MainWindow", "راهنما"))
        self.action_about.setText(_translate("MainWindow", "درباره"))
        self.action_close.setText(_translate("MainWindow", "بستن"))
        self.action.setText(_translate("MainWindow", "تغییر رمز ورود"))


