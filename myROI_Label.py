from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QLabel
from fonction_gra import *

class MyLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    xx = 0
    yy = 0
    flag = False
    loadPixmap = None
    capturePixmap = None
    l = 0
    h = 0
    # 鼠标点击事件
    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()


    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawRect(rect)
        echelle = ECHELLE()
        self.l = int(abs(self.x1 - self.x0) * echelle)
        self.h = int(abs(self.y1 - self.y0) * echelle)
        text = "H:" + str(self.h) + " mm" + "\t" + "L:" + str(self.l) + " mm"
        xb = rect.bottomRight().x()
        yb = rect.bottomRight().y()
        if self.h != 0 and self.l != 0:
            painter.drawText(xb-120, yb+30, str(text))

        # 避免宽或高为零时拷贝截图有误;
        if rect.width() == 0:
            rect.setWidth(1)
        if rect.height() == 0:
            rect.setHeight(1)
        if self.pixmap():
            self.capturePixmap = self.pixmap().toImage().copy(rect)
