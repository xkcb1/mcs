<<<<<<< HEAD
import binascii
import os
import sys
import PyQt5.QtGui as QtGui
=======
import os,sys
import PyQt5.QtGui as QtGui
import vtk
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import *
from lib.readConfig import readConfig
from lib.StyleReader import StyleReader
from pathlib import Path
import lib.WindowMenu
import lib.core.function.FileIcon
from lib.core.function.FileIcon import *
<<<<<<< HEAD
# 3d
from lib.pure.NbtTree import *
# math
from pathlib import Path
# sip
from PyQt5 import sip

import lib.core.function.FileIcon
# morelib
=======
#3d
from lib.pure.NbtTree import *
#math
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
import numpy as np
import math
from numpy import *
import numpy
<<<<<<< HEAD
# error
import datetime
import traceback
# nbt
import nbtlib
from PyQt5.QtOpenGL import QGLWidget
from lib.pure.MakeObj import MakeStlFileByNbt
# 方便一次性导入所有的基础要用的库
import threading
from threading import *
# 多线程库
import gc
# from time import process_time
from time import process_time
import time
# 内存管理库
# 程序内存限制库
# node editor
from lib.core.node.node_node import Node
from lib.core.node.node_graphics_view import QDMGraphicsView
from lib.core.node.node_scene import Scene
from lib.core.node.node_node import Node
from lib.core.node.node_edge import *
# setting function
from lib.core.function.setting_function import *
# theme
import qdarkstyle
from qdarkstyle.light.palette import LightPalette
import qdarktheme
import qtvscodestyle as qtvsc
from qt_material import apply_stylesheet
from PyQt5.QtWebEngineWidgets import *
#
import lib.core.module.Info as info
# win32
import win32gui
import win32con
import win32api
import psutil
import win32process
import subprocess
# vtk
from PyQt5.QtOpenGL import QGLWidget
from lib.pure.MakeObj import MakeStlFileByNbt
############################# METHOD ###################################
rewrite_print = print
print_ = print


def print(*arg, SELF=None, widgetList=None):
    # 首先，调用原始的print函数将内容打印到控制台。
    rewrite_print(*arg)
    # 如果日志文件所在的目录不存在，则创建一个目录。
    # output_dir = "./log_file"
    # 打开（或创建）日志文件并将内容写入其中。
    # log_name = 'log.txt'
    # filename = os.path.join(output_dir, log_name)
    rewrite_print(*arg, file=open("/log.txt", "a"))
    try:
        # rewrite_print(SELF,widgetList)
=======
#error
import traceback
#nbt
import nbtlib
#use vtk
from PyQt5.QtOpenGL import QGLWidget
from vtk import *
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from lib.pure.MakeObj import MakeStlFileByNbt
#方便一次性导入所有的基础要用的库
import threading
from threading import *
#多线程库
################################################################
rewrite_print = print
print_ = print
def print(*arg,SELF=None,widgetList=None):
    # 首先，调用原始的print函数将内容打印到控制台。
    #rewrite_print(*arg)
    # 如果日志文件所在的目录不存在，则创建一个目录。
    #output_dir = "./log_file"
    # 打开（或创建）日志文件并将内容写入其中。
    #log_name = 'log.txt'
    #filename = os.path.join(output_dir, log_name)
    rewrite_print(*arg,file=open("./log_file/log.txt","a"))
    try:
        #rewrite_print(SELF,widgetList)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
        for widget in widgetList:
            for value in arg:
                widget.append(str(value))
    except:
        pass
################################################################
<<<<<<< HEAD


def clearLog():
    with open("/log.txt", "w") as wf:
        wf.write('')
################################################################


def getLog():
    with open("/log.txt", "r") as rf:
        getlogfile = rf.read()
    return getlogfile
# globals()['SELF'] = self
################################################################


def GetDir(self, Lastpath, tabCount):  # 从Main里迁移出来
    for file_name in os.listdir(Lastpath):
        if os.path.isdir(Lastpath+'//'+file_name) == True:
            # print(file_name)
            # is folder
            # print(Lastpath+'\\'+file_name)
            self.pathList.append(tabCount*'  '+file_name)
            self.Projectfolders = self.Projectfolders + 1
            GetDir(self, Lastpath+'\\'+file_name, tabCount=tabCount+1)
        else:
            self.pathList.append(tabCount*'  '+file_name)
            self.Projectfiles += 1
################################ CLASS ################################


class MemoryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.MainWidget = QWidget(self)
        self.MainWidget.setObjectName('memory_widget')
        self.MainWidget.setStyleSheet(
            '''#memory_widget{border: 1px solid lightgray;}''')
        # ProcessBar
        self.MainWidget.resize(104, 17)
        #
        self.setFixedHeight(17)
        self.ProcessBar = QWidget(self.MainWidget)
        self.ProcessBar.move(2, 2)
        self.ProcessBar.setFixedHeight(13)
        #
        self.ProcessBar.setStyleSheet(
            '''background-color:rgba(200,200,200,0.7);border-right:1px solid rgba(200,200,200,0.9);''')
        #
        self.text = QLabel(self)
        self.text.setText('memory:0%')
        self.text.setStyleSheet('''color:lightgray;''')
        self.text.move(2, 0)
        self.text.setMinimumWidth(100)
        self.text.setFixedHeight(17)
        self.text.setStyleSheet('border:0px;')
        self.setMinimumWidth(104)
        ##########################################
        self.timethread = Time_thread()
        self.timethread.sinout.connect(self.Refresh_label)
        self.countTimer = QTimer(self)                      # 实例化一个计时器
        # 将timeout与槽函数相连，计时器溢出时执行槽函数刷新界面
        self.countTimer.timeout.connect(self.timeout_fun)
        self.timethread.start()
        self.count_start()

    def timeout_fun(self):
        info = psutil.virtual_memory()
        use = psutil.Process(os.getpid()).memory_info().rss
        total = info.total
        rate = info.percent
        self.ProcessBar.resize(int(rate), 15)
        self.text.setText('memory:'+str(rate)+'%')
        self.setToolTip(str(int(use/1024/1024)) + ' MB / ' +
                        str(int(info.total/1024/1024)) + ' GB')

    def count_start(self):
        self.countTimer.start(1000)                         # 开始计时，定时1s执行一次

    def thread_start(self):
        self.timethread.start()

    def Refresh_label(self):
        pass


class UseMemory(QWidget):
    def __init__(self, APP_MEMORY):
        super().__init__()
        self.APP_MEMORY = APP_MEMORY
        self.MainWidget = QWidget(self)
        self.MainWidget.setObjectName('memory_widget')
        self.MainWidget.setStyleSheet(
            '''#memory_widget{border: 1px solid lightgray;}''')
        # ProcessBar
        self.MainWidget.resize(104, 17)
        #
        self.setFixedHeight(17)
        self.ProcessBar = QWidget(self.MainWidget)
        self.ProcessBar.move(2, 2)
        self.ProcessBar.setFixedHeight(13)
        #
        self.ProcessBar.setStyleSheet(
            '''background-color:rgba(150,150,150,0.7);border-right:1px solid rgba(150,150,150,0.9);''')
        #
        self.text = QLabel(self)
        self.text.setText('APP use:0%')
        self.text.setStyleSheet('''color:lightgray;''')
        self.text.move(2, 0)
        self.text.setMinimumWidth(100)
        self.text.setFixedHeight(17)
        self.text.setStyleSheet('border:0px;')
        self.setMinimumWidth(104)
        ##########################################
        self.timethread = Time_thread()
        self.timethread.sinout.connect(self.Refresh_label)
        self.countTimer = QTimer(self)                      # 实例化一个计时器
        # 将timeout与槽函数相连，计时器溢出时执行槽函数刷新界面
        self.countTimer.timeout.connect(self.timeout_fun)
        self.timethread.start()
        self.count_start()

    def timeout_fun(self):
        p = psutil.Process(os.getpid())
        rate = (p.memory_info().rss/1024/1024) / self.APP_MEMORY
        self.ProcessBar.resize(int(rate*100), 15)
        self.text.setText('APP use:'+str(rate*100)[:4]+'%')
        self.setToolTip(str(p.memory_info().rss/1024/1024)+" MB / 4 GB")

    def count_start(self):
        self.countTimer.start(1000)                         # 开始计时，定时1s执行一次

    def thread_start(self):
        self.timethread.start()

    def Refresh_label(self):
        pass


class Time_thread(QThread):
    sinout = pyqtSignal(str)

    def __init__(self):
        super(Time_thread, self).__init__()
        print('Time_thread Start...')

    def run(self):
        while (True):
            time.sleep(2)


class AttributePanel(QFrame):
    # 参数1：Name:str,参数2：Attribute:dict,参数3：ifopen:boolean,
    def __init__(self, Name: str, AttributeDic: dict, funcList: list, ifopen: bool = False):
=======
def clearLog():
    with open("./log_file/log.txt","w") as wf:
        wf.write('')
################################################################
def getLog():
    with open("./log_file/log.txt","r") as rf:
        getlogfile = rf.read()
    return getlogfile
#globals()['SELF'] = self
################################################################
def GetDir(self,Lastpath,tabCount):#从Main里迁移出来
    for file_name in os.listdir(Lastpath):
        if os.path.isdir(Lastpath+'//'+file_name) == True:
            #print(file_name)
            #is folder
            #print(Lastpath+'\\'+file_name)
            self.pathList.append(tabCount*'  '+file_name)
            self.Projectfolders = self.Projectfolders + 1
            GetDir(self,Lastpath+'\\'+file_name,tabCount = tabCount+1)
        else:
            self.pathList.append(tabCount*'  '+file_name)
            self.Projectfiles += 1
################################################################
class AttributePanel(QFrame):
    # 参数1：Name:str,参数2：Attribute:dict,参数3：ifopen:boolean,
    def __init__(self, Name: str, AttributeDic: dict, funcList: list,ifopen: bool = False):
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
        # ifopen默认为FALSE，就是展开
        super().__init__()
        # start
        self.Name = Name
        self.Attribute = AttributeDic
        self.ifopen = ifopen
        self.funcList = funcList
        self.ItemCount = 0
        for i in self.Attribute:
            self.ItemCount += 1
        # self.setMinimumHeight(20)
        self.UIinit()
