import sys
from comment import commentWindow
from PyQt5 import QtWidgets


class commentrepere(QtWidgets.QMainWindow, commentWindow):
    s = ''
    def __init__(self):
        super(commentrepere, self).__init__()
        self.setupUi(self)
        self.textBrowser.textChanged.connect(self.text)

    def text(self):

        commentrepere.s = (self.textBrowser.toPlainText())
        myFile = open("comments/txt/commentreper.txt", "w")
        myFile.write(commentrepere.s)
        myFile.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = commentrepere()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()