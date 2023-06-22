from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets


class LListView(QtWidgets.QListView):
    def __init__(self, parent=None):
        super(LListView, self).__init__(parent)
        self.model = QtGui.QStandardItemModel(self)
        self.setModel(self.model)

        self.setAcceptDrops(False)
        self.setViewMode(QtWidgets.QListView.IconMode)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setIconSize(QtCore.QSize(50, 50))
        self.setResizeMode(QtWidgets.QListView.Adjust)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)


class RListView(QtWidgets.QListView):
    def __init__(self, parent=None):
        super(RListView, self).__init__(parent)
        self.model = QtGui.QStandardItemModel(self)
        self.setModel(self.model)

        self.setAcceptDrops(True)
        self.setViewMode(QtWidgets.QListView.IconMode)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setIconSize(QtCore.QSize(50, 50))
        self.setResizeMode(QtWidgets.QListView.Adjust)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        central_widget = QtWidgets.QWidget()
        self.l_view = LListView()
        self.r_view = RListView()

        self.setCentralWidget(central_widget)
        lay = QtWidgets.QHBoxLayout(central_widget)
        lay.addWidget(self.l_view)
        lay.addWidget(self.r_view)
        self.loadImages()

    def loadImages(self):
        images = Path("./img").glob("*.*")
        for image in images:
            item = QtGui.QStandardItem()
            item.setIcon(QtGui.QIcon(str(image)))
            self.l_view.model.appendRow(item)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