<<<<<<< HEAD

=======
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    def UIinit(self) -> None:
        self.IsZoomSmall = 0
        # 25是属性框收缩后的高度
        self.setObjectName('ATTRIBUTEPanel')
        self.setStyleSheet('''
#ATTRIBUTEPanel{
    border-radius:4px;
    border:1px solid #ddd
}
''')
        # self.setMaximumWidth(999999)
        self.MainLayoutATTR = QVBoxLayout()
        self.setLayout(self.MainLayoutATTR)
        self.MainLayoutATTR.setContentsMargins(0, 0, 0, 0)
        self.MainLayoutATTR.setSpacing(0)
        self.OptionLayout_Widget = QWidget()
        self.OptionLayout_Widget.setMinimumHeight(25)
        self.OptionLayout_Widget.setMaximumHeight(25)
        self.OptionLayout_Widget.setStyleSheet(
            'background-color:rgba(0,0,0,0);border:0px;')
        self.OptionLayout = QHBoxLayout()
        self.OptionLayout.setContentsMargins(5, 0, 0, 0)
        self.MainLayoutATTR.addWidget(self.OptionLayout_Widget)
        self.OptionLayout_Widget.setLayout(self.OptionLayout)
        self.ThisName = QPushButton()
        # self.ThisName.setStyleSheet('background-color:red;')
        self.ThisName.setMinimumHeight(25)
        self.ThisName.setMaximumHeight(25)
        self.ThisName.clicked.connect(self.zoomPanel)
        #
        self.Other = QWidget()
        self.Other.setObjectName('OtherSplitter')
        self.ThisName.setObjectName('thisAttrName')
        self.ThisName.setText(self.Name)
        self.ThisName.setIcon(QIcon("./img/bottom_to.png"))
<<<<<<< HEAD
        self.ThisName.setStyleSheet('''
#thisAttrName{
    text-align: left;
    font-weight: bold;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}''')
=======
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
        # print(self.Name)
        self.OptionLayout.addWidget(self.ThisName)
        self.OptionLayout.addWidget(self.Other)
        #
        self.MainWidget = QWidget()
        self.MainLayoutATTR.addWidget(self.MainWidget)
        self.MainLayoutEdit = QGridLayout()
        self.MainLayoutEdit.setContentsMargins(0, 0, 0, 0)
        self.MainWidget.setLayout(self.MainLayoutEdit)
        self.Gx = 0
        self.Gy = 0
        # self.setLayout(MainLayoutATTR)
        # make the attributes from dict
        self.makeUI()
        if self.ifopen == True:
            self.IsZoomSmall = 1
            self.toBig()
        else:
            self.IsZoomSmall = 0
            self.toSmall()

    def toSmall(self):  # 收缩
        self.ThisName.setIcon(QIcon("./img/bottom_to.png"))
        print('toSmall')
        animationSmall = QPropertyAnimation(self, b"geometry")
        animationSmall.setDuration(1000)
        self.setMaximumHeight(25)
        start = self.geometry()
        animationSmall.setEndValue(start)
        animationSmall.start()
        self.MainWidget.hide()

    def toBig(self):  # 扩展
        print('toBig')
        self.ThisName.setIcon(QIcon("./img/ToOpen_.png"))
        animationBig = QPropertyAnimation(self, b"geometry")
        animationBig.setDuration(1000)
        self.setMaximumHeight(self.ItemCount*25+35)
        start = self.geometry()
        animationBig.setEndValue(start)
        animationBig.start()
        self.MainWidget.show()

    def makeUI(self):
        self.MainLayoutEdit.setContentsMargins(4, 4, 4, 4)
        self.count = 0
        for EditItem in self.Attribute:
            ItemName = QLabel()
            ItemName.setText(EditItem)
            ItemName.setObjectName('ItemName')
            ThisType = type(self.Attribute[EditItem])
            if ThisType == type('str'):  # 如果是字符串
                EditItemWidget = QLineEdit()
                EditItemWidget.setObjectName('EditItemWidget')
                EditItemWidget.setStyleSheet('')
                if self.funcList != None:
                    EditItemWidget.textChanged.connect(self.changeText)
                    EditItemWidget.ClassName = str(self.count)
                EditItemWidget.setText(self.Attribute[EditItem])
                ItemName.setStyleSheet('''
                                   background-image:url(./img/gray2.png);
                                   background-repeat:no-repeat;
                                   padding-left:15px;
                                   margin-left:4px;
<<<<<<< HEAD
                                   border:0px;
                                   background-position: center left;''')
=======
                                   border:0px;''')
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
            elif ThisType == type(1):  # 如果是整型
                EditItemWidget = QPushButton()
                EditItemWidget.setObjectName('EditItemWidget_button')
                EditItemWidget.setText(str(self.Attribute[EditItem]))
                if self.funcList != None:
                    EditItemWidget.clicked.connect(self.changeButton)
                    EditItemWidget.ClassName = str(self.count)
                ItemName.setStyleSheet('''
                                   background-image:url(./img/blue2.png);
                                   background-repeat:no-repeat;
                                   padding-left:15px;
                                   margin-left:4px;
