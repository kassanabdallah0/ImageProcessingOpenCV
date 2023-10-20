from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class cWindow(object):

    _translate = QtCore.QCoreApplication.translate

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photos/icon.png"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 445, 230))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 2))
        self.choix = QtWidgets.QMenuBar(MainWindow)
        self.choix.setGeometry(QtCore.QRect(0, 0, 765, 2))
        self.menubar.setObjectName("menubar")
        self.choix.setObjectName("Choix")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.choice = QtWidgets.QMenu(self.choix)
        self.menumenu.setObjectName("menumenu")
        self.choice.setObjectName("choice")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionplus = QtWidgets.QAction(MainWindow)
        self.actionplus.setObjectName("actionplus")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsym = QtWidgets.QAction(MainWindow)
        self.actionsym.setObjectName("actionsym")
        self.actionint = QtWidgets.QAction(MainWindow)
        self.actionint.setObjectName("actionint")
        self.actionquad = QtWidgets.QAction(MainWindow)
        self.actionquad.setObjectName("actionquad")
        self.menumenu.addAction(self.actionplus)
        self.menumenu.addAction(self.actionsave)
        self.choice.addAction(self.actionsym)
        self.choice.addAction(self.actionint)
        self.choice.addAction(self.actionquad)
        self.menubar.addAction(self.menumenu.menuAction())
        self.menubar.addAction(self.choice.menuAction())

        MainWindow.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(cWindow._translate("MainWindow", "Cotation"))
        self.label.setText(cWindow._translate("MainWindow", "_"))
        self.menumenu.setTitle(cWindow._translate("MainWindow", "Menu"))
        self.choice.setTitle(cWindow._translate("MainWindow", "Choix"))
        self.actionplus.setText(cWindow._translate("MainWindow", "Plus"))
        self.actionsave.setText(cWindow._translate("MainWindow", "Sauvegarder"))
        self.actionint.setText(cWindow._translate("MainWindow", "Grav_sur"))
        self.actionsym.setText(cWindow._translate("MainWindow", "Grav_sym"))
        self.actionquad.setText(cWindow._translate("MainWindow", "Quad"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = cWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
