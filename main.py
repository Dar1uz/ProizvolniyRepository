from PyQt6.QtGui import QColor, QPainter
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QRectF
from PyQt6 import uic  # Импортируем uic
from random import randint
from UI import Ui_Form

class MyApplication(QWidget, Ui_Form):
    do_paint = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setPen(color)
            qp.setBrush(color)
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