<<<<<<< HEAD
                                   border:0px;
                                   background-position: center left;''')
=======
                                   border:0px;''')
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
            elif self.Attribute[EditItem].__class__ == Ppath:  # 如果是Ppath类型
                EditItemWidget = QPushButton()
                EditItemWidget.setObjectName('EditItemWidget_button_Path')
                EditItemWidget.setText(str(self.Attribute[EditItem].path))
                if self.funcList != None:
                    EditItemWidget.clicked.connect(self.changeButton)
                    EditItemWidget.ClassName = str(self.count)
                ItemName.setStyleSheet('''
                                   background-image:url(./img/yellow2.png);
                                   background-repeat:no-repeat;
                                   padding-left:15px;
                                   margin-left:4px;
<<<<<<< HEAD
                                   border:0px;
                                   background-position: center left;''')
=======
                                   border:0px;''')
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
            elif ThisType == type(True):  # 如果是布尔值
                EditItemWidget = QPushButton()
                EditItemWidget.setObjectName('EditItemWidget_button')
                EditItemWidget.setText(str(self.Attribute[EditItem]))
                if self.funcList != None:
                    EditItemWidget.clicked.connect(self.changeButton)
                    EditItemWidget.ClassName = str(self.count)
                ItemName.setStyleSheet('''
                                   background-image:url(./img/purple2.png);
                                   background-repeat:no-repeat;
                                   padding-left:15px;
                                   margin-left:4px;
<<<<<<< HEAD
                                   border:0px;
                                   background-position: center left;''')
                EditItemWidget.clicked.connect(self.ChangeBoolean)
            elif ThisType == type([1]):  # 如果是列表
                EditItemWidget = QComboBox()
                EditItemWidget.setObjectName('EditItemWidget_search')
                if self.funcList != None:
                    EditItemWidget.currentIndexChanged.connect(
                        self.changeSearch)
=======
                                   border:0px;''')
                EditItemWidget.clicked.connect(self.ChangeBoolean)
            elif ThisType == type([1]):#如果是列表
                EditItemWidget = QComboBox()
                EditItemWidget.setObjectName('EditItemWidget_search')
                if self.funcList != None:
                    EditItemWidget.currentIndexChanged.connect(self.changeSearch)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
                    EditItemWidget.ClassName = str(self.count)
                for item in self.Attribute[EditItem]:
                    EditItemWidget.addItem(item)
                ItemName.setStyleSheet('''
                                   background-image:url(./img/organe2.png);
                                   background-repeat:no-repeat;
                                   padding-left:15px;
                                   margin-left:4px;
<<<<<<< HEAD
                                   border:0px;
                                   background-position: center left;''')
            # ItemName.setMaximumWidth(70)
            self.MainLayoutEdit.addWidget(ItemName, self.Gx, self.Gy)
            # print(self.Gx,self.Gy,1,1)
            self.Gy += 1
            self.MainLayoutEdit.addWidget(EditItemWidget, self.Gx, self.Gy)
            # print(self.Gx,self.Gy,1,1)
=======
                                   border:0px;''')
            #ItemName.setMaximumWidth(70)
            self.MainLayoutEdit.addWidget(ItemName,self.Gx,self.Gy)
            #print(self.Gx,self.Gy,1,1)
            self.Gy += 1
            self.MainLayoutEdit.addWidget(EditItemWidget,self.Gx,self.Gy)
            #print(self.Gx,self.Gy,1,1)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
            self.Gx += 1
            self.Gy = 0
            self.count += 1
            # 通过type来判断需要放置一个什么样的QObject
<<<<<<< HEAD

=======
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    def changeSearch(self):
        sender = self.sender()
        getIndex = int(sender.ClassName)
        self.funcList[getIndex](self)
<<<<<<< HEAD

=======
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    def changeText(self):
        sender = self.sender()
        getIndex = int(sender.ClassName)
        self.funcList[getIndex](self)
<<<<<<< HEAD

=======
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    def changeButton(self):
        sender = self.sender()
        getIndex = int(sender.ClassName)
        self.funcList[getIndex](self)
<<<<<<< HEAD

=======
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    def zoomPanel(self, mode: int) -> None:
        print('clicked')
        # mode 1 扩展
        # mode 0 收缩
        if self.IsZoomSmall == 0:  # 已经是收缩
            self.toBig()
            self.IsZoomSmall = 1  # 已经是扩展
        else:
            self.toSmall()
            self.IsZoomSmall = 0

    def ChangeBoolean(self):
        getSender = self.sender()
        if getSender.text() == 'False':
            getSender.setText('True')
        else:
            getSender.setText('False')
################################################################
<<<<<<< HEAD


class Ppath:
    def __init__(self, path):
        self.path = path
################################################################


class PQWidget(QWidget):
    def __init__(self, parent_):
        self.parent_ = parent_
        super().__init__()

=======
class Ppath:
    def __init__(self,path):
        self.path = path
################################################################
class PQWidget(QWidget):
    def __init__(self,parent_):
        self.parent_ = parent_
        super().__init__()
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.parent_.isMaximized():  # 缩小
            self.parent_.THIS_Widget.setContentsMargins(7, 7, 7, 7)
            self.parent_.verticalLayout__.setContentsMargins(1, 1, 1, 1)
            self.parent_.showNormal()  # 切换放大按钮图标
            self.parent_.pushButton_2.setToolTip(
                "<html><head/><body><p>最大化</p></body></html>")
        else:  # 放大
            self.parent_.THIS_Widget.setContentsMargins(0, 0, 0, 0)
            self.parent_.verticalLayout__.setContentsMargins(0, 0, 0, 0)
            self.parent_.showMaximized()
            self.parent_.pushButton_2.setToolTip(
                "<html><head/><body><p>恢复</p></body></html>")
        return super().mouseDoubleClickEvent(a0)
<<<<<<< HEAD

=======
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    def paintEvent(self, evt):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        # 反锯齿
        painter.setRenderHint(QPainter.Antialiasing)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
################################################################
<<<<<<< HEAD


=======
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=-1, hspacing=-1, vspacing=-1):
        super(FlowLayout, self).__init__(parent)
        self._hspacing = hspacing
        self._vspacing = vspacing
        self._items = []
        self.setContentsMargins(margin, margin, margin, margin)

    def __del__(self):
        del self._items[:]

    def addItem(self, item):
        self._items.append(item)

    def horizontalSpacing(self):
        if self._hspacing >= 0:
            return self._hspacing
        else:
            return self.smartSpacing(
                QStyle.PM_LayoutHorizontalSpacing)

    def verticalSpacing(self):
        if self._vspacing >= 0:
            return self._vspacing
        else:
            return self.smartSpacing(
                QStyle.PM_LayoutVerticalSpacing)

    def count(self):
        return len(self._items)

    def itemAt(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]

    def takeAt(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)

    def expandingDirections(self):
        return QtCore.Qt.Orientations(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.doLayout(QtCore.QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QtCore.QSize()
        for item in self._items:
            size = size.expandedTo(item.minimumSize())
        left, top, right, bottom = self.getContentsMargins()
        size += QtCore.QSize(left + right, top + bottom)
        return size

    def doLayout(self, rect, testonly):
        left, top, right, bottom = self.getContentsMargins()
        effective = rect.adjusted(+left, +top, -right, -bottom)
        x = effective.x()
        y = effective.y()
        lineheight = 0
        for item in self._items:
            widget = item.widget()
            hspace = self.horizontalSpacing()
            if hspace == -1:
                hspace = widget.style().layoutSpacing(
                    QSizePolicy.PushButton,
                    QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            vspace = self.verticalSpacing()
            if vspace == -1:
                vspace = widget.style().layoutSpacing(
                    QSizePolicy.PushButton,
                    QSizePolicy.PushButton, QtCore.Qt.Vertical)
            nextX = x + item.sizeHint().width() + hspace
            if nextX - hspace > effective.right() and lineheight > 0:
                x = effective.x()
                y = y + lineheight + vspace
                nextX = x + item.sizeHint().width() + hspace
                lineheight = 0
            if not testonly:
                item.setGeometry(
                    QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))
            x = nextX
            lineheight = max(lineheight, item.sizeHint().height())
        return y + lineheight - rect.y() + bottom

    def smartSpacing(self, pm):
        parent = self.parent()
        if parent is None:
            return -1
        elif parent.isWidgetType():
            return parent.style().pixelMetric(pm, None, parent)
        else:
            return parent.spacing()
################################################################
<<<<<<< HEAD


class FlowBox(QFrame):
    def __init__(self, name, type, clickButton, size_=[50, 64]):
=======
class FlowBox(QWidget):
    def __init__(self,name,type):
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
        super(FlowBox, self).__init__()
        self.setContentsMargins(5, 5, 5, 5)
        self.type = type
        self.name = name
<<<<<<< HEAD
        self.clickButton = clickButton
        self.size_ = size_
        self.ThisLayout = QVBoxLayout(self)
        self.setMaximumSize(size_[0], size_[1])
        self.setMinimumSize(size_[0], size_[1])
        self.ThisLayout.setContentsMargins(0, 0, 0, 0)
=======
        self.ThisLayout = QVBoxLayout(self)
        self.setMaximumSize(50,64)
        self.setMinimumSize(50,64)
        self.ThisLayout.setContentsMargins(0,0,0,0)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
        self.ThisLayout.setSpacing(0)
        #
        self.setObjectName('baseFlowBox')
        self.setStyleSheet('''
    border: 0px;
    border-radius: 4px;
    margin:0px;
''')
        #
<<<<<<< HEAD
        self.IconLabel = QWidget()  # 图标
        self.IconLabel.setMaximumSize(size_[0]-10, 24)
        self.IconLabel.setMinimumSize(size_[0]-10, 24)
        self.NameLabel = QTextBrowser()  # 名字
        self.NameLabel.setHorizontalScrollBarPolicy(1)
        self.NameLabel.setVerticalScrollBarPolicy(1)
        # self.NameLabel.setAlignment(Qt.AlignCenter)
        # self.NameLabel.setWordWrap(True)
        #
=======
        self.IconLabel = QWidget()#图标
        self.IconLabel.setMaximumSize(40,24)
        self.IconLabel.setMinimumSize(40,24)
        self.NameLabel = QLabel()#名字
        #self.NameLabel.setAlignment(Qt.AlignCenter)
        #self.NameLabel.setWordWrap(True)
        #
        self.NameLabel.setWordWrap(True)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
        self.NameLabel.setAlignment(QtCore.Qt.AlignTop)
        #
        type_ = self.type+'.svg'
        if self.type == 'mcfunction':
            type_ = self.type+'.png'
        if self.name == 'readme':
            type_ = 'readme.svg'
        self.IconLabel.setStyleSheet(f'''
                                     background-image: url(./img/file/icons/{type_});
                                     background-repeat: no-repeat;
                                     background-position: center center;''')
<<<<<<< HEAD
        # self.IconLabel.setScaledContents(True)

        self.NameLabel.setText(self.name)
        self.NameLabel.setMaximumWidth(size_[0]-10)
        self.NameLabel.setMinimumWidth(size_[0]-10)
=======
        #self.IconLabel.setScaledContents(True)
        if len(self.name) > 8:
            self.name = self.name[:8]+'\n'+self.name[8:]
        if len(self.name) > 16:
            self.name = self.name[:16]+'\n'+self.name[16:]
        self.NameLabel.setText(self.name)
        self.NameLabel.setMaximumWidth(40)
        self.NameLabel.setMinimumWidth(40)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
        self.NameLabel.setStyleSheet('''font-family: monospace;
                                     font-size:10px;
                                     ''')
        self.NameLabel.setToolTip(self.name)
<<<<<<< HEAD
        # add
        self.ThisLayout.addWidget(self.IconLabel)
        self.ThisLayout.addWidget(self.NameLabel)

=======
        #add
        self.ThisLayout.addWidget(self.IconLabel)
        self.ThisLayout.addWidget(self.NameLabel)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawRoundedRect(
            0, 0, self.width() - 1, self.height() - 1, 5, 5)
        super(FlowBox, self).paintEvent(event)
<<<<<<< HEAD

    def mousePressEvent(self, evt) -> None:
        self.clickButton(self.name)
################################################################


=======
################################################################
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
class FlowWidget(QScrollArea):
    def __init__(self, parent) -> None:
        super().__init__()
        self.setWidgetResizable(True)
<<<<<<< HEAD
        self.ThisWidget = QFrame(self)
        self.ThisLayout = FlowLayout(self.ThisWidget, hspacing=12, vspacing=12)
        self.setWidget(self.ThisWidget)
        self.setObjectName('AssetWidget')
        # 完成初始化控件部分
=======
        self.ThisWidget = QWidget(self)
        self.ThisLayout = FlowLayout(self.ThisWidget,hspacing=12, vspacing=12)
        self.setWidget(self.ThisWidget)
        self.setObjectName('AssetWidget')
        #完成初始化控件部分
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
        self.setStyleSheet('''
