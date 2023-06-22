<<<<<<< HEAD
# 每个module要求实现一个init(parent,Name,self)函数，来获取此次初始化
import os
import sys
=======
#每个module要求实现一个init(parent,Name,self)函数，来获取此次初始化
import os,sys
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import *
from lib.readConfig import readConfig
from lib.StyleReader import StyleReader
<<<<<<< HEAD
# import base functions
from lib.base import *
# end
################################################################################################


def init(parent, Name, self):
=======
#import base functions
from lib.base import *
#end
################################################################################################
def init(parent,Name,self):
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    globals()['SELF'] = self
    ThisWidget = QWidget()
    parent.addWidget(ThisWidget)
    ThisLayout = QVBoxLayout(ThisWidget)
<<<<<<< HEAD
    ThisLayout.setContentsMargins(0, 0, 0, 0)
    ThisLayout.setSpacing(0)
    def change_path(path):
        AssetMainWidget.setRootPath(path)
    PathWidget = PpathWidget(
        readConfig()['path']+'/'+readConfig()['name'], change_path)
=======
    ThisLayout.setContentsMargins(0,0,0,0)
    ThisLayout.setSpacing(0)
    PathWidget = PpathWidget(readConfig()['path']+'/'+readConfig()['name'])
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    ################################################################
    SearchWidget = QWidget()
    SearchWidget.setMaximumHeight(25)
    SearchWidget.setMinimumHeight(25)
    SearchInput = QLineEdit()
    SearchInput.setMaximumHeight(25)
    SearchInput.setMinimumHeight(25)
    SearchInput.setPlaceholderText('输入文件名或文件后缀名来搜索')
    SearchInput.setObjectName('SearchPathWidget')
    FileStructure = QComboBox()
    FileStructure.setView(QListView())
    FileStructure.setMaximumHeight(25)
    FileStructure.setMinimumHeight(25)
    FileStructure.setObjectName('ChooseList')
<<<<<<< HEAD
    # layout _1
    FileStructure_layout = QHBoxLayout(SearchWidget)
    FileStructure_layout.addWidget(SearchInput)
    FileStructure_layout.addWidget(FileStructure)
    FileStructure_layout.setContentsMargins(0, 0, 0, 0)
=======
    #layout _1 
    FileStructure_layout = QHBoxLayout(SearchWidget)
    FileStructure_layout.addWidget(SearchInput)
    FileStructure_layout.addWidget(FileStructure)
    FileStructure_layout.setContentsMargins(0,0,0,0)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    FileStructure_layout.setSpacing(0)
    #
    setting = readConfig()
    path = setting['path']
    self.Projectfolders = 0
    self.Projectfiles = 0
    self.pathList = [setting['name']]
<<<<<<< HEAD
    GetDir(self, path+'/'+setting['name'], 1)
=======
    GetDir(self,path+'/'+setting['name'],1)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    FileStructure.addItems(self.pathList)
    ################################################################
    BottomWidget = QLabel()
    BottomWidget.setMaximumHeight(20)
    BottomWidget.setMinimumHeight(20)
<<<<<<< HEAD
    BottomWidget.setStyleSheet(
        'border:0px;border-top:1px solid '+self.theme+';')
    PathWidget.setStyleSheet(
        '#pathWidget{border:0px;border-top:1px solid '+self.theme+';}')
    # BottomWidget.setObjectName('bottomInfoPanel_Resource')
    AssetMainWidget = AssetWidget(
        self, readConfig()['path']+'/'+readConfig()['name'], BottomWidget,print,PathWidget)
=======
    BottomWidget.setStyleSheet('border:0px;border-top:1px solid #e5e5e5;')
    PathWidget.setStyleSheet('#pathWidget{border:0px;border-top:1px solid #e5e5e5;}')
    #BottomWidget.setObjectName('bottomInfoPanel_Resource')
    AssetMainWidget = AssetWidget(self,readConfig()['path']+'/'+readConfig()['name'],BottomWidget)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    ThisLayout.addWidget(PathWidget)
    ThisLayout.addWidget(SearchWidget)
    ThisLayout.addWidget(AssetMainWidget)
    ThisLayout.addWidget(BottomWidget)
<<<<<<< HEAD
=======

    
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
