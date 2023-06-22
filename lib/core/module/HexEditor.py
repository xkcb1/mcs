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
SELF = None


def PUBLIC_update(filePath, fileName) -> None:
    # 先清空文本编辑器
    # left
    temp = ''
    getOut = analysis(filePath)
    count_words = 0
    count_lines = 0
    for char in getOut:
        if count_words == 1:
            temp += char + ' '
            count_words = 0
            if count_lines == 16:
                count_lines = 0
                temp += '\n'
        else:
            temp += char
            count_words += 1
    for HEX_EDITOR in SELF.HEX_VIEW:
        HEX_EDITOR.setText(temp)
    for QLABEL_NBT_name in SELF.QLABEL_NBT_name_LIST:
        QLABEL_NBT_name.setText('HEX - '+fileName)
    del temp, count_words, count_lines
    gc.collect()
    # right
    getStr = ''
    with open(filePath, 'rb') as fb:
        get = fb.read()
    for i in get:
        getStr += chr(i)
    for QLABEL_NBT_ASCII_Name in SELF.QLABEL_NBT_ASCII_Name_LIST:
        QLABEL_NBT_ASCII_Name.setText('ASCII - '+fileName)
    for ASCII_Viewer in SELF.ASCII_VIEW:
        ASCII_Viewer.setText(getStr)
    del getStr, get
    gc.collect()


def init(parent, Name, self):
    global SELF
    globals()['SELF'] = self
    SELF = self
    ThisWidget = QWidget()
    parent.addWidget(ThisWidget)
    ThisLayout = QHBoxLayout()
    ThisLayout.setContentsMargins(0, 0, 0, 0)
    ThisLayout.setSpacing(0)
    ThisWidget.setLayout(ThisLayout)
    # leftDiv
    leftDiv = QWidget()
    left_layout = QVBoxLayout(leftDiv)
    left_layout.setContentsMargins(0, 0, 0, 0)
    left_layout.setSpacing(0)
    QLABEL_NBT_name = QLabel()
    QLABEL_NBT_name.setMaximumHeight(25)
    QLABEL_NBT_name.setMinimumHeight(25)
    self.QLABEL_NBT_name_LIST.append(QLABEL_NBT_name)
    This_HEX_editor = QTextBrowser()
    self.HEX_VIEW.append(This_HEX_editor)
    #
    left_layout.addWidget(QLABEL_NBT_name)
    left_layout.addWidget(This_HEX_editor)
    # rightDiv
    rightDiv = QWidget()
    right_layout = QVBoxLayout(rightDiv)
    right_layout.setContentsMargins(0, 0, 0, 0)
    right_layout.setSpacing(0)
    This_ASCII_Viewer = QTextEdit()
    self.ASCII_VIEW.append(This_ASCII_Viewer)
    QLABEL_NBT_ASCII_Name = QLabel()
    QLABEL_NBT_ASCII_Name.setMaximumHeight(25)
    QLABEL_NBT_ASCII_Name.setMinimumHeight(25)
    self.QLABEL_NBT_ASCII_Name_LIST.append(QLABEL_NBT_ASCII_Name)
    right_layout.addWidget(QLABEL_NBT_ASCII_Name)
    right_layout.addWidget(This_ASCII_Viewer)
    # add
    ThisLayout.addWidget(leftDiv)
    ThisLayout.addWidget(rightDiv)
    # setStyleSheet
    QLABEL_NBT_name.setStyleSheet(
        'border:0px;border-bottom:1px solid '+self.theme+';border-right:1px solid '+self.theme+';border-top:1px solid '+self.theme+';')
    This_HEX_editor.setStyleSheet(
        'border:0px;border-right:1px solid '+self.theme+';')
    QLABEL_NBT_ASCII_Name.setStyleSheet(
        'border:0px;border-bottom:1px solid '+self.theme+';border-top:1px solid '+self.theme+';')
    This_ASCII_Viewer.setStyleSheet(
        'border:0px;')
    # end
    SELF.PUBLIC_update = PUBLIC_update
=======
#import base functions
from lib.base import *
#end
def init(parent,Name,self):
    globals()['SELF'] = self
    ThisWidget = QWidget()
    parent.addWidget(ThisWidget)
    
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
