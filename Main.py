import os,sys
import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import getpass
import time
#import core
from lib.StyleReader import StyleReader
from lib.newWindow import *
from lib.fileTreeView import CreateFileTree
from lib.readConfig import readConfig
import lib.WindowMenu as WindowMenuThis
import lib.core.ui.ChoicePanel as ChoicePanel
import lib.core.function.TabPanel
import lib.core.function.Starter as Starter
import lib.core.function.Setting as Setting
import lib.core.function.TabBar as TabBar
#more lib
from lib.core.ui.newPanelWindow import PanelWindow
#from function
import lib.core.function.About as About
#import base functions
from lib.base import *
print('in Main application')
#end
ColorLineList = []
WindowLineList = []
OptionWidgetList = []
Window_self = None
class PFrame(QFrame):
    #重写mousePressEvent事件
    def mousePressEvent(self,evt) -> None:
        global Window_self
        #color line
        ColorLine = self.findChild(QWidget,"ColorLine_"+self.objectName())
        #print(ColorLine)
        ColorLine.setStyleSheet('background:#4888FF;')
        for OtherLine in ColorLineList:
            if OtherLine != ColorLine:
                try:
                    OtherLine.setStyleSheet('background:rgba(0,0,0,0);')
                except:
                    pass
        #window line一根线，装饰用的
        Windowline = self.findChild(QWidget,"WindowLine_"+self.objectName())
        Windowline.setStyleSheet('background-image:url(./img/main_2/titlePanel.png);background-repeat:repeat-x;background-position:0px,center;')
        for OtherWindowLine in WindowLineList:
            if OtherWindowLine != Windowline:
                try:
                    OtherWindowLine.setStyleSheet('background:rgba(0,0,0,0);')
                except:
                    pass
        #option widget一整个选项条
        OptionWidget = self.findChild(QWidget,"option_"+self.objectName())
        OptionWidget.setStyleSheet("#"+"option_"+self.objectName()+'{background-color:#eee;}')
        for option_widget in OptionWidgetList:
            if option_widget != OptionWidget:
                try:
                    option_widget.setStyleSheet("#"+"option_"+self.objectName()+'{background-color:rgba(0,0,0,0);}')
                except:
                    pass
        #在子窗口类里的pos需要改一下，这个是什么？
        #print(evt.globalPos().x(),Window_self.geometry().x())
        PointPos = QPoint(evt.globalPos().x() - Window_self.geometry().x(),evt.globalPos().y() - Window_self.geometry().y())
        #print(PointPos)
        ChoicePanel.CheckRemoveThePanel(PointPos)
        #print(evt.x(),evt.y(),dir(self))
       
