import os
import dummy_serial
import test_minimalmodbus
import minimalmodbus as mb
import time, serial, serial.tools.list_ports

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from threading import Thread
from PyQt5.QtCore import QObject, QThread, QSettings, pyqtSignal, pyqtSlot

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        # uic.loadUi(os.getcwd()+"/gui.ui", self) # Load the .ui file

        self.setObjectName("MainWindow")
        self.resize(811, 309)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(4)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_MW = QtWidgets.QWidget()
        self.tab_MW.setAutoFillBackground(True)
        self.tab_MW.setObjectName("tab_MW")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_MW)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.tab_MW)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(15, 10, 15, 10)
        self.gridLayout.setHorizontalSpacing(75)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.SPInput = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.SPInput.sizePolicy().hasHeightForWidth())
        self.SPInput.setSizePolicy(sizePolicy)
        self.SPInput.setMinimumSize(QtCore.QSize(175, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.SPInput.setFont(font)
        self.SPInput.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.SPInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SPInput.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.SPInput.setSpecialValueText("")
        self.SPInput.setAccelerated(True)
        self.SPInput.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.SPInput.setMinimum(20)
        self.SPInput.setObjectName("SPInput")
        self.gridLayout.addWidget(self.SPInput, 2, 1, 1, 1)
        self.SPLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SPLabel.sizePolicy().hasHeightForWidth())
        self.SPLabel.setSizePolicy(sizePolicy)
        self.SPLabel.setMinimumSize(QtCore.QSize(175, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.SPLabel.setFont(font)
        self.SPLabel.setObjectName("SPLabel")
        self.gridLayout.addWidget(self.SPLabel, 0, 1, 1, 1)
        self.COMPortWatlow = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.COMPortWatlow.sizePolicy().hasHeightForWidth())
        self.COMPortWatlow.setSizePolicy(sizePolicy)
        self.COMPortWatlow.setMinimumSize(QtCore.QSize(175, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.COMPortWatlow.setFont(font)
        self.COMPortWatlow.setAutoFillBackground(True)
        self.COMPortWatlow.setObjectName("COMPortWatlow")
        self.gridLayout.addWidget(self.COMPortWatlow, 1, 0, 1, 1)
        self.StartButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy)
        self.StartButton.setMinimumSize(QtCore.QSize(175, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.gridLayout.addWidget(self.StartButton, 2, 0, 2, 1)
        self.SPDisplay = QtWidgets.QLCDNumber(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.SPDisplay.sizePolicy().hasHeightForWidth())
        self.SPDisplay.setSizePolicy(sizePolicy)
        self.SPDisplay.setMinimumSize(QtCore.QSize(175, 51))
        self.SPDisplay.setAutoFillBackground(True)
        self.SPDisplay.setLineWidth(2)
        self.SPDisplay.setSmallDecimalPoint(False)
        self.SPDisplay.setDigitCount(7)
        self.SPDisplay.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.SPDisplay.setObjectName("SPDisplay")
        self.gridLayout.addWidget(self.SPDisplay, 1, 1, 1, 1)
        self.StopButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy)
        self.StopButton.setMinimumSize(QtCore.QSize(175, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.StopButton.setFont(font)
        self.StopButton.setObjectName("StopButton")
        self.gridLayout.addWidget(self.StopButton, 2, 2, 2, 1)
        self.COMLabelWatlow = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.COMLabelWatlow.sizePolicy().hasHeightForWidth())
        self.COMLabelWatlow.setSizePolicy(sizePolicy)
        self.COMLabelWatlow.setMinimumSize(QtCore.QSize(175, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.COMLabelWatlow.setFont(font)
        self.COMLabelWatlow.setObjectName("COMLabelWatlow")
        self.gridLayout.addWidget(self.COMLabelWatlow, 0, 0, 1, 1)
        self.PVDisplay = QtWidgets.QLCDNumber(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.PVDisplay.sizePolicy().hasHeightForWidth())
        self.PVDisplay.setSizePolicy(sizePolicy)
        self.PVDisplay.setMinimumSize(QtCore.QSize(175, 51))
        self.PVDisplay.setAutoFillBackground(True)
        self.PVDisplay.setLineWidth(2)
        self.PVDisplay.setDigitCount(7)
        self.PVDisplay.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.PVDisplay.setObjectName("PVDisplay")
        self.gridLayout.addWidget(self.PVDisplay, 1, 2, 1, 1)
        self.EngageButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.EngageButton.sizePolicy().hasHeightForWidth())
        self.EngageButton.setSizePolicy(sizePolicy)
        self.EngageButton.setMinimumSize(QtCore.QSize(175, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.EngageButton.setFont(font)
        self.EngageButton.setObjectName("EngageButton")
        self.gridLayout.addWidget(self.EngageButton, 3, 1, 1, 1)
        self.PVLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PVLabel.sizePolicy().hasHeightForWidth())
        self.PVLabel.setSizePolicy(sizePolicy)
        self.PVLabel.setMinimumSize(QtCore.QSize(175, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PVLabel.setFont(font)
        self.PVLabel.setObjectName("PVLabel")
        self.gridLayout.addWidget(self.PVLabel, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame)
        self.tabWidget.addTab(self.tab_MW, "")
        self.tab_CNFG = QtWidgets.QWidget()
        self.tab_CNFG.setAutoFillBackground(True)
        self.tab_CNFG.setObjectName("tab_CNFG")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_CNFG)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 10, 20, 20)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MaxTemp = QtWidgets.QSpinBox(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MaxTemp.sizePolicy().hasHeightForWidth())
        self.MaxTemp.setSizePolicy(sizePolicy)
        self.MaxTemp.setMinimumSize(QtCore.QSize(121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.MaxTemp.setFont(font)
        self.MaxTemp.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MaxTemp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MaxTemp.setAccelerated(True)
        self.MaxTemp.setMaximum(1000)
        self.MaxTemp.setObjectName("MaxTemp")
        self.gridLayout_2.addWidget(self.MaxTemp, 2, 7, 1, 1)
        self.SPOptionsLabel = QtWidgets.QLabel(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SPOptionsLabel.sizePolicy().hasHeightForWidth())
        self.SPOptionsLabel.setSizePolicy(sizePolicy)
        self.SPOptionsLabel.setMinimumSize(QtCore.QSize(150, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.SPOptionsLabel.setFont(font)
        self.SPOptionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SPOptionsLabel.setObjectName("SPOptionsLabel")
        self.gridLayout_2.addWidget(self.SPOptionsLabel, 0, 2, 1, 1)
        self.PVOptionsLabel = QtWidgets.QLabel(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PVOptionsLabel.sizePolicy().hasHeightForWidth())
        self.PVOptionsLabel.setSizePolicy(sizePolicy)
        self.PVOptionsLabel.setMinimumSize(QtCore.QSize(150, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PVOptionsLabel.setFont(font)
        self.PVOptionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PVOptionsLabel.setObjectName("PVOptionsLabel")
        self.gridLayout_2.addWidget(self.PVOptionsLabel, 0, 3, 1, 1)
        self.TempOptionsLabel = QtWidgets.QLabel(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TempOptionsLabel.sizePolicy().hasHeightForWidth())
        self.TempOptionsLabel.setSizePolicy(sizePolicy)
        self.TempOptionsLabel.setMinimumSize(QtCore.QSize(150, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.TempOptionsLabel.setFont(font)
        self.TempOptionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TempOptionsLabel.setObjectName("TempOptionsLabel")
        self.gridLayout_2.addWidget(self.TempOptionsLabel, 0, 7, 1, 1)
        self.MinTemp = QtWidgets.QSpinBox(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MinTemp.sizePolicy().hasHeightForWidth())
        self.MinTemp.setSizePolicy(sizePolicy)
        self.MinTemp.setMinimumSize(QtCore.QSize(121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.MinTemp.setFont(font)
        self.MinTemp.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MinTemp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MinTemp.setAccelerated(True)
        self.MinTemp.setMaximum(1000)
        self.MinTemp.setObjectName("MinTemp")
        self.gridLayout_2.addWidget(self.MinTemp, 1, 7, 1, 1)
        self.PVRegister = QtWidgets.QSpinBox(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.PVRegister.sizePolicy().hasHeightForWidth())
        self.PVRegister.setSizePolicy(sizePolicy)
        self.PVRegister.setMinimumSize(QtCore.QSize(121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.PVRegister.setFont(font)
        self.PVRegister.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.PVRegister.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PVRegister.setAccelerated(True)
        self.PVRegister.setMaximum(1000)
        self.PVRegister.setObjectName("PVRegister")
        self.gridLayout_2.addWidget(self.PVRegister, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 4, 1, 1)
        self.SPRegister = QtWidgets.QSpinBox(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.SPRegister.sizePolicy().hasHeightForWidth())
        self.SPRegister.setSizePolicy(sizePolicy)
        self.SPRegister.setMinimumSize(QtCore.QSize(121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.SPRegister.setFont(font)
        self.SPRegister.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.SPRegister.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SPRegister.setAccelerated(True)
        self.SPRegister.setMaximum(1000)
        self.SPRegister.setObjectName("SPRegister")
        self.gridLayout_2.addWidget(self.SPRegister, 1, 2, 1, 1)
        self.MinTempLabel = QtWidgets.QLabel(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MinTempLabel.sizePolicy().hasHeightForWidth())
        self.MinTempLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.MinTempLabel.setFont(font)
        self.MinTempLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MinTempLabel.setObjectName("MinTempLabel")
        self.gridLayout_2.addWidget(self.MinTempLabel, 1, 5, 1, 1)
        self.PVFuncCode = QtWidgets.QSpinBox(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.PVFuncCode.sizePolicy().hasHeightForWidth())
        self.PVFuncCode.setSizePolicy(sizePolicy)
        self.PVFuncCode.setMinimumSize(QtCore.QSize(121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.PVFuncCode.setFont(font)
        self.PVFuncCode.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.PVFuncCode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PVFuncCode.setAccelerated(True)
        self.PVFuncCode.setMinimum(0)
        self.PVFuncCode.setMaximum(16)
        self.PVFuncCode.setObjectName("PVFuncCode")
        self.gridLayout_2.addWidget(self.PVFuncCode, 2, 3, 1, 1)
        self.SPFuncCode = QtWidgets.QSpinBox(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.SPFuncCode.sizePolicy().hasHeightForWidth())
        self.SPFuncCode.setSizePolicy(sizePolicy)
        self.SPFuncCode.setMinimumSize(QtCore.QSize(121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.SPFuncCode.setFont(font)
        self.SPFuncCode.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.SPFuncCode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SPFuncCode.setAccelerated(True)
        self.SPFuncCode.setMinimum(0)
        self.SPFuncCode.setMaximum(16)
        self.SPFuncCode.setObjectName("SPFuncCode")
        self.gridLayout_2.addWidget(self.SPFuncCode, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(5, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 6, 1, 1)
        self.MaxTemLabel = QtWidgets.QLabel(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MaxTemLabel.sizePolicy().hasHeightForWidth())
        self.MaxTemLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.MaxTemLabel.setFont(font)
        self.MaxTemLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MaxTemLabel.setObjectName("MaxTemLabel")
        self.gridLayout_2.addWidget(self.MaxTemLabel, 2, 5, 1, 1)
        self.FuncCodeLabel = QtWidgets.QLabel(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FuncCodeLabel.sizePolicy().hasHeightForWidth())
        self.FuncCodeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.FuncCodeLabel.setFont(font)
        self.FuncCodeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FuncCodeLabel.setObjectName("FuncCodeLabel")
        self.gridLayout_2.addWidget(self.FuncCodeLabel, 2, 0, 1, 1)
        self.RegLabel = QtWidgets.QLabel(self.tab_CNFG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegLabel.sizePolicy().hasHeightForWidth())
        self.RegLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.RegLabel.setFont(font)
        self.RegLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RegLabel.setObjectName("RegLabel")
        self.gridLayout_2.addWidget(self.RegLabel, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(5, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(2, 2)
        self.gridLayout_2.setColumnStretch(3, 2)
        self.gridLayout_2.setColumnStretch(4, 1)
        self.gridLayout_2.setColumnStretch(7, 2)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_CNFG, "")
        self.tab_DIR = QtWidgets.QWidget()
        self.tab_DIR.setObjectName("tab_DIR")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_DIR)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_DIR)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowser_2.setPalette(palette)
        self.textBrowser_2.setAutoFillBackground(True)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_2.setOpenExternalLinks(True)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_6.addWidget(self.textBrowser_2)
        self.tabWidget.addTab(self.tab_DIR, "")
        self.tab_ABT = QtWidgets.QWidget()
        self.tab_ABT.setAutoFillBackground(True)
        self.tab_ABT.setObjectName("tab_ABT")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_ABT)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_ABT)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowser.setPalette(palette)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab_ABT, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.statusBar.setFont(font)
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)
        self.actionInformation = QtWidgets.QAction()
        self.actionInformation.setObjectName("actionInformation")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Heat Controller App"))
        self.SPLabel.setText(_translate("MainWindow", "SP (degr C)"))
        self.StartButton.setText(_translate("MainWindow", "START"))
        self.StopButton.setText(_translate("MainWindow", "STOP"))
        self.COMLabelWatlow.setText(_translate("MainWindow", "COM Port"))
        self.EngageButton.setText(_translate("MainWindow", "Engage"))
        self.PVLabel.setText(_translate("MainWindow", "PV (degr C)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_MW), _translate("MainWindow", "Main Window"))
        self.SPOptionsLabel.setText(_translate("MainWindow", "SP Options"))
        self.PVOptionsLabel.setText(_translate("MainWindow", "PV Options"))
        self.TempOptionsLabel.setText(_translate("MainWindow", "Temp Options"))
        self.MinTempLabel.setText(_translate("MainWindow", "Min (degr C)"))
        self.MaxTemLabel.setText(_translate("MainWindow", "Max (degr C)"))
        self.FuncCodeLabel.setText(_translate("MainWindow", "Function Code"))
        self.RegLabel.setText(_translate("MainWindow", "Register #"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_CNFG), _translate("MainWindow", "Configure"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\',\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\',\'Arial\',\'Arial\'; font-size:14pt; font-weight:600; text-decoration: underline;\">How to use:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">1) Locate the manual for your temperature controller and make sure that it supports Modbus RTU serial communications</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">2) Use the same manual to determine the read/write register number and writing function code for the set point (SP) of your controller, then also determine the read register and reading function code for the process variable (PV)</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">3) Select the &quot;Configure&quot; tab and enter the register numbers and function codes from steps (2) and (3), you can also set a desired minimum and maximum allowable SP temperature on this tab (optional)</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">4) Select the &quot;Main Window&quot; tab and use the drop down menu under &quot;COM port&quot; to select your controller\'s communication port (check device manager if you are unsure)</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">5) Click the &quot;START&quot; button to trigger the read displays to update every 1 second, the button will grey out to visually confirm the GUI is continuously running</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">6) Use the &quot;SP (degr C)&quot; column to write new set points to your controller by entering a value or using the up.down arrows of the spin box and pressing the &quot;Engage&quot; button (only temeratures within the range set on the &quot;Configure&quot; tab are valid)</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">7) Once you are finished with an experiment, use the &quot;STOP&quot; button to stop the continuous readings and to reset the set point to the minimum temperature</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial,Arial\';\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Additional notes:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">* This application is set up to save the settings from the &quot;Configure&quot; tab, so it will automatically load the values that were used the last time the app was used. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">* The COM port will automatically switch to the &quot;DUMMY&quot; port if a connection cannot be established with the selected port. Make sure you are selecting the correct port for your device to resolve this.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">* Hitting the start button when the &quot;DUMMY&quot; COM port is selected will begin a testing protocol. In this protocol, the PV will increase or decrease by 1 every second until it matches whatever the current SP is. This test protocol can be used to help you understand how to use the app.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_DIR), _translate("MainWindow", "Directions"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\',\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">This GUI was made to control a Watlow EHG-SL10 heat controller. The tool was developed by Corey R. Randall at Colorado School of Mines in 2022. </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial,Arial\';\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">Although the program is available as a single executable file, the original files (gui.ui and main.py) are included on </span><a href=\"https://github.com/c-randall\"><span style=\" font-family:\'Arial,Arial\'; text-decoration: underline; color:#0068da;\">Github</span></a><span style=\" font-family:\'Arial,Arial\';\">. These files can be edited to control other Modbus RTU heat controllers by adjusting the appropriate read/write registers inside the main.py file. </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial,Arial\';\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Arial\';\">Moderate knowledge of the Python coding language is necessary to understand and modify the original files. An environment with dependencies for pyqt5-tools (used to build the GUI) and minimalmodbus (used for the serial communication) is required. </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ABT), _translate("MainWindow", "About"))
        self.actionInformation.setText(_translate("MainWindow", "Information"))

        self.settings = QSettings("Heat_Controller", "Configuration")

        try:
            # load saved SP Options
            self.SPRegister.setValue(self.settings.value("SPRegister"))
            self.SPFuncCode.setValue(self.settings.value("SPFuncCode"))

            # load saved PV Options
            self.PVRegister.setValue(self.settings.value("PVRegister"))
            self.PVFuncCode.setValue(self.settings.value("PVFuncCode"))

            # load saved Temp Options
            self.MinTemp.setValue(self.settings.value("MinTemp"))
            self.MaxTemp.setValue(self.settings.value("MaxTemp"))
        except:
            # default SP Options
            self.SPRegister.setValue(34)
            self.SPFuncCode.setValue(6)

            # default PV Options
            self.PVRegister.setValue(20)
            self.PVFuncCode.setValue(3)

            # default Temp Options
            self.MinTemp.setValue(20)
            self.MaxTemp.setValue(99)

        # status time (ms)
        self.statusTime = 3000

        # COMPortsList
        self.ports = ["DUMMY"]
        self.ports.extend([p.device for p in serial.tools.list_ports.comports()])

        for i,p in enumerate(self.ports):
            self.COMPortWatlow.addItem(p)

        # StartButton modifiers
        self.StartButton.clicked.connect(self.start_loop)
        self.StartButton.setStyleSheet("QPushButton:enabled {background-color: #6baa41;}\n"
                                       "QPushButton {background-color: grey;}\n")

        #EngageButton modifiers
        self.EngageButton.clicked.connect(self.write_SP)
        self.EngageButton.setStyleSheet("QPushButton:enabled {background-color: #5E8CAD;}\n"
                                        "QPushButton:pressed {background-color: grey;}\n")

        # StopButton modifiers
        self.StopButton.clicked.connect(self.stop_loop)
        self.StopButton.setStyleSheet("QPushButton:enabled {background-color: #d94e47;}\n"
                                      "QPushButton:pressed {background-color: grey;}\n")

        # Fix ColumnStretch on MainWindow
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        # create first instance of reader
        self.storeSerial = mb.serial.Serial
        dictConnection = self.connection()
        self.reader = Reader(dictConnection,self.PVDisplay,self.SPDisplay)

        for k in dictConnection.keys():
            setattr(self,k,dictConnection[k])

        # Show the GUI
        self.show()

    def connection(self):
        flag = 0
        COM = self.COMPortWatlow.currentText()

        self.minT = self.MinTemp.value()
        self.maxT = self.MaxTemp.value()
        minT = self.minT
        maxT = self.maxT

        self.SP_reg = self.SPRegister.value()
        self.PV_reg = self.PVRegister.value()
        SP_reg = self.SP_reg
        PV_reg = self.PV_reg

        self.SP_FuncCode = self.SPFuncCode.value()
        self.PV_FuncCode = self.PVFuncCode.value()
        SP_FuncCode = self.SP_FuncCode
        PV_FuncCode = self.PV_FuncCode

        self.SPInput.setMinimum(self.minT)
        self.SPInput.setMaximum(self.maxT)
        self.SPInput.setSpecialValueText("min "+str(self.minT))

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
            watlow.read_register(self.SP_reg,0)
            watlow.read_register(self.PV_reg,0)

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

        return {"watlow":watlow, "COM":COM, "flag":flag, "minT": minT, "maxT":maxT,
                "SP_reg":SP_reg, "PV_reg":PV_reg, "SP_FuncCode":SP_FuncCode, "PV_FuncCode":PV_FuncCode}

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

        if SP < self.minT:
            SP = self.minT
            self.SPInput.setValue(self.minT)
            self.statusBar.showMessage("Min allowed temp is "+str(self.minT)+" C",self.statusTime)
        if SP > self.maxT:
            SP = self.maxT
            self.SPInput.setValue(self.maxT)
            self.statusBar.showMessage("Max allowed temp is "+str(self.maxT)+" C",self.statusTime)

        if self.COM != "DUMMY":
            try: self.watlow.write_register(self.SP_reg,SP,0,functioncode=self.SP_FuncCode)
            except: self.statusBar.showMessage("Lost connection... check cable",self.statusTime)

        self.display_SP(SP)

        self.statusBar.showMessage("Set point updating...",self.statusTime)

    def stop_loop(self):
        self.reader.run = 0
        self.write_SP(SP=self.minT)
        self.display_SP(self.minT)

    def display_PV(self,PV):
        if self.COM != "DUMMY":
            try: PV = self.watlow.read_register(self.PV_reg,0)
            except: self.statusBar.showMessage("Lost connection... check cable",self.statusTime)
        self.PVDisplay.display(PV)

    def display_SP(self,SP):
        if self.COM != "DUMMY":
            try: SP = self.watlow.read_register(self.SP_reg,0)
            except: self.statusBar.showMessage("Lost connection... check cable",self.statusTime)
        self.SPDisplay.display(SP)

    def closeEvent(self,event):
        self.settings.setValue("SPRegister",self.SPRegister.value())
        self.settings.setValue("SPFuncCode",self.SPFuncCode.value())

        self.settings.setValue("PVRegister",self.PVRegister.value())
        self.settings.setValue("PVFuncCode",self.PVFuncCode.value())

        self.settings.setValue("MinTemp",self.MinTemp.value())
        self.settings.setValue("MaxTemp",self.MaxTemp.value())

class Reader(QThread):
    finished = pyqtSignal()
    PV_sig = pyqtSignal(int)
    SP_sig = pyqtSignal(int)

    def __init__(self,dictConnection,PVDisplay,SPDisplay):
        QThread.__init__(self)

        for k in dictConnection.keys():
            setattr(self,k,dictConnection[k])

        if self.COM == 'DUMMY': self.PV_reg, self.SP_reg = 4097, 4097

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

                self.PV_sig.emit(self.PV)
                self.SP_sig.emit(self.SP)
                time.sleep(1)

            self.finished.emit()

        else:
            while self.run:
                try:
                    self.PV = self.watlow.read_register(self.PV_reg,0)
                    self.SP = self.watlow.read_register(self.SP_reg,0)
                except:
                    None

                self.PV_sig.emit(self.PV)
                self.SP_sig.emit(self.SP)
                time.sleep(1)

            self.finished.emit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = Ui_MainWindow()
    sys.exit(app.exec_())
