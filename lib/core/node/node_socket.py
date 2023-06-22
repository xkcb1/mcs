from lib.core.node.node_graphics_socket import QDMGraphicsSocket

LEFT_TOP = 1
LEFT_BOTTON = 2
RIGHT_TOP = 3
RIGHT_BOTTON = 4


class Socket():
    def __init__(self, node, index=0, position=LEFT_TOP, socket_type=1):

        self.node = node
        self.index = index
        self.socket_type = socket_type
        self.edge = None
        self.grSocket = QDMGraphicsSocket(self.node.grNode, self.socket_type)

        self.position = position
        self.grSocket.setPos(*self.node.getSocketPosition(index, position))

    def getSocketPosition(self):
        return self.node.getSocketPosition(self.index, self.position)

    def setConnectedEdge(self, edge=None):
        self.edge = edge

    def hasEdge(self):
        return self.edge is not None
