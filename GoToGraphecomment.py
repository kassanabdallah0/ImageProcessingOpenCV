import sys

from comment import commentWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import pickle


class commentgraphe(QtWidgets.QMainWindow, commentWindow):
    s =''
    def __init__(self):
        super(commentgraphe, self).__init__()
        self.setupUi(self)
        self.textBrowser.textChanged.connect(self.text)
    def text(self):

        myFile = open("comments/txt/commentcourbe.txt", "w")
        commentgraphe.s = (self.textBrowser.toPlainText())

        myFile.write(commentgraphe.s)

        myFile.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = commentgraphe()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()