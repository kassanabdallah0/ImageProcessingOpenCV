
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from myROI_Label import MyLabel
from PyQt5.QtGui import QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
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
"    color: rgb(0, 0, 0);\n"
"}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Importer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Importer.setObjectName("PushButton_Importer")
        self.gridLayout.addWidget(self.pushButton_Importer, 0, 0, 1, 1)
        self.pusButton_Sauvegarder = QtWidgets.QPushButton(self.centralwidget)
        self.pusButton_Sauvegarder.setObjectName("pushButton_Sauvegarder")
        self.gridLayout.addWidget(self.pusButton_Sauvegarder, 0, 2, 1, 1)
        self.pushButton_Gravillonage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Gravillonage.setObjectName("PushButton_Gravillonage")
        self.gridLayout.addWidget(self.pushButton_Gravillonage, 0, 5, 1, 1)
        self.pushButton_Quadrillage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Quadrillage.setObjectName("pushButton_Quadrillage")
        self.gridLayout.addWidget(self.pushButton_Quadrillage, 0, 6, 1, 1)
        self.pushButton_Analyse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Analyse.setObjectName("pushButton_Analyse")
        self.gridLayout.addWidget(self.pushButton_Analyse, 0, 8, 1, 1)
        self.pushButton_Aide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Aide.setObjectName("Aide")
        self.gridLayout.addWidget(self.pushButton_Aide, 0, 3, 1, 1)
        self.pushButton_Camera = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Camera.setObjectName("pushButton_Camera")
        self.gridLayout.addWidget(self.pushButton_Camera, 0, 1, 1, 1)
        self.pushButton_tree = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tree.setObjectName("pushButton_tree")
        self.gridLayout.addWidget(self.pushButton_tree, 0, 9, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(0, 155, 232)")
        self.tabWidget.setObjectName("tabWidget")
        self.Principale = QtWidgets.QWidget()
        self.Principale.setStyleSheet("")
        self.Principale.setObjectName("Principale")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.Principale)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.scrollArea_Principael = QtWidgets.QScrollArea(self.Principale)
        self.scrollArea_Principael.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(61, 123, 184);\n"
"border-color: transparent;")
        self.scrollArea_Principael.setWidgetResizable(True)
        self.scrollArea_Principael.setObjectName("scrollArea_Principael")
        self.scrollAreaWidgetContents_Principal = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_Principal.setGeometry(QtCore.QRect(0, 0, 772, 503))
        self.scrollAreaWidgetContents_Principal.setStyleSheet("background-color:rgb(193, 193, 193);")
        self.scrollAreaWidgetContents_Principal.setObjectName("scrollAreaWidgetContents_Principal")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_Principal)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.Image_principale = MyLabel(self.scrollAreaWidgetContents_Principal)
        self.Image_principale.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:transparent;\n"
