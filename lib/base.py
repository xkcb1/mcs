import os,sys
import PyQt5.QtGui as QtGui
import vtk
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import *
from lib.readConfig import readConfig
from lib.StyleReader import StyleReader
from pathlib import Path
import lib.WindowMenu
import lib.core.function.FileIcon
from lib.core.function.FileIcon import *
#3d
from lib.pure.NbtTree import *
#math
import numpy as np
import math
from numpy import *
import numpy
#error
import traceback
#nbt
import nbtlib
#use vtk
from PyQt5.QtOpenGL import QGLWidget
from vtk import *
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from lib.pure.MakeObj import MakeStlFileByNbt
#方便一次性导入所有的基础要用的库
################################################################
rewrite_print = print
print_ = print
def print(*arg,SELF=None,widgetList=None):
    # 首先，调用原始的print函数将内容打印到控制台。
    #rewrite_print(*arg)
    # 如果日志文件所在的目录不存在，则创建一个目录。
    #output_dir = "./log_file"
    # 打开（或创建）日志文件并将内容写入其中。
    #log_name = 'log.txt'
    #filename = os.path.join(output_dir, log_name)
    rewrite_print(*arg,file=open("./log_file/log.txt","a"))
    try:
        #rewrite_print(SELF,widgetList)
        for widget in widgetList:
            for value in arg:
                widget.append(str(value))
    except:
        pass
################################################################
def clearLog():
    with open("./log_file/log.txt","w") as wf:
        wf.write('')
################################################################
def getLog():
    with open("./log_file/log.txt","r") as rf:
        getlogfile = rf.read()
    return getlogfile
#globals()['SELF'] = self
################################################################
def GetDir(self,Lastpath,tabCount):#从Main里迁移出来
    for file_name in os.listdir(Lastpath):
        if os.path.isdir(Lastpath+'//'+file_name) == True:
            #print(file_name)
            #is folder
            #print(Lastpath+'\\'+file_name)
            self.pathList.append(tabCount*'  '+file_name)
            self.Projectfolders = self.Projectfolders + 1
            GetDir(self,Lastpath+'\\'+file_name,tabCount = tabCount+1)
        else:
            self.pathList.append(tabCount*'  '+file_name)
            self.Projectfiles += 1
