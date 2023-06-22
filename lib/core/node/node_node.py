from lib.core.node.node_graphics_node import QMGraphicsNode
from lib.base import *
from lib.core.node.node_socket import *


class Node():
    def __init__(self, scene, title, inputs, outputs):
        self.scene = scene

        self.title = title
        self.content = QDMNodeContentWidget()
        self.grNode = QMGraphicsNode(self, self.title)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.socket_spacing = 22

        # crate socket for inputs and outputs
        self.inputs = []
        self.outputs = []
        counter = 0
        for item in inputs:
            socket = Socket(node=self, index=counter, position=LEFT_TOP)
            counter += 1
            self.inputs.append(socket)

        counter = 0
        for item in outputs:
            socket = Socket(node=self, index=counter, position=RIGHT_BOTTON)
            counter += 1
            self.outputs.append(socket)

    def getSocketPosition(self, index, position):
        if position in (LEFT_TOP, LEFT_BOTTON):
            x = 0
        else:
            x = self.grNode.width
        if position in (LEFT_BOTTON, RIGHT_BOTTON):
            y = -index * self.socket_spacing + self.grNode.height - \
                self.grNode._padding - self.grNode.edge_size
        else:
            y = index * self.socket_spacing + self.grNode.title_height + \
                self.grNode._padding + self.grNode.edge_size

        return [x, y]

    @property
    def pos(self):
        return self.grNode.pos()

    def setPos(self, x, y):
        self.grNode.setPos(x, y)

    def updateConnectedEdges(self):
        for socket in self.inputs + self.outputs:
            if socket.hasEdge():
                socket.edge.updatePosition()


class QDMNodeContentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.wdg_label = QLabel("一个标题")
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QTextEdit("foo"))
