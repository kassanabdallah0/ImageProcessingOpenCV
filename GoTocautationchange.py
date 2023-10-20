import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from cautationchange import cWindow
import pickle
import os


class cotationWindow(QtWidgets.QMainWindow, cWindow):
    count = 0
    _translate = QtCore.QCoreApplication.translate
    rx = QRegExp("[A-E]")
    rx.setPattern("[1-5]")
    v = QRegExpValidator(rx)
    infolist = []
    bi = True
    bq = False

    def __init__(self):
        super(cotationWindow, self).__init__()
        self.setupUi(self)
        self.filename = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.filename.setObjectName("Filename")
        self.gridLayout_2.addWidget(self.filename, 0, 1, 1, 1)
        self.name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.name, 0, 2, 1, 1)
        self.symbole = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.symbole.setObjectName("symbole")
        self.gridLayout_2.addWidget(self.symbole, 1, 2, 1, 1)
        self.symbole.setValidator(cotationWindow.v)
        self.symbole.setMaxLength(1)
        self.symbolelist = []
        self.symbolelist.insert(cotationWindow.count, self.symbole)
        self.pourcentage = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.pourcentage.setObjectName("pourcentage")
        self.gridLayout_2.addWidget(self.pourcentage, 1, 0, 1, 1)
        self.pourcentage.setValidator(QDoubleValidator())
        self.pourcentage.setMaxLength(6)
        self.pourcentagelist = []
        self.labellist = []
        self.pourcentagelist.insert(cotationWindow.count, self.pourcentage)
        self.labellist.insert(cotationWindow.count, self.label)
        self.actionplus.triggered.connect(self.plus)

        self.actionsave.setShortcut("Ctrl+S")
        self.actionsave.setStatusTip('Save File')
        self.actionsave.triggered.connect(self.save)
        self.name.setMaxLength(15)
        self.name.setText('Nom fichier')
        self.filename.setText("Nom fichier")

        self.actionsym.triggered.connect(self.choixsym)
        self.actionint.triggered.connect(self.choixint)
        self.actionquad.triggered.connect(self.choixquad)

        self.chlabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.chlabel.setObjectName("choice titre")
        self.gridLayout_2.addWidget(self.chlabel, 0, 0, 1, 1)
        self.chlabel.setText('choix int')
        sss = ''
        try:
            with open('txt/info.bin', 'wb') as file:
                pickle.dump(sss, file, pickle.HIGHEST_PROTOCOL)
        except (IOError, pickle.PicklingError):
            print('Erreur d\'écriture.')

    def plus(self):

        cotationWindow.count += 1
        if cotationWindow.count <= 4:
            self.line = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.line.setObjectName('pourcentage_'f'{cotationWindow.count}')
            self.gridLayout_2.addWidget(self.line, cotationWindow.count + 1, 0, 1, 1)
            self.line.setValidator(QDoubleValidator())
            self.line.setMaxLength(6)
            self.pourcentagelist.insert(cotationWindow.count, self.line)

            self.label_l = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.label_l.setObjectName('label_'f'{cotationWindow.count}')
            self.gridLayout_2.addWidget(self.label_l, cotationWindow.count + 1, 1, 1, 1)
            self.label_l.setText(cotationWindow._translate("MainWindow", "%"))
            self.labellist.insert(cotationWindow.count, self.label_l)

            self.symbol_s = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.symbol_s.setObjectName('symbole_'f'{cotationWindow.count}')
            self.gridLayout_2.addWidget(self.symbol_s, cotationWindow.count + 1, 2, 1, 1)
            self.symbol_s.setValidator(cotationWindow.v)
            self.symbol_s.setMaxLength(1)
            self.symbolelist.insert(cotationWindow.count, self.symbol_s)
            if cotationWindow.count == 4:
                self.actionplus.setVisible(False)



    def save(self):

        if cotationWindow.count == 1:
            var = [self.pourcentage.text(), self.symbole.text()]
            var1 = [self.pourcentagelist[1].text(), self.symbolelist[1].text()]

            cotationWindow.infolist = [var, var1]
            if os.path.exists('txt/info.bin'):
                os.remove('txt/info.bin')
            try:
                with open('txt/info.bin', 'wb') as file:
                    pickle.dump(cotationWindow.infolist, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écriture.')

        elif cotationWindow.count == 2:
            var = [self.pourcentage.text(), self.symbole.text()]
            var1 = [self.pourcentagelist[1].text(), self.symbolelist[1].text()]
            var2 = [self.pourcentagelist[2].text(), self.symbolelist[2].text()]
            cotationWindow.infolist = [var, var1, var2]
            if os.path.exists('txt/info.bin'):
                os.remove('txt/info.bin')
            try:
                with open('txt/info.bin', 'wb') as file:
                    pickle.dump(cotationWindow.infolist, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écriture.')
        elif cotationWindow.count == 3:
            var = [self.pourcentage.text(), self.symbole.text()]
            var1 = [self.pourcentagelist[1].text(), self.symbolelist[1].text()]
            var2 = [self.pourcentagelist[2].text(), self.symbolelist[2].text()]
            var3 = [self.pourcentagelist[3].text(), self.symbolelist[3].text()]
            cotationWindow.infolist = [var, var1, var2, var3]
            if os.path.exists('txt/info.bin'):
                os.remove('txt/info.bin')
            try:
                with open('txt/info.bin', 'wb') as file:
                    pickle.dump(cotationWindow.infolist, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écriture.')
        elif cotationWindow.count == 4:
            var = [self.pourcentage.text(), self.symbole.text()]
            print(1)
            var1 = [self.pourcentagelist[1].text(), self.symbolelist[1].text()]
            print(2)
            var2 = [self.pourcentagelist[2].text(), self.symbolelist[2].text()]
            print(3)
            var3 = [self.pourcentagelist[3].text(), self.symbolelist[3].text()]
            print(4)
            var4 = [self.pourcentagelist[4].text(), self.symbolelist[4].text()]
            print(5)
            cotationWindow.infolist = [var, var1, var2, var3, var4]
            print(6)
            if os.path.exists('txt/info.bin'):
                os.remove('txt/info.bin')
                print(7)
            try:
                with open('txt/info.bin', 'wb') as file:
                    pickle.dump(cotationWindow.infolist, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écriture.')
        else:
            if os.path.exists('txt/info.bin'):
                os.remove('txt/info.bin')
            var = [self.pourcentage.text(), self.symbole.text()]
            cotationWindow.infolist = [var]
            try:
                with open('txt/info.bin', 'wb') as file:
                    pickle.dump(cotationWindow.infolist, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.PicklingError):
                print('Erreur d\'écriture.')

        if cotationWindow.bi == True and cotationWindow.bq == False:
            s = self.name.text()
            print(1)
            if s == 'filename':
                return None
            else:
                if os.path.exists('cotation_surface/'f'{s}.bin'):
                    os.remove('cotation_surface/'f'{s}.bin')
                    print(1)
                try:
                    with open('cotation_surface/'f'{s}.bin', 'wb') as file:
                        pickle.dump(cotationWindow.infolist, file, pickle.HIGHEST_PROTOCOL)
                        pickle.dump(cotationWindow.bi, file, pickle.HIGHEST_PROTOCOL)
                        pickle.dump(cotationWindow.bq, file, pickle.HIGHEST_PROTOCOL)
                        print(1)
                except (IOError, pickle.PicklingError):
                    print('Erreur d\'écriture.')

        elif cotationWindow.bi == False and cotationWindow.bq == False:
            s = self.name.text()
            if s == 'filename':
                return None
            else:
                if os.path.exists('cotation_symbole/'f'{s}.bin'):
                    os.remove('cotation_symbole/'f'{s}.bin')
                try:
                    with open('cotation_symbole/'f'{s}.bin', 'wb') as file:
                        pickle.dump(cotationWindow.infolist, file, pickle.HIGHEST_PROTOCOL)
                        pickle.dump(cotationWindow.bi, file, pickle.HIGHEST_PROTOCOL)
                        pickle.dump(cotationWindow.bq, file, pickle.HIGHEST_PROTOCOL)
                except (IOError, pickle.PicklingError):
                    print('Erreur d\'écriture.')
        if cotationWindow.bi == False and cotationWindow.bq == True:
            s = self.name.text()

            if s == 'filename':
                return None
            else:
                if os.path.exists('cotation_quad/'f'{s}.bin'):
                    os.remove('cotation_quad/'f'{s}.bin')
                try:
                    with open('cotation_quad/'f'{s}.bin', 'wb') as file:
                        pickle.dump(cotationWindow.infolist, file, pickle.HIGHEST_PROTOCOL)
                        pickle.dump(cotationWindow.bi, file, pickle.HIGHEST_PROTOCOL)
                        pickle.dump(cotationWindow.bq, file, pickle.HIGHEST_PROTOCOL)
                except (IOError, pickle.PicklingError):
                    print('Erreur d\'écriture.')

    def choixint(self):
        cotationWindow.bi = True
        self.chlabel.setText('choix int')
        cotationWindow.bq = False

    def choixsym(self):
        self.chlabel.setText('choix sym')
        cotationWindow.bi = False
        cotationWindow.bq = False

    def choixquad(self):
        self.chlabel.setText('choix quad')
        cotationWindow.bq = True
        cotationWindow.bi = False


if __name__ == '__main__':
    Program = QtWidgets.QApplication(sys.argv)
    MyProg = cotationWindow()
    MyProg.show()
    sys.exit(Program.exec_())
