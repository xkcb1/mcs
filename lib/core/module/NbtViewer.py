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
bottomWidget = None
SELF = None
# end


'''def onTreeClicked(index):
    print_(SELF.sender(), index)
    global bottomWidget, treeView, SELF
    for treeView in SELF.TREE_VIEW:
        item = treeView.currentItem()
        bottomWidget.setText("key=%s, value=%s" % (item.text(0), item.text(1)))
'''


def PUBLIC_OpenNbtFile(filepath=None):
    global bottomWidget, SELF
    if (filepath == None) or (type(filepath) == type(True)):
        filepath = QFileDialog.getOpenFileName(SELF, "选择文件")
    if filepath[0] != '':
        print_('openNbtfile:', filepath)
        print('openNbtfile:', filepath)
        for treeView in SELF.TREE_VIEW:
            name = 'newThread_'+str(SELF.thread_count)
            globals()[name
                      ] = NbtTrewwThread(filepath[0], treeView)
            exec(name +
                 '.finished.connect('+name+'.deleteLater)')
            exec(name + '.start()')
            SELF.thread_count += 1
        # MakeHexEditorStart()
        fileName = filepath[0].split('/')[-1]
        SELF.PUBLIC_update(filepath[0], fileName)
        gc.collect()


def init(parent, Name, self):
    global bottomWidget, treeView, SELF
=======
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
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    SELF = self
    globals()['SELF'] = self
    ThisWidget = QWidget()
    parent.addWidget(ThisWidget)
    ThisLayout = QVBoxLayout(ThisWidget)
<<<<<<< HEAD
    ThisLayout.setContentsMargins(0, 0, 0, 0)
=======
    ThisLayout.setContentsMargins(0,0,0,0)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    ThisLayout.setSpacing(0)
    ThisWidget.setLayout(ThisLayout)
    #
    TopWidget = QWidget()
    TopWidget.setMaximumHeight(25)
    TopWidget.setMinimumHeight(25)
    ThisLayout.addWidget(TopWidget)
    ThisTopLayout = QHBoxLayout(TopWidget)
<<<<<<< HEAD
    ThisTopLayout.setContentsMargins(0, 0, 0, 0)
    ThisTopLayout.setSpacing(0)
    OpenButton = QPushButton()
    OpenButton.setStyleSheet(f'''background-image: url(./img/icons/file-plus.svg);
    background-repeat: no-repeat;
    background-position: center right;
    border:1px solid {self.theme};''')  # file-plus.svg
    OpenButton.setMinimumSize(25, 25)
    OpenButton.clicked.connect(PUBLIC_OpenNbtFile)
=======
    ThisTopLayout.setContentsMargins(0,0,0,0)
    ThisTopLayout.setSpacing(0)
    OpenButton = QPushButton()
    OpenButton.setStyleSheet('''background-image: url(./img/icons/file-plus.svg);
    background-repeat: no-repeat;
    background-position: center right;
    border:1px solid #e5e5e5;''')#file-plus.svg
    OpenButton.setMinimumSize(25,25)
    OpenButton.clicked.connect(OpenNbtFile)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
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
<<<<<<< HEAD
    self.TREE_VIEW.append(treeView)
    # treeView.clicked.connect(onTreeClicked)
=======
    treeView.clicked.connect(onTreeClicked)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    treeView.setStyleSheet('''
#thisTreeView{
    border: 0px !important;
    border-radius: 0px !important;
<<<<<<< HEAD
=======
}
#thisTreeView:focus{
    border: 1px solid #4888FF;
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
}''')
    ThisLayout.addWidget(treeView)
    #
    bottomWidget = QLabel()
    bottomWidget.setMaximumHeight(20)
    bottomWidget.setMinimumHeight(20)
    ThisLayout.addWidget(bottomWidget)
<<<<<<< HEAD
    bottomWidget.setStyleSheet(
        'border:0px;border-top:1px solid '+self.theme+';')
    treeView.setColumnCount(2)
    treeView.setHeaderLabels(['Key', 'Value'])
    # treeView.setStyle(QStyleFactory.create('windows'))
    # treeView.selectionModel().currentChanged.connect(onCurrentChanged)
    self.PUBLIC_OpenNbtFile = PUBLIC_OpenNbtFile
=======
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
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
