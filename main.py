import sys
import io

from random import randint

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor

tr = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>330</x>
      <y>220</y>
      <width>111</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Жми</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class WidgetArt(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(tr)
        uic.loadUi(f, self)
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
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(5, 50)
        qp.drawEllipse(100, 400, a, a)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(5, 50)
        qp.drawEllipse(200, 400, a, a)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(5, 50)
        qp.drawEllipse(300, 400, a, a)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(5, 50)
        qp.drawEllipse(400, 400, a, a)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(5, 50)
        qp.drawEllipse(500, 400, a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetArt()
    ex.show()
    sys.exit(app.exec())