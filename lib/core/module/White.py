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
def init(parent,Name,self):
    globals()['SELF'] = self
    ThisWidget = QWidget()
    parent.addWidget(ThisWidget)
    