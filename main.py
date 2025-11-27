import sys
import io

from random import randint

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor


class WidgetArt(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.draw)
        self.flag = False

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.dr(qp)
            qp.end()
        self.flag = False

    def dr(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        a = randint(5, 50)
        qp.drawEllipse(100, 400, a, a)
        a = randint(5, 50)
        qp.drawEllipse(200, 400, a, a)
        a = randint(5, 50)
        qp.drawEllipse(300, 400, a, a)
        a = randint(5, 50)
        qp.drawEllipse(400, 400, a, a)
        a = randint(5, 50)
        qp.drawEllipse(500, 400, a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetArt()
    ex.show()
    sys.exit(app.exec())