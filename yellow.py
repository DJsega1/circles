import sys

from PyQt5 import uic
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.click)
        self.paint = False

    def click(self):
        self.paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.paint:
            for i in range(randint(1, 100)):
                radius = randint(1, 100)
                qp = QPainter()
                qp.begin(self)
                qp.setBrush(QColor(255, 255, 0))
                qp.drawEllipse(randint(0, self.width()), randint(0, self.height()), radius, radius)
                qp.end()
                self.paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
