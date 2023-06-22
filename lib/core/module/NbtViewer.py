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
    SELF = self
    globals()['SELF'] = self
    ThisWidget = QWidget()
    parent.addWidget(ThisWidget)
    ThisLayout = QVBoxLayout(ThisWidget)
    ThisLayout.setContentsMargins(0, 0, 0, 0)
    ThisLayout.setSpacing(0)
    ThisWidget.setLayout(ThisLayout)
    #
    TopWidget = QWidget()
    TopWidget.setMaximumHeight(25)
    TopWidget.setMinimumHeight(25)
    ThisLayout.addWidget(TopWidget)
    ThisTopLayout = QHBoxLayout(TopWidget)
    ThisTopLayout.setContentsMargins(0, 0, 0, 0)
    ThisTopLayout.setSpacing(0)
    OpenButton = QPushButton()
    OpenButton.setStyleSheet(f'''background-image: url(./img/icons/file-plus.svg);
    background-repeat: no-repeat;
    background-position: center right;
    border:1px solid {self.theme};''')  # file-plus.svg
    OpenButton.setMinimumSize(25, 25)
    OpenButton.clicked.connect(PUBLIC_OpenNbtFile)
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
    self.TREE_VIEW.append(treeView)
    # treeView.clicked.connect(onTreeClicked)
    treeView.setStyleSheet('''
#thisTreeView{
    border: 0px !important;
    border-radius: 0px !important;
}''')
    ThisLayout.addWidget(treeView)
    #
    bottomWidget = QLabel()
    bottomWidget.setMaximumHeight(20)
    bottomWidget.setMinimumHeight(20)
    ThisLayout.addWidget(bottomWidget)
    bottomWidget.setStyleSheet(
        'border:0px;border-top:1px solid '+self.theme+';')
    treeView.setColumnCount(2)
    treeView.setHeaderLabels(['Key', 'Value'])
    # treeView.setStyle(QStyleFactory.create('windows'))
    # treeView.selectionModel().currentChanged.connect(onCurrentChanged)
    self.PUBLIC_OpenNbtFile = PUBLIC_OpenNbtFile
