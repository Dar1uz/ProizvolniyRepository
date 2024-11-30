from PyQt6.QtGui import QColor, QPainter
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QRectF
from PyQt6 import uic  # Импортируем uic
from random import randint

class MyApplication(QWidget):
    do_paint = False
    color = QColor(255, 255, 0)

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(self.color)
            qp.setBrush(self.color)
            a = randint(50, 300)
            rectangle = QRectF(11, 50, a, a)
            qp.drawEllipse(rectangle)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyApplication()
    main.show()
    sys.exit(app.exec())