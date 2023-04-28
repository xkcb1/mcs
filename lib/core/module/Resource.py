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
from lib.fileTreeView import CreateFileTree
#end
#从designer生成的模板
def setupUi(self, Frame):
    self.Projectfiles = 0
    self.Projectfolders = 0
    self.verticalLayout_2 = QtWidgets.QVBoxLayout(Frame)
    self.verticalLayout_2.setContentsMargins(1, 0, 1, 0)
    self.verticalLayout_2.setSpacing(0)
    self.widget_ = QtWidgets.QWidget(Frame)
    self.widget_.setObjectName("Resource_widget")
    self.widget_.setMaximumSize(QtCore.QSize(16777215, 25))
    self.widget_.setMinimumHeight(25)
    #struct Resource
    OpenButton = QPushButton()
    OpenButton.setObjectName('OpenButton_Resource')
    OpenButton.setMinimumWidth(18)
    OpenButton.setMaximumWidth(18)
    OpenButton.setMinimumHeight(25)
    OpenButton.setIcon(QIcon('./img/icons/folder-plus.svg'))
    #new
    self.FileStructure = QComboBox()
    self.FileStructure.setView(QListView())
    self.FileStructure.setMaximumHeight(25)
    self.FileStructure.setMinimumHeight(25)
    self.FileStructure.setObjectName('ChooseList')
    #layout _1 
    self.FileStructure_layout = QHBoxLayout()
    self.FileStructure_layout.addWidget(OpenButton)
    self.FileStructure_layout.addWidget(self.FileStructure)
    #
    self.setting = readConfig()
    self.path = self.setting['path']
    self.pathList = [self.setting['name']]
    GetDir(self,self.path+'/'+self.setting['name'],1)
    self.FileStructure.addItems(self.pathList)
    #
    self.horizontalLayout_ = QtWidgets.QHBoxLayout(self.widget_)
    self.horizontalLayout_.setContentsMargins(0, 2, 0, 0)
    self.horizontalLayout_.setSpacing(2)
    self.pushButton = QPushButton(self.widget_)
    self.pushButton.setIcon(QIcon('./img/icons/corner-up-left.svg'))
    self.pushButton.setObjectName("pb_1")
    self.pushButton.setMaximumSize(QtCore.QSize(18, 18))
    self.horizontalLayout_.addWidget(self.pushButton)
    self.pushButton_2 = QtWidgets.QPushButton(self.widget_)
    self.pushButton_2.setMaximumSize(QtCore.QSize(18, 18))
    self.pushButton_2.setObjectName("pb_2")
    self.pushButton_2.setIcon(QIcon('./img/icons/corner-up-right.svg'))
    self.horizontalLayout_.addWidget(self.pushButton_2)
    self.lineEdit = QtWidgets.QLineEdit(self.widget_)
    self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 18))
    self.lineEdit.setObjectName("lineEdit")
    self.lineEdit.setText(self.setting['path'])
    self.horizontalLayout_.addWidget(self.lineEdit)
    self.verticalLayout_2.addWidget(self.widget_)
    self.verticalLayout_ = QtWidgets.QVBoxLayout()
    self.verticalLayout_.setSpacing(0)
    #filetree
    self.fileTreeView = CreateFileTree(self)
    styleFile = './style/module/fileTreeView.qss'
    qssStyle_FileTreeView = StyleReader.readQSS(styleFile)
    self.fileTreeView.setStyleSheet(qssStyle_FileTreeView)
    self.fileTreeView.setObjectName('fileTreeView')
    self.fileTreeView.setAnimated(True)
    #bottom info panel
    bottomInfoPanel = QLabel(f"项目名:{self.setting['name']} | 文件夹数:{self.Projectfolders} | 文件数:{self.Projectfiles}")
    bottomInfoPanel.setMaximumHeight(20)
    bottomInfoPanel.setMinimumHeight(20)
    bottomInfoPanel.setObjectName("bottomInfoPanel_Resource")
    bottomInfoPanel.setStyleSheet('''border:0px;background-color: #f9f9f9;color:#aaa;border-top:1px solid #e5e5e5;
                                  border-bottom-left-radius:7px;border-bottom-right-radius:7px;''')
    #
    self.verticalLayout_.setContentsMargins(0,0,0,0)
    self.verticalLayout_.addLayout(self.FileStructure_layout)
    self.verticalLayout_.addWidget(self.fileTreeView)
    self.verticalLayout_.addWidget(bottomInfoPanel)
    self.verticalLayout_2.addLayout(self.verticalLayout_)
def init(parent,Name,self):
    globals()['SELF'] = self
    print("init ->",Name)#输出调试
    #正式开始实现
    #布局
    InFrameWidget = QWidget()
    parent.addWidget(InFrameWidget)
    #导入现在的布局
    setupUi(self,InFrameWidget)
    #基础控件部分
'''def CreateFileTree(self):
    #filetreeview
    self.model = QFileSystemModel()
    self.model.setRootPath(readConfig()['path']+'/'+readConfig()['name'])
    self.fileTreeView = QTreeView()
    self.fileTreeView.setModel(self.model)
    self.fileTreeView.setAnimated(False)
    self.fileTreeView.setIndentation(20)
    self.fileTreeView.setRootIndex(self.model.index(readConfig()['path']+'/'+readConfig()['name']))
    self.fileTreeView.setSortingEnabled(True)
    for i in [1,2,3]:
        self.fileTreeView.setColumnHidden(i, True)
    return self.fileTreeView
    pass'''
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