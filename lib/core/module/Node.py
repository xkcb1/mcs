# 每个module要求实现一个init(parent,Name,self)函数，来获取此次初始化
import os
import sys
import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import *
from lib.readConfig import readConfig
from lib.StyleReader import StyleReader
# import base functions
from lib.base import *
# more lib
# images for the dark skin
# end

SELF = None


def init(parent, Name, self):
    globals()['SELF'] = self
    global SELF
    SELF = self
    ThisWidget = QWidget()
    parent.addWidget(ThisWidget)
    # main
    self.nodeToptabs = QTabWidget()
    self.nodeToptabs.TabShape(1)
    self.nodeToptabs.setObjectName('nodeToptabs')

    # tabs.setTabPosition(QTabWidget.West)
    self.nodeToptabs.setMovable(True)
    self.nodeToptabs.setTabsClosable(True)
    self.nodeToptabs.setContentsMargins(0, 0, 0, 0)
    ThisWidget_layout = QHBoxLayout()
    ThisWidget.setLayout(ThisWidget_layout)
    ThisWidget_layout.setSpacing(0)
    ThisWidget_layout.setContentsMargins(0, 0, 0, 0)
    ThisWidget_layout.addWidget(self.nodeToptabs)
    addNodeEditor('untitled')


def addNodeEditor(name):
    newTabWidget = QWidget()
    SELF.nodeToptabs.addTab(
        newTabWidget, QIcon(''), name + '.mcNode')
    This_layout = QVBoxLayout()
    This_layout.setContentsMargins(0, 0, 0, 0)
    This_layout.setSpacing(0)
    newTabWidget.setLayout(This_layout)
    #
    scene = Scene()
    grScene = scene.grScene
    node1 = Node(scene, "这是一个节点", inputs=[0, 0, 0], outputs=[3])
    node2 = Node(scene, "这是第二个节点", inputs=[1, 1, 1], outputs=[3])
    node3 = Node(scene, "这是第三个节点", inputs=[2, 2, 2], outputs=[3])

    node1.setPos(-350, -250)
    node2.setPos(-75, 0)
    node3.setPos(200, -150)

    edge1 = Edge(scene, node1.outputs[0], node2.inputs[0], type=2)
    edge2 = Edge(scene, node2.outputs[0], node3.inputs[0], type=2)

    # create graphics view
    view = QDMGraphicsView(grScene)
    This_layout.addWidget(view)
