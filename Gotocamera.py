import sys
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from camera import camerawidget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from datetime import datetime
from PyQt5 import QtGui
import numpy as np


def getcontours(img, imgcontours):
    img_copy = imgcontours.copy()
    contours1, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours1 = sorted(contours1, key=cv2.contourArea, reverse=True)
    if len(contours1) == 0:
        return None
    c = contours1[0]
    print(cv2.contourArea(c))
    cv2.drawContours(imgcontours, c, -1, (255, 0, 255), 1)
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    print(len(approx))
    result = imgcontours
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(imgcontours, (x, y), (x + w, y + h), (0, 255, 0), 2)
        result = img_copy[y:y + h, x:x + w]
    return result

class root(QtWidgets.QMainWindow, camerawidget):
    i = 0
    cap = cv2.VideoCapture(i)
    result = None
    def __init__(self):

        super(root, self).__init__()
        self.setupUi(self)
        if not self.cap.isOpened():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.msg = QMessageBox()
            self.msg.setWindowIcon(icon)
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setWindowTitle("ERREUR")
            self.msg.setText(
                "Aucune caméra n'a été détécter.")
            self.msg.show()
            return None
        self.width, self.height = 1200, 1080
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        #self.cameraLabel.setScaledContents(True)
        #self.imageLabel.setScaledContents(True)
        self.captureBTN.clicked.connect(self.captureimg)
        self.browseButton.clicked.connect(self.destBrowse)
        self.timer = QTimer()
        self.timer.start(10)
        self.timer.timeout.connect(self.ShowFeed)
        self.closebutton.clicked.connect(self.closefct)
        self.pushButton_Close.clicked.connect(self.closefct)
        self.actionChoix.triggered.connect(self.chnagefct)

    def ShowFeed(self):
        width, height = self.cameraLabel.width(), self.cameraLabel.height()
        '''
        if width != self.width or height != self.height:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        '''
        ret, frame = self.cap.read()
        if ret:
            imgcontours = frame.copy()
            imgBlur = cv2.GaussianBlur(frame, (7, 7), 1)
            imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
            # imgcanny = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 8)
            imgcanny = cv2.Canny(imgGray, 82, 148)
            kernel = np.ones((5, 5))
            imgDil = cv2.dilate(imgcanny, kernel=kernel, iterations=1)
            self.result = getcontours(imgDil, imgcontours)
            frame = cv2.flip(imgcontours, 1)
            frame = cv2.resize(frame, (width-5, height-5))
            cv2.putText(frame, datetime.now().strftime('%d/%m/%Y %H:%M:%S'), (20, 30), cv2.FONT_HERSHEY_DUPLEX, 0.5,
                        (0, 255, 255))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            videoImg = self.convert_nparray_to_QPixmap(frame)
            self.cameraLabel.setPixmap(videoImg)
        if self.imageLabel.capturePixmap:
            width, height = self.imageLabel.width(), self.imageLabel.height()
            saved_image = cv2.resize(self.saved_image, (width-5, height-5))
            videoImg = self.convert_nparray_to_QPixmap(saved_image)
            self.imageLabel.setPixmap(videoImg)
    def destBrowse(self):

        destDirectory = QtWidgets.QFileDialog.getSaveFileName(self, filter="Images (*.jpg *.xpm *.png)")
        destDirectory = destDirectory[0]
        print(destDirectory)
        self.saveLocationEntry.setText(str(destDirectory))
        if self.imageLabel.pixmap():
            if self.saveLocationEntry.text() != '':
                image_path = self.saveLocationEntry.text()
            else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.msg = QMessageBox()
                self.msg.setWindowIcon(icon)
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setWindowTitle("Attention")
                self.msg.setText(
                    "Vous n'avez pas  selecté un dossier pour sauvegarder l'image")
                self.msg.show()
                return None
            imgName = image_path
            success = cv2.imwrite(imgName, self.frame)
            saved_image = cv2.imread(imgName)
            if success:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Photos/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.msg = QMessageBox()
                self.msg.setWindowIcon(icon)
                self.msg.setIcon(QMessageBox.Information)
                self.msg.setWindowTitle("Réussite")
                self.msg.setText(
                    "L'image capturée est sauvegardée dans " + imgName)
                self.msg.show()
                print(6)
                return None

    def captureimg(self):
        self.result = cv2.resize(self.result, (self.imageLabel.width(), self.imageLabel.height()))
        self.frame = cv2.flip(self.result, 1)
        self.saved_image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        width, height = self.cameraLabel.width(), self.cameraLabel.height()
        saved_image = cv2.resize(self.saved_image, (width-5, height-5))
        videoImg = self.convert_nparray_to_QPixmap(saved_image)
        self.imageLabel.setPixmap(videoImg)
        self.tabWidget.setTabVisible(1, True)
        self.tabWidget.setCurrentIndex(1)
        print(5)

    def convert_nparray_to_QPixmap(self, img):

        w, h, ch = img.shape
        if img.ndim == 1:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        qimg = QImage(img.data, h, w, 3 * h, QImage.Format_RGB888)
        qpixmap = QPixmap(qimg)
        return qpixmap

    def closefct(self):
        ret, frame = self.cap.read()
        if ret:
            self.cap.release()
        self.tabWidget.setTabVisible(1, False)
        self.saveLocationEntry.setText("")
        self.close()
    def chnagefct(self):
        if self.i == 0:
            self.i = 1
            if cv2.VideoCapture(self.i).grab():
                self.cap.release()
                self.cap = cv2.VideoCapture(self.i)
            else:
                self.i = 0
        elif self.i == 1:
            self.i = 2
            if cv2.VideoCapture(self.i).grab():
                self.cap.release()
                self.cap = cv2.VideoCapture(self.i)
            else:
                self.i = 1
        elif self.i == 2:
            self.i = 0
            if cv2.VideoCapture(self.i).grab():
                self.cap.release()
                self.cap = cv2.VideoCapture(self.i)
            else:
                self.i = 2

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = root()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()