"border-color: transparent;")
        self.Image_principale.setObjectName("Image_principale")
        self.Image_principale.setPixmap(QPixmap("Photos/icon.png"))
        self.Image_principale.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.gridLayout_14.addWidget(self.Image_principale, 0, 0, 1, 1)
        self.scrollArea_Principael.setWidget(self.scrollAreaWidgetContents_Principal)
        self.gridLayout_15.addWidget(self.scrollArea_Principael, 0, 0, 5, 4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem, 5, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem1, 5, 1, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.Principale)
        self.groupBox_9.setObjectName("groupBox_9")
        self.groupBox_9.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                              "                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248));")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_3 = QtWidgets.QLabel(self.groupBox_9)
        self.label_3.setStyleSheet("border-color:transparent; \n"
                                   "color: rgb(0,0,0);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_24.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_9)
        self.label_2.setStyleSheet("border-color:transparent; \n"
                                   "color: rgb(0,0,0);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_24.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_9, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem3, 2, 3, 1, 1)
        self.tabWidget.addTab(self.Principale, "")
        self.Gravillonage = QtWidgets.QWidget()
        self.Gravillonage.setObjectName("Gravillonage")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.Gravillonage)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.scrollArea_Gravillonage = QtWidgets.QScrollArea(self.Gravillonage)
        self.scrollArea_Gravillonage.setStyleSheet("background-color: transparent;\n"
"border-color: transparent;")
        self.scrollArea_Gravillonage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_Gravillonage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_Gravillonage.setWidgetResizable(True)
        self.scrollArea_Gravillonage.setObjectName("scrollArea_Gravillonage")
        self.scrollAreaWidgetContents_Gravillonage = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_Gravillonage.setGeometry(QtCore.QRect(0, 0, 873, 529))
        self.scrollAreaWidgetContents_Gravillonage.setStyleSheet("QMenu {\n"
"    background-color: white;\n"
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
"}")
        self.scrollAreaWidgetContents_Gravillonage.setObjectName("scrollAreaWidgetContents_Gravillonage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_Gravillonage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_Gravillonage)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        '''
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 4, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem6, 2, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem7, 3, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem8, 1, 3, 1, 1)
        '''
        self.gridLayout_radioButton = QtWidgets.QGridLayout()
        self.gridLayout_radioButton.setObjectName("gridLayout_radioButton")
        '''
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_radioButton.addItem(spacerItem9, 3, 3, 1, 1)
        '''
        self.nbr = QtWidgets.QLabel(self.scrollAreaWidgetContents_Gravillonage)
        self.nbr.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: transparent;\n"
"border-color: transparent;")
        self.nbr.setObjectName("nbr")
        self.Resultats_Grav_GroupBox = QtWidgets.QGroupBox(self.Gravillonage)
        self.Resultats_Grav_GroupBox.setObjectName("Resultats_Grav_GroupeBox")
        self.Resultats_Grav_GroupBox.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                              "                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248));"
                                                   "border-style:outset; "
                                                   "border-width:1px; "
                                                   "border-width:1px; "
                                                   "border-radius:3px; 	"
                                                   "border-color:rgb(0, 155, 232)")
        self.gridLayout_01 = QtWidgets.QGridLayout(self.Resultats_Grav_GroupBox)
        self.gridLayout_01.setObjectName("GridLayout_01")
        self.gridLayout_01.addWidget(self.nbr, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.Resultats_Grav_GroupBox, 2, 0, 1, 1)
        '''
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_radioButton.addItem(spacerItem10, 2, 3, 1, 1)
        '''
        self.surface = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_Gravillonage)
        self.surface.setStyleSheet("QCheckBox {\n"
"    background-color:       white;\n"
"    color:                  black;\n"
"    border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(0, 155, 232);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:3px;\n"
"    border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:          15px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"    border-radius: 3px;\n"
"     border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"    border-radius: 3px;\n"
"     border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"")
        self.surface.setObjectName("surface")
        self.gridLayout_radioButton.addWidget(self.surface, 0, 0, 1, 1)
        self.perimetre = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_Gravillonage)
        self.perimetre.setStyleSheet("QCheckBox {\n"
"    background-color:       white;\n"
"    color:                  black;\n"
"    border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(0, 155, 232);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:3px;\n"
"    border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:          15px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"    border-radius: 3px;\n"
"     border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"    border-radius: 3px;\n"
"     border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"")
        self.perimetre.setObjectName("perimetre")
        self.gridLayout_radioButton.addWidget(self.perimetre, 1, 0, 1, 1)
        self.indice = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_Gravillonage)
        self.indice.setStyleSheet("QCheckBox {\n"
"    background-color:       white;\n"
"    color:                  black;\n"
"    border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(0, 155, 232);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:3px;\n"
"    border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:          15px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"    border-radius: 3px;\n"
"     border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"    border-radius: 3px;\n"
"     border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"")
        self.indice.setObjectName("indice")
        self.gridLayout_radioButton.addWidget(self.indice, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_Gravillonage)
        self.checkBox.setStyleSheet("QCheckBox {\n"
"    background-color:       white;\n"
"    color:                  black;\n"
"    border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(0, 155, 232);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:3px;\n"
"    border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:          15px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"    border-radius: 3px;\n"
"     border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"    border-radius: 3px;\n"
"     border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_radioButton.addWidget(self.checkBox, 1, 1, 1, 1)
        '''
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_radioButton.addItem(spacerItem11, 0, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_radioButton.addItem(spacerItem12, 1, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_radioButton.addItem(spacerItem13, 1, 1, 1, 1)
        '''
        self.Parametre_groupBox_Grav = QtWidgets.QGroupBox(self.Gravillonage)
        self.Parametre_groupBox_Grav.setObjectName("Parametre_Grav_GroupBox")
        self.Parametre_groupBox_Grav.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                              "                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248));"
                                                   "border-style:outset; border-width:1px; border-width:1px; border-radius:3px; 	border-color:rgb(0, 155, 232)"
	)


        self.gridLayout_4 = QtWidgets.QGridLayout(self.Parametre_groupBox_Grav)
        self.gridLayout_4.setObjectName("GridLayout_4")
        self.gridLayout_4.addLayout(self.gridLayout_radioButton, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.Parametre_groupBox_Grav, 1, 0, 1, 1)
        '''
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_Gravillonage)
        self.line.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 12, 5, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem15, 12, 4, 1, 1)
        '''
        self.gridLayout_thresh = QtWidgets.QGridLayout()
        self.gridLayout_thresh.setObjectName("gridLayout_thresh")
        '''
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_thresh.addItem(spacerItem16, 0, 2, 1, 1)
        '''
        self.threshlabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Gravillonage)
        self.threshlabel.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: transparent;\n"
"border-color: transparent;")
        self.threshlabel.setObjectName("threshlabel")
        self.gridLayout_thresh.addWidget(self.threshlabel, 0, 0, 1, 1)
        '''
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_thresh.addItem(spacerItem17, 0, 0, 1, 1)
        '''
        self.tresh = QtWidgets.QSlider(self.scrollAreaWidgetContents_Gravillonage)
        self.tresh.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"   background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"   background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.tresh.setMinimum(0)
        self.tresh.setMaximum(235)
        self.tresh.setSingleStep(1)
        self.tresh.setPageStep(10)
        self.tresh.setOrientation(QtCore.Qt.Horizontal)
        self.tresh.setObjectName("tresh")
        self.gridLayout_thresh.addWidget(self.tresh, 0, 1, 1, 3)
        '''
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem18, 9, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem19, 4, 0, 1, 1)
        '''
        self.scrollArea_Image = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_Gravillonage)
        self.scrollArea_Image.setStyleSheet("background-color: rgb(61, 123, 184);")
        self.scrollArea_Image.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea_Image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea_Image.setLineWidth(3)
        self.scrollArea_Image.setMidLineWidth(3)
        self.scrollArea_Image.setWidgetResizable(True)
        self.scrollArea_Image.setObjectName("scrollArea_Image")
        self.scrollAreaWidgetContents_Image = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_Image.setGeometry(QtCore.QRect(0, 0, 612, 474))
        self.scrollAreaWidgetContents_Image.setStyleSheet("background-color:rgb(193, 193, 193);")
        self.scrollAreaWidgetContents_Image.setObjectName("scrollAreaWidgetContents_Image")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_Image)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.scrollArea_Image.setWidget(self.scrollAreaWidgetContents_Image)
        self.gridLayout_2.addWidget(self.scrollArea_Image, 0, 3, 11, 9)
        self.gridLayout_filtre = QtWidgets.QGridLayout()
        self.gridLayout_filtre.setObjectName("gridLayout_filtre")
        '''
        spacerItem20 = QtWidgets.QSpacerItem(35, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_filtre.addItem(spacerItem20, 2, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(35, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_filtre.addItem(spacerItem21, 0, 4, 1, 1)
        '''
        self.filtre = QtWidgets.QLabel(self.scrollAreaWidgetContents_Gravillonage)
        self.filtre.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: transparent;\n"
"border-color: transparent;")
        self.filtre.setObjectName("filtre")
        self.gridLayout_filtre.addWidget(self.filtre, 2, 2, 1, 1)
        self.filtremoins = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Gravillonage)
        self.filtremoins.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"width: 5px;")
        self.filtremoins.setObjectName("filtremoins")
        self.gridLayout_filtre.addWidget(self.filtremoins, 2, 0, 1, 1)
        '''
        spacerItem22 = QtWidgets.QSpacerItem(34, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_filtre.addItem(spacerItem22, 2, 3, 1, 1)
        '''
        self.filtreplus = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Gravillonage)
        self.filtreplus.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);")
        self.filtreplus.setObjectName("filtreplus")
        self.gridLayout_filtre.addWidget(self.filtreplus, 2, 4, 1, 1)
        '''
        spacerItem23 = QtWidgets.QSpacerItem(35, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_filtre.addItem(spacerItem23, 0, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem24, 8, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem25, 12, 3, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem26, 5, 0, 2, 1)
        '''
        self.gridLayout_contours = QtWidgets.QGridLayout()
        self.gridLayout_contours.setObjectName("gridLayout_contours")
        '''
        spacerItem27 = QtWidgets.QSpacerItem(29, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_contours.addItem(spacerItem27, 0, 4, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(29, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_contours.addItem(spacerItem28, 0, 3, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(29, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_contours.addItem(spacerItem29, 0, 1, 1, 1)
        '''
        self.contoursmoins = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Gravillonage)
        self.contoursmoins.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);")
        self.contoursmoins.setObjectName("contoursmoins")
        self.gridLayout_contours.addWidget(self.contoursmoins, 0, 0, 1, 1)
        self.contours = QtWidgets.QLabel(self.scrollAreaWidgetContents_Gravillonage)
        self.contours.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: transparent;\n"
"border-color: transparent;")
        self.contours.setObjectName("contours")
        self.gridLayout_contours.addWidget(self.contours, 0, 2, 1, 1)
        '''
        spacerItem30 = QtWidgets.QSpacerItem(29, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_contours.addItem(spacerItem30, 1, 0, 1, 1)
        '''
        self.contoursplus = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Gravillonage)
        self.contoursplus.setStyleSheet("\n"
"    \n"
"background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"\n"
"")
        self.contoursplus.setObjectName("contoursplus")
        self.gridLayout_contours.addWidget(self.contoursplus, 0, 4, 1, 1)
        self.Filtre_grav_groupeBox = QtWidgets.QGroupBox(self.Gravillonage)
        self.Filtre_grav_groupeBox.setObjectName("Filtre_GroupeBox_Grav")
        self.Filtre_grav_groupeBox.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                              "                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248));"
                                                   "border-style:outset; border-width:1px; border-width:1px; border-radius:3px; 	border-color:rgb(0, 155, 232)")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Filtre_grav_groupeBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.addLayout(self.gridLayout_filtre, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_contours, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_thresh, 2, 0, 1, 1)
        self.Commentaire_groupBox_grav = QtWidgets.QGroupBox(self.Gravillonage)
        self.Commentaire_groupBox_grav.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
                                                "                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248));")
        self.Commentaire_groupBox_grav.setObjectName("Commentaire_groupBox_grav")
        self.gridLayout_23_grav = QtWidgets.QGridLayout(self.Commentaire_groupBox_grav)
        self.gridLayout_23_grav.setObjectName("gridLayout_23_grav")
        spacerItem41_grav = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23_grav.addItem(spacerItem41_grav, 0, 1, 1, 1)
        self.textEdit_commentaire_grav = QtWidgets.QTextEdit(self.Commentaire_groupBox_grav)
        self.textEdit_commentaire_grav.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_commentaire_grav.setObjectName("textEdit_commentaire")
        self.gridLayout_23_grav.addWidget(self.textEdit_commentaire_grav, 1, 0, 1, 3)
        spacerItem42_grav = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23_grav.addItem(spacerItem42_grav, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.Filtre_grav_groupeBox, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.Commentaire_groupBox_grav, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setStyleSheet("background-color: white;"
                                        "color: black;")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 4, 0, 1, 1)
        '''
        self.line_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents_Gravillonage)
        self.line_7.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"border: transparent;")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 11, 3, 1, 3)
        
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_Gravillonage)
        self.line_3.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"border: transparent;")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 0, 2, 4, 1)
        self.line_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents_Gravillonage)
        self.line_6.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"border: transparent;")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 7, 2, 4, 1)
        '''
        self.scrollArea_Gravillonage.setWidget(self.scrollAreaWidgetContents_Gravillonage)
        self.gridLayout_13.addWidget(self.scrollArea_Gravillonage, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Gravillonage, "")
        self.Quadrillage = QtWidgets.QWidget()
        self.Quadrillage.setObjectName("Quadrillage")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.Quadrillage)
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem31, 0, 7, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem32, 0, 4, 1, 1)
        self.parametre_groupBox = QtWidgets.QGroupBox(self.Quadrillage)
        self.parametre_groupBox.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248));")
        self.parametre_groupBox.setObjectName("parametre_groupBox")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.parametre_groupBox)
        self.gridLayout_25.setObjectName("gridLayout_25")
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem33, 0, 0, 1, 4)
        self.v_spinBox = QtWidgets.QSpinBox(self.parametre_groupBox)
        self.v_spinBox.setStyleSheet("background-color:rgb(245, 245, 245);\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.v_spinBox.setObjectName("v_spinBox")
        self.gridLayout_25.addWidget(self.v_spinBox, 2, 1, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.t_horizontalSlider = QtWidgets.QSlider(self.parametre_groupBox)
        self.t_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"   background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"   background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 12px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.t_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.t_horizontalSlider.setObjectName("t_horizontalSlider")
        self.horizontalLayout_16.addWidget(self.t_horizontalSlider)
        self.gridLayout_25.addLayout(self.horizontalLayout_16, 1, 2, 1, 2)
        self.thresh_label = QtWidgets.QLabel(self.parametre_groupBox)
        self.thresh_label.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 5px;\n"
"color: rgb(0, 0, 0);")
        self.thresh_label.setObjectName("thresh_label")
        self.gridLayout_25.addWidget(self.thresh_label, 1, 0, 1, 1)
        self.Vertical_label = QtWidgets.QLabel(self.parametre_groupBox)
        self.Vertical_label.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 5px;\n"
"color: rgb(0, 0, 0);")
        self.Vertical_label.setObjectName("Vertical_label")
        self.gridLayout_25.addWidget(self.Vertical_label, 2, 0, 1, 1)
        self.h_spinBox = QtWidgets.QSpinBox(self.parametre_groupBox)
        self.h_spinBox.setStyleSheet("background-color:rgb(245, 245, 245);\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"\n"
"color: rgb(0, 0, 0);")
        self.h_spinBox.setObjectName("h_spinBox")
        self.gridLayout_25.addWidget(self.h_spinBox, 3, 1, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem34, 4, 3, 1, 1)
        self.Horizontale_label = QtWidgets.QLabel(self.parametre_groupBox)
        self.Horizontale_label.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 5px;\n"
"color: rgb(0, 0, 0);")
        self.Horizontale_label.setObjectName("Horizontale_label")
        self.gridLayout_25.addWidget(self.Horizontale_label, 3, 0, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem35, 4, 2, 1, 1)
        self.t_spinBox = QtWidgets.QSpinBox(self.parametre_groupBox)
        self.t_spinBox.setStyleSheet("background-color:rgb(245, 245, 245);\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.t_spinBox.setObjectName("t_spinBox")
        self.gridLayout_25.addWidget(self.t_spinBox, 1, 1, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem36, 4, 0, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem37, 4, 1, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.v_horizontalSlider = QtWidgets.QSlider(self.parametre_groupBox)
        self.v_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"   background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"   background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 12px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.v_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.v_horizontalSlider.setObjectName("v_horizontalSlider")
        self.horizontalLayout_15.addWidget(self.v_horizontalSlider)
        self.gridLayout_25.addLayout(self.horizontalLayout_15, 2, 2, 1, 2)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.h_horizontalSlider = QtWidgets.QSlider(self.parametre_groupBox)
        self.h_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"   background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"   background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 12px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.h_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.h_horizontalSlider.setObjectName("h_horizontalSlider")
        self.horizontalLayout_14.addWidget(self.h_horizontalSlider)
        self.gridLayout_25.addLayout(self.horizontalLayout_14, 3, 2, 1, 2)
        self.gridLayout_16.addWidget(self.parametre_groupBox, 5, 7, 1, 1)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem38, 0, 3, 1, 1)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem39, 0, 0, 1, 2)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem40, 0, 5, 1, 1)
        self.Commentaire_groupBox = QtWidgets.QGroupBox(self.Quadrillage)
        self.Commentaire_groupBox.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248));")
        self.Commentaire_groupBox.setObjectName("Commentaire_groupBox")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.Commentaire_groupBox)
        self.gridLayout_23.setObjectName("gridLayout_23")
        spacerItem41 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem41, 0, 1, 1, 1)
        self.textEdit_commentaire = QtWidgets.QTextEdit(self.Commentaire_groupBox)
        self.textEdit_commentaire.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_commentaire.setObjectName("textEdit_commentaire")
        self.gridLayout_23.addWidget(self.textEdit_commentaire, 1, 0, 1, 3)
        spacerItem42 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem42, 2, 1, 1, 1)
        self.gridLayout_16.addWidget(self.Commentaire_groupBox, 7, 7, 1, 1)
        self.comBox_quad = QtWidgets.QComboBox(self.centralwidget)
        self.comBox_quad.setStyleSheet("background-color: white;"
                                    "color: black;")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.addItem("")
        self.comBox_quad.setObjectName(u"comBox_quad")
        self.gridLayout_16.addWidget(self.comBox_quad, 8, 7, 1, 1)
        self.autres_groupBox = QtWidgets.QGroupBox(self.Quadrillage)
        self.autres_groupBox.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248));")
        self.autres_groupBox.setObjectName("autres_groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.autres_groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.dark_radio_button = QtWidgets.QRadioButton(self.autres_groupBox)
        self.dark_radio_button.setStyleSheet("QRadioButton {\n"
"    background-color:       white;\n"
"    color:                  black;\n"
"    border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(0, 155, 232);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:3px;\n"
"    border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:          15px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"    border-radius: 3px;\n"
"     border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid black;\n"
"    border-radius: 3px;\n"
"     border-style:outset;\n"
"    border-width:1px;\n"
"    border-radius:3px;\n"
"    border-color:rgb(208, 0, 0);\n"
"}\n"
"")
        self.dark_radio_button.setObjectName("dark_radio_button")
        self.verticalLayout_9.addWidget(self.dark_radio_button)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.Expension_label = QtWidgets.QLabel(self.autres_groupBox)
        self.Expension_label.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 5px;\n"
"color: rgb(0, 0, 0);")
        self.Expension_label.setObjectName("Expension_label")
        self.horizontalLayout_18.addWidget(self.Expension_label)
        self.e_spinBox = QtWidgets.QSpinBox(self.autres_groupBox)
        self.e_spinBox.setStyleSheet("background-color:rgb(245, 245, 245);\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.e_spinBox.setObjectName("e_spinBox")
        self.horizontalLayout_18.addWidget(self.e_spinBox)
        self.e_horizontalSlider = QtWidgets.QSlider(self.autres_groupBox)
        self.e_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"   background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"   background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(0, 155, 232);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 12px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.e_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.e_horizontalSlider.setObjectName("e_horizontalSlider")
        self.e_horizontalSlider.setSliderPosition(0)
        self.e_horizontalSlider.setSingleStep(1)
        self.e_horizontalSlider.setPageStep(2)
        self.horizontalLayout_18.addWidget(self.e_horizontalSlider)
        self.verticalLayout_9.addLayout(self.horizontalLayout_18)
        self.verticalLayout_6.addLayout(self.verticalLayout_9)
        self.gridLayout_16.addWidget(self.autres_groupBox, 4, 7, 1, 1)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem43, 0, 6, 1, 1)
        self.Resultats_groupBox = QtWidgets.QGroupBox(self.Quadrillage)
        self.Resultats_groupBox.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248));")
        self.Resultats_groupBox.setObjectName("Resultats_groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Resultats_groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.surface_label = QtWidgets.QLabel(self.Resultats_groupBox)
        self.surface_label.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 5px;\n"
"color: rgb(0, 0, 0);")
        self.surface_label.setObjectName("surface_label")
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(72)
        self.classification_label = QtWidgets.QLabel(self.Resultats_groupBox)
        self.classification_label.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 5px;\n"
"color: rgb(255, 0, 0);\n"
"font-size: 25px;")
        self.classification_label.setObjectName("classification_label")
        self.classification_label.setFont(self.font)
        self.verticalLayout_7.addWidget(self.classification_label)
        self.verticalLayout_7.addWidget(self.surface_label)
        self.norme_label = QtWidgets.QLabel(self.Resultats_groupBox)
        self.norme_label.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 5px;\n"
"color: rgb(0, 0, 0);")
        self.norme_label.setObjectName("norme_label")
        self.verticalLayout_7.addWidget(self.norme_label)
        self.gridLayout_16.addWidget(self.Resultats_groupBox, 3, 7, 1, 1)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem44, 0, 2, 1, 1)
        spacerItem45 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem45, 6, 7, 1, 1)
        spacerItem46 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem46, 8, 7, 1, 1)
        self.tabWidget_Image = QtWidgets.QTabWidget(self.Quadrillage)
        self.tabWidget_Image.setStyleSheet("background-color:rgb(193, 193, 193);")
        self.tabWidget_Image.setObjectName("tabWidget_Image")
        self.Originale = QtWidgets.QWidget()
        self.Originale.setStyleSheet("background-color:rgb(193, 193, 193);")
        self.Originale.setObjectName("Originale")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.Originale)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.tabWidget_Image.addTab(self.Originale, "")
        self.Binaire = QtWidgets.QWidget()
        self.Binaire.setStyleSheet("background-color:rgb(193, 193, 193);")
        self.Binaire.setObjectName("Binaire")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.Binaire)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.tabWidget_Image.addTab(self.Binaire, "")
        self.Traite = QtWidgets.QWidget()
        self.Traite.setStyleSheet("background-color:rgb(193, 193, 193);")
        self.Traite.setObjectName("Traite")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.Traite)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.tabWidget_Image.addTab(self.Traite, "")
        self.Contours = QtWidgets.QWidget()
        self.Contours.setStyleSheet("background-color:rgb(193, 193, 193);")
        self.Contours.setObjectName("Contours")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.Contours)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.tabWidget_Image.addTab(self.Contours, "")
        self.gridLayout_16.addWidget(self.tabWidget_Image, 1, 0, 8, 7)
        self.tabWidget.addTab(self.Quadrillage, "")
        self.Analyse = QtWidgets.QWidget()
        self.Analyse.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248));\n"
"border-color:transparent;\n"
"")
        self.Analyse.setObjectName("Analyse")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.Analyse)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.scrollArea_Analyse = QtWidgets.QScrollArea(self.Analyse)
        self.scrollArea_Analyse.setEnabled(True)
        self.scrollArea_Analyse.setStyleSheet("")
        self.scrollArea_Analyse.setWidgetResizable(True)
        self.scrollArea_Analyse.setObjectName("scrollArea_Analyse")
        self.scrollAreaWidgetContents_Analyse = QtWidgets.QWidget(self.Analyse)
        self.scrollAreaWidgetContents_Analyse.setGeometry(QtCore.QRect(0, 0, 873, 529))
        self.scrollAreaWidgetContents_Analyse.setObjectName("scrollAreaWidgetContents_Analyse")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_Analyse)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem47 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem47, 1, 1, 1, 1)
        spacerItem48 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem48, 3, 1, 1, 1)
        spacerItem49 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem49, 4, 1, 1, 1)
        self.gridLayout_resultats = QtWidgets.QGridLayout()
        self.gridLayout_resultats.setObjectName("gridLayout_resultats")
        self.Resultats_groupeBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_Analyse)
        self.Resultats_groupeBox.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248))")
        self.Resultats_groupeBox.setObjectName("Resultats_groupeBox")
        self.Resultats_groupeBox.setStyleSheet("border-width:5px;")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.Resultats_groupeBox)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.maxa = QtWidgets.QLabel(self.Resultats_groupeBox)
        self.maxa.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 3px;\n"
"color: rgb(0, 0, 0);")
        self.maxa.setObjectName("maxa")
        self.gridLayout_22.addWidget(self.maxa, 1, 0, 1, 1)
        self.maxp = QtWidgets.QLabel(self.Resultats_groupeBox)
        self.maxp.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 3px;\n"
"color: rgb(0, 0, 0);")
        self.maxp.setObjectName("maxp")
        self.gridLayout_22.addWidget(self.maxp, 2, 0, 1, 1)
        self.itotal = QtWidgets.QLabel(self.Resultats_groupeBox)
        self.itotal.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 3px;\n"
"color: rgb(0, 0, 0);")
        self.itotal.setObjectName("itotal")
        self.gridLayout_22.addWidget(self.itotal, 4, 0, 1, 1)
        self.caut = QtWidgets.QLabel(self.Resultats_groupeBox)
        self.caut.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 3px;\n"
"color: rgb(255, 0, 0);"
                                "font-size: 25px;")
        self.caut.setFont(self.font)
        self.caut.setObjectName("caut")
        self.gridLayout_22.addWidget(self.caut, 0, 0, 1, 1)
        self.atotal = QtWidgets.QLabel(self.Resultats_groupeBox)
        self.atotal.setStyleSheet("background-color:white;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:3px;\n"
"border-color:rgb(170, 0, 0);\n"
"width: 3px;\n"
"color: rgb(0, 0, 0);"
                                  "")
        self.atotal.setObjectName("atotal")
        self.gridLayout_22.addWidget(self.atotal, 3, 0, 1, 1)
        self.gridLayout_resultats.addWidget(self.Resultats_groupeBox, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_resultats, 0, 0, 1, 1)
        spacerItem50 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem50, 6, 1, 1, 1)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem51, 1, 0, 1, 1)
        spacerItem52 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem52, 0, 1, 1, 1)
        spacerItem53 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem53, 5, 1, 1, 1)
        self.Graphe_groupeBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_Analyse)
        self.Graphe_groupeBox.setObjectName("Graphe_groupeBox")
        self.Graphe_groupeBox.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248); border-width:5px;")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.Graphe_groupeBox)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.verticalLayout_Graphe = QtWidgets.QVBoxLayout()
        self.verticalLayout_Graphe.setObjectName("verticalLayout_Graphe")
        self.gridLayout_21.addLayout(self.verticalLayout_Graphe, 0, 0, 1, 1)
        spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem54, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.Graphe_groupeBox, 3, 2, 4, 1)
        '''
        self.groupBox_cotation = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_Analyse)
        self.groupBox_cotation.setObjectName("groupBox_cotation")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_cotation)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_cotation = QtWidgets.QVBoxLayout()
        self.verticalLayout_cotation.setObjectName("verticalLayout_cotation")
        self.gridLayout_4.addLayout(self.verticalLayout_cotation, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_cotation, 1, 0, 1, 1)
        '''
        self.Courbe_groupeBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_Analyse)
        self.Courbe_groupeBox.setObjectName("Courbe_groupeBox")
        self.Courbe_groupeBox.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248); \n"
"        border-width:5px;")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.Courbe_groupeBox)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.verticalLayout_Courbe = QtWidgets.QVBoxLayout()
        self.verticalLayout_Courbe.setObjectName("verticalLayout_Courbe")
        self.gridLayout_20.addLayout(self.verticalLayout_Courbe, 0, 0, 1, 1)
        spacerItem56 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem56, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.Courbe_groupeBox, 0, 2, 3, 1)
        self.scrollArea_Analyse.setWidget(self.scrollAreaWidgetContents_Analyse)
        self.gridLayout_12.addWidget(self.scrollArea_Analyse, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Analyse, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 919, 21))
        self.menubar.setObjectName("menubar")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.menumenu.setObjectName("menumenu")
        self.menuCotation = QtWidgets.QMenu(self.menubar)
        self.menuCotation.setObjectName("menuCotation")
        self.menuEchelle = QtWidgets.QMenu(self.menubar)
        self.menuEchelle.setObjectName("menuEchelle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionDefault_Cotation = QtWidgets.QAction(MainWindow)
        self.actionDefault_Cotation.setObjectName("actionDefault_Cotation")
        self.actionNouveau_Cotation = QtWidgets.QAction(MainWindow)
        self.actionNouveau_Cotation.setObjectName("actionNouveau_Cotation")
        self.actionOuvrire_Cotation = QtWidgets.QAction(MainWindow)
        self.actionOuvrire_Cotation.setObjectName("actionOuvrire_Cotation")
        self.actionDefault_Echelle = QtWidgets.QAction(MainWindow)
        self.actionDefault_Echelle.setObjectName("actionDefault_Echelle")
        self.actionNouveau_Echelle = QtWidgets.QAction(MainWindow)
        self.actionNouveau_Echelle.setObjectName("actionNouveau_Echelle")
        self.actionOuvrire_Echelle = QtWidgets.QAction(MainWindow)
        self.actionOuvrire_Echelle.setObjectName("actionOuvrire_Echelle")
        self.actionAnalyse = QtWidgets.QAction(MainWindow)
        self.actionAnalyse.setObjectName("actionAnalyse")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menumenu.addAction(self.actionImport)
        self.menumenu.addAction(self.actionAnalyse)
        self.menumenu.addAction(self.actionSave)
        self.menumenu.addAction(self.actionExit)
        self.menuCotation.addAction(self.actionDefault_Cotation)
        self.menuCotation.addAction(self.actionNouveau_Cotation)
        self.menuCotation.addAction(self.actionOuvrire_Cotation)
        self.menuEchelle.addAction(self.actionDefault_Echelle)
        self.menuEchelle.addAction(self.actionNouveau_Echelle)
        self.menuEchelle.addAction(self.actionOuvrire_Echelle)
        self.menubar.addAction(self.menumenu.menuAction())
        self.menubar.addAction(self.menuCotation.menuAction())
        self.menubar.addAction(self.menuEchelle.menuAction())

        self.dockWidget_Plaque = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_Plaque.setObjectName("DockWidget_Plaque")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("DockWidgetContents_Plaque")
        self.gridLayout_DockWidget = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_DockWidget.setObjectName("GridLayout_DockWidget")

        self.treeWidget_Plaque = QtWidgets.QTreeWidget(self.dockWidgetContents)
        qtreewidgetitem = QtWidgets.QTreeWidgetItem()
        qtreewidgetitem.setText(0, "Plaque")
        self.treeWidget_Plaque.setHeaderItem(qtreewidgetitem)
        self.treeWidget_Plaque.setObjectName("treeWidget_Plaque")
        self.gridLayout_DockWidget.addWidget(self.treeWidget_Plaque, 0, 0, 1, 1)
        self.dockWidget_Plaque.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockWidget_Plaque)

        self.status_label_icon = QtWidgets.QLabel()
        self.status_label_icon.setPixmap(QPixmap("Photos/icon.png").scaled(30, 20))
        self.status_label_icon.setStyleSheet("border-color:transparent;")
        self.status_label_text = QtWidgets.QLabel()
        self.status_label_text.setStyleSheet("background-color: transparent; \n"
                                             "color:(0,0,0);")

        self.status_label_text.setText("HMRexpert-Logiciel")
        self.statusbar.addWidget(self.status_label_icon)
        self.statusbar.addWidget(self.status_label_text)
        self.statusbar.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 rgb(217, 217, 217), stop:1 rgb(248, 248, 248)); \n"
                                     "color:(0,0,0);")
        self.label_aide = QtWidgets.QLabel()
        self.label_aide.setText("aide-mode est active ")
        self.statusbar.addWidget(self.label_aide, 1)
        self.label_aide.setVisible(False)

        self.t_spinBox.setMinimum(0)
        self.h_spinBox.setMinimum(1)
        self.v_spinBox.setMinimum(1)
        self.e_spinBox.setMinimum(0)
        self.v_horizontalSlider.setMinimum(1)
        self.h_horizontalSlider.setMinimum(1)
        self.t_horizontalSlider.setMinimum(0)
        self.e_horizontalSlider.setMinimum(0)

        self.t_spinBox.setMaximum(255)
        self.h_spinBox.setMaximum(500)
        self.v_spinBox.setMaximum(500)
        self.e_spinBox.setMaximum(5)

        self.v_horizontalSlider.setMaximum(500)
        self.h_horizontalSlider.setMaximum(500)
        self.t_horizontalSlider.setMaximum(255)
        self.e_horizontalSlider.setMaximum(5)

        self.Gravillonage.setEnabled(False)
        self.tabWidget.setTabVisible(1, False)
        self.Quadrillage.setEnabled(False)
        self.tabWidget.setTabVisible(2, False)
        self.Analyse.setEnabled(False)
        self.tabWidget.setTabVisible(3, False)

        self.actionSave.setEnabled(False)
        self.actionAnalyse.setEnabled(False)

        self.pusButton_Sauvegarder.setEnabled(False)
        self.pushButton_Analyse.setEnabled(False)
        self.pushButton_Gravillonage.setEnabled(False)
        self.pushButton_Quadrillage.setEnabled(False)

        self.pushButton_Importer.setIcon(QtGui.QIcon("photos/import_icon.ico"))
        self.pushButton_Importer.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Analyse.setIcon(
            QtGui.QIcon("photos/sticker_png_circle_logo_analysis_business_data_analysis_symbol_Rbv_icon.ico"))
        self.pushButton_Analyse.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Gravillonage.setIcon(QtGui.QIcon("photos/download_tP1_icon.ico"))
        self.pushButton_Gravillonage.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Quadrillage.setIcon(QtGui.QIcon("photos/download_tP1_icon.ico"))
        self.pushButton_Quadrillage.setIconSize(QtCore.QSize(35, 35))
        self.pusButton_Sauvegarder.setIcon(QtGui.QIcon("photos/save_disk_png_clipart_DuY_icon.ico"))
        self.pusButton_Sauvegarder.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Camera.setIcon(QtGui.QIcon("photos/camera_qh3_icon.ico"))
        self.pushButton_Camera.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_Aide.setIcon(QtGui.QIcon("photos/interrogation_KGv_icon.ico"))
        self.pushButton_Aide.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_tree.setIcon(QtGui.QIcon("photos/arborescence_logo.ico"))
        self.pushButton_tree.setIconSize(QtCore.QSize(35, 35))
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_Image.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HMRexpert-logiciel"))
        self.pushButton_Quadrillage.setText(_translate("MainWindow", "Quadrillage"))
        self.pushButton_Gravillonage.setText(_translate("MainWindow", "Gravillonnage"))
        self.pushButton_Importer.setText(_translate("MainWindow", "Importer"))
        self.pushButton_Analyse.setText(_translate("MainWindow", "Analyse"))
        self.pusButton_Sauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.pushButton_Aide.setText(_translate("MainWindow", "Aide"))
        self.pushButton_Camera.setText(_translate("MainWindow", "Camera"))
        self.pushButton_tree.setText(_translate("MainWindow", "Arborescence"))
        #self.Image_principale.setText(_translate("MainWindow", "Importer une plaque pour commencer"))
        self.groupBox_9.setTitle(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Echelle:"))
        self.label_2.setText(_translate("MainWindow", "Resolution:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Principale), _translate("MainWindow", "Principale"))
        self.nbr.setText(_translate("MainWindow", "Nombre d impacts: "))
        self.surface.setText(_translate("MainWindow", "Surface"))
        self.perimetre.setText(_translate("MainWindow", "Perimetre"))
        self.indice.setText(_translate("MainWindow", "Indice"))
        self.checkBox.setText(_translate("MainWindow", "Image originale"))
        self.threshlabel.setText(_translate("MainWindow", 'seuil: 'f'{self.tresh.value()} '))
        self.filtre.setText(_translate("MainWindow", "filtre: 1"))
        self.filtremoins.setText(_translate("MainWindow", "-"))
        self.filtreplus.setText(_translate("MainWindow", "+"))
        self.contoursmoins.setText(_translate("MainWindow", "-"))
        self.contours.setText(_translate("MainWindow", "contours: 1"))
        self.contoursplus.setText(_translate("MainWindow", "+"))
        self.Parametre_groupBox_Grav.setTitle(_translate("MainWindow", "Paramètres"))
        self.Filtre_grav_groupeBox.setTitle(_translate("MainWindow", "Filtres"))
        self.Resultats_Grav_GroupBox.setTitle(_translate("MainWindow", "Résultats"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Gravillonage), _translate("MainWindow", "Gravillonnage"))
        self.parametre_groupBox.setTitle(_translate("MainWindow", "Paramètres"))
        self.thresh_label.setText(_translate("MainWindow", "Seuil:"))
        self.Vertical_label.setText(_translate("MainWindow", "Vertical:"))
        self.Horizontale_label.setText(_translate("MainWindow", "Horizontal:"))
        self.Commentaire_groupBox.setTitle(_translate("MainWindow", "Commentaire"))
        self.Commentaire_groupBox_grav.setTitle(_translate("MainWindow", "Commentaire"))
        self.autres_groupBox.setTitle(_translate("MainWindow", "Autres"))
        self.dark_radio_button.setText(_translate("MainWindow", "Fond blanc"))
        self.Expension_label.setText(_translate("MainWindow", "Expansion:"))
        self.Resultats_groupBox.setTitle(_translate("MainWindow", "Résultat"))
        self.surface_label.setText(_translate("MainWindow", "Surface: "))
        self.classification_label.setText(_translate("MainWindow", "Cotation:"))
        self.norme_label.setText(_translate("MainWindow", "Norme:"))
        self.tabWidget_Image.setTabText(self.tabWidget_Image.indexOf(self.Originale), _translate("MainWindow", "Originale"))
        self.tabWidget_Image.setTabText(self.tabWidget_Image.indexOf(self.Binaire), _translate("MainWindow", "Binaire"))
        self.tabWidget_Image.setTabText(self.tabWidget_Image.indexOf(self.Traite), _translate("MainWindow", "Traité"))
        self.tabWidget_Image.setTabText(self.tabWidget_Image.indexOf(self.Contours), _translate("MainWindow", "Contours"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Quadrillage), _translate("MainWindow", "Quadrillage"))
        self.Resultats_groupeBox.setTitle(_translate("MainWindow", "Resultats"))
        self.maxa.setText(_translate("MainWindow", "Max Surface Des Impacts: "))
        self.maxp.setText(_translate("MainWindow", "Max Perimètre Des Impacts: "))
        self.itotal.setText(_translate("MainWindow", "Somme Surface Des Impacts: "))
        self.caut.setText(_translate("MainWindow", "cotation: "))
        self.atotal.setText(_translate("MainWindow", "Surface total: "))
        self.Graphe_groupeBox.setTitle(_translate("MainWindow", "Graphique"))
        self.Courbe_groupeBox.setTitle(_translate("MainWindow", "Courbe"))
        #self.groupBox_cotation.setTitle(_translate("MainWindow", "Cotation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Analyse), _translate("MainWindow", "Résultats"))
        self.menumenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuCotation.setTitle(_translate("MainWindow", "Cotation"))
        self.menuEchelle.setTitle(_translate("MainWindow", "Echelle"))
        self.actionImport.setText(_translate("MainWindow", "Importer"))
        self.actionSave.setText(_translate("MainWindow", "Sauvegarder"))
        self.actionDefault_Cotation.setText(_translate("MainWindow", "Default(Stellantis)"))
        self.actionNouveau_Cotation.setText(_translate("MainWindow", "Nouveau"))
        self.actionOuvrire_Cotation.setText(_translate("MainWindow", "Ouvrir"))
        self.actionDefault_Echelle.setText(_translate("MainWindow", "Default"))
        self.actionNouveau_Echelle.setText(_translate("MainWindow", "Nouveau"))
        self.actionOuvrire_Echelle.setText(_translate("MainWindow", "Ouvrir"))
        self.actionAnalyse.setText(_translate("MainWindow", "Analyse"))
        self.actionExit.setText(_translate("MainWindow", "Quitter"))
        #comboBox
        self.comboBox.setItemText(0, _translate("MainWindow", u"Par défaut", None))
        self.comboBox.setItemText(1, _translate("MainWindow",
                                                                u"R\u00e9sistance \u00e0 l'immersion dans l'eau", None))
        self.comboBox.setItemText(2,
                                  _translate("MainWindow", u"Cloquage \u00e0 l'humidit\u00e9 ", None))
        self.comboBox.setItemText(3, _translate("MainWindow", u"Vieillissement en autoclave", None))
        self.comboBox.setItemText(4, _translate("MainWindow", u"Adh\u00e9rence", None))
        self.comboBox.setItemText(5, _translate("MainWindow",
                                                                u"R\u00e9sistance \u00e0 l'abrasion \u00e0 sec ", None))
        self.comboBox.setItemText(6, _translate("MainWindow", u"Emboutissage Erichsen", None))
        self.comboBox.setItemText(7, _translate("MainWindow", u"Tachages par les produits chimiques ",
                                                                None))
        self.comboBox.setItemText(8, _translate("MainWindow", u"D\u00e9trempe par les solvants ", None))
        self.comboBox.setItemText(9, _translate("MainWindow", u"Tenue \u00e0 l'acide sulfurique", None))
        self.comboBox.setItemText(10, _translate("MainWindow", u"Attaques biologiques", None))
        self.comboBox.setItemText(11, _translate("MainWindow", u"Four \u00e0 Gradiant ", None))
        self.comboBox.setItemText(12, _translate("MainWindow", u"Vieillissement Artificiel WOM", None))
        self.comboBox.setItemText(13,
                                  _translate("MainWindow", u"Vieillissement Artificiel aux UVB", None))
        self.comboBox.setItemText(14, _translate("MainWindow",
                                                                 u"Vieillissement Artificiel aux UVB + tehrmocyle",
                                                                 None))
        self.comBox_quad.setItemText(0, _translate("MainWindow", u"Par défaut", None))
        self.comBox_quad.setItemText(1, _translate("MainWindow",
                                                u"R\u00e9sistance \u00e0 l'immersion dans l'eau", None))
        self.comBox_quad.setItemText(2,
                                  _translate("MainWindow", u"Cloquage \u00e0 l'humidit\u00e9 ", None))
        self.comBox_quad.setItemText(3, _translate("MainWindow", u"Vieillissement en autoclave", None))
        self.comBox_quad.setItemText(4, _translate("MainWindow", u"Adh\u00e9rence", None))
        self.comBox_quad.setItemText(5, _translate("MainWindow",
                                                u"R\u00e9sistance \u00e0 l'abrasion \u00e0 sec ", None))
        self.comBox_quad.setItemText(6, _translate("MainWindow", u"Emboutissage Erichsen", None))
        self.comBox_quad.setItemText(7, _translate("MainWindow", u"Tachages par les produits chimiques ",
                                                None))
        self.comBox_quad.setItemText(8, _translate("MainWindow", u"D\u00e9trempe par les solvants ", None))
        self.comBox_quad.setItemText(9, _translate("MainWindow", u"Tenue \u00e0 l'acide sulfurique", None))
        self.comBox_quad.setItemText(10, _translate("MainWindow", u"Attaques biologiques", None))
        self.comBox_quad.setItemText(11, _translate("MainWindow", u"Four \u00e0 Gradiant ", None))
        self.comBox_quad.setItemText(12, _translate("MainWindow", u"Vieillissement Artificiel WOM", None))
        self.comBox_quad.setItemText(13,
                                  _translate("MainWindow", u"Vieillissement Artificiel aux UVB", None))
        self.comBox_quad.setItemText(14, _translate("MainWindow",
                                                 u"Vieillissement Artificiel aux UVB + tehrmocyle",
                                                 None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
