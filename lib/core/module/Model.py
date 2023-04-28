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
#model需要opengl的功能，不使用qt3d
from lib.base import *
from lib.core.opengl.Optimizermaster.FileHandler import FileHandler
from lib.core.opengl.PpyGl import *
#import base functions
from lib.base import *
#end
#不知道为什么，qt系列的3d功能好混乱，而且教程很少
SELF = None
def init(parent: QVBoxLayout, Name, self):
    global SELF
    globals()['SELF'] = self
    SELF = self
    # 可以统一不用定义在self下
    ThisWidget = QWidget()
    ThisWidget.setStyleSheet('border:0px;')
    parent.addWidget(ThisWidget)
    self.ModelToptabs = QTabWidget()
    self.ModelToptabs.TabShape(1)
    self.ModelToptabs.setObjectName('ModelEditor')
    self.ModelToptabs.setStyleSheet('''
QTabBar::tab {
    padding-left: 5px;
    border-right: 1px solid #ccc;
    background-color: rgba(0,0,0,0);
    padding-right:0px;
    padding-top:4px;
    border-left: 0px;
}
QTabBar::tab:selected {
    border-top: 2px solid #4888ff !important;
    background-color: #eee;
    padding-left: 5px;
    padding-right:0px;
    border-right: 1px solid #ccc;
    border-bottom: 0px;
}
QTabBar::tab:!selected{
    
}
QTabBar::tab:first {
    border-left: 0px !important;
}
#ModelEditor {
    background-color: #eee;
    padding: 0px;
    border: 0px !important;
}
QTabBar::tab-bar{
    background-color: #ddd;
}
QTabWidget::pane{
	border:none;
    border-top: 1px solid #e5e5e5;
}
QTabWidget {
    border: 0px;
    border-top: 1px solid #e5e5e5;
}
''')
    # tabs.setTabPosition(QTabWidget.West)
    self.ModelToptabs.setMovable(True)
    self.ModelToptabs.setTabsClosable(True)
    self.ModelToptabs.setContentsMargins(0, 0, 0, 0)
    ThisWidget_layout = QVBoxLayout()
    ThisWidget.setLayout(ThisWidget_layout)
    ThisWidget_layout.addWidget(self.ModelToptabs)
    ThisWidget_layout.setContentsMargins(0, 0, 0, 0)
    # test
    AddModelEditor(self, 'newModel', 'newNBT')

    # AddModelEditor(self,'Model','openNBT')
ModelFile = {'newNBT': './img/icons/box.svg',
             'openNBT': './img/icons/codesandbox.svg',
             'newJson': '', 
             'openJson': ''}
model = []
def AddModelEditor(self, Name, mode):
    globals()[Name+"_Widget"+str(self.index)] = World()
    self.ModelToptabs.addTab(
        globals()[Name+"_Widget"+str(self.index)], QIcon(ModelFile[mode]), Name+'.nbt')
    self.ModelToptabs.currentChanged.connect(ClickTextEditor)
    self.index = self.index + 1
    #
def ClickTextEditor():
    pass
def getfile():
    dlg=QtWidgets.QFileDialog()
    f=dlg.getOpenFileName(SELF,'Open File','.','STL File (*.stl)')
    file=FileHandler().load_mesh(f[0])#f[0]是路径，f[1]是类型
    data=array(file['mesh'],'f')
    print(data)
    model.append({'material':Materials[0],'data':data})
    ThisWorld = SELF.ModelToptabs.currentWidget().widget()
    print(ThisWorld)
    '''SELF.qlistwidget.addItem(f[0].split('/')[-1].split('.')[0])
    SELF.qlistwidget.setCurrentItem(SELF.qlistwidget.item(0))
    SELF.opengl_widget.initdata(model)
    #print(data)
    SELF.opengl_widget.update()'''