################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Starting point created by: Qt User Interface Compiler version 5.15.2
##
## Modifications to compiled .ui file were completed by Corey R. Randall. These
## include: adding space for readability, rearranging objects to match GUI
## layout and make modifying the UI easier, function codes to add capabilities
## to UI objects (e.g. buttons, spinbox, combobox, etc.).
##
## NOTES: To modidy this code for another Modbus RTU controller, make note of
## the read and write registers from the user manual. Afterward, do a search to
## replace the read registers (hard-coded as 20 in this file) and the write
## registers (hard-coded as 34 in this file). You may also choose to reset the
## allowable min and max values of the SPInput object. Lastly, the stop_loop
## function is currently set up to reset the controller set point to 20C before
## stopping the reading protocol.
################################################################################

import minimalmodbus as mb
import dummy_serial
import test_minimalmodbus
import time, serial, serial.tools.list_ports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from threading import Thread

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(4)

        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)

        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(18)

        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(24)

        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())

        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)

        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)

        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)

        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)

        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(2)

        MainWindow.resize(733, 308)
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setFont(font)

        self.actionInformation = QAction(MainWindow)
        self.actionInformation.setObjectName(u"actionInformation")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 591, 271))

        self.tabWidget.setFont(font1)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)

        self.tab_MW = QWidget()
        self.tab_MW.setObjectName(u"tab_MW")
        self.tab_MW.setAutoFillBackground(True)

        self.verticalLayout = QVBoxLayout(self.tab_MW)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)

        self.frame = QFrame(self.tab_MW)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(75)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(15, 10, 15, 10)

        self.COMLabelWatlow = QLabel(self.frame)
        self.COMLabelWatlow.setObjectName(u"COMLabelWatlow")
        sizePolicy3.setHeightForWidth(self.COMLabelWatlow.sizePolicy().hasHeightForWidth())
        self.COMLabelWatlow.setSizePolicy(sizePolicy3)
        self.COMLabelWatlow.setMinimumSize(QSize(175, 31))
        self.COMLabelWatlow.setFont(font2)

        self.gridLayout.addWidget(self.COMLabelWatlow, 0, 0, 1, 1)

        self.COMPortWatlow = QComboBox(self.frame)

        self.ports = ["DUMMY"]
        self.ports.extend([p.device for p in serial.tools.list_ports.comports()])

        for i,p in enumerate(self.ports):
            self.COMPortWatlow.addItem("")

        self.COMPortWatlow.setObjectName(u"COMPortWatlow")
        sizePolicy3.setHeightForWidth(self.COMPortWatlow.sizePolicy().hasHeightForWidth())
        self.COMPortWatlow.setSizePolicy(sizePolicy3)
        self.COMPortWatlow.setMinimumSize(QSize(175, 51))
        self.COMPortWatlow.setBaseSize(QSize(0, 0))
        self.COMPortWatlow.setFont(font2)
        self.COMPortWatlow.setAutoFillBackground(False)
        self.COMPortWatlow.setEditable(False)
        self.COMPortWatlow.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.COMPortWatlow, 1, 0, 1, 1)

        self.StartButton = QPushButton(self.frame)
        self.StartButton.setObjectName(u"StartButton")
        sizePolicy4.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy4)
        self.StartButton.setMinimumSize(QSize(175, 111))
        self.StartButton.setStyleSheet("QPushButton:enabled {background-color: #6baa41;}\n"
                                       "QPushButton {background-color: grey;}\n")
        self.StartButton.setFont(font2)
        self.StartButton.clicked.connect(self.start_loop)

        self.gridLayout.addWidget(self.StartButton, 2, 0, 2, 1)

        self.SPLabel = QLabel(self.frame)
        self.SPLabel.setObjectName(u"SPLabel")
        sizePolicy3.setHeightForWidth(self.SPLabel.sizePolicy().hasHeightForWidth())
        self.SPLabel.setSizePolicy(sizePolicy3)
        self.SPLabel.setMinimumSize(QSize(175, 31))
        self.SPLabel.setFont(font2)

        self.gridLayout.addWidget(self.SPLabel, 0, 1, 1, 1)

        self.SPDisplay = QLCDNumber(self.frame)
        self.SPDisplay.setObjectName(u"SPDisplay")
        self.SPDisplay.setMinimumSize(QSize(175, 51))
        self.SPDisplay.setAutoFillBackground(True)
        self.SPDisplay.setLineWidth(2)
        self.SPDisplay.setSmallDecimalPoint(False)
        self.SPDisplay.setDigitCount(7)
        self.SPDisplay.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.SPDisplay, 1, 1, 1, 1)

        self.SPInput = QSpinBox(self.frame)
        self.SPInput.setObjectName(u"SPInput")
        sizePolicy2.setHeightForWidth(self.SPInput.sizePolicy().hasHeightForWidth())
        self.SPInput.setSizePolicy(sizePolicy2)
        self.SPInput.setMinimumSize(QSize(175, 51))
        self.SPInput.setFont(font3)
        self.SPInput.setLayoutDirection(Qt.RightToLeft)
        self.SPInput.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SPInput.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SPInput.setAccelerated(True)
        self.SPInput.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.SPInput.setMinimum(20)
        self.SPInput.setMaximum(99)
        self.SPInput.setSpecialValueText("min 20")

        self.gridLayout.addWidget(self.SPInput, 2, 1, 1, 1)

        self.EngageButton = QPushButton(self.frame)
        self.EngageButton.setObjectName(u"EngageButton")
        sizePolicy5.setHeightForWidth(self.EngageButton.sizePolicy().hasHeightForWidth())
        self.EngageButton.setSizePolicy(sizePolicy5)
        self.EngageButton.setMinimumSize(QSize(175, 51))
        self.EngageButton.setStyleSheet("QPushButton:enabled {background-color: #5E8CAD;}\n"
                                        "QPushButton:pressed {background-color: grey;}\n")
        self.EngageButton.setFont(font2)
        self.EngageButton.clicked.connect(self.write_SP)

        self.gridLayout.addWidget(self.EngageButton, 3, 1, 1, 1)

        self.PVLabel = QLabel(self.frame)
        self.PVLabel.setObjectName(u"PVLabel")
        sizePolicy3.setHeightForWidth(self.PVLabel.sizePolicy().hasHeightForWidth())
        self.PVLabel.setSizePolicy(sizePolicy3)
        self.PVLabel.setMinimumSize(QSize(175, 31))
        self.PVLabel.setFont(font2)

        self.PVDisplay = QLCDNumber(self.frame)
        self.PVDisplay.setObjectName(u"PVDisplay")
        self.PVDisplay.setMinimumSize(QSize(175, 51))
        self.PVDisplay.setAutoFillBackground(True)
        self.PVDisplay.setLineWidth(2)
        self.PVDisplay.setDigitCount(7)
        self.PVDisplay.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.PVLabel, 0, 2, 1, 1)
        self.gridLayout.setRowStretch(0, 2)

        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame)

        self.gridLayout.addWidget(self.PVDisplay, 1, 2, 1, 1)

        self.StopButton = QPushButton(self.frame)
        self.StopButton.setObjectName(u"StopButton")
        sizePolicy4.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy4)
        self.StopButton.setMinimumSize(QSize(175, 111))
        self.StopButton.setStyleSheet("QPushButton:enabled {background-color: #d94e47;}\n"
                                      "QPushButton:pressed {background-color: grey;}\n")
        self.StopButton.setFont(font2)
        self.StopButton.clicked.connect(self.stop_loop)

        self.gridLayout.addWidget(self.StopButton, 2, 2, 2, 1)

        self.tabWidget.addTab(self.tab_MW, "")
        self.tab_ABT = QWidget()
        self.tab_ABT.setObjectName(u"tab_ABT")
        self.tab_ABT.setAutoFillBackground(True)

        self.verticalLayout_4 = QVBoxLayout(self.tab_ABT)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)

        palette = QPalette()
        brush = QBrush(QColor(235, 236, 235, 0))
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        self.textBrowser = QTextBrowser(self.tab_ABT)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 11, 571, 221))
        self.textBrowser.setPalette(palette)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)
        self.textBrowser.setOpenExternalLinks(True)
        self.tabWidget.addTab(self.tab_ABT, "")

        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_4.addWidget(self.textBrowser)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setFont(font4)
        self.statusTime = 3000
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Heat Controller App", None))
        self.actionInformation.setText(QCoreApplication.translate("MainWindow", u"Information", None))

        self.COMLabelWatlow.setText(QCoreApplication.translate("MainWindow", u"COM Port", None))

        for i,p in enumerate(self.ports):
            self.COMPortWatlow.setItemText(i, QCoreApplication.translate("MainWindow", p, None))

        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"START", None))

        self.SPLabel.setText(QCoreApplication.translate("MainWindow", u"SP (degr C)", None))
        self.EngageButton.setText(QCoreApplication.translate("MainWindow", u"Engage", None))

        self.PVLabel.setText(QCoreApplication.translate("MainWindow", u"PV (degr C)", None))
        self.StopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_MW), QCoreApplication.translate("MainWindow", u"Main Window", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial','Arial','Arial'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,Arial';\">This GUI was made to control a Watlow EHG-SL10 heat controller. The tool was developed by Corey R. Randall at Colorado School of Mines in 2022. </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial,Arial';\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\"><span style=\" font-family:'Arial,Arial';\">Although the program is available as a single executable file, the original files (gui.ui and main.py) are included on </span><a href=\"https://github.com/c-randall\"><span style=\" font-family:'Arial,Arial'; text-decoration: underline; color:#0068da;\">Github</span></a><span style=\" font-family:'Arial,Arial';\">. These files can be edited to control other Modbus RTU heat controllers by adjusting the appropriate read/write registers inside the main.py file. </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial,Arial';\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial,Arial';\">Moderate knowledge of the Python coding language is necessary to understand and modify the original f"
                        "iles. An environment with dependencies for pyqt5-tools (used to build the GUI) and minimalmodbus (used for the serial communication) is required. </span></p></body></html>", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ABT), QCoreApplication.translate("MainWindow", u"About", None))

        # create first instance of reader
        self.storeSerial = mb.serial.Serial
        dictConnection = self.connection()
        self.reader = Reader(dictConnection,self.PVDisplay,self.SPDisplay)

        for k in dictConnection.keys():
            setattr(self,k,dictConnection[k])

    def connection(self):
        flag = 0
        COM = self.COMPortWatlow.currentText()

        try:
            mb.serial.Serial = self.storeSerial
            watlow = mb.Instrument(COM,1)
            watlow.serial.baudrate = 9600
            watlow.serial.bytesize = 8
            watlow.serial.timeout  = 1
            watlow.serial.parity   = serial.PARITY_NONE
            watlow.serial.stopbits = 1

            watlow.mode = mb.MODE_RTU
            watlow.clear_buffers_each_transaction = True
            watlow.read_register(20,0)
            watlow.read_register(34,0)

            self.statusBar.showMessage("Connected to "+COM,self.statusTime)

        except:
            if COM != "DUMMY":
                flag = 1
                statusText = "Cannot connect to "+COM
            else:
                statusText = "Connecting to "+COM

            self.statusBar.showMessage(statusText,self.statusTime)

            self.COMPortWatlow.setCurrentText("DUMMY")
            dummy_serial.RESPONSES = test_minimalmodbus.RTU_RESPONSES
            mb.serial.Serial = dummy_serial.Serial
            watlow = mb.Instrument('DUMMYPORTNAME',1)

            COM = self.COMPortWatlow.currentText()
            # watlow.read_register(4097,1)
            # watlow.write_register(4097,823.6,1)

        return {"watlow":watlow, "COM":COM, "flag":flag}

    def start_loop(self):

        dictConnection = self.connection()

        for k in dictConnection.keys():
            setattr(self,k,dictConnection[k])

        self.thread = QThread()
        self.reader = Reader(dictConnection,self.PVDisplay,self.SPDisplay)
        self.reader.moveToThread(self.thread)
        self.thread.started.connect(self.reader.runner)
        self.reader.finished.connect(self.thread.quit)
        self.reader.finished.connect(self.reader.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.reader.PV_sig.connect(self.display_PV)
        self.reader.SP_sig.connect(self.display_SP)

        self.thread.start()

        self.StartButton.setEnabled(False)
        self.thread.finished.connect(lambda: self.StartButton.setEnabled(True))

    def write_SP(self,**kwargs):
        SP = kwargs.get('SP',self.SPInput.value())
        if SP < 20:
            SP = 20
            self.SPInput.setValue(20)
            self.SPInput.setStatusTip("Temps allowed: 20--99 C")
            self.statusBar.showMessage("Min allowed temp is 20 C",self.statusTime)
        if SP > 99:
            SP = 99
            self.SPInput.setValue(99)
            self.statusBar.showMessage("Max allowed temp is 99 C",self.statusTime)

        if self.COM != "DUMMY":
            self.watlow.write_register(34,SP,0,functioncode=6)

        self.display_SP(SP)

        self.statusBar.showMessage("Set point updating...",self.statusTime)

    def stop_loop(self):
        self.reader.run = 0
        self.write_SP(SP=20)
        self.display_SP(20)

    def display_PV(self,PV):
        if self.COM != "DUMMY": PV = self.watlow.read_register(20,0)
        self.PVDisplay.display(PV)

    def display_SP(self,SP):
        if self.COM != "DUMMY": SP = self.watlow.read_register(34,0)
        self.SPDisplay.display(SP)

class Reader(QThread):
    finished = pyqtSignal()
    PV_sig = pyqtSignal(int)
    SP_sig = pyqtSignal(int)

    def __init__(self,dictConnection,PVDisplay,SPDisplay):
        QThread.__init__(self)

        for k in dictConnection.keys():
            setattr(self,k,dictConnection[k])

        if self.COM == 'DUMMY': self.PV_reg, self.SP_reg = 4097, 4097
        else: self.PV_reg, self.SP_reg = 20, 34

        self.PVDisplay = PVDisplay
        self.SPDisplay = SPDisplay

        self.PV = self.watlow.read_register(self.PV_reg,0)
        self.SP = self.watlow.read_register(self.SP_reg,0)

        self.run = 1

    def runner(self):
        if self.COM == 'DUMMY':
            self.PV = self.PVDisplay.intValue()
            while all([self.run,self.flag == 0]):
                self.SP = self.SPDisplay.intValue()
                if self.PV > self.SP:
                    self.PV = self.PV - 1
                elif self.PV < self.SP:
                    self.PV = self.PV + 1

                # if self.SP > 99:
                #     self.SP = 0
                # else:
                #     self.SP = self.SP + 1

                self.PV_sig.emit(self.PV)
                self.SP_sig.emit(self.SP)
                time.sleep(1)

            self.finished.emit()

        else:
            while self.run:
                self.PV = self.watlow.read_register(self.PV_reg,0)
                self.SP = self.watlow.read_register(self.SP_reg,0)

                self.PV_sig.emit(self.PV)
                self.SP_sig.emit(self.SP)
                time.sleep(1)

            self.finished.emit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
