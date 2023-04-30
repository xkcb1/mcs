#每个module要求实现一个init(parent,Name,self)函数，来获取此次初始化
import os,sys
import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import *
from lib.readConfig import readConfig
from lib.StyleReader import StyleReader
#import base functions
from lib.base import *
#end
################################################################################################
def init(parent,Name,self):
    globals()['SELF'] = self
    ThisWidget = QWidget()
    parent.addWidget(ThisWidget)
    ThisLayout = QVBoxLayout(ThisWidget)
    ThisLayout.setContentsMargins(0,0,0,0)
    ThisLayout.setSpacing(0)
    PathWidget = PpathWidget(readConfig()['path']+'/'+readConfig()['name'])
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
    #layout _1 
    FileStructure_layout = QHBoxLayout(SearchWidget)
    FileStructure_layout.addWidget(SearchInput)
    FileStructure_layout.addWidget(FileStructure)
    FileStructure_layout.setContentsMargins(0,0,0,0)
    FileStructure_layout.setSpacing(0)
    #
    setting = readConfig()
    path = setting['path']
    self.Projectfolders = 0
    self.Projectfiles = 0
    self.pathList = [setting['name']]
    GetDir(self,path+'/'+setting['name'],1)
    FileStructure.addItems(self.pathList)
    ################################################################
    BottomWidget = QLabel()
    BottomWidget.setMaximumHeight(20)
    BottomWidget.setMinimumHeight(20)
    BottomWidget.setStyleSheet('border:0px;border-top:1px solid #e5e5e5;')
    PathWidget.setStyleSheet('#pathWidget{border:0px;border-top:1px solid #e5e5e5;}')
    #BottomWidget.setObjectName('bottomInfoPanel_Resource')
    AssetMainWidget = AssetWidget(self,readConfig()['path']+'/'+readConfig()['name'],BottomWidget)
    ThisLayout.addWidget(PathWidget)
    ThisLayout.addWidget(SearchWidget)
    ThisLayout.addWidget(AssetMainWidget)
    ThisLayout.addWidget(BottomWidget)

    