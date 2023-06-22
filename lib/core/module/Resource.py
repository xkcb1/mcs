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
from lib.fileTreeView import CreateFileTree
# end
# 从designer生成的模板


def setupUi(self, Frame):
    self.Projectfiles = 0
    self.Projectfolders = 0
    self.verticalLayout_2 = QVBoxLayout(Frame)
    self.verticalLayout_2.setContentsMargins(1, 0, 1, 0)
    self.verticalLayout_2.setSpacing(0)
    self.widget_ = QWidget(Frame)

    # struct Resource
    OpenButton = QPushButton()

    OpenButton.setIcon(QIcon('./img/icons/folder-plus.svg'))
    OpenButton.setMaximumWidth(52)
    # new
    self.FileStructure = QComboBox()
    self.FileStructure.setView(QListView())

    # layout _1
    self.FileStructure_layout = QHBoxLayout()
    self.FileStructure_layout.addWidget(OpenButton)
    self.FileStructure_layout.addWidget(self.FileStructure)
    #
    self.setting = readConfig()
    self.path = self.setting['path']
    self.pathList = [self.setting['name']]
    GetDir(self, self.path+'/'+self.setting['name'], 1)
    self.FileStructure.addItems(self.pathList)
    #
    self.horizontalLayout_ = QHBoxLayout(self.widget_)
    self.horizontalLayout_.setContentsMargins(0, 2, 0, 0)
    self.horizontalLayout_.setSpacing(2)
    self.pushButton = QPushButton(self.widget_)
    self.pushButton.setIcon(QIcon('./img/icons/chevron-left.svg'))

    self.horizontalLayout_.addWidget(self.pushButton)
    self.pushButton_2 = QPushButton(self.widget_)

    self.pushButton_2.setIcon(QIcon('./img/icons/chevron-right.svg'))
    self.horizontalLayout_.addWidget(self.pushButton_2)
    self.lineEdit = QLineEdit(self.widget_)

    self.lineEdit.setText(self.setting['path'])
    self.horizontalLayout_.addWidget(self.lineEdit)
    self.verticalLayout_2.addWidget(self.widget_)
    self.verticalLayout_ = QVBoxLayout()
    self.verticalLayout_.setSpacing(0)
    # filetree
    self.fileTreeView = CreateFileTree(self)

    self.fileTreeView.setObjectName('fileTreeView')
    self.fileTreeView.setAcceptDrops(False)
    self.fileTreeView.setEditTriggers(
        QtWidgets.QAbstractItemView.NoEditTriggers)
    # self.fileTreeView.setResizeMode(QtWidgets.QListView.Adjust)
    self.fileTreeView.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
    self.fileTreeView.setAnimated(True)
    # bottom info panel
    bottomInfoPanel = QLabel(
        f"项目名:{self.setting['name']} | 文件夹数:{self.Projectfolders} | 文件数:{self.Projectfiles}")

    #
    self.verticalLayout_.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout_.addLayout(self.FileStructure_layout)
    self.verticalLayout_.addWidget(self.fileTreeView)
    self.verticalLayout_.addWidget(bottomInfoPanel)
    self.verticalLayout_2.addLayout(self.verticalLayout_)


def init(parent, Name, self):
    globals()['SELF'] = self
    print("init ->", Name)  # 输出调试
    # 正式开始实现
    # 布局
    InFrameWidget = QWidget()
    parent.addWidget(InFrameWidget)
    # 导入现在的布局
    setupUi(self, InFrameWidget)


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
