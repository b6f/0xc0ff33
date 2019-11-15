import sys
from PyQt5 import QtWidgets, QtGui, uic, QtCore


class W(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw_circles)
        self.do_draw = False

    def draw_circles(self):
        self.do_draw = True
        self.repaint()

    def paintEvent(self, a0):
        if not self.do_draw:
            return
        self.do_draw = False

        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setBrush(QtGui.QColor(255, 255, 0))

        painter.drawEllipse(QtCore.QPoint(70, 80), 30., 30.)
        painter.drawEllipse(QtCore.QPoint(100, 200), 50., 50.)

        painter.end()


app = QtWidgets.QApplication(sys.argv)
ex = W()
ex.show()
sys.exit(app.exec_())