class NewEditor(MyWindow):
    def __init__(self):
        global Window_self
        super().__init__()
        Window_self = self
        globals()['SELF'] = self
        self.EditorList = []
        self.Editorindex = 0
        self.index = 0
        self.panelWindowCount = 0
        self.SettingWindowCount = 0
        self.LogIndex = 0
        self.outputIndex = 0
        self.childPanelCount = 0
        with open('./config/config.json','r',encoding='utf-8') as ReadConfig:
            self.Config = eval(ReadConfig.read())
        with open(self.Config['path']+'/'+self.Config['name']+'/.mcstudio/'+self.Config['name']+'.mcsProject','r',encoding='utf-8') as ProjectConfig:
            self.ProjectConfig = eval(ProjectConfig.read())
        self.AllChildWindow = {}
        self.ChildWindowCount = 1
        self.setting = {}
        self.initUI()
        self.Projectfolders = 0
        self.Projectfiles = 0
        self.UseTheme()
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
    def CreatChildWindow(self,parent:QWidget,mode,spliterList:list,Old_widget_splitter_to:str,layoutThis=None):#在这里创建了子面板
        if Old_widget_splitter_to == '1':
            #to <1> widget
            pass
        elif Old_widget_splitter_to == '2':
            #to <2> wdiget
            pass
        else:
            pass
        #负责分隔并且给每个块都附加上基础样式和控件，并且设置好内嵌父控件
        if layoutThis == None:
            MainWidgetlayout = QHBoxLayout()
            MainWidgetlayout.setContentsMargins(0,0,0,0)
            parent.setLayout(MainWidgetlayout)
        if mode == Qt.Vertical:
            NewSpliter = QSplitter(Qt.Vertical)
        elif mode == Qt.Horizontal:
            NewSpliter = QSplitter(Qt.Horizontal)
        NewSpliter.setObjectName("SPLITTERS")
        NewSpliter.setHandleWidth(2)
        #QFRAME分隔
        Qweiget_1 = PFrame()
        Qweiget_1.setObjectName('PURE_WIDGET_SPLITTER_'+str(self.ChildWindowCount))
        Qweiget_1.setStyleSheet('QFrame{background-color:#f9f9f9;border:1px solid #ddd;margin:0px;border-radius:3px;}')
        self.ChildWindowCount = self.ChildWindowCount + 1
        Qweiget_2 = PFrame()
        Qweiget_2.setObjectName('PURE_WIDGET_SPLITTER_'+str(self.ChildWindowCount))
        Qweiget_2.setStyleSheet('QFrame{background-color:#f9f9f9;border:1px solid #ddd;margin:0px;border-radius:3px;}')
        #命名
        self.ChildWindowCount = self.ChildWindowCount + 1
        NewSpliter.addWidget(Qweiget_1)
        Qweiget_1.setMinimumSize(0,0)#
        Qweiget_2.setMinimumSize(0,0)#
        NewSpliter.addWidget(Qweiget_2)
        NewSpliter.setSizes(spliterList)
        if layoutThis == None:
            MainWidgetlayout.addWidget(NewSpliter)
        else:
            layoutThis.addWidget(NewSpliter)
        WidgetList = [Qweiget_1,Qweiget_2]
        #重写mousePressEvent事件
        return WidgetList
        pass
    def makeTabWidget(self,StartTabList:list):
        self.Toptabs = QTabWidget()
        #tabs.setTabPosition(QTabWidget.West)
        self.Toptabs.setMovable(True)
        self.Toptabs.setTabsClosable(True)
        for TabName in StartTabList:
            globals()['QTabWidget_'+TabName] = QWidget()
            globals()['QTabWidget_'+TabName].setObjectName('thisTabWidget')
            #lib.core.function.TabPanel.AppendTabWidget(self,globals()['QTabWidget_'+TabName],TabName)#初始化tab栏
            self.Toptabs.addTab(globals()['QTabWidget_'+TabName],TabName)
        self.Toptabs.currentChanged.connect(self.on_tabWidget_currentChanged)
    def on_tabWidget_currentChanged(self):
        pass
    def openFolder(self):
        os.system('start '+self.setting['path']+'/'+self.setting['name'])

    def GetDir(self,Lastpath,tabCount):
        for file_name in os.listdir(Lastpath):
            if os.path.isdir(Lastpath+'//'+file_name) == True:
                #print(file_name)
                #is folder
                #print(Lastpath+'\\'+file_name)
                self.pathList.append(tabCount*'  '+file_name)
                self.Projectfolders = self.Projectfolders + 1
                self.GetDir(Lastpath+'\\'+file_name,tabCount = tabCount+1)
            else:
                self.pathList.append(tabCount*'  '+file_name)
                self.Projectfiles += 1
    def center(self):#居中_方法
        ScreenWidth = QGuiApplication.primaryScreen().geometry().width()
        ScreenHeight = QGuiApplication.primaryScreen().geometry().height()
        self.move(ScreenWidth/2 - self.W/2, ScreenHeight/2 - self.H/2)
    def initUI(self):
        #self.setFixedSize(self.W,self.H)#禁止改变大小
        self.User = getpass.getuser()
        #self.setGeometry(300, 300, 250, 150)
        # #(x, y, w, h)
        self.VboxLayOut_This = QVBoxLayout()
        self.VboxLayOut_This.setContentsMargins(0, 0, 0, 0)
        self.VboxLayOut_This.setSpacing(0)
        self.TopDIV = QWidget()
        self.TopDIV.setObjectName('TopDIV')
        self.TopDIV.setMinimumHeight(30)
        self.TopDIV.setMaximumHeight(30)
        #self.VboxLayOut_This.addWidget(self.TopDIV)
        #VBoxLayout
        self.Tool_head_DIV = QWidget(self.widget)
        self.Tool_head_DIV.move(30,0)
        self.Tool_head_DIV.resize(390,29)
        self.Tool_head_DIV.setObjectName('Tool_head_DIV')
        self.MakeToolDIV()
        #this
        #设置标题栏的tip-path
        self.label_2.setToolTip(self.Config['path'])
        self.makeTabWidget(TabBar.editors)
        #make tabs widget
        #self.MainWidget = QWidget()
        #self.MainWidget.setObjectName('MainWidget')
        self.boxlayout_1 = QVBoxLayout()
        self.boxlayout_1.setContentsMargins(0, 0, 0, 0)
        self.boxlayout_1.setSpacing(0)
        self.Toptabs.setContentsMargins(0,0,0,0)
        self.Toptabs.setObjectName('Toptabs')
        self.boxlayout_1.addWidget(self.Toptabs)
        #self.Toptabs.setMaximumHeight(45)
        #self.boxlayout_1.addWidget(self.MainWidget)
        self.BottomDiv = QWidget()
        self.BottomDiv.setContentsMargins(0,0,0,0)
        self.BottomDiv.setMaximumHeight(20)
        self.BottomDiv.setMinimumHeight(20)
        self.BottomDiv.setObjectName('BottomDiv')
        self.boxlayout_1.addWidget(self.BottomDiv)
        self.widget_2.setLayout(self.boxlayout_1)
        #init后续初始化
        #初始化-1
        self.MakeChildWindow()
    def recursiveDict(self,dict,parentWidget):
        SplitterSize = [0,0]
        This_Dict = {}
        for key in dict:
            if key != "PROJECT_LIST":
                if dict[key]['float'] == 'left' or dict[key]['float'] == 'right':
                    mode = Qt.Horizontal
                else:
                    mode = Qt.Vertical
                This_Dict[dict[key]['float']] = dict[key]['size']
        for i in This_Dict:
            if i == 'left' or i == 'top':
               SplitterSize[0] = This_Dict[i]
            else:
                SplitterSize[1] = This_Dict[i]
        WidgetList = self.CreatChildWindow(parentWidget,mode,SplitterSize,"1")#创建分隔控件
        #CreatChildWindow(self,parent,mode,spliterList:list,Old_widget_splitter_to:str):
        tempCount = 0
        for key_s in dict:#修饰样式以及子控件实现
            if key_s != "PROJECT_LIST":
                if dict[key_s]['Children'] != None:#如果他有children
                    self.recursiveDict(dict[key_s]['Children'],WidgetList[tempCount])#递归给子布局
                    #为父控件重置样式
                    WidgetList[tempCount].setContentsMargins(0,0,0,0)
                    WidgetList[tempCount].setStyleSheet("")
                else:
                    self.SetChildWindow_STYLE(WidgetList[tempCount],dict[key_s])#设置样式的吧
                tempCount += 1#tempCount自加1
    def SetChildWindow_STYLE(self,widget,dict:dict):
        #set the child window's style
        #颜色条
        ChildLayout = QVBoxLayout()
        ChildLayout.setContentsMargins(0,0,0,0)
        ChildLayout.setSpacing(0)
        #layout end
        ColorLine = QWidget()
        ColorLine.setMaximumHeight(2)
        ColorLine.setMinimumHeight(2)
        ColorLine.setStyleSheet('')
        ColorLine.setStyleSheet('background-color:rgba(0,0,0,0);border:0px')
        ColorLine.setObjectName("ColorLine_"+widget.objectName())
        ColorLineList.append(ColorLine)
        #top-option-widget
        OptionWidget = QWidget()
        OptionWidget.setStyleSheet('')
        OptionWidget.setMinimumHeight(20)
        OptionWidget.setMaximumHeight(20)
        OptionWidget.setObjectName('option_'+widget.objectName())
        OptionWidgetList.append(OptionWidget)
        #make the option buttons
        #close button->
        OptionLayout = QHBoxLayout()#layout this widget
        #end of layout
        CloseButton = QPushButton()#关闭此面板
        CloseButton.setObjectName('Close_Button')#完成
        CloseButton.setMaximumHeight(20)
        CloseButton.setMaximumWidth(20)
        CloseButton.setToolTip("Close the Panel")
        CloseButton.clicked.connect(self.closePanel)
        #setting
        settingButton = QPushButton()#设置此面板
        settingButton.setObjectName('setting_Button')
        settingButton.setMaximumHeight(20)
        settingButton.setMaximumWidth(20)
        settingButton.setToolTip('Setting Panel')
        #splitter
        splitterButton = QPushButton()#分割此面板
        splitterButton.setObjectName(dict['Window'])
        splitterButton.setMaximumHeight(20)
        splitterButton.setMaximumWidth(20)
        splitterButton.setStyleSheet('''
*{background-image: url(./img/main/split.png);
background-color: rgba(0, 0, 0, 0.0);
background-repeat: no-repeat;
background-position: center center;}
:hover {
    background-color: #eee;
    border: 1px solid #ccc;
}''')
        splitterButton.setToolTip('Split the Panel - Horizontal')
        splitterButton.clicked.connect(self.splitPanel)
        #split-v
        splitterButton_v = QPushButton()#分割此面板
        splitterButton_v.setObjectName(dict['Window'])
        splitterButton_v.setMaximumHeight(20)
        splitterButton_v.setMaximumWidth(20)
        splitterButton_v.setStyleSheet('''
*{background-image: url(./img/main/split_v.png);
background-color: rgba(0, 0, 0, 0.0);
background-repeat: no-repeat;
background-position: center center;}
:hover {
    background-color: #eee;
    border: 1px solid #ccc;
}''')
        splitterButton_v.setToolTip('Split the Panel - Vertical')
        splitterButton_v.clicked.connect(self.splitPanel_V)
        #out window
        outButton = QPushButton()#弹出此面板
        outButton.setObjectName(dict['Window'])
        outButton.setMaximumHeight(20)
        outButton.setMaximumWidth(20)
        outButton.setStyleSheet('''
*{background-image: url(./img/main/out3_2.png);
background-color: rgba(0, 0, 0, 0.0);
background-repeat: no-repeat;
background-position: center center;}
:hover {
    background-color: #eee;
    border: 1px solid #ccc;
}''')
        outButton.setToolTip('Pop up window')
        outButton.clicked.connect(self.PopUpWindow)
        #Line->
        Line = QWidget()#子窗口的分割线
        Line.setObjectName("WindowLine_"+widget.objectName())
        Line.setMaximumHeight(7)
        #Window name->
        WindowName = QPushButton(dict['Window'])#主类名
        WindowName.clicked.connect(self.OutTheChoicePanel)
        WindowName.setToolTip(dict['Window'])
        WindowLineList.append(Line)
        #给名称设置样式-icon
        IconPath = WindowMenuThis.WindowMenu[dict['Window']]['icon']
        WindowName.setIcon(QIcon(IconPath))
        WindowName.setStyleSheet('background-image: url(./img/bottom_to.png);background-position:right center;background-repeat:no-repeat;')
        #WindowName.setMaximumWidth(7*len(dict['Window']))
        WindowName.setObjectName('WindowName')
        #set layout
        OptionLayout.addWidget(WindowName)
        OptionLayout.addWidget(Line)
        OptionLayout.setStretch(1,2)
        OptionLayout.addWidget(outButton)
        OptionLayout.addWidget(splitterButton)
        OptionLayout.addWidget(splitterButton_v)
        OptionLayout.addWidget(settingButton)
        OptionLayout.addWidget(CloseButton)
        OptionLayout.setSpacing(0)
        CloseButton.setContentsMargins(0,0,0,0)
        OptionWidget.setContentsMargins(0,0,0,0)
        OptionLayout.setContentsMargins(2,0,0,0)
        OptionWidget.setLayout(OptionLayout)
        #Main-widget
        Child_main_widget = QWidget()
        Child_main_widget.setObjectName('Child_main_widget_'+str(self.childPanelCount))
        #立刻加一咯
        self.childPanelCount = self.childPanelCount + 1
        #add widget to layout
        ChildLayout.addWidget(ColorLine)
        ChildLayout.addWidget(OptionWidget)
        ChildLayout.addWidget(Child_main_widget)
        widget.setLayout(ChildLayout)
        #初始化面板->this:1
        Starter.PanelStarter(WindowName,self,dict['Window'])#def PanelStarter(Sender:QPushButton,self,Name) -> None:#导入模块部分
        pass
    def OutTheChoicePanel(self):
        #print(self.geometry())
        ChoicePanel.OutTheChoicePanel(self.sender(),self,self.geometry())
    def MakeChildWindow(self):
        #make childewindow
        for item in TabBar.editors:
            globals()['QTabWidget_'+item].setContentsMargins(2,2,2,2)
            #self.MainWidget.setContentsMargins(2,2,2,2)
            try:
                self.recursiveDict(WindowMenuThis.StarterInfo[item],globals()['QTabWidget_'+item])#产生窗口
                print('[info] : successful started<'+item+f'> {str(time.localtime().tm_hour)}:{str(time.localtime().tm_min)}:{str(time.localtime().tm_sec)} \n')
            except Exception as e:
                print(WindowMenuThis)
                print('[Error] : Starter<'+item+f'> failed {str(time.localtime().tm_hour)}:{str(time.localtime().tm_min)}:{str(time.localtime().tm_sec)}\n',e)
                print(traceback.format_exc())
    def MakeToolDIV(self):#菜单栏部分
        self.ToolBar = []
        self.layoutBox_Head = QHBoxLayout()
        #layout
        self.Tool_file = QPushButton('文件(F)')
        self.Tool_edit = QPushButton('编辑(E)')
        self.Tool_select = QPushButton('选择(S)')
        self.Tool_run = QPushButton("运行(R)")
        self.Tool_control = QPushButton("设置(C)")
        self.Tool_control.clicked.connect(self.Tool_control_clicked)
        self.Tool_help = QPushButton("帮助(H)")
        self.Tool_about = QPushButton("关于(A)")
        self.Tool_about.clicked.connect(self.Tool_about_APP)
        self.layoutBox_Head.addWidget(self.Tool_file)
        self.layoutBox_Head.addWidget(self.Tool_edit)
        self.layoutBox_Head.addWidget(self.Tool_select)
        self.layoutBox_Head.addWidget(self.Tool_run)
        self.layoutBox_Head.addWidget(self.Tool_control)
        self.layoutBox_Head.addWidget(self.Tool_help)
        self.layoutBox_Head.addWidget(self.Tool_about)
        self.layoutBox_Head.setSpacing(0)
        self.layoutBox_Head.setContentsMargins(0,0,0,0)
        #list
        self.ToolBar.append(self.Tool_file)
        self.ToolBar.append(self.Tool_edit)
        self.ToolBar.append(self.Tool_select)
        self.ToolBar.append(self.Tool_run)
        self.ToolBar.append(self.Tool_control)
        self.ToolBar.append(self.Tool_help)
        self.ToolBar.append(self.Tool_about)
        #self
        self.Tool_head_DIV.setLayout(self.layoutBox_Head)
    #非UI的都写在下面
    def UseTheme(self):
        styleFile = './style/main.qss'
        qssStyle = StyleReader.readQSS(styleFile)
        self.setStyleSheet(qssStyle)
    def focusInEvent(self, a0: PyQt5.QtGui.QFocusEvent):
        # super().focusInEvent(a0)
        self.label_2.setStyleSheet('color:#666 !important;')
        for Button in self.ToolBar:
            Button.setStyleSheet('color:#232323;')
    def focusOutEvent(self, a0: PyQt5.QtGui.QFocusEvent):
        self.label_2.setStyleSheet('color:#aaa !important;')
        for Button in self.ToolBar:
            Button.setStyleSheet('color:#666;')
        pass
    def closeEvent(self, event):
        with open('./config/config.json','r',encoding='utf-8') as ReadConfig:
            getThisConfig = eval(ReadConfig.read())
        getThisConfig['w'] = self.width()
        getThisConfig['h'] = self.height()
        getThisConfig['x'] = self.x()
        getThisConfig['y'] = self.y()
        with open('./config/config.json','w',encoding='utf-8') as NewConfig:
            NewConfig.write(str(getThisConfig))
        pass
    #window.menu function this
    #一些其他的函数
    #some other function
    def Strange_recursive_delete(self,sender,recursive):
        if recursive > 0:
            if sender.parent().parent().__class__ == PFrame:
                print('this is the Pframe',sender.parent().parent())
                if sender.parent().count() == 1:
                    print('delete')
                    if sender.parent().parent().parent().count() == 1:
                        self.Strange_recursive_delete(sender.parent().parent(),recursive-1)
                    else:
                        recursive = 0
                    sender.parent().parent().deleteLater()
                    #如果在子空间内的2个面板被全部删除，则删除这个子空间的父部件
    def closePanel(self):
        sender = self.sender()
        #print(sender.parent().parent().parent())
        out = 1
        ThisIndex = sender.parent().parent().parent().indexOf(sender.parent().parent())
        if ThisIndex == 1:
            out = 0
        sender.parent().parent().deleteLater()
        #print(sender.parent().parent().parent().count())
        sender.parent().parent().parent().setSizes([100])
        #print(sender.parent().parent().parent().parent())
        recursive = int(self.ChildWindowCount/2) + 1#最小递归次数，可以被count = 0时提前返回
        self.Strange_recursive_delete(sender.parent().parent(),recursive)
        sender.parent().parent().parent().setSizes([100])
    #改写一个接受参数的
    def closePanel_sender(self,sender):
        #print(sender.parent().parent().parent())
        out = 1
        ThisIndex = sender.parent().parent().parent().indexOf(sender.parent().parent())
        if ThisIndex == 1:
            out = 0
        sender.parent().parent().deleteLater()
        #print(sender.parent().parent().parent().count())
        sender.parent().parent().parent().setSizes([100])
        #print(sender.parent().parent().parent().parent())
        recursive = int(self.ChildWindowCount/2) + 1#最小递归次数，可以被count = 0时提前返回
        self.Strange_recursive_delete(sender.parent().parent(),recursive)
        sender.parent().parent().parent().setSizes([100])
    def splitPanel(self):
        senderThis = self.sender()
        try:
            for line in ColorLineList:
                if line.objectName() == "ColorLine_"+senderThis.parent().parent().objectName():
                    ColorLineList.remove(line)
                    break
            for wline in WindowLineList:
                if wline.objectName() == "WindowLine_"+senderThis.parent().parent().objectName():
                    WindowLineList.remove(wline)
                    break
            for oline in OptionWidgetList:
                if oline.objectName() == "option_"+senderThis.parent().parent().objectName():
                    OptionWidgetList.remove(oline)
                    break
        except:
            pass
        thisSplitterWidget = senderThis.parent().parent()
        ThisLayout = thisSplitterWidget.layout()
        #thisSplitterWidget.setLayout(None)
        item_list = list(range(ThisLayout.count()))
        item_list.reverse()# 倒序删除，避免影响布局顺序
        for i in item_list:
            item = ThisLayout.itemAt(i)
            ThisLayout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()
        getWidget = self.CreatChildWindow(thisSplitterWidget,Qt.Horizontal,[10,10],"1",layoutThis=ThisLayout)#创建分隔控件
        thisSplitterWidget.setStyleSheet("")
        self.SetChildWindow_STYLE(getWidget[0],{'Window':senderThis.objectName()})#0
        self.SetChildWindow_STYLE(getWidget[1],{'Window':'White'})#1
    #复制一个splitPanel_V
    def splitPanel_V(self):
        senderThis = self.sender()
        #print(ColorLineList)
        try:
            for line in ColorLineList:
                if line.objectName() == "ColorLine_"+senderThis.parent().parent().objectName():
                    ColorLineList.remove(line)
                    break
            for wline in WindowLineList:
                if wline.objectName() == "WindowLine_"+senderThis.parent().parent().objectName():
                    WindowLineList.remove(wline)
                    break
            for oline in OptionWidgetList:
                if oline.objectName() == "option_"+senderThis.parent().parent().objectName():
                    OptionWidgetList.remove(oline)
                    break
        except:
            pass
        #'option_'+widget.objectName()
        thisSplitterWidget = senderThis.parent().parent()
        ThisLayout = thisSplitterWidget.layout()
        #thisSplitterWidget.setLayout(None)
        item_list = list(range(ThisLayout.count()))
        item_list.reverse()# 倒序删除，避免影响布局顺序
        for i in item_list:
            item = ThisLayout.itemAt(i)
            ThisLayout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()
        getWidget = self.CreatChildWindow(thisSplitterWidget,Qt.Vertical,[10,10],"1",layoutThis=ThisLayout)#创建分隔控件
        thisSplitterWidget.setStyleSheet("")
        self.SetChildWindow_STYLE(getWidget[0],{'Window':senderThis.objectName()})#0
        self.SetChildWindow_STYLE(getWidget[1],{'Window':'White'})#1
    #PopUpWindow可能会有点复杂
    def PopUpWindow(self):
        sender = self.sender()
        Frame_X = sender.pos().x()
        Frame_Y = sender.pos().y()
        Width_ = sender.parent().parent().width()
        Height_ = sender.parent().parent().height()
        ThisSenderName = sender.objectName()
        Pos_X = sender.mapToGlobal(sender.pos()).x()#控件相对于屏幕的位置
        Pos_Y = sender.mapToGlobal(sender.pos()).y()
        print(Pos_X,Pos_Y,Width_,Height_)
        globals()['PanelWindow_This_'+str(self.panelWindowCount)] = PanelWindow()
        thisWindow = globals()['PanelWindow_This_'+str(self.panelWindowCount)]
        thisWindow.resize(Width_+35,Height_+28)
        thisWindow.show()
        screen = QDesktopWidget().screenGeometry()
        print(Frame_X,Width_)
        size = thisWindow.geometry()
        thisWindow.move(Pos_X - Frame_X - (Width_) + sender.width() + 62,Pos_Y - Frame_Y - 14)
        #globals()['PanelWindow_This_'+str(self.panelWindowCount)].label_2.setText(ThisSenderName)
        #globals()['PanelWindow_This_'+str(self.panelWindowCount)].setMaximumSize(Width_,Height_)
        print(thisWindow.geometry())
        #
        thisWindow.Config = self.Config
        #
        thisWindow.WindowName.setText(sender.objectName())
        #thisWindow.WindowName.clicked.connect(self.OutTheChoicePanel)
        thisWindow.WindowName.setToolTip(sender.objectName())
        #WindowLineList.append(Line)
        #给名称设置样式-icon
        IconPath = WindowMenuThis.WindowMenu[sender.objectName()]['icon']
        thisWindow.WindowName.setIcon(QIcon(IconPath))
        thisWindow.WindowName.setStyleSheet('''background-image: url(./img/bottom_to.png);
                                            background-position:right center;
                                            background-repeat:no-repeat;
                                            padding-right:15px;
                                            background-color:#CAE6FC;
                                            margin-left:5px;
                                            border-radius:4px;''')
        #WindowName.setMaximumWidth(7*len(dict['Window']))
        thisWindow.WindowName.setObjectName('WindowName')
        #thisWindow.horizontalLayout.addWidget(thisWindow.WindowName)
        thisWindow.WindowName.move(15,15)
        Starter.PanelStarter(thisWindow.WindowName,thisWindow,sender.objectName())#def PanelStarter(Sender:QPushButton,self,Name) -> None:#导入模块部分
        Name = sender.objectName()
        thisLayout = QVBoxLayout()
        thisLayout.setContentsMargins(0,0,0,0)
        thisLayout.setSpacing(0)
        #thisWindow.widget_2.setStyleSheet('*{border-bottom-left-radius:7px;border-bottom-right-radius:7px;}')
        thisWindow.widget_2.setLayout(thisLayout)
        #give value
        thisWindow.EditorList = self.EditorList
        thisWindow.Editorindex = self.Editorindex
        thisWindow.index = self.index
        thisWindow.panelWindowCount = self.panelWindowCount
        thisWindow.SettingWindowCount = self.SettingWindowCount
        thisWindow.LogIndex = self.LogIndex
        thisWindow.outputIndex = self.outputIndex
        thisWindow.childPanelCount = self.childPanelCount
        thisWindow.Config = self.Config
        thisWindow.ProjectConfig = self.ProjectConfig
        thisWindow.AllChildWindow = self.AllChildWindow
        thisWindow.ChildWindowCount = self.ChildWindowCount
        thisWindow.setting = self.setting
        thisWindow.Projectfolders = self.Projectfolders
        thisWindow.Projectfiles = self.Projectfiles
        #give value
        exec(f"lib.core.module.{Name}.init(thisLayout,'{Name}',thisWindow)")#进入主初始化模块
        self.closePanel_sender(sender)#删除面板
        self.panelWindowCount += 1
    def Tool_about_APP(self):
        #about the application
        print('open about window')
        #window.menu function this -> Tool_control_clicked
        sender = self.sender()
        globals()['NewAboutWindow_'+str(self.SettingWindowCount)] = PanelWindow()#直接复用好了
        styleFile = './style/main.qss'
        qssStyle = StyleReader.readQSS(styleFile)
        thisAbout = globals()['NewAboutWindow_'+str(self.SettingWindowCount)]
        thisAbout.setStyleSheet(qssStyle)
        thisAbout.resize(400,177)
        screen = QDesktopWidget().screenGeometry()
        size = thisAbout.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)
        thisAbout.move(newLeft,newTop)
        thisAbout.WindowName.setText('About')
        thisAbout.WindowName.setStyleSheet('margin-left:7px;')
        MainLayout = QVBoxLayout()
        thisAbout.widget_2.setLayout(MainLayout)
        #thisAbout.widget_2.setStyleSheet('background-color:#f9f9f9;')
        #thisAbout.widget.setStyleSheet('background-color:#fff;')
        MainLayout.addWidget(About.MakeAbout())
        thisAbout.show()
        self.SettingWindowCount += 1#自加
    def Tool_control_clicked(self):
        print('open settings window')
        #window.menu function this -> Tool_control_clicked
        sender = self.sender()
        globals()['NewSettingWindow_'+str(self.SettingWindowCount)] = Setting.SettingWindow(self,self.User)#直接复用好了
        ThisSetting = globals()['NewSettingWindow_'+str(self.SettingWindowCount)]
        styleFile = './style/main.qss'
        qssStyle = StyleReader.readQSS(styleFile)
        screen = QDesktopWidget().screenGeometry()
        size = ThisSetting.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)
        ThisSetting.WindowName.setText('Setting - '+self.User)
        ThisSetting.setWindowTitle('Setting - '+self.User)
        ThisSetting.WindowName.setStyleSheet('margin-left:7px;')
        ThisSetting.setStyleSheet(qssStyle)
        ThisSetting.resize(760,660)
        ThisSetting.move(newLeft,newTop)
        ThisSetting.show()
        self.SettingWindowCount += 1#自加
    def getAllWidget(self,lastWidget):
        for widget in lastWidget.children():
            rewrite_print(widget)
            try:
                widget.setStyleSheet('')
            except:
                pass
            if len(widget.children()) != 0:
                self.getAllWidget(widget)