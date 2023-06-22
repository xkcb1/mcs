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
# model需要opengl的功能，不使用qt3d
# import base functions
from lib.base import *
# end
# 不知道为什么，qt系列的3d功能好混乱，而且教程很少
SELF = None


def init(parent: QVBoxLayout, Name, self) -> None:
    global SELF
    globals()['SELF'] = self
    SELF = self
    # 可以统一不用定义在self下
    MODELThisWidget = QWidget()
    MODELThisWidget.setStyleSheet('border:0px;')
    parent.addWidget(MODELThisWidget)
    thisLayout = QVBoxLayout(MODELThisWidget)
    MODELThisWidget.setLayout(thisLayout)
    # add
    # PureEditor = UrsinaPureEditor(thisLayout, self, MODELThisWidget)


class UrsinaPureEditor:
    def __init__(self, Layout, parent, MODELThisWidget):
        self.Layout = Layout
        self.parent = parent
        self.MODELThisWidget = MODELThisWidget
        self.UrsinaPureEditor()

    def UrsinaPureEditor(self):
        cmd = 'python UrsinaPureEditor/UrsinaPureEditor.init.py '
        pid = subprocess.Popen(cmd, shell=True).pid
        print(pid)
        #
        time.sleep(1)
        hwnd = win32gui.FindWindowEx(
            0, 0, "WinGraphicsWindow0", "UrsinaPureEditor")
        window = QWindow.fromWinId(hwnd)
        UrsinaWidget = self.parent.createWindowContainer(
            window, self.MODELThisWidget)
        self.Layout.addWidget(UrsinaWidget)
