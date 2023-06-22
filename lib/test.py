<<<<<<< HEAD
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
=======
import sys
import vtk
from PyQt5 import QtCore, QtGui
from PyQt5 import Qt

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MainWindow(Qt.QMainWindow):

    def __init__(self, parent = None):
        Qt.QMainWindow.__init__(self, parent)

    def addx(self):
        self.frame = Qt.QFrame()
        self.vl = Qt.QVBoxLayout()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtkWidget)

        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        # Create source
        source = vtk.vtkSphereSource()
        source.SetCenter(0, 0, 0)
        source.SetRadius(5.0)

        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())

        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        self.ren.AddActor(actor)

        self.ren.ResetCamera()

        self.frame.setLayout(self.vl)
        self.setCentralWidget(self.frame)


        self.iren.Initialize()
        self.iren.Start()

if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