################################################################
class AttributePanel(QFrame):
    # 参数1：Name:str,参数2：Attribute:dict,参数3：ifopen:boolean,
    def __init__(self, Name: str, AttributeDic: dict, funcList: list,ifopen: bool = False):
        # ifopen默认为FALSE，就是展开
        super().__init__()
        # start
        self.Name = Name
        self.Attribute = AttributeDic
        self.ifopen = ifopen
        self.funcList = funcList
        self.ItemCount = 0
        for i in self.Attribute:
            self.ItemCount += 1
        # self.setMinimumHeight(20)
        self.UIinit()
    def UIinit(self) -> None:
        self.IsZoomSmall = 0
        # 25是属性框收缩后的高度
        self.setObjectName('ATTRIBUTEPanel')
        self.setStyleSheet('''
#ATTRIBUTEPanel{
    background-color: #f6f6f6;
    border-radius:4px;
    border:1px solid #ddd
}
''')
        # self.setMaximumWidth(999999)
        self.MainLayoutATTR = QVBoxLayout()
        self.setLayout(self.MainLayoutATTR)
        self.MainLayoutATTR.setContentsMargins(0, 0, 0, 0)
        self.MainLayoutATTR.setSpacing(0)
        self.OptionLayout_Widget = QWidget()
        self.OptionLayout_Widget.setMinimumHeight(25)
        self.OptionLayout_Widget.setMaximumHeight(25)
        self.OptionLayout_Widget.setStyleSheet(
            'background-color:rgba(0,0,0,0);border:0px;')
        self.OptionLayout = QHBoxLayout()
        self.OptionLayout.setContentsMargins(5, 0, 0, 0)
        self.MainLayoutATTR.addWidget(self.OptionLayout_Widget)
        self.OptionLayout_Widget.setLayout(self.OptionLayout)
        self.ThisName = QPushButton()
        # self.ThisName.setStyleSheet('background-color:red;')
        self.ThisName.setMinimumHeight(25)
        self.ThisName.setMaximumHeight(25)
        self.ThisName.clicked.connect(self.zoomPanel)
        #
        self.Other = QWidget()
        self.Other.setObjectName('OtherSplitter')
        self.ThisName.setObjectName('thisAttrName')
        self.ThisName.setText(self.Name)
        self.ThisName.setIcon(QIcon("./img/bottom_to.png"))
        # print(self.Name)
        self.OptionLayout.addWidget(self.ThisName)
        self.OptionLayout.addWidget(self.Other)
        #
        self.MainWidget = QWidget()
        self.MainLayoutATTR.addWidget(self.MainWidget)
        self.MainLayoutEdit = QGridLayout()
        self.MainLayoutEdit.setContentsMargins(0, 0, 0, 0)
        self.MainWidget.setLayout(self.MainLayoutEdit)
        self.Gx = 0
        self.Gy = 0
        # self.setLayout(MainLayoutATTR)
        # make the attributes from dict
        self.makeUI()
        if self.ifopen == True:
            self.IsZoomSmall = 1
            self.toBig()
        else:
            self.IsZoomSmall = 0
            self.toSmall()

    def toSmall(self):  # 收缩
        self.ThisName.setIcon(QIcon("./img/bottom_to.png"))
        print('toSmall')
        animationSmall = QPropertyAnimation(self, b"geometry")
        animationSmall.setDuration(1000)
        self.setMaximumHeight(25)
        start = self.geometry()
        animationSmall.setEndValue(start)
        animationSmall.start()
        self.MainWidget.hide()

    def toBig(self):  # 扩展
        print('toBig')
        self.ThisName.setIcon(QIcon("./img/ToOpen_.png"))
        animationBig = QPropertyAnimation(self, b"geometry")
        animationBig.setDuration(1000)
        self.setMaximumHeight(self.ItemCount*25+35)
        start = self.geometry()
        animationBig.setEndValue(start)
        animationBig.start()
        self.MainWidget.show()

    def makeUI(self):
        self.MainLayoutEdit.setContentsMargins(4, 4, 4, 4)
        self.count = 0
        for EditItem in self.Attribute:
            ItemName = QLabel()
            ItemName.setText(EditItem)
            ItemName.setObjectName('ItemName')
            ThisType = type(self.Attribute[EditItem])
            if ThisType == type('str'):  # 如果是字符串
                EditItemWidget = QLineEdit()
                EditItemWidget.setObjectName('EditItemWidget')
                EditItemWidget.setStyleSheet('')
                if self.funcList != None:
                    EditItemWidget.textChanged.connect(self.changeText)
                    EditItemWidget.ClassName = str(self.count)
                EditItemWidget.setText(self.Attribute[EditItem])
                ItemName.setStyleSheet('''
                                   color:#111;
                                   background-image:url(./img/gray2.png);
                                   background-repeat:no-repeat;
                                   padding-left:15px;
                                   margin-left:4px;
                                   border:0px;''')
            elif ThisType == type(1):  # 如果是整型
                EditItemWidget = QPushButton()
                EditItemWidget.setObjectName('EditItemWidget_button')
                EditItemWidget.setText(str(self.Attribute[EditItem]))
                if self.funcList != None:
                    EditItemWidget.clicked.connect(self.changeButton)
                    EditItemWidget.ClassName = str(self.count)
                ItemName.setStyleSheet('''
                                   color:#111;
                                   background-image:url(./img/blue2.png);
                                   background-repeat:no-repeat;
                                   padding-left:15px;
                                   margin-left:4px;
                                   border:0px;''')
            elif self.Attribute[EditItem].__class__ == Ppath:  # 如果是Ppath类型
                EditItemWidget = QPushButton()
                EditItemWidget.setObjectName('EditItemWidget_button_Path')
                EditItemWidget.setText(str(self.Attribute[EditItem].path))
                if self.funcList != None:
                    EditItemWidget.clicked.connect(self.changeButton)
                    EditItemWidget.ClassName = str(self.count)
                ItemName.setStyleSheet('''
                                   color:#111;
                                   background-image:url(./img/yellow2.png);
                                   background-repeat:no-repeat;
                                   padding-left:15px;
                                   margin-left:4px;
                                   border:0px;''')
            elif ThisType == type(True):  # 如果是布尔值
                EditItemWidget = QPushButton()
                EditItemWidget.setObjectName('EditItemWidget_button')
                EditItemWidget.setText(str(self.Attribute[EditItem]))
                if self.funcList != None:
                    EditItemWidget.clicked.connect(self.changeButton)
                    EditItemWidget.ClassName = str(self.count)
                ItemName.setStyleSheet('''
                                   color:#111;
                                   background-image:url(./img/purple2.png);
                                   background-repeat:no-repeat;
                                   padding-left:15px;
                                   margin-left:4px;
                                   border:0px;''')
                EditItemWidget.clicked.connect(self.ChangeBoolean)
            elif ThisType == type([1]):#如果是列表
                EditItemWidget = QComboBox()
                EditItemWidget.setObjectName('EditItemWidget_search')
                if self.funcList != None:
                    EditItemWidget.currentIndexChanged.connect(self.changeSearch)
                    EditItemWidget.ClassName = str(self.count)
                for item in self.Attribute[EditItem]:
                    EditItemWidget.addItem(item)
                ItemName.setStyleSheet('''
                                   color:#111;
                                   background-image:url(./img/organe2.png);
                                   background-repeat:no-repeat;
                                   padding-left:15px;
                                   margin-left:4px;
                                   border:0px;''')
            #ItemName.setMaximumWidth(70)
            self.MainLayoutEdit.addWidget(ItemName,self.Gx,self.Gy)
            #print(self.Gx,self.Gy,1,1)
            self.Gy += 1
            self.MainLayoutEdit.addWidget(EditItemWidget,self.Gx,self.Gy)
            #print(self.Gx,self.Gy,1,1)
            self.Gx += 1
            self.Gy = 0
            self.count += 1
            # 通过type来判断需要放置一个什么样的QObject
    def changeSearch(self):
        sender = self.sender()
        getIndex = int(sender.ClassName)
        self.funcList[getIndex](self)
    def changeText(self):
        sender = self.sender()
        getIndex = int(sender.ClassName)
        self.funcList[getIndex](self)
    def changeButton(self):
        sender = self.sender()
        getIndex = int(sender.ClassName)
        self.funcList[getIndex](self)
    def zoomPanel(self, mode: int) -> None:
        print('clicked')
        # mode 1 扩展
        # mode 0 收缩
        if self.IsZoomSmall == 0:  # 已经是收缩
            self.toBig()
            self.IsZoomSmall = 1  # 已经是扩展
        else:
            self.toSmall()
            self.IsZoomSmall = 0

    def ChangeBoolean(self):
        getSender = self.sender()
        if getSender.text() == 'False':
            getSender.setText('True')
        else:
            getSender.setText('False')
