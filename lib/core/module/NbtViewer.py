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
bottomWidget = None
treeView = None
SELF = None
#end
def onTreeClicked(index):
    global bottomWidget,treeView,SELF
    item = treeView.currentItem()
    bottomWidget.setText("key=%s, value=%s"%(item.text(0), item.text(1)))
def init(parent,Name,self):
    global bottomWidget,treeView,SELF
    SELF = self
    globals()['SELF'] = self
    ThisWidget = QWidget()
    parent.addWidget(ThisWidget)
    ThisLayout = QVBoxLayout(ThisWidget)
    ThisLayout.setContentsMargins(0,0,0,0)
    ThisLayout.setSpacing(0)
    ThisWidget.setLayout(ThisLayout)
    #
    TopWidget = QWidget()
    TopWidget.setMaximumHeight(25)
    TopWidget.setMinimumHeight(25)
    ThisLayout.addWidget(TopWidget)
    ThisTopLayout = QHBoxLayout(TopWidget)
    ThisTopLayout.setContentsMargins(0,0,0,0)
    ThisTopLayout.setSpacing(0)
    OpenButton = QPushButton()
    OpenButton.setStyleSheet('''background-image: url(./img/icons/file-plus.svg);
    background-repeat: no-repeat;
    background-position: center right;
    border:1px solid #e5e5e5;''')#file-plus.svg
    OpenButton.setMinimumSize(25,25)
    OpenButton.clicked.connect(OpenNbtFile)
    SearchInput = QLineEdit()
    SearchInput.setMaximumHeight(25)
    SearchInput.setMinimumHeight(25)
    SearchInput.setPlaceholderText('输入标签名来搜索')
    SearchInput.setObjectName('SearchPathWidget')
    ThisTopLayout.addWidget(OpenButton)
    ThisTopLayout.addWidget(SearchInput)
    #
    treeView = QTreeWidget()
    treeView.setObjectName('thisTreeView')
    treeView.clicked.connect(onTreeClicked)
    treeView.setStyleSheet('''
#thisTreeView{
    border: 0px !important;
    border-radius: 0px !important;
}
#thisTreeView:focus{
    border: 1px solid #4888FF;
}''')
    ThisLayout.addWidget(treeView)
    #
    bottomWidget = QLabel()
    bottomWidget.setMaximumHeight(20)
    bottomWidget.setMinimumHeight(20)
    ThisLayout.addWidget(bottomWidget)
    bottomWidget.setStyleSheet('border:0px;border-top:1px solid #e5e5e5;')
    treeView.setColumnCount(2)
    treeView.setHeaderLabels(['Key','Value'])
    #treeView.setStyle(QStyleFactory.create('windows'))
    #treeView.selectionModel().currentChanged.connect(onCurrentChanged)
def OpenNbtFile():
    global bottomWidget,treeView,SELF
    filepath = QFileDialog.getOpenFileName(SELF, "选择文件")
    print_('openNbtfile:',filepath)
    print('openNbtfile:',filepath)
    SELF.makeTreethread = NbtTrewwThread(filepath[0],treeView)
    SELF.makeTreethread.start()
    #MakeHexEditorStart()