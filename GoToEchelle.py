import pickle
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from GUI_Echelle import EchelleWindow

class echelle(QtWidgets.QMainWindow, EchelleWindow):

    def __init__(self):
        super(echelle, self).__init__()
        self.setupUi(self)
        self.longueur.setValidator(QIntValidator())
        self.longueur.setMaxLength(3)
        self.largeure.setMaxLength(3)
        self.largeure.setValidator(QIntValidator())
        self.filename.setMaxLength(15)
        self.actionsauvegarder.triggered.connect(self.sauvegarder)

    def sauvegarder(self):
        if self.filename.text() == '' or self.longueur.text() == '' or self.largeure.text() == '':
            return None
        else:
            long = int(self.longueur.text())
            larg = int(self.largeure.text())
            name = self.filename.text()
            try:
                with open('echelle/'f'{name}.bin', 'wb') as file:
                    pickle.dump(long, file, pickle.HIGHEST_PROTOCOL)
                    pickle.dump(larg, file, pickle.HIGHEST_PROTOCOL)
            except (IOError, pickle.UnpicklingError):
                print('Erreur de lecture.')


if __name__ == '__main__':
    Program = QtWidgets.QApplication(sys.argv)
    Myechelle = echelle()
    Myechelle.show()
    sys.exit(Program.exec_())
