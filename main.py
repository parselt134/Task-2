import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class YellowCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        x1, y1 = randint(0, 400), randint(0, 400)
        size = randint(0, 100)
        qp.drawEllipse(x1, y1, size, size)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = YellowCircle()
    widget.show()
    sys.exit(app.exec())
