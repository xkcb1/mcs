import os,sys
import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets
from PyQt5.QtCore import *
from lib.StyleReader import StyleReader
import getpass
from lib.readConfig import readConfig
def CreateFileTree(self):
    #filetreeview
    self.model = QDirModel()
    #self.model.setRootPath(readConfig()['path']+'/'+readConfig()['name'])
    self.fileTreeView = QTreeView()
    self.fileTreeView.setModel(self.model)
    self.fileTreeView.setAnimated(True)
    self.fileTreeView.setIndentation(10)
    self.fileTreeView.setRootIndex(self.model.index(readConfig()['path']+'/'+readConfig()['name']))
    self.fileTreeView.setSortingEnabled(True)
    self.fileTreeView.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)
    self.fileTreeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
	# 设置水平滚动条为按需显示
    self.fileTreeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
    # 设置双击或者按下Enter键时，树节点可编辑
    self.fileTreeView.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)
    # 设置树节点为单选
    self.fileTreeView.setSelectionMode(QAbstractItemView.SingleSelection)
    # 设置选中节点时为整行选中
    self.fileTreeView.setSelectionBehavior(QAbstractItemView.SelectRows)
    self.fileTreeView.setAutoExpandDelay(-1)   
    # 设置自动展开延时为-1，表示自动展开不可用
    self.fileTreeView.setItemsExpandable(True)    
    # 设置是否可以展开项
    self.fileTreeView.setSortingEnabled(True)   
    # 设置单击头部可排序
    self.fileTreeView.setWordWrap(True)   
    # 设置自动换行
    self.fileTreeView.setHeaderHidden(False)   
    # 设置不隐藏头部
    self.fileTreeView.setExpandsOnDoubleClick(True)
    # 设置双击可以展开节点
    self.fileTreeView.header().setVisible(True)    
    # 设置显示头部   
    # 为树控件设置数据模型
    return self.fileTreeView