################################################################
class Ppath:
    def __init__(self,path):
        self.path = path
################################################################
class PQWidget(QWidget):
    def __init__(self,parent_):
        self.parent_ = parent_
        super().__init__()
    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.parent_.isMaximized():  # 缩小
            self.parent_.THIS_Widget.setContentsMargins(7, 7, 7, 7)
            self.parent_.verticalLayout__.setContentsMargins(1, 1, 1, 1)
            self.parent_.showNormal()  # 切换放大按钮图标
            self.parent_.pushButton_2.setToolTip(
                "<html><head/><body><p>最大化</p></body></html>")
        else:  # 放大
            self.parent_.THIS_Widget.setContentsMargins(0, 0, 0, 0)
            self.parent_.verticalLayout__.setContentsMargins(0, 0, 0, 0)
            self.parent_.showMaximized()
            self.parent_.pushButton_2.setToolTip(
                "<html><head/><body><p>恢复</p></body></html>")
        return super().mouseDoubleClickEvent(a0)
    def paintEvent(self, evt):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        # 反锯齿
        painter.setRenderHint(QPainter.Antialiasing)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
################################################################
class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=-1, hspacing=-1, vspacing=-1):
        super(FlowLayout, self).__init__(parent)
        self._hspacing = hspacing
        self._vspacing = vspacing
        self._items = []
        self.setContentsMargins(margin, margin, margin, margin)

    def __del__(self):
        del self._items[:]

    def addItem(self, item):
        self._items.append(item)

    def horizontalSpacing(self):
        if self._hspacing >= 0:
            return self._hspacing
        else:
            return self.smartSpacing(
                QStyle.PM_LayoutHorizontalSpacing)

    def verticalSpacing(self):
        if self._vspacing >= 0:
            return self._vspacing
        else:
            return self.smartSpacing(
                QStyle.PM_LayoutVerticalSpacing)

    def count(self):
        return len(self._items)

    def itemAt(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]

    def takeAt(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)

    def expandingDirections(self):
        return QtCore.Qt.Orientations(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.doLayout(QtCore.QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QtCore.QSize()
        for item in self._items:
            size = size.expandedTo(item.minimumSize())
        left, top, right, bottom = self.getContentsMargins()
        size += QtCore.QSize(left + right, top + bottom)
        return size

    def doLayout(self, rect, testonly):
        left, top, right, bottom = self.getContentsMargins()
        effective = rect.adjusted(+left, +top, -right, -bottom)
        x = effective.x()
        y = effective.y()
        lineheight = 0
        for item in self._items:
            widget = item.widget()
            hspace = self.horizontalSpacing()
            if hspace == -1:
                hspace = widget.style().layoutSpacing(
                    QSizePolicy.PushButton,
                    QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            vspace = self.verticalSpacing()
            if vspace == -1:
                vspace = widget.style().layoutSpacing(
                    QSizePolicy.PushButton,
                    QSizePolicy.PushButton, QtCore.Qt.Vertical)
            nextX = x + item.sizeHint().width() + hspace
            if nextX - hspace > effective.right() and lineheight > 0:
                x = effective.x()
                y = y + lineheight + vspace
                nextX = x + item.sizeHint().width() + hspace
                lineheight = 0
            if not testonly:
                item.setGeometry(
                    QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))
            x = nextX
            lineheight = max(lineheight, item.sizeHint().height())
        return y + lineheight - rect.y() + bottom

    def smartSpacing(self, pm):
        parent = self.parent()
        if parent is None:
            return -1
        elif parent.isWidgetType():
            return parent.style().pixelMetric(pm, None, parent)
        else:
            return parent.spacing()
################################################################
class FlowBox(QWidget):
    def __init__(self,name,type):
        super(FlowBox, self).__init__()
        self.setContentsMargins(5, 5, 5, 5)
        self.type = type
        self.name = name
        self.ThisLayout = QVBoxLayout(self)
        self.setMaximumSize(50,64)
        self.setMinimumSize(50,64)
        self.ThisLayout.setContentsMargins(0,0,0,0)
        self.ThisLayout.setSpacing(0)
        #
        self.setObjectName('baseFlowBox')
        self.setStyleSheet('''
    border: 0px;
    border-radius: 4px;
    margin:0px;
''')
        #
        self.IconLabel = QWidget()#图标
        self.IconLabel.setMaximumSize(40,24)
        self.IconLabel.setMinimumSize(40,24)
        self.NameLabel = QLabel()#名字
        #self.NameLabel.setAlignment(Qt.AlignCenter)
        #self.NameLabel.setWordWrap(True)
        #
        self.NameLabel.setWordWrap(True)
        self.NameLabel.setAlignment(QtCore.Qt.AlignTop)
        #
        type_ = self.type+'.svg'
        if self.type == 'mcfunction':
            type_ = self.type+'.png'
        if self.name == 'readme':
            type_ = 'readme.svg'
        self.IconLabel.setStyleSheet(f'''
                                     background-image: url(./img/file/icons/{type_});
                                     background-repeat: no-repeat;
                                     background-position: center center;''')
        #self.IconLabel.setScaledContents(True)
        if len(self.name) > 8:
            self.name = self.name[:8]+'\n'+self.name[8:]
        if len(self.name) > 16:
            self.name = self.name[:16]+'\n'+self.name[16:]
        self.NameLabel.setText(self.name)
        self.NameLabel.setMaximumWidth(40)
        self.NameLabel.setMinimumWidth(40)
        self.NameLabel.setStyleSheet('''font-family: monospace;
                                     font-size:10px;
                                     color:#222;''')
        self.NameLabel.setToolTip(self.name)
        #add
        self.ThisLayout.addWidget(self.IconLabel)
        self.ThisLayout.addWidget(self.NameLabel)
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawRoundedRect(
            0, 0, self.width() - 1, self.height() - 1, 5, 5)
        super(FlowBox, self).paintEvent(event)
################################################################
class FlowWidget(QScrollArea):
    def __init__(self, parent) -> None:
        super().__init__()
        self.setWidgetResizable(True)
        self.ThisWidget = QWidget(self)
        self.ThisLayout = FlowLayout(self.ThisWidget,hspacing=12, vspacing=12)
        self.setWidget(self.ThisWidget)
        self.setObjectName('AssetWidget')
        #完成初始化控件部分
        self.setStyleSheet('''
#AssetWidget{
    border-radius: 0px !important;
    border: 1px solid rgba(0, 0, 0, 0.0);
}
#AssetWidget:focus {
    border: 1px solid #4888FF;
}
                           ''')
        self.ThisWidget.setObjectName('AssetWidget')

################################################################
class AssetWidget(FlowWidget):
    def __init__(self, parent,path,bottom) -> None:
        super().__init__(parent)
        self.path = path
        self.parent = parent
        self.FileList = []
        self.DirList = []
        self.AllList = []
        self.fileCount = []
        self.DirCount = []
        self.bottom = bottom
        self.setRootPath(self.path)
    def setRootPath(self,path):
        #更换目录用的
        self.path = path
        get_file_path(self.path,self.FileList,self.DirList)
        get_ALL_file_count(self.path,self.fileCount,self.DirCount)
        self.AllList = self.FileList + self.DirList
        #rewrite_print(self.FileList,self.DirList,self.AllList)
        self.bottom.setText(f'文件夹数:{str(len(self.fileCount))} | 文件数:{str(len(self.DirCount))}')
        self.update()#读取目录并更换完后，进行重新绘制
        
    def update(self):
        #重新渲染界面用的
        for item in self.AllList:
            name = item.split('\\')[-1]
            if name[0] == '.':
                self.ThisLayout.addWidget(FlowBox(name,'folder-base'))
                #self.ThisLayout.addWidget(Bubble(name))
            elif len(name.split('.')) == 1:
                self.ThisLayout.addWidget(FlowBox(name,'folder-base'))
                #self.ThisLayout.addWidget(Bubble(name))
            elif len(name.split('.')) == 2:
                self.ThisLayout.addWidget(FlowBox(name,name.split('.')[-1]))
                #self.ThisLayout.addWidget(Bubble(name))
            #self.ThisLayout.addWidget(FlowBox())
        pass
################################################################
class Bubble(QLabel):
    def __init__(self, text):
        super(Bubble, self).__init__(text)
        self.word = text
        self.setContentsMargins(5, 5, 5, 5)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawRoundedRect(
            0, 0, self.width() - 1, self.height() - 1, 5, 5)
        super(Bubble, self).paintEvent(event)
################################################################
def get_file_path(root_path,file_list,dir_list):
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            #递归获取所有文件和目录的路径
            #get_file_path(dir_file_path,file_list,dir_list)
        else:
            file_list.append(dir_file_path)
def get_ALL_file_count(root_path,file_list_count,dir_list_count):
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list_count.append(dir_file_path)
            #递归获取所有文件和目录的路径
            get_ALL_file_count(dir_file_path,file_list_count,dir_list_count)
        else:
            file_list_count.append(dir_file_path)
################################################################
class PpathWidget(QScrollArea):
    def __init__(self,path):
        super().__init__()
        self.initUI()
        self.path = path
        self.setRootPath(path)
    def initUI(self):
        self.ThisWidget = QWidget(self)
        self.setWidgetResizable(True)
        self.ThisLayout = QHBoxLayout(self.ThisWidget)
        self.setWidget(self.ThisWidget)
        self.ThisLayout.setContentsMargins(2,0,0,0)
        self.setMaximumHeight(25)
        self.setMinimumHeight(25)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setObjectName('pathWidget')
        
    def setRootPath(self,path):
        self.RootPath = path
        self.path = path
        #rewrite_print(path)
        for Item in self.path.split('/'):
            ThisButton = QPushButton()
            ThisButton.setObjectName('PpathWidgetButton')
            ThisButton.setIcon(QIcon('./img/icons/folder.svg'))
            ThisButton.setText(Item + ' >')
            self.ThisLayout.addWidget(ThisButton)
        self.ThisLayout.addWidget(QWidget())
        self.ThisLayout.addStretch(999)
########################################################################

