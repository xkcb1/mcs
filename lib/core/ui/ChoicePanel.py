# ChoicePanel core module
import os
import sys
import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import lib.WindowMenu as WindowMenuThis
import lib.core.function.Starter as Starter
import functools
# import base functions
from lib.base import *
# end
ChoicePanel_Width = 500
ChoicePanel_Height = 230
ChoicePanelDict = {}
ChoicePanelCount = 0
This_Self = None
LastSender = None
ThisMainPanel = None
SELF = None
ChoicePanel_Style = {}


def OutTheChoicePanel(sender: QPushButton, self, WindowPos) -> None:
    global SELF, ChoicePanel_Style
    SELF = self
    ChoicePanel_Style = "{border : 1px solid auto;"
    globals()['SELF'] = self
    global ChoicePanelCount, ChoicePanelDict, This_Self, LastSender, ThisMainPanel
    if sender == LastSender:
        # 如果上一个sender==现在的sender，则删除此次操作
        print('[!]:is common menu button')
        cleanGraph()
        for i in ChoicePanelDict:
            print('func 1')
            self.findChild(QWidget, i).deleteLater()
            ChoicePanelDict = {}
        LastSender.setObjectName('WindowName')
        LastSender.setStyleSheet(
            '#WindowName{ color:gray;border: 1px solid rgba(0,0,0,0);padding-left:2px;padding-right:15px;background-color: rgba(0,0,0,0);background-image: url(./img/bottom_to.png);background-position:right center;background-repeat:no-repeat;}')
        LastSender = None
        return
    if LastSender != None:
        cleanGraph()
        # 如果点击时，上一个不是None(连续点击几个自带event监听的控件时)
        # LastSender.setStyleSheet('border: 1px solid rgba(0,0,0,0);background-color: rgba(0,0,0,0);background-image: url(./img/bottom_to.png);background-position:right center;background-repeat:no-repeat;')
        LastSender.setObjectName('WindowName')
        LastSender.setStyleSheet(
            '#WindowName{ color:gray;border: 1px solid rgba(0,0,0,0);padding-left:2px;padding-right:15px;background-color: rgba(0,0,0,0);background-image: url(./img/bottom_to.png);background-position:right center;background-repeat:no-repeat;}')
    LastSender = sender
    # 修改按钮样式
    This_Self = self
    # 处理:点击窗口标题时弹出的 窗口类型 选择框的弹出 以及 初始化窗口内容
    # 获取控件->判断弹出方向top left right bottom->绘制选择框->初始化内容&&删除选择框
    Frame_X = sender.pos().x()
    Frame_Y = sender.pos().y()
    Pos_X = sender.mapToGlobal(sender.pos()).x()  # 控件相对于屏幕的位置
    Pos_Y = sender.mapToGlobal(sender.pos()).y()
    window_x = WindowPos.x()  # 窗口相对于屏幕的位置
    window_y = WindowPos.y()
    widget_Width = sender.width()
    widget_Height = sender.height()  # 控件的宽度
    window_width = WindowPos.width()  # 窗口的宽度
    window_height = WindowPos.height()
    # x = Pos_X - window_x 控件相对于窗口的位置
    # 判断弹出的方向和位置step 1'
    # x坐标
    if Pos_X - window_x + ChoicePanel_Width < window_width:  # 如果弹出框的坐标+宽度 < 窗口总宽度 则正常的往右方弹出
        # to right
        x = Pos_X - window_x - Frame_X
        a = 'right'
    else:  # 否则往左弹出
        # to left
        x = Pos_X - window_x + widget_Width - ChoicePanel_Width - Frame_X
        a = 'left'
        # 控件相对于窗口的位置 + 控件宽度 = 控件右侧边的位置，控件右侧边的位置 - 弹出框宽度 = 以控件右侧为基准，往左的弹出框位置的坐标点
    # y坐标
    if Pos_Y - window_y + ChoicePanel_Height < window_height:
        # to bottom
        y = Pos_Y - window_y + widget_Height - Frame_Y - 2
        b = 'bottom'
    else:
        y = Pos_Y - window_y - ChoicePanel_Height - Frame_Y + 2
        b = 'top'
        # to top
    # 通过展现方向来控制sender的圆角
    sender.setObjectName('WindowName')
    if b == 'bottom':
        sender.setStyleSheet(
            "#WindowName{ color:gray;padding-left:2px;padding-right:15px;border: 1px solid #aaa;border-top-left-radius: 7px;border-top-right-radius: 7px;background-color: #567dbc;background-image: url(./img/bottom_blue.png);background-position:right center;background-repeat:no-repeat;}")
    else:
        sender.setStyleSheet(
            "#WindowName{ color:gray;padding-left:2px;padding-right:15px;border: 1px solid #aaa;border-bottom-left-radius: 7px;border-bottom-right-radius: 7px;background-color: #567dbc;background-image: url(./img/bottom_blue.png);background-position:right center;background-repeat:no-repeat;}")
    # 默认是 right-bottom
    for i in ChoicePanelDict:
        self.findChild(QWidget, i).deleteLater()
        ChoicePanelDict = {}
    # 清除一遍
    ChoicePanel = QWidget(self)
    ThisMainPanel = ChoicePanel
    # 向全局赋值
    ChoicePanel.resize(ChoicePanel_Width, ChoicePanel_Height)
    ChoicePanel.move(x, y)
    ChoicePanel.setObjectName("ChoicePanel_"+str(ChoicePanelCount))
    # ChoicePanel.setStyleSheet("background-color:red;")
    ChoicePanelDict["ChoicePanel_"+str(ChoicePanelCount)
                    ] = [x, y, ChoicePanel_Width, ChoicePanel_Height, a, b]
    DrawChoicePanel(ChoicePanel, a, b, "ChoicePanel_" +
                    str(ChoicePanelCount), sender.text(), sender)
    ChoicePanel.show()
    # 实现ChoicePanel样式和细节
    ChoicePanelCount += 1
    pass


