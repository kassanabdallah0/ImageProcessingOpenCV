import sys
from comment import commentWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import pickle

class  commenttable(QtWidgets.QMainWindow, commentWindow):

    data = []
    longueur = 0
    s = ''

    def __init__(self):
        super(commenttable, self).__init__()
        self.setupUi(self)
        self.textBrowser.textChanged.connect(self.text)

        try:
            with open('comments/txt/table.bin', 'rb') as file:
                commenttable.longueur = pickle.load(file)
                i = 0
                while i < commenttable.longueur:
                    x = pickle.load(file)
                    s = ['numero d impact:'f'{x[0]}','X:'f'{x[1]}','Y:'f'{x[2]}','perimetre:'f'{x[3]}','area:'f'{x[4]}','pourcentage:'f'{x[5]}','cotation:'f'{x[6]}']
                    print(s)
                    commenttable.data.insert(i, s)
                    i += 1
                print(commenttable.data)
        except (IOError, pickle.UnpicklingError):
            print('Erreur de lecture.')
        print(commenttable.longueur)

    def text(self):
        commenttable.s = (self.textBrowser.toPlainText())
        myFile = open("comments/txt/commenttable.txt", "w")
        myFile.write(commenttable.s)
        print(commenttable.s)
        myFile.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = commenttable()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   main()