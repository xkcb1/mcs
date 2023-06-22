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
# end
LastTime = '2023.4.10'
versionThis = '0.0.1 Development Bate'


def init(parent, Name, self):
    globals()['SELF'] = self
    ThisWidget = QWidget()
    parent.addWidget(ThisWidget)
    AppIcon = QLabel()
    AppIcon.setPixmap(QtGui.QPixmap('./img/appicon/big_alpha_5.png'))
    AppIcon.setStyleSheet('''border: 0px;''')
    MainLayout = QVBoxLayout()
    MainLayout.addStretch(100)
    MainLayout.addWidget(AppIcon, alignment=Qt.AlignCenter)
    MainLayout.setSpacing(20)
    ThisWidget.setLayout(MainLayout)
    ################################################################
    KeyPanel_0 = QFrame()
    KeyPanel_0.setObjectName("KeyPanel_0")
    KeyPanel_0_layout = QHBoxLayout(KeyPanel_0)
    KeyPanel_0.setStyleSheet('''#KeyPanel_0{border:1px solid #ddd !important;}
                             ''')
    KeyPanel_0.setMaximumHeight(30)
    labelA_0 = QLabel()
    labelA_0.setText(
        f'<a style="border: 0px;font-size:13px;text-align: right;">Last Updata time :</a>')
    #
    labelA_0.setStyleSheet('''border: 0px;
                           background-color:rgba(0,0,0,0);
                             background-image: url(./img/windowIcon/alert-triangle_red.svg);
                             background-position: left center;
                             background-repeat: no-repeat;
                             padding-left:25px;''')
    labelA_0.setMinimumHeight(28)
    LabelB_0 = QLabel()
    LabelB_0.setText(f' <b style="border: 0px;font-size:14px;">{LastTime}</b>')
    LabelB_0.setStyleSheet(
        'background-color:rgba(0,0,0,0);border: 0px;border-radius:5px;text-align: center;padding-left:3px;')

    #
    labelC_0 = QLabel()
    labelC_0.setText('<a style="font-size:14px;">Version :</a>')
    labelC_0.setStyleSheet('background-color:rgba(0,0,0,0);border: 0px;')
    #
    LabelD_0 = QLabel()
    LabelD_0.setText(
        f' <b style="border: 0px;font-size:14px;">{versionThis}</b>')
    LabelD_0.setStyleSheet(
        'background-color:rgba(0,0,0,0);border: 0px;border-radius:5px;text-align: center;padding-left:3px;')
    #
    KeyPanel_0_layout.addWidget(labelA_0)
    KeyPanel_0_layout.addWidget(LabelB_0)
    KeyPanel_0_layout.addWidget(labelC_0)
    KeyPanel_0_layout.addWidget(LabelD_0)
    ########################################################################
    KeyPanel_1 = QWidget()
    KeyPanel_1_layout = QHBoxLayout(KeyPanel_1)
    labelA_1 = QLabel()
    labelA_1.setText('<a style="font-size:13px;text-align: right;">打开文件</a>')
    labelA_1.setMaximumWidth(70)
    labelA_1.setMinimumWidth(70)
    #
    LabelB_1 = QLabel()
    LabelB_1.setText(' <b style="font-size:14px;">ctrl</b>')
    LabelB_1.setStyleSheet(
        'border-radius:5px;text-align: center;padding-left:3px;')
    LabelB_1.setMaximumWidth(35)
    LabelB_1.setMinimumSize(35, 22)
    LabelB_1.setMaximumHeight(22)
    #
    labelC_1 = QLabel()
    labelC_1.setText('<a style="font-size:14px;">+</a>')
    #
    LabelD_1 = QLabel()
    LabelD_1.setText(' <b style="font-size:14px;">o</b>')
    LabelD_1.setStyleSheet(
        'border-radius:5px;text-align: center;padding-left:3px;')
    LabelD_1.setMaximumWidth(20)
    LabelD_1.setMinimumSize(20, 22)
    LabelD_1.setMaximumHeight(22)
    #
    KeyPanel_1_layout.addWidget(labelA_1)
    KeyPanel_1_layout.addWidget(LabelB_1)
    KeyPanel_1_layout.addWidget(labelC_1)
    KeyPanel_1_layout.addWidget(LabelD_1)
    ################################################################
    KeyPanel_2 = QWidget()
    KeyPanel_2_layout = QHBoxLayout(KeyPanel_2)
    labelA_2 = QLabel()
    labelA_2.setText('<a style="font-size:13px;text-align: right;">打开文件夹</a>')
    labelA_2.setMaximumWidth(70)
    labelA_2.setMinimumWidth(70)
    #
    LabelB_2 = QLabel()
    LabelB_2.setText(' <b style="font-size:14px;">ctrl</b>')
    LabelB_2.setStyleSheet(
        'border-radius:5px;text-align: center;padding-left:3px;')
    LabelB_2.setMaximumWidth(35)
    LabelB_2.setMinimumSize(35, 22)
    LabelB_2.setMaximumHeight(22)
    #
    labelC_2 = QLabel()
    labelC_2.setText('<a style="font-size:14px;">+</a>')
    #
    LabelD_2 = QLabel()
    LabelD_2.setText(' <b style="font-size:14px;">d</b>')
    LabelD_2.setStyleSheet(
        'border-radius:5px;text-align: center;padding-left:3px;')
    LabelD_2.setMaximumWidth(20)
    LabelD_2.setMinimumSize(20, 22)
    LabelD_2.setMaximumHeight(22)
    #
    KeyPanel_2_layout.addWidget(labelA_2)
    KeyPanel_2_layout.addWidget(LabelB_2)
    KeyPanel_2_layout.addWidget(labelC_2)
    KeyPanel_2_layout.addWidget(LabelD_2)
    ################################################################
    KeyPanel_3 = QWidget()
    KeyPanel_3_layout = QHBoxLayout(KeyPanel_3)
    labelA_3 = QLabel()
    labelA_3.setText('<a style="font-size:13px;">新建文件</a>')
    labelA_3.setMaximumWidth(70)
    labelA_3.setMinimumWidth(70)
    #
    LabelB_3 = QLabel()
    LabelB_3.setText(' <b style="font-size:14px;">ctrl</b>')
    LabelB_3.setStyleSheet(
        'border-radius:5px;text-align: center;padding-left:3px;')
    LabelB_3.setMaximumWidth(35)
    LabelB_3.setMinimumSize(35, 22)
    LabelB_3.setMaximumHeight(22)
    #
    labelC_3 = QLabel()
    labelC_3.setText('<a style="font-size:14px;">+</a>')
    #
    LabelD_3 = QLabel()
    LabelD_3.setText(' <b style="font-size:14px;">n</b>')
    LabelD_3.setStyleSheet(
        'border-radius:5px;text-align: center;padding-left:3px;')
    LabelD_3.setMaximumWidth(20)
    LabelD_3.setMinimumSize(20, 22)
    LabelD_3.setMaximumHeight(22)
    #
    KeyPanel_3_layout.addWidget(labelA_3)
    KeyPanel_3_layout.addWidget(LabelB_3)
    KeyPanel_3_layout.addWidget(labelC_3)
    KeyPanel_3_layout.addWidget(LabelD_3)
    #
    KeyPanel_3_layout.setContentsMargins(0, 0, 0, 0)
    KeyPanel_2_layout.setContentsMargins(0, 0, 0, 0)
    KeyPanel_0_layout.setContentsMargins(10, 0, 10, 0)

    KeyPanel_1_layout.setContentsMargins(0, 0, 0, 0)

    ################################################################
    KeyPanel_3.setMaximumHeight(27)
    KeyPanel_2.setMaximumHeight(27)

    KeyPanel_1.setMaximumHeight(27)
    MainLayout.addWidget(KeyPanel_0, alignment=Qt.AlignCenter)

    MainLayout.addWidget(KeyPanel_2, alignment=Qt.AlignCenter)
    MainLayout.addWidget(KeyPanel_1, alignment=Qt.AlignCenter)
    MainLayout.addWidget(KeyPanel_3, alignment=Qt.AlignCenter)
    MainLayout.addWidget(QWidget())
    MainLayout.setContentsMargins(30, 30, 30, 30)
    MainLayout.addStretch(100)
    KeyPanel_1.setStyleSheet('''border: 0px;''')

    KeyPanel_2.setStyleSheet('''border: 0px;''')
    KeyPanel_3.setStyleSheet('''border: 0px;''')
