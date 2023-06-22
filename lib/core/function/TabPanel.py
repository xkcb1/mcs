##TabWidget core module
#import basic lib
import os,sys
import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#import lib
import lib.WindowMenu
def AppendTabWidget(self,Widget,TabName):
    #初始化菜单栏2
    for item in lib.WindowMenu.WindowMenu:
        #把WindowMenu里的名字全部for出来
        if item == TabName:
            #如果确定是这个tab，则准备开始初始化
            pass
    pass