def CheckRemoveThePanel(ClickPos) -> None:
    global ChoicePanelDict, This_Self, LastSender
    if LastSender != None:
        LastSender.setObjectName('WindowName')  # 把id恢复，获取到hover样式
        LastSender.setStyleSheet(
            '#WindowName{ color:gray;border: 1px solid rgba(0,0,0,0);padding-left:2px;padding-right:15px;background-color: rgba(0,0,0,0);background-image: url(./img/bottom_to.png);background-position:right center;background-repeat:no-repeat;}')
        cleanGraph()
    if ChoicePanelDict == {}:
        # 如果弹出框记录里什么都没有，就直接返回咯
        return
    else:
        # print(ChoicePanelDict)
        for panel in ChoicePanelDict:
            # 开始判断是否删除 弹出框
            pos = ChoicePanelDict[panel]
            if ClickPos.x() < pos[0] or ClickPos.x() > (pos[0]+pos[2]):
                # print(ClickPos.x(),pos[0],(pos[0]+pos[2]),pos)
                cleanGraph()
                for i in ChoicePanelDict:
                    print('func 3')
                    This_Self.findChild(QWidget, i).deleteLater()
                    ChoicePanelDict = {}
                LastSender = None
                return
            else:
                # print(ClickPos.x(),pos[0],(pos[0]+pos[2]),pos)
                # 在x指定区域内，开始判断y
                # print(pos)
                if ClickPos.y() < pos[1] or ClickPos.y() > (pos[1]+pos[3]):
                    cleanGraph()
                    for i in ChoicePanelDict:
                        print('func 4')
                        This_Self.findChild(QWidget, i).deleteLater()
                        ChoicePanelDict = {}
                    LastSender = None
                    return
                else:
                    # 完全在指定区域
                    print('[!]:in ChoicePanel')
                    if pos[5] == 'bottom':
                        LastSender.setStyleSheet(
                            "color:gray;padding-left:2px;padding-right:15px;border: 1px solid #aaa;border-top-left-radius: 7px;border-top-right-radius: 7px;background-color: #cbe8ff;background-image: url(./img/bottom_blue.png);background-position:right center;background-repeat:no-repeat;")
                    else:
                        LastSender.setStyleSheet(
                            "color:gray;padding-left:2px;padding-right:15px;border: 1px solid #aaa;border-bottom-left-radius: 7px;border-bottom-right-radius: 7px;background-color: #cbe8ff;background-image: url(./img/bottom_blue.png);background-position:right center;background-repeat:no-repeat;")
                    This_Self.effect_shadow = QGraphicsDropShadowEffect()
                    This_Self.effect_shadow.setOffset(0, 0)  # 偏移
                    This_Self.effect_shadow.setBlurRadius(33)  # 阴影半径
                    This_Self.effect_shadow.setColor(QtCore.Qt.gray)  # 阴影颜色
                    for i in ChoicePanelDict:
                        This_Self.findChild(QWidget, i).setGraphicsEffect(
                            This_Self.effect_shadow)  # 将设置套用到button窗口中


def DrawChoicePanel(Widget: QWidget, marginA, marginB, Name, ThisPanel, sender: QPushButton) -> None:
    global This_Self
    # print(Widget,marginA,marginB,Name,ThisPanel,sender)
    # Draw the ChoicePanel,Widget is ChoicePanel
    # creating a QGraphicsDropShadowEffect object
    This_Self.effect_shadow = QGraphicsDropShadowEffect()
    This_Self.effect_shadow.setOffset(0, 0)  # 偏移
    This_Self.effect_shadow.setBlurRadius(20)  # 阴影半径
    This_Self.effect_shadow.setColor(QtCore.Qt.gray)  # 阴影颜色
    Widget.setGraphicsEffect(This_Self.effect_shadow)  # 将设置套用到button窗口中
    # 设置主控件阴影
    This_Self.effect_shadow_Sender = QGraphicsDropShadowEffect()
    This_Self.effect_shadow_Sender.setOffset(0, 0)  # 偏移
    This_Self.effect_shadow_Sender.setBlurRadius(20)  # 阴影半径
    This_Self.effect_shadow_Sender.setColor(QtCore.Qt.gray)  # 阴影颜色
    sender.setGraphicsEffect(This_Self.effect_shadow_Sender)
    # 设置sender阴影
    ChoicePanel_Style_this = ChoicePanel_Style
    if marginB == 'bottom':  # 默认情况
        ChoicePanel_Style_this += "border-bottom-right-radius: 3px;border-bottom-left-radius: 3px;"
        if marginA == 'right':  # 默认情况
            ChoicePanel_Style_this += "border-top-right-radius: 3px;"
        else:
            ChoicePanel_Style_this += "border-top-left-radius: 3px;"
    else:
        ChoicePanel_Style_this += "border-top-right-radius: 3px;border-top-left-radius: 3px;"
        if marginA == 'right':  # 默认情况
            ChoicePanel_Style_this += "border-bottom-right-radius: 3px;"
        else:
            ChoicePanel_Style_this += "border-bottom-left-radius: 3px;"
    ChoicePanel_Style_this = "#"+Name + ChoicePanel_Style_this + "}"
    # print(ChoicePanel_Style_this)
    Widget.setObjectName(Name)
    Widget.setStyleSheet(ChoicePanel_Style_this)
    # 开始绘制内部控件
    ChoiceLayout = QHBoxLayout()
    ChoiceLayout.setContentsMargins(3, 3, 3, 3)
    ChoiceLayout.setSpacing(4)
    # 1
    Layout_1 = QVBoxLayout()
    Layout_1.setSpacing(0)
    SmallTitle_1 = QPushButton("标准")
    # SmallTitle_1.setFont(QFont("Arial",11))
    SmallTitle_1.setObjectName('smallTitle')
    SmallTitle_1.setMaximumHeight(33)
    SmallTitle_1.setMinimumHeight(33)
    Layout_1.addWidget(SmallTitle_1)
    for Name in WindowMenuThis.WindowMenuInChoice['Standard']:
        This_Self.ChoiceButton = QPushButton(Name)
        This_Self.ChoiceButton.setToolTip(Name)
        This_Self.ChoiceButton.setObjectName('ChoiceButton')
        This_Self.ChoiceButton.setStyleSheet('''
#ChoiceButton{
    background-color: rgba(0, 0, 0, 0.0);
    border-radius: 5px !important;
    text-align: left;
    margin-left: 5px;
    margin-right: 5px;
    border: 1px solid rgba(0, 0, 0, 0.0);
    padding-left: 3px;
    margin-top: 2px;
    margin-bottom: 2px;
    color:gray;
}
#ChoiceButton:hover {
    background-color:#92b8ff;
    border: 1px solid #567dbc;
}''')
        This_Self.ChoiceButton.setMaximumHeight(24)
        This_Self.ChoiceButton.setMinimumHeight(24)
        This_Self.ChoiceButton.clicked.connect(
            functools.partial(ChangePanel, Name))
        This_Self.ChoiceButton.setIcon(
            QIcon(WindowMenuThis.WindowMenuInChoice['Standard'][Name]['icon']))
        if Name == ThisPanel:
            This_Self.ChoiceButton.setObjectName('ChoiceButton_this')
            # This_Self.ChoiceButton.clicked.connect(None)
        Layout_1.addWidget(This_Self.ChoiceButton)
    Layout_1.addWidget(QWidget())
    # 2
    Layout_2 = QVBoxLayout()
    SmallTitle_2 = QPushButton("常规")
    SmallTitle_2.setObjectName('smallTitle')
    SmallTitle_2.setMaximumHeight(33)
    SmallTitle_2.setMinimumHeight(33)
    Layout_2.addWidget(SmallTitle_2)
    for Name in WindowMenuThis.WindowMenuInChoice['Convention']:
        This_Self.ChoiceButton = QPushButton(Name)
        This_Self.ChoiceButton.setToolTip(Name)
        This_Self.ChoiceButton.setObjectName('ChoiceButton')
        This_Self.ChoiceButton.setStyleSheet('''
#ChoiceButton{
    background-color: rgba(0, 0, 0, 0.0);
    border-radius: 5px !important;
    text-align: left;
    margin-left: 5px;
    margin-right: 5px;
    border: 1px solid rgba(0, 0, 0, 0.0);
    padding-left: 3px;
    margin-top: 2px;
    margin-bottom: 2px;
    color:gray;
}
#ChoiceButton:hover {
    background-color:#92b8ff;
    border: 1px solid #567dbc;
}''')
        This_Self.ChoiceButton.setMaximumHeight(24)
        This_Self.ChoiceButton.setMinimumHeight(24)
        This_Self.ChoiceButton.clicked.connect(
            functools.partial(ChangePanel, Name))
        This_Self.ChoiceButton.setIcon(
            QIcon(WindowMenuThis.WindowMenuInChoice['Convention'][Name]['icon']))
        if Name == ThisPanel:
            This_Self.ChoiceButton.setObjectName('ChoiceButton_this')
            # This_Self.ChoiceButton.clicked.connect(None)
        Layout_2.addWidget(This_Self.ChoiceButton)
    Layout_2.addWidget(QWidget())
    Layout_2.setSpacing(0)
    # 3
    Layout_3 = QVBoxLayout()
    Layout_3.setSpacing(0)
    SmallTitle_3 = QPushButton("扩展")
    SmallTitle_3.setObjectName('smallTitle')
    SmallTitle_3.setMaximumHeight(33)
    SmallTitle_3.setMinimumHeight(33)
    Layout_3.addWidget(SmallTitle_3)
    for Name in WindowMenuThis.WindowMenuInChoice['extend']:
        This_Self.ChoiceButton = QPushButton(Name)
        This_Self.ChoiceButton.setToolTip(Name)
        This_Self.ChoiceButton.setObjectName('ChoiceButton')
        This_Self.ChoiceButton.setStyleSheet('''
#ChoiceButton{
    background-color: rgba(0, 0, 0, 0.0);
    border-radius: 5px !important;
    text-align: left;
    margin-left: 5px;
    margin-right: 5px;
    border: 1px solid rgba(0, 0, 0, 0.0);
    padding-left: 3px;
    margin-top: 2px;
    margin-bottom: 2px;
    color:gray;
}
#ChoiceButton:hover {
    background-color:#92b8ff;
    border: 1px solid #567dbc;
}''')
        This_Self.ChoiceButton.setMaximumHeight(24)
        This_Self.ChoiceButton.setMinimumHeight(24)
        This_Self.ChoiceButton.clicked.connect(
            functools.partial(ChangePanel, Name))
        # 新方法是用childAT办法
        This_Self.ChoiceButton.setIcon(
            QIcon(WindowMenuThis.WindowMenuInChoice['extend'][Name]['icon']))
        if Name == ThisPanel:
            This_Self.ChoiceButton.setObjectName('ChoiceButton_this')
            # This_Self.ChoiceButton.clicked.connect(None)
        Layout_3.addWidget(This_Self.ChoiceButton)
    Layout_3.addWidget(QWidget())
    # new一个新的面板
    Layout_4 = QVBoxLayout()
    Layout_4.setSpacing(0)
    SmallTitle_4 = QPushButton("工具")
    SmallTitle_4.setObjectName('smallTitle')
    SmallTitle_4.setMaximumHeight(33)
    SmallTitle_4.setMinimumHeight(33)
    Layout_4.addWidget(SmallTitle_4)
    for Name in WindowMenuThis.WindowMenuInChoice['tools']:
        This_Self.ChoiceButton = QPushButton(Name)
        This_Self.ChoiceButton.setToolTip(Name)
        This_Self.ChoiceButton.setObjectName('ChoiceButton')
        This_Self.ChoiceButton.setStyleSheet('''
#ChoiceButton{
    background-color: rgba(0, 0, 0, 0.0);
    border-radius: 5px !important;
    text-align: left;
    margin-left: 5px;
    margin-right: 5px;
    border: 1px solid rgba(0, 0, 0, 0.0);
    padding-left: 3px;
    margin-top: 2px;
    margin-bottom: 2px;
    color:gray;
}
#ChoiceButton:hover {
    background-color:#92b8ff;
    border: 1px solid #567dbc;
}''')
        This_Self.ChoiceButton.setMaximumHeight(24)
        This_Self.ChoiceButton.setMinimumHeight(24)
        This_Self.ChoiceButton.clicked.connect(
            functools.partial(ChangePanel, Name))
        # 新方法是用childAT办法
        This_Self.ChoiceButton.setIcon(
            QIcon(WindowMenuThis.WindowMenuInChoice['tools'][Name]['icon']))
        if Name == ThisPanel:
            # print(Name,This_Self.ChoiceButton)
            This_Self.ChoiceButton.setObjectName('ChoiceButton_this')
            # This_Self.ChoiceButton.clicked.connect(None)
        Layout_4.addWidget(This_Self.ChoiceButton)
    Layout_4.addWidget(QWidget())
    # end
    Layout_1.setContentsMargins(0, 0, 0, 0)
    Layout_2.setContentsMargins(0, 0, 0, 0)
    Layout_3.setContentsMargins(0, 0, 0, 0)
    Layout_4.setContentsMargins(0, 0, 0, 0)
    ChoiceLayout.addLayout(Layout_1)
    ChoiceLayout.addLayout(Layout_2)
    ChoiceLayout.addLayout(Layout_4)  # 顺序翻反一下
    ChoiceLayout.addLayout(Layout_3)
    Widget.setLayout(ChoiceLayout)
    pass


def cleanGraph():
    This_Self.effect_shadow.setBlurRadius(0)  # 阴影半径
    # This_Self.effect_shadow_Sender.setBlurRadius(0) #sender
    # This_Self.effect_shadow = QGraphicsDropShadowEffect(This_Self)
    This_Self.effect_shadow.setOffset(0, 0)  # 偏移
    # This_Self.effect_shadow.setColor(QtCore.Qt.blue)  # 阴影颜色
    ThisMainPanel.setGraphicsEffect(This_Self.effect_shadow)  # 将设置套用到button窗口中


def ChangePanel(Name):
    global ChoicePanelDict, LastSender, ThisMainPanel, This_Self
    cleanGraph()
    for i in ChoicePanelDict:
        print('func 5')
        This_Self.findChild(QWidget, i).deleteLater()
        ChoicePanelDict = {}
    # 改变此panel的内容
    # 获取到此按钮
    # PointerPos = QCursor.pos()
    # print(Name)
    LastSender.setObjectName('WindowName')  # 把id恢复，获取到hover样式
    LastSender.setStyleSheet(
        '#WindowName{ color:gray;border: 1px solid rgba(0,0,0,0);padding-left:2px;padding-right:15px;background-color: rgba(0,0,0,0);background-image: url(./img/bottom_to.png);background-position:right center;background-repeat:no-repeat;}')
    LastSender.setText(Name)
    This_Sender = LastSender
    LastSender = None
    # 删除现有的panel
    # 准备开始初始化新的panel
    # 应该在这里就去获取到点击的按钮
    # 把sender的text()->str作为参数传入，初始化函数
    Starter.PanelStarter(This_Sender, This_Self, Name)
    pass