#AssetWidget{
    border-radius: 0px !important;
    border: 1px solid rgba(0, 0, 0, 0.0);
}
<<<<<<< HEAD
=======
#AssetWidget:focus {
    border: 1px solid #4888FF;
}
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
                           ''')
        self.ThisWidget.setObjectName('AssetWidget')

################################################################
<<<<<<< HEAD


class AssetWidget(FlowWidget):
    def __init__(self, parent, path, bottom, changefile, pathWidget, filetype='*', size_=[50, 64]) -> None:
=======
class AssetWidget(FlowWidget):
    def __init__(self, parent,path,bottom) -> None:
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
        super().__init__(parent)
        self.path = path
        self.parent = parent
        self.FileList = []
<<<<<<< HEAD
        self.pathWidget = pathWidget
        self.DirList = []
        self.AllList = []
        self.size_ = size_
        self.fileCount = []
        self.filetype = filetype
        self.DirCount = []
        self.bottom = bottom
        self.setRootPath(self.path)
        self.changefile = changefile

    def deleteLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.parent.deleteLayout(item.layout())

    def setRootPath(self, path):
        # 更换目录用的
        self.path = path
        print('AssetWidget.Path ->', path)
        #
        item_list = list(
            range(self.ThisLayout.count()))
        item_list.reverse()  # 倒序删除，避免影响布局顺序
        for i in item_list:
            item = self.ThisLayout.itemAt(i)
            self.ThisLayout.removeItem(item)
            item.widget().deleteLater()
            if item.widget():
                item.widget().deleteLater()
        #
        self.deleteLayout(self.ThisLayout)
        self.ThisLayout.update()
        self.FileList = []
        self.DirList = []
        self.fileCount = []
        self.DirCount = []
        get_file_path(self.path, self.FileList, self.DirList)
        get_ALL_file_count(self.path, self.fileCount, self.DirCount)
        self.AllList = self.FileList + self.DirList
        # rewrite_print(self.FileList,self.DirList,self.AllList)
        self.bottom.setText(
            f'文件夹数:{str(len(self.fileCount))} | 文件数:{str(len(self.DirCount))}')
        self.update()  # 读取目录并更换完后，进行重新绘制

    def click(self, name):
        for dir in self.DirList:
            if dir.split('\\')[-1] == name:
                self.path = self.path + '/' + name
                self.setRootPath(self.path)
                self.changefile(self.path, 'path')
                self.pathWidget.setRootPath(self.path)
                return
        for file in self.FileList:
            if file.split('\\')[-1] == name:
                self.changefile(file, 'file')

    def update(self):
        # 重新渲染界面用的
        if self.filetype == '*':
            for item in self.AllList:
                name = item.split('\\')[-1]
                if name[0] == '.':
                    self.ThisLayout.addWidget(
                        FlowBox(name, 'folder-base', self.click, self.size_))
                    # self.ThisLayout.addWidget(Bubble(name))
                elif len(name.split('.')) == 1:
                    self.ThisLayout.addWidget(
                        FlowBox(name, 'folder-base', self.click, self.size_))
                    # self.ThisLayout.addWidget(Bubble(name))
                elif len(name.split('.')) == 2:
                    self.ThisLayout.addWidget(
                        FlowBox(name, name.split('.')[-1], self.click, self.size_))
                    # self.ThisLayout.addWidget(Bubble(name))
                # self.ThisLayout.addWidget(FlowBox())

        else:
            for item in self.AllList:
                name = item.split('\\')[-1]
                file_type_this = item.split('\\')[-1].split('.')[-1]
                if file_type_this == self.filetype:
                    self.ThisLayout.addWidget(
                        FlowBox(name, name.split('.')[-1], self.click, self.size_))
                    # self.ThisLayout.addWidget(Bubble(name))
                # self.ThisLayout.addWidget(FlowBox())

        pass
################################################################


=======
        self.DirList = []
        self.AllList = []
        self.fileCount = []
        self.DirCount = []
        self.bottom = bottom
        self.setRootPath(self.path)
    def setRootPath(self,path):
        #更换目录用的
        self.path = path
        get_file_path(self.path,self.FileList,self.DirList)
        get_ALL_file_count(self.path,self.fileCount,self.DirCount)
        self.AllList = self.FileList + self.DirList
        #rewrite_print(self.FileList,self.DirList,self.AllList)
        self.bottom.setText(f'文件夹数:{str(len(self.fileCount))} | 文件数:{str(len(self.DirCount))}')
        self.update()#读取目录并更换完后，进行重新绘制
        
    def update(self):
        #重新渲染界面用的
        for item in self.AllList:
            name = item.split('\\')[-1]
            if name[0] == '.':
                self.ThisLayout.addWidget(FlowBox(name,'folder-base'))
                #self.ThisLayout.addWidget(Bubble(name))
            elif len(name.split('.')) == 1:
                self.ThisLayout.addWidget(FlowBox(name,'folder-base'))
                #self.ThisLayout.addWidget(Bubble(name))
            elif len(name.split('.')) == 2:
                self.ThisLayout.addWidget(FlowBox(name,name.split('.')[-1]))
                #self.ThisLayout.addWidget(Bubble(name))
            #self.ThisLayout.addWidget(FlowBox())
        pass
################################################################
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
class Bubble(QLabel):
    def __init__(self, text):
        super(Bubble, self).__init__(text)
        self.word = text
        self.setContentsMargins(5, 5, 5, 5)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawRoundedRect(
            0, 0, self.width() - 1, self.height() - 1, 5, 5)
        super(Bubble, self).paintEvent(event)
################################################################
<<<<<<< HEAD


def get_file_path(root_path, file_list, dir_list):
    # 获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        # 获取目录或者文件的路径
        dir_file_path = os.path.join(root_path, dir_file)
        # 判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            # 递归获取所有文件和目录的路径
            # get_file_path(dir_file_path,file_list,dir_list)
        else:
            file_list.append(dir_file_path)


def get_ALL_file_count(root_path, file_list_count, dir_list_count):
    # 获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        # 获取目录或者文件的路径
        dir_file_path = os.path.join(root_path, dir_file)
        # 判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list_count.append(dir_file_path)
            # 递归获取所有文件和目录的路径
            get_ALL_file_count(dir_file_path, file_list_count, dir_list_count)
        else:
            file_list_count.append(dir_file_path)
################################################################


class PpathWidget(QScrollArea):
    def __init__(self, path, change_function):
        super().__init__()
        self.initUI()
        self.PathList = []
        self.path = path
        self.setRootPath(path)
        self.change_function = change_function

=======
def get_file_path(root_path,file_list,dir_list):
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            #递归获取所有文件和目录的路径
            #get_file_path(dir_file_path,file_list,dir_list)
        else:
            file_list.append(dir_file_path)
def get_ALL_file_count(root_path,file_list_count,dir_list_count):
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list_count.append(dir_file_path)
            #递归获取所有文件和目录的路径
            get_ALL_file_count(dir_file_path,file_list_count,dir_list_count)
        else:
            file_list_count.append(dir_file_path)
################################################################
class PpathWidget(QScrollArea):
    def __init__(self,path):
        super().__init__()
        self.initUI()
        self.path = path
        self.setRootPath(path)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    def initUI(self):
        self.ThisWidget = QWidget(self)
        self.setWidgetResizable(True)
        self.ThisLayout = QHBoxLayout(self.ThisWidget)
        self.setWidget(self.ThisWidget)
<<<<<<< HEAD
        self.ThisLayout.setContentsMargins(2, 0, 0, 0)
        self.setMaximumHeight(35)
        self.setMinimumHeight(35)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setObjectName('pathWidget')

    def setRootPath(self, path):
        self.PathList = []
        self.RootPath = path
        self.path = path
        item_list = list(
            range(self.ThisLayout.count()))
        item_list.reverse()  # 倒序删除，避免影响布局顺序
        for i in item_list:
            item = self.ThisLayout.itemAt(i)
            self.ThisLayout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()
        # rewrite_print(path)
        for Item in self.path.split('/'):
            ThisButton = QPushButton()
            ThisButton.setIcon(QIcon('./img/icons/folder.svg'))
            ThisButton.setText(Item)
            ThisButton.clicked.connect(self.change)
            RIGHT_label = QLabel()
            RIGHT_label.setText('>')
            self.ThisLayout.addWidget(ThisButton)
            self.ThisLayout.addWidget(RIGHT_label)
            self.PathList.append(Item)
        self.ThisLayout.addWidget(QWidget())
        self.ThisLayout.addStretch(999)

    def getPath(self):
        return self.RootPath

    def change(self):
        thisSender = self.sender().text()
        index = self.PathList.index(thisSender)
        newList = self.PathList[0:index]+[thisSender]
        self.PathList = newList
        # del
        self.path = '/'.join(newList)
        self.setRootPath(self.path)
        self.change_function(self.path)
########################################################################


def analysis(bin_path: str) -> str:
    with open(bin_path, 'rb') as f:
        # 读取全部行
        all_data = f.readlines()
        outStr = ''
        for i in all_data:
            # 二进制（bytes）类型转换成十六进制类型
            hex_str = binascii.b2a_hex(i).decode('unicode_escape')
            # 以str格式逐行写入到文本
            outStr = outStr + str(hex_str) + '\n'
    return outStr


key_map = {
    "0": 0x30, "1": 0x31, "2": 0x32, "3": 0x33, "4": 0x34, "5": 0x35, "6": 0x36, "7": 0x37, "8": 0x38, "9": 0x39,
    'F1': 112, 'F2': 113, 'F3': 114, 'F4': 115, 'F5': 116, 'F6': 117, 'F7': 118, 'F8': 119,
    'F9': 120, 'F10': 121, 'F11': 122, 'F12': 123, 'F13': 124, 'F14': 125, 'F15': 126, 'F16': 127,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90,
    'BACKSPACE': 8, 'TAB': 9, 'TABLE': 9, 'CLEAR': 12,
    'ENTER': 13, 'SHIFT': 16, 'CTRL': 17,
    'CONTROL': 17, 'ALT': 18, 'ALTER': 18, 'PAUSE': 19, 'BREAK': 19, 'CAPSLK': 20, 'CAPSLOCK': 20, 'ESC': 27,
    ' ': 32, 'SPACEBAR': 32, 'PGUP': 33, 'PAGEUP': 33, 'PGDN': 34, 'PAGEDOWN': 34, 'END': 35, 'HOME': 36,
    'LEFT': 37, 'UP': 38, 'RIGHT': 39, 'DOWN': 40, 'SELECT': 41, 'PRTSC': 42, 'PRINTSCREEN': 42, 'SYSRQ': 42,
    'SYSTEMREQUEST': 42, 'EXECUTE': 43, 'SNAPSHOT': 44, 'INSERT': 45, 'DELETE': 46, 'HELP': 47, 'WIN': 91,
    'WINDOWS': 91, 'NMLK': 144,
    '.': 0xBE,
    'NUMLK': 144, 'NUMLOCK': 144, 'SCRLK': 145,
    '[': 219, ']': 221, '+': 107, '-': 109}
=======
        self.ThisLayout.setContentsMargins(2,0,0,0)
        self.setMaximumHeight(25)
        self.setMinimumHeight(25)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setObjectName('pathWidget')
        
    def setRootPath(self,path):
        self.RootPath = path
        self.path = path
        #rewrite_print(path)
        for Item in self.path.split('/'):
            ThisButton = QPushButton()
            ThisButton.setObjectName('PpathWidgetButton')
            ThisButton.setIcon(QIcon('./img/icons/folder.svg'))
            ThisButton.setText(Item + ' >')
            self.ThisLayout.addWidget(ThisButton)
        self.ThisLayout.addWidget(QWidget())
        self.ThisLayout.addStretch(999)
########################################################################

>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
