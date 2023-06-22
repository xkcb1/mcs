from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math


class QDMGraphicsScene(QGraphicsScene):
    def __init__(self, scene, parent=None):
        super().__init__(parent)

        self.scene = scene

        # setting
        self.gridSize = 20
        self.gridSquares = 5

        self._color_background = QColor("#393939")
        self._color_light = QColor("#2f2f2f")
        self._color_drak = QColor("#292929")

        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_drak = QPen(self._color_drak)
        self._pen_drak.setWidth(2)

        self.setBackgroundBrush(self._color_background)

    def setGrScene(self, width, height):
        self.setSceneRect(-width // 2, -height // 2, width, height)

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.gridSize)
        first_top = top - (top % self.gridSize)
        lines_light, lines_drak = [], []
        for x in range(first_left, right, self.gridSize):
            if (x % 100 != 0):
                lines_light.append(QLine(x, top, x, bottom))
            else:
                lines_drak.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.gridSize):
            if (y % 100 != 0):
                lines_light.append(QLine(left, y, right, y))
            else:
                lines_drak.append(QLine(left, y, right, y))

        painter.setPen(self._pen_light)
        # painter.drawLine(lines_light)
        for i in lines_light:
            painter.drawLine(i)
        painter.setPen(self._pen_drak)
        for i in lines_drak:
            painter.drawLine(i)
