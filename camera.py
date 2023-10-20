

from PyQt5 import QtCore, QtGui, QtWidgets
from myROI_Label import MyLabel

class camerawidget(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 428)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("QMenuBar {\n"
                                 "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                 "                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248));\n"
                                 "    spacing: 3px; /* spacing between menu bar items */\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item {\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "    padding: 1px 4px;\n"
                                 "      background-color:white;\n"
                                 "    border-style:outset;\n"
                                 "    border-width:1px;\n"
                                 "    border-radius:3px;\n"
                                 "    border-color:rgb(0, 155, 232);\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
                                 "    background: #a8a8a8;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:pressed {\n"
                                 "    background: #888888;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu {\n"
                                 "    background-color:rgb(255, 255, 255);\n"
                                 "    margin: 2px; /* some spacing around the menu */\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item {\n"
                                 "    padding: 2px 25px 2px 20px;\n"
                                 "    border: 1px solid transparent; /* reserve space for selection border */\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item:selected {\n"
                                 "    border-color: darkblue;\n"
                                 "    background: rgba(100, 100, 100, 150);\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::icon:checked { /* appearance of a \'checked\' icon */\n"
                                 "    background: gray;\n"
                                 "    border: 1px inset gray;\n"
                                 "    position: absolute;\n"
                                 "    top: 1px;\n"
                                 "    right: 1px;\n"
                                 "    bottom: 1px;\n"
                                 "    left: 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::separator {\n"
                                 "    height: 2px;\n"
                                 "    background: lightblue;\n"
                                 "    margin-left: 10px;\n"
                                 "    margin-right: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::indicator {\n"
                                 "    width: 13px;\n"
                                 "    height: 13px;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QStatusBar QLabel {\n"
                                 "    border: 3px solid white;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel {\n"
                                 "\n"
                                 "    font: 10pt \"Palatino Linotype\";\n"
                                 "    text-decoration: underline;\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                         "")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                     "border-style:outset;\n"
                                     "    border-width:1px;\n"
                                     "    border-radius:3px;\n"
                                     "    border-color:rgb(0, 155, 232)")
        self.Capture = QtWidgets.QWidget()
        self.Capture.setObjectName("Capture")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Capture)
        self.gridLayout_2.setObjectName("gridLayout_2")
        #self.gridLayout_2.addWidget(self.saveLocationEntry, 3, 0, 1, 1)
        self.captureBTN = QtWidgets.QPushButton(self.Capture)
        self.captureBTN.setObjectName("captureBTN")
        self.captureBTN.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);")
        self.gridLayout_2.addWidget(self.captureBTN, 0, 2, 1, 1)
        #self.gridLayout_2.addWidget(self.browseButton, 3, 1, 1, 1)
        self.closebutton = QtWidgets.QPushButton(self.Capture)
        self.closebutton.setObjectName("CloseBTN")
        self.closebutton.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);")
        self.gridLayout_2.addWidget(self.closebutton, 4, 2, 1, 1)
        self.cameraLabel = QtWidgets.QLabel(self.Capture)
        self.cameraLabel.setText("")
        self.cameraLabel.setObjectName("cameraLabel")
        self.gridLayout_2.addWidget(self.cameraLabel, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Capture, "")
        self.Result = QtWidgets.QWidget()
        self.Result.setObjectName("Result")
        self.browseButton = QtWidgets.QPushButton(self.Result)
        self.browseButton.setObjectName("browseButton")
        self.browseButton.setStyleSheet("background-color:white;\n"
                                        "border-style:outset;\n"
                                        "border-width:1px;\n"
                                        "border-radius:3px;\n"
                                        "border-color:rgb(0, 155, 232);")
        self.saveLocationEntry = QtWidgets.QLineEdit(self.Result)
        self.saveLocationEntry.setObjectName("saveLocationEntry")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Result)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.imageLabel = MyLabel(self.Result)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.gridLayout_3.addWidget(self.imageLabel, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.browseButton, 3, 2, 1, 1)
        self.gridLayout_3.addWidget(self.saveLocationEntry, 3, 1, 1, 1)
        self.pushButton_Import = QtWidgets.QPushButton(self.Result)
        self.pushButton_Import.setObjectName("pushButton_Import")
        self.pushButton_Import.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);")
        self.pushButton_Close = QtWidgets.QPushButton(self.Result)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.pushButton_Close.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);")
        self.gridLayout_3.addWidget(self.pushButton_Import, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.pushButton_Close, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Result, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 22))
        self.menubar.setObjectName("menubar")
        self.actionChoix = QtWidgets.QAction(MainWindow)
        self.actionChoix.setObjectName("actionChoix")
        self.menubar.addAction(self.actionChoix)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tabWidget.setTabVisible(1, False)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.imageLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        #MainWindow.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        # enable custom window hint
        MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # disable (but not hide) close button
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.actionChoix.setText(_translate("MainWindow", "Changer"))
        self.captureBTN.setText(_translate("MainWindow", "Capturer"))
        self.browseButton.setText(_translate("MainWindow", "Enrigistrer"))
        self.closebutton.setText(_translate("MainWindow", "Quitter"))
        self.pushButton_Close.setText(_translate("MainWindow", "Quitter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Capture), _translate("MainWindow", "Capturer"))
        self.pushButton_Import.setText(_translate("MainWindow", "Importer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Result), _translate("MainWindow", "Résultats"))

