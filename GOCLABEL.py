import sys
from comment import commentWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
class  commentlabel(QtWidgets.QMainWindow, commentWindow):

    s = ''
    ss = ''
    f = ''
    t = ''
    c = ''
    def __init__(self):
        super(commentlabel, self).__init__()
        self.setupUi(self)
        self.textBrowser.textChanged.connect(self.text)

    def text(self):
        commentlabel.s = (self.textBrowser.toPlainText())
        myFile = open('comments/txt/commentlabel.txt', "w")
        myFile.write(''f'{commentlabel.s}')
        myFile.close()
        print(commentlabel.s)
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = commentlabel()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   main()