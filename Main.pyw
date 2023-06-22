import os
import sys
import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import getpass
import time
# import core
from lib.StyleReader import StyleReader
from lib.fileTreeView import CreateFileTree
from lib.readConfig import readConfig
import lib.WindowMenu as WindowMenuThis
import lib.core.ui.ChoicePanel as ChoicePanel
import lib.core.function.TabPanel
import lib.core.function.Starter as Starter
import lib.core.function.Setting as Setting
import lib.core.function.TabBar as TabBar
# more lib
from lib.core.ui.newPanelWindow import PanelWindow
# from function
import lib.core.function.About as About
# import base functions
from lib.base import *
# from start import START
print('in Main application')
# end
# theme
WindowLineList = []
OptionWidgetList = []
Window_self = None
SELF = None


class PFrame(QFrame):
    # 重写mousePressEvent事件
    def mousePressEvent(self, evt) -> None:
        global Window_self
        # color line

        Windowline = self.findChild(QWidget, "WindowLine_"+self.objectName())
        self.setStyleSheet('#'+self.objectName() +
                           '{border:1px solid #4888FF;border-radius:0px;}')
        Windowline.setStyleSheet(
            'background-image:url(./img/main_2/titlePanel.png);background-repeat:repeat-x;background-position:0px,center;')
        for OtherWindowLine in WindowLineList:
            if OtherWindowLine != Windowline:
                try:
                    OtherWindowLine.parent().parent().setStyleSheet('#'+OtherWindowLine.parent().parent().objectName() +
                                                                    '{border-radius:0px;}')
                    OtherWindowLine.setStyleSheet('background:rgba(0,0,0,0);')
                except:
                    pass
        # option widget一整个选项条
        OptionWidget = self.findChild(QWidget, "option_"+self.objectName())
        OptionWidget.setStyleSheet("#"+"option_"+self.objectName()+'{}')
        for option_widget in OptionWidgetList:
            if option_widget != OptionWidget:
                try:
                    option_widget.setStyleSheet(
                        "#"+"option_"+self.objectName()+'{background-color:rgba(0,0,0,0);}')
                except:
                    pass
        # 在子窗口类里的pos需要改一下，这个是什么？
        # print(evt.globalPos().x(),Window_self.geometry().x())
        PointPos = QPoint(evt.globalPos().x() - Window_self.geometry().x(),
                          evt.globalPos().y() - Window_self.geometry().y())
        # print(PointPos)
        ChoicePanel.CheckRemoveThePanel(PointPos)
        # print(evt.x(),evt.y(),dir(self))


class NewEditor(QMainWindow):
    def __init__(self, app, start):
        # start
        QtWidgets.qApp.processEvents()

        print_('[!] : start MCS')
        global Window_self
        super().__init__()
        Window_self = self
        globals()['SELF'] = self
        self.theme = '#555'
        self.start = start
        #
        self.start.prompt.setText(f'进入主程序准备阶段 . . . {str(self.start.pv)}%')
        QtWidgets.qApp.processEvents()
        #
        self.EditorList = []
        self.app = app
        self.Editorindex = 0
        self.Theme = {'bg': '#ededed', 'QFrame': '#f9f9f9'}
        self.index = 0
        self.panelWindowCount = 0
        self.SettingWindowCount = 0
        self.OPEN_VTK_WIDGET = []
        self.VTK_render = []
        self.IsReloading = False
        self.VTK_irender = []
        self.WebList = []
        self.TREE_VIEW = []
        self.openTerminal = True
        self.makeTerminal()
        self.QLABEL_NBT_ASCII_Name_LIST = []
        self.HEX_VIEW = []
        self.ASCII_VIEW = []
        self.QLABEL_NBT_name_LIST = []
        self.AllChildWindow = {}
        self.ChildWindowCount = 1
        self.setting = {}
        self.thread_count = 0
        self.LogIndex = 0
        self.outputIndex = 0
        self.childPanelCount = 0
        self.Projectfolders = 0
        self.Projectfiles = 0
        self.newUntitledFileCount = 0
        self.py_list = ['3.8', '3.9', '3.10', '3.11', 'auto']
        self.version_list = ['0.1', '0.2', '0.3', 'auto']
        #
        with open('./config/config.json', 'r', encoding='utf-8') as ReadConfig:
            self.Config = eval(ReadConfig.read())
        with open(self.Config['path']+'/'+self.Config['name']+'/.mcstudio/'+self.Config['name']+'.mcsProject', 'r', encoding='utf-8') as ProjectConfig:
            self.ProjectConfig = eval(ProjectConfig.read())
        self.initUI()
        self.UseTheme()
        self.updateOutPut()
        self.make_extend_menuBar()
        print_('[!] : end start MCS')
        print_(f'use time:{process_time()}s')
        self.activateWindow()
        self.setFocus()

    def make_extend_menuBar(self):
        h_line1 = QFrame()
        h_line1.setFrameShape(QFrame.VLine)
        h_line1.setFrameShadow(QFrame.Sunken)
        ################################
        self.TopMenuBar = QWidget(self)
        self.TopMenuBar.setMinimumWidth(260)
        self.TopMenuBar.setObjectName('TopMenuBar')
        self.TopMenuBar.setStyleSheet(
            '''
#TopMenuBar{background-color:rgba(0,0,0,0);}
#TopMenuBar QLabel {
    background-color:rgba(0,0,0,0);
}
#TopMenuBar QPushbutton {
    background-color:rgba(0,0,0,0);
}
#TopMenuBar QCombox {
    background-color:rgba(0,0,0,0);
}
#run {
    background-color:rgba(0,0,0,0);
}
            ''')
        self.TopMenuBar.setMaximumHeight(26)
        this_layout = QHBoxLayout(self.TopMenuBar)
        this_layout.setContentsMargins(0, 0, 0, 0)

        self.TopMenuBar.move(460, 1)
        #
        this_layout.addWidget(h_line1)
        #
        self.Game_Version = QComboBox(self)
        self.Game_Version.setMinimumWidth(80)
        self.Game_Version.setView(QListView())
        this_layout.addWidget(self.Game_Version)
        ################################
        for version in self.version_list:
            self.Game_Version.addItem(QIcon("./img/Minecraft.png"), version)
        # minecraft version
        h_line2 = QFrame()
        h_line2.setFrameShape(QFrame.VLine)
        h_line2.setFrameShadow(QFrame.Sunken)
        this_layout.addWidget(h_line2)
        # run
        run = QPushButton()
        run.setIcon(QIcon('./img/icons/play.svg'))
        run.setText('run')
        run.setObjectName('run')
        this_layout.addWidget(run)
        #
        h_line3 = QFrame()
        h_line3.setFrameShape(QFrame.VLine)
        h_line3.setFrameShadow(QFrame.Sunken)
        this_layout.addWidget(h_line3)
        # python version
        self.py_Version = QComboBox()
        self.py_Version.setView(QListView())
        self.py_Version.setMinimumWidth(80)
        this_layout.addWidget(self.py_Version)
        for py in self.py_list:
            self.py_Version.addItem(QIcon("./img/file/icons/python.svg"), py)
        # minecraft version
        h_line4 = QFrame()
        h_line4.setFrameShape(QFrame.VLine)
        h_line4.setFrameShadow(QFrame.Sunken)
        this_layout.addWidget(h_line4)
        # folder
        folder = QPushButton(self)
        folder.setText(self.Config['name'])
        folder.setIcon(QIcon('./img/file/icons/folder-queue-open.svg'))
        folder.setObjectName('folder')
        folder.setStyleSheet('''
#folder{background-color:rgba(0, 127, 212,0.15);border:1px solid #007FD4;}
#folder:hover {
    background-color:rgba(150,150,150,0.4);
} ''')
        folder.move(355, 2)
        folder.clicked.connect(self.openProject)
        folder.setMaximumHeight(23)

    def updateOutPut(self):
        with open('./log.txt', 'r', encoding='utf-8') as output:
            self.OutPut_Widget.setText(output.read())

    def openProject(self):
        os.system('start "" "'+self.Config['path']+'/'+self.Config['name']+'"')

    def UseTheme(self):
        self.setStyleSheet('''
QSplitter::handle {
    background-color: rgba(0, 0, 0, 0.0);
    margin: 0px !important;
    padding: 0px !important;
    border: 0px !important;
}
QSplitter::handle:pressed  {
    border: 0px !important;
}
#ChoiceButton_this {
    border-radius: 5px !important;

    text-align: left;
    margin-left: 5px;
    margin-right: 5px;
    padding-left: 3px;

    border: 1px solid #567dbc;
    margin-top: 2px;
    margin-bottom: 2px;
}
#smallTitle {
    border: 0px;
    border-bottom: 1px solid #aaa;
    color:gray;
    text-align: left;
    background-color: rgba(0, 0, 0, 0.0);
    border-radius: 0px !important;
    margin-left: 5px;
    margin-right: 5px;
    margin-bottom: 5px;
    margin-top: 5px;
    padding-left: 5px;
    font-size: 11.5px;
}
* {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
QTabWidget::pane{
	border-right:0px;
    border-bottom:0px;
}
QTabWidget {
    border-right:0px;
    border-bottom:0px;
}

    ''')

    def CreatChildWindow(self, parent: QWidget, mode, spliterList: list, Old_widget_splitter_to: str, layoutThis=None):  # 在这里创建了子面板
        if Old_widget_splitter_to == '1':
            # to <1> widget
            pass
        elif Old_widget_splitter_to == '2':
            # to <2> wdiget
            pass
        else:
            pass
        # 负责分隔并且给每个块都附加上基础样式和控件，并且设置好内嵌父控件
        if layoutThis == None:
            MainWidgetlayout = QHBoxLayout()
            MainWidgetlayout.setContentsMargins(0, 0, 0, 0)
            parent.setLayout(MainWidgetlayout)
        if mode == Qt.Vertical:
            NewSpliter = QSplitter(Qt.Vertical)
        elif mode == Qt.Horizontal:
            NewSpliter = QSplitter(Qt.Horizontal)
        NewSpliter.setObjectName("SPLITTERS")
        NewSpliter.setStyleSheet('''
background-color: rgba(0, 0, 0, 0.0);
margin: 0px !important;
padding: 0px !important;
''')
        NewSpliter.setHandleWidth(3)
        # QFRAME分隔
        QWidget_1 = PFrame()
        QWidget_1.setObjectName(
            'PURE_WIDGET_SPLITTER_'+str(self.ChildWindowCount))
        QWidget_1.setStyleSheet(
            '#PURE_WIDGET_SPLITTER_'+str(self.ChildWindowCount) + '{margin:0px;border-radius:0px;}')
        self.ChildWindowCount = self.ChildWindowCount + 1
        QWidget_2 = PFrame()
        QWidget_2.setObjectName(
            'PURE_WIDGET_SPLITTER_'+str(self.ChildWindowCount))
        QWidget_2.setStyleSheet(
            '#PURE_WIDGET_SPLITTER_'+str(self.ChildWindowCount) + '{margin:0px;border-radius:0px;}')
        # 命名
        # 设置边框

        # end
        self.ChildWindowCount = self.ChildWindowCount + 1
        NewSpliter.addWidget(QWidget_1)
        QWidget_1.setMinimumSize(0, 0)
        QWidget_2.setMinimumSize(0, 0)
        NewSpliter.addWidget(QWidget_2)
        NewSpliter.setSizes(spliterList)
        if layoutThis == None:
            MainWidgetlayout.addWidget(NewSpliter)
        else:
            layoutThis.addWidget(NewSpliter)
        WidgetList = [QWidget_1, QWidget_2]
        # 重写mousePressEvent事件
        return WidgetList
        pass

    def makeTabWidget(self, StartTabList: list):
        self.Toptabs = QTabWidget()
        # tabs.setTabPosition(QTabWidget.West)
        self.Toptabs.setMovable(True)
        self.Toptabs.setTabsClosable(True)
        for TabName in StartTabList:
            globals()['QTabWidget_'+TabName] = QWidget()
            globals()['QTabWidget_'+TabName].setObjectName('thisTabWidget')
            # lib.core.function.TabPanel.AppendTabWidget(self,globals()['QTabWidget_'+TabName],TabName)#初始化tab栏
            self.Toptabs.addTab(globals()['QTabWidget_'+TabName], TabName)
            QtWidgets.qApp.processEvents()

    def openFolder(self):
        os.system('start '+self.setting['path']+'/'+self.setting['name'])

    def GetDir(self, Lastpath, tabCount):
        for file_name in os.listdir(Lastpath):
            if os.path.isdir(Lastpath+'//'+file_name) == True:
                # print(file_name)
                # is folder
                # print(Lastpath+'\\'+file_name)
                self.pathList.append(tabCount*'  '+file_name)
                self.Projectfolders = self.Projectfolders + 1
                self.GetDir(Lastpath+'\\'+file_name, tabCount=tabCount+1)
            else:
                self.pathList.append(tabCount*'  '+file_name)
                self.Projectfiles += 1

    def center(self):  # 居中_方法
        ScreenWidth = QGuiApplication.primaryScreen().geometry().width()
        ScreenHeight = QGuiApplication.primaryScreen().geometry().height()
        self.move(ScreenWidth/2 - self.W/2, ScreenHeight/2 - self.H/2)

    def initUI(self):
        # self.setFixedSize(self.W,self.H)#禁止改变大小
        self.THIS_MAIN_WIDGET = QWidget()
        self.setCentralWidget(self.THIS_MAIN_WIDGET)
        self.User = getpass.getuser()
        # self.setGeometry(300, 300, 250, 150)
        # #(x, y, w, h)
        self.VboxLayOut_This = QVBoxLayout()
        self.VboxLayOut_This.setContentsMargins(0, 0, 0, 0)
        self.VboxLayOut_This.setSpacing(0)
        self.TopDIV = QWidget()
        self.TopDIV.setObjectName('TopDIV')
        self.TopDIV.setMinimumHeight(30)
        self.TopDIV.setMaximumHeight(30)
        # self.VboxLayOut_This.addWidget(self.TopDIV)
        # VBoxLayout
        '''self.Tool_head_DIV = QWidget(self.widget)
        self.Tool_head_DIV.move(30,0)
        self.Tool_head_DIV.resize(390,29)
        self.Tool_head_DIV.setObjectName('Tool_head_DIV')'''
        self.MakeToolDIV()
        # this
        # 设置标题栏的tip-path
        self.makeTabWidget(TabBar.editors)
        # make tabs widget
        # self.MainWidget = QWidget()
        # self.MainWidget.setObjectName('MainWidget')
        self.boxlayout_1 = QVBoxLayout()
        self.boxlayout_1.setContentsMargins(0, 0, 0, 0)
        self.boxlayout_1.setSpacing(0)
        self.Toptabs.setContentsMargins(0, 0, 0, 0)
        self.Toptabs.setObjectName('Toptabs')
        self.boxlayout_1.addWidget(self.Toptabs)
        self.Toptabs.tabBarClicked.connect(self.reloadEditor)
        # self.Toptabs.setMaximumHeight(45)
        # self.boxlayout_1.addWidget(self.MainWidget)
        self.THIS_MAIN_WIDGET.setLayout(self.boxlayout_1)
        self.THIS_MAIN_WIDGET.setObjectName('THIS_MAIN_WIDGET')
        # init后续初始化
        # 初始化-1
        self.MakeChildWindow()
        #
        self.setWindowIcon(QIcon('./img/appicon/icon32.png'))
        self.UseToolBar()
        # Status
        self.StatusText = 'MCS already started'
        self.status = self.statusBar()
        self.status.setContentsMargins(0, 0, 0, 0)
        # 状态栏本身显示的信息 第二个参数是信息停留的时间，单位是毫秒，默认是0（0表示在下一个操作来临前一直显示）
        self.status.showMessage(self.StatusText, 0)
        self.APP_MEMORY = 4*1024  # 4GB内存
        self.Memory = MemoryWidget()
        #
        self.UseMemory = UseMemory(self.APP_MEMORY)
        #
        self.HELP_button = QPushButton()
        self.HELP_button.setIcon(QIcon('./img/icons/help-circle.svg'))
        self.HELP_button.setFixedSize(16, 16)
        #
        self.INFO = QPushButton()
        self.INFO.setIcon(QIcon('./img/icons/message-square.svg'))
        self.INFO.setFixedSize(16, 16)
        #
        self.status.addPermanentWidget(self.UseMemory, stretch=0)
        self.status.addPermanentWidget(self.Memory, stretch=0)
        self.status.addPermanentWidget(self.INFO, stretch=0)

        self.status.addPermanentWidget(self.HELP_button, stretch=0)
        #

    def reloadEditor(self, a0):
        Name = SELF.Toptabs.tabText(a0)
        if Name == 'Editor':
            if self.IsReloading == False:
                print('reloading')
                self.WebList[0].reload()
                self.IsReloading = True

    def event(self, QEvent):
        if QEvent.type() == QEvent.StatusTip:
            if QEvent.tip() == "":
                QEvent = QStatusTipEvent(self.StatusText)  # 此处为要始终显示的内容
        return super().event(QEvent)

    def UseToolBar(self):
        leftBar = QToolBar('leftBar')
        self.addToolBar(Qt.LeftToolBarArea, leftBar)
        leftBar.setOrientation(Qt.Vertical)
        # add actions
        search = QAction(QIcon("./img/icons/search.svg"), "search", self)
        leftBar.addAction(search)
        #
        lib = QAction(QIcon("./img/icons/grid.svg"), "lib", self)
        leftBar.addAction(lib)
        #
        drive = QAction(QIcon("./img/icons/hard-drive.svg"), "drive", self)
        leftBar.addAction(drive)
        #
        git = QAction(QIcon("./img/icons/git-merge.svg"), "git", self)
        leftBar.addAction(git)
        #
        layout = QAction(QIcon("./img/icons/layout.svg"), "layout", self)
        leftBar.addAction(layout)
        #
        info = QAction(QIcon("./img/icons/info.svg"), "info", self)
        leftBar.addAction(info)
        #
        terminal = QAction(QIcon("./img/icons/terminal.svg"), "terminal", self)
        leftBar.addAction(terminal)
        #
        self.max = QAction(QIcon("./img/icons/maximize-2.svg"), "max", self)
        leftBar.addAction(self.max)
        leftBar.actionTriggered[QAction].connect(self.leftbtnpressed)
        # leftBar.setMinimumWidth(35)

    def leftbtnpressed(self, a):
        if a.text() == 'max':
            if self.isFullScreen() == False:
                self.setWindowState(Qt.WindowFullScreen)
                self.max.setIcon(QIcon("./img/icons/minimize-2.svg"))
            else:
                self.setWindowState(Qt.WindowNoState)
                self.max.setIcon(QIcon("./img/icons/maximize-2.svg"))
        elif a.text() == 'terminal':
            self.UseTerminal()
        elif a.text() == 'info':
            self.Tool_about_APP()

    def UseTerminal(self):
        if self.openTerminal == False:
            # 显示
            self.openTerminal = True
            self.Terminal.show()
        else:
            # 不显示
            self.Terminal.hide()
            self.openTerminal = False

    def makeTerminal(self):
        self.OutPut_Widget = QTextBrowser()
        self.OutPut_Widget.insertHtml('<a>ready to start [output]</a>')
        self.Terminal = QDockWidget("output", self)
        self.Terminal.setWidget(self.OutPut_Widget)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.Terminal)
        #
        self.start.prompt.setText(f'刷新 output 面板 . . . {str(self.start.pv)}%')
        QtWidgets.qApp.processEvents()

    def recursiveDict(self, dict, parentWidget):
        SplitterSize = [0, 0]
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
        WidgetList = self.CreatChildWindow(
            parentWidget, mode, SplitterSize, "1")  # 创建分隔控件
        # CreatChildWindow(self,parent,mode,spliterList:list,Old_widget_splitter_to:str):
        tempCount = 0
        for key_s in dict:  # 修饰样式以及子控件实现
            if key_s != "PROJECT_LIST":
                if dict[key_s]['Children'] != None:  # 如果他有children
                    self.recursiveDict(
                        dict[key_s]['Children'], WidgetList[tempCount])  # 递归给子布局
                    # 为父控件重置样式
                    WidgetList[tempCount].setContentsMargins(0, 0, 0, 0)
                    WidgetList[tempCount].setStyleSheet(
                        "#"+WidgetList[tempCount].objectName()+'{border:0px;}')
                else:
                    self.SetChildWindow_STYLE(
                        WidgetList[tempCount], dict[key_s])  # 设置样式的吧
                tempCount += 1  # tempCount自加1

    def SetChildWindow_STYLE(self, widget, dict: dict):
        # set the child window's style
        # 颜色条
        ChildLayout = QVBoxLayout()
        ChildLayout.setContentsMargins(0, 0, 0, 0)
        ChildLayout.setSpacing(0)
        # layout end
        # top-option-widget
        OptionWidget = QWidget()
        OptionWidget.setStyleSheet('')
        OptionWidget.setMinimumHeight(20)
        OptionWidget.setMaximumHeight(20)
        OptionWidget.setObjectName('option_'+widget.objectName())
        OptionWidgetList.append(OptionWidget)
        # make the option buttons
        # close button->
        OptionLayout = QHBoxLayout()  # layout this widget
        # end of layout
        CloseButton = QPushButton()  # 关闭此面板
        CloseButton.setObjectName('Close_Button')  # 完成
        CloseButton.setMaximumHeight(20)
        CloseButton.setMaximumWidth(20)
        CloseButton.setToolTip("Close the Panel")
        CloseButton.clicked.connect(self.closePanel)
        CloseButton.setStyleSheet('''
*{background-image: url(./img/big_close__.png);
background-color: transparent;
background-repeat: no-repeat;
background-position: center center;}
*:hover {
    background-color: rgb(255, 112, 112);
    border: 1px solid #ccc;
}''')
        # setting
        # splitter
        splitterButton = QPushButton()  # 分割此面板
        splitterButton.setObjectName(dict['Window'])
        splitterButton.setMaximumHeight(20)
        splitterButton.setMaximumWidth(20)
        splitterButton.setStyleSheet('''
*{background-image: url(./img/main/split.png);
background-repeat: no-repeat;
background-position: center center;}
''')
        splitterButton.setToolTip('Split the Panel - Horizontal')
        splitterButton.clicked.connect(self.splitPanel)
        # split-v
        splitterButton_v = QPushButton()  # 分割此面板
        splitterButton_v.setObjectName(dict['Window'])
        splitterButton_v.setMaximumHeight(20)
        splitterButton_v.setMaximumWidth(20)
        splitterButton_v.setStyleSheet('''
*{background-image: url(./img/main/split_v.png);
background-repeat: no-repeat;
background-position: center center;}
''')
        splitterButton_v.setToolTip('Split the Panel - Vertical')
        splitterButton_v.clicked.connect(self.splitPanel_V)
        # out window
        outButton = QPushButton()  # 弹出此面板
        outButton.setObjectName(dict['Window'])
        outButton.setMaximumHeight(20)
        outButton.setMaximumWidth(20)
        outButton.setStyleSheet('''
*{background-image: url(./img/main/out3_2.png);
background-repeat: no-repeat;
background-position: center center;}
''')
        outButton.setToolTip('Pop up window')
        outButton.clicked.connect(self.PopUpWindow)
        # Line->
        Line = QWidget()  # 子窗口的分割线
        Line.setObjectName("WindowLine_"+widget.objectName())
        Line.setMaximumHeight(7)
        # Window name->
        WindowName = QPushButton()  # 主类名
        WindowName.clicked.connect(self.OutTheChoicePanel)
        WindowName.setToolTip(dict['Window'])
        WindowName.setObjectName('WindowName')
        WindowName.setText(dict['Window'])
        WindowName.setStyleSheet('''
#WindowName {
    background-color: rgba(0, 0, 0, 0.0);
    padding-left:2px;
    padding-right:15px;
    border: 1px solid rgba(0, 0, 0, 0.0);
    background-image: url(./img/bottom_to.png);
    background-position:right center;
    background-repeat:no-repeat;
    color:gray;
}
#WindowName:hover{
    background-color: #567dbc;
}''')
        WindowLineList.append(Line)
        # 给名称设置样式-icon
        IconPath = WindowMenuThis.WindowMenu[dict['Window']]['icon']
        WindowName.setIcon(QIcon(IconPath))
        # WindowName.setMaximumWidth(7*len(dict['Window']))
        # set layout
        OptionLayout.addWidget(WindowName)
        OptionLayout.addWidget(Line)
        OptionLayout.setStretch(1, 2)
        OptionLayout.addWidget(outButton)
        OptionLayout.addWidget(splitterButton)
        OptionLayout.addWidget(splitterButton_v)
        OptionLayout.addWidget(CloseButton)
        OptionLayout.setSpacing(0)
        CloseButton.setContentsMargins(0, 0, 0, 0)
        OptionWidget.setContentsMargins(0, 0, 0, 0)
        OptionLayout.setContentsMargins(2, 0, 0, 0)
        OptionWidget.setLayout(OptionLayout)
        # Main-widget
        Child_main_widget = QWidget()
        Child_main_widget.setObjectName(
            'Child_main_widget_'+str(self.childPanelCount))
        # 立刻加一咯
        self.childPanelCount = self.childPanelCount + 1
        # add widget to layout
        ChildLayout.addWidget(OptionWidget)
        ChildLayout.addWidget(Child_main_widget)
        widget.setLayout(ChildLayout)
        # 初始化面板->this:1
        # def PanelStarter(Sender:QPushButton,self,Name) -> None:#导入模块部分
        Starter.PanelStarter(WindowName, self, dict['Window'])
        pass

    def OutTheChoicePanel(self):
        # print(self.geometry())
        ChoicePanel.OutTheChoicePanel(self.sender(), self, self.geometry())

    def MakeChildWindow(self):
        # make childewindow
        for item in TabBar.editors:
            globals()['QTabWidget_'+item].setContentsMargins(2, 2, 2, 2)
            # self.MainWidget.setContentsMargins(2,2,2,2)
            try:
                self.recursiveDict(WindowMenuThis.StarterInfo[item], globals()[
                                   'QTabWidget_'+item])  # 产生窗口
                print('[info] : successful started<'+item +
                      f'> {str(time.localtime().tm_hour)}:{str(time.localtime().tm_min)}:{str(time.localtime().tm_sec)} \n')
                QtWidgets.qApp.processEvents()
            except Exception as e:
                print(WindowMenuThis)
                print('[Error] : Starter<'+item +
                      f'> failed {str(time.localtime().tm_hour)}:{str(time.localtime().tm_min)}:{str(time.localtime().tm_sec)}\n', e)
                print(traceback.format_exc())
                QtWidgets.qApp.processEvents()

    def closeEvent(self, event):
        for VtkWidget in self.OPEN_VTK_WIDGET:
            VtkWidget.Finalize()
        with open('./config/config.json', 'r', encoding='utf-8') as ReadConfig:
            getThisConfig = eval(ReadConfig.read())
        getThisConfig['w'] = self.width()
        getThisConfig['h'] = self.height()
        getThisConfig['x'] = self.x()
        getThisConfig['y'] = self.y()
        with open('./config/config.json', 'w', encoding='utf-8') as NewConfig:
            NewConfig.write(str(getThisConfig))
        pass
    # window.menu function this
    # 一些其他的函数
    # some other function

    def Strange_recursive_delete(self, sender, recursive):
        if recursive > 0:
            if sender.parent().parent().__class__ == PFrame:
                print('this is the Pframe', sender.parent().parent())
                if sender.parent().count() == 1:
                    print('delete')
                    if sender.parent().parent().parent().count() == 1:
                        self.Strange_recursive_delete(
                            sender.parent().parent(), recursive-1)
                    else:
                        recursive = 0
                    sender.parent().parent().deleteLater()
                    # 如果在子空间内的2个面板被全部删除，则删除这个子空间的父部件

    def closePanel(self):
        sender = self.sender()
        # print(sender.parent().parent().parent())
        out = 1
        ThisIndex = sender.parent().parent().parent().indexOf(sender.parent().parent())
        if ThisIndex == 1:
            out = 0
        sender.parent().parent().deleteLater()
        # print(sender.parent().parent().parent().count())
        sender.parent().parent().parent().setSizes([100])
        # print(sender.parent().parent().parent().parent())
        recursive = int(self.ChildWindowCount/2) + \
            1  # 最小递归次数，可以被count = 0时提前返回
        self.Strange_recursive_delete(sender.parent().parent(), recursive)
        sender.parent().parent().parent().setSizes([100])
    # 改写一个接受参数的

    def closePanel_sender(self, sender):
        # print(sender.parent().parent().parent())
        out = 1
        ThisIndex = sender.parent().parent().parent().indexOf(sender.parent().parent())
        if ThisIndex == 1:
            out = 0
        sender.parent().parent().deleteLater()
        # print(sender.parent().parent().parent().count())
        sender.parent().parent().parent().setSizes([100])
        # print(sender.parent().parent().parent().parent())
        recursive = int(self.ChildWindowCount/2) + \
            1  # 最小递归次数，可以被count = 0时提前返回
        self.Strange_recursive_delete(sender.parent().parent(), recursive)
        sender.parent().parent().parent().setSizes([100])

    def splitPanel(self):
        senderThis = self.sender()
        LastName = senderThis.parent().children()[1].text()
        try:
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
        # thisSplitterWidget.setLayout(None)
        item_list = list(range(ThisLayout.count()))
        item_list.reverse()  # 倒序删除，避免影响布局顺序
        for i in item_list:
            item = ThisLayout.itemAt(i)
            ThisLayout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()
        getWidget = self.CreatChildWindow(thisSplitterWidget, Qt.Horizontal, [
                                          10, 10], "1", layoutThis=ThisLayout)  # 创建分隔控件
        thisSplitterWidget.setStyleSheet(
            '#'+thisSplitterWidget.objectName()+"{border:0px;}")
        self.SetChildWindow_STYLE(
            getWidget[0], {'Window': LastName})  # 0
        self.SetChildWindow_STYLE(getWidget[1], {'Window': 'White'})  # 1
    # 复制一个splitPanel_V

    def splitPanel_V(self):
        senderThis = self.sender()
        LastName = senderThis.parent().children()[1].text()
        # print(ColorLineList)
        try:
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
        # 'option_'+widget.objectName()
        thisSplitterWidget = senderThis.parent().parent()
        ThisLayout = thisSplitterWidget.layout()
        # thisSplitterWidget.setLayout(None)
        item_list = list(range(ThisLayout.count()))
        item_list.reverse()  # 倒序删除，避免影响布局顺序
        for i in item_list:
            item = ThisLayout.itemAt(i)
            ThisLayout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()
        getWidget = self.CreatChildWindow(thisSplitterWidget, Qt.Vertical, [
                                          10, 10], "1", layoutThis=ThisLayout)  # 创建分隔控件
        thisSplitterWidget.setStyleSheet(
            '#'+thisSplitterWidget.objectName()+"{border:0px;}")
        self.SetChildWindow_STYLE(
            getWidget[0], {'Window': LastName})  # 0
        self.SetChildWindow_STYLE(getWidget[1], {'Window': 'White'})  # 1
    # PopUpWindow可能会有点复杂

    def PopUpWindow(self):
        sender = self.sender()
        LastName = sender.parent().children()[1].text()
        Frame_X = sender.pos().x()
        Frame_Y = sender.pos().y()
        Width_ = sender.parent().parent().width()
        Height_ = sender.parent().parent().height()
        ThisSenderName = sender.objectName()
        Pos_X = sender.mapToGlobal(sender.pos()).x()  # 控件相对于屏幕的位置
        Pos_Y = sender.mapToGlobal(sender.pos()).y()
        print(Pos_X, Pos_Y, Width_, Height_)
        globals()['PanelWindow_This_' +
                  str(self.panelWindowCount)] = QMainWindow(self)
        thisWindow = globals()['PanelWindow_This_'+str(self.panelWindowCount)]
        thisWindow.resize(Width_, Height_ - 30)
        thisWindow.show()
        screen = QDesktopWidget().screenGeometry()
        print(Frame_X, Width_)
        size = thisWindow.geometry()
        thisWindow.move(Pos_X - Frame_X - (Width_) +
                        sender.width() + 62, Pos_Y - Frame_Y)
        # globals()['PanelWindow_This_'+str(self.panelWindowCount)].label_2.setText(ThisSenderName)
        # globals()['PanelWindow_This_'+str(self.panelWindowCount)].setMaximumSize(Width_,Height_)
        print(thisWindow.geometry())
        #
        thisWindow.Config = self.Config
        #
        thisWindow.THIS_MAIN_WIDGET = QWidget()
        # WindowLineList.append(Line)
        # 给名称设置样式-icon
        IconPath = WindowMenuThis.WindowMenu[LastName]['icon']
        # Starter.PanelStarter(thisWindow.WindowName,thisWindow,sender.objectName())#def PanelStarter(Sender:QPushButton,self,Name) -> None:#导入模块部分
        Name = LastName
        thisLayout = QVBoxLayout()
        thisLayout.setContentsMargins(0, 0, 0, 0)
        thisLayout.setSpacing(0)
        # thisWindow.widget_2.setStyleSheet('*{border-bottom-left-radius:7px;border-bottom-right-radius:7px;}')
        thisWindow.setCentralWidget(thisWindow.THIS_MAIN_WIDGET)
        thisWindow.THIS_MAIN_WIDGET.setLayout(thisLayout)
        thisWindow.THIS_MAIN_WIDGET.setObjectName('THIS_MAIN_WIDGET_')
        thisWindow.setWindowTitle(Name)
        # give value
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
        # give value
        # 进入主初始化模块
        exec(f"lib.core.module.{Name}.init(thisLayout,'{Name}',thisWindow)")
        self.closePanel_sender(sender)  # 删除面板
        self.panelWindowCount += 1

    def Tool_about_APP(self):
        # about the application
        print('open about window')
        # window.menu function this -> Tool_control_clicked
        sender = self.sender()
        globals()['NewAboutWindow_'+str(self.SettingWindowCount)
                  ] = PanelWindow()  # 直接复用好了
        thisAbout = globals()['NewAboutWindow_'+str(self.SettingWindowCount)]
        thisAbout.resize(400, 500)
        screen = QDesktopWidget().screenGeometry()
        size = thisAbout.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)
        thisAbout.move(newLeft, newTop)
        thisAbout.WindowName.setText('About')
        thisAbout.WindowName.setStyleSheet('margin-left:7px;')
        MainLayout = QVBoxLayout()
        thisAbout.widget_2.setLayout(MainLayout)
        # thisAbout.widget_2.setStyleSheet('background-color:#f9f9f9;')
        # thisAbout.widget.setStyleSheet('background-color:#fff;')
        MainLayout.addWidget(About.MakeAbout())
        thisAbout.show()
        self.SettingWindowCount += 1  # 自加

    def Tool_control_clicked(self):
        print('open settings window')
        # window.menu function this -> Tool_control_clicked
        sender = self.sender()
        globals()['NewSettingWindow_'+str(self.SettingWindowCount)
                  ] = Setting.SettingWindow(self, self.User)  # 直接复用好了
        ThisSetting = globals()['NewSettingWindow_' +
                                str(self.SettingWindowCount)]
        screen = QDesktopWidget().screenGeometry()
        size = ThisSetting.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)

        ThisSetting.setWindowTitle('Setting - '+self.User)
        ThisSetting.WindowName.setText('Setting - '+self.User)

        ThisSetting.resize(760, 660)
        ThisSetting.move(newLeft, newTop)
        ThisSetting.show()
        self.SettingWindowCount += 1  # 自加

    def getAllWidget(self, lastWidget):
        for widget in lastWidget.children():
            rewrite_print(widget)
            try:
                widget.setStyleSheet('')
            except:
                pass
            if len(widget.children()) != 0:
                self.getAllWidget(widget)

    def MakeToolDIV(self):  # 菜单栏部分
        menubar = self.menuBar()
        # bar
        ###
        FILE = ['新建项目', '打开项目', '新建文件', '打开文件',
                '最近打开的项目', '保存', '保存副本', '打包为zip', '关闭']
        FILE_FUNC = [print, print, print, print,
                     print, print, print, print, qApp.quit]
        FILE_KEY = ['Ctrl+N', 'Ctrl+O', '', '', '',
                    'Ctrl+S', 'Ctrl+Shift+S', 'Ctrl+P', 'Ctrl+Q']
        fileMenu = menubar.addMenu("文件(F)")
        for i in range(len(FILE)):
            Act = QAction(QIcon('exit.png'), FILE[i], self)
            Act.setShortcut(FILE_KEY[i])
            Act.triggered.connect(FILE_FUNC[i])
            fileMenu.addAction(Act)
        ####
        editMenu = menubar.addMenu("编辑(E)")
        EDIT = ['撤销', '恢复', '剪切', '复制', '粘贴', '查找', '替换', '添加方块', '删除方块']
        EDIT_FUNC = [print, print, print, print,
                     print, print, print, print, print]
        EDIT_KEY = ['Ctrl+Z', 'Ctrl+Y', 'Ctrl+X', 'Ctrl+C',
                    'Ctrl+V', 'Ctrl+Alt+F', 'Ctrl+H', 'Ctrl+A', 'Ctrl+D']
        for i in range(len(EDIT)):
            Act = QAction(QIcon('exit.png'), EDIT[i], self)
            Act.setShortcut(EDIT_KEY[i])
            Act.triggered.connect(EDIT_FUNC[i])
            editMenu.addAction(Act)
        ###
        select = menubar.addMenu("选择(S)")
        SELECT = ['全选', '反向选', '勾选', '自由选取']
        SELECT_FUNC = [print, print, print, print]
        SELECT_KEY = ['Ctrl+Shift+S', 'Ctrl+Alt+S',
                      'Ctrl+Shift+T', 'Ctrl+Shift+F']
        for i in range(len(SELECT)):
            Act = QAction(QIcon('exit.png'), SELECT[i], self)
            Act.setShortcut(SELECT_KEY[i])
            Act.triggered.connect(SELECT_FUNC[i])
            select.addAction(Act)
        ###
        run = menubar.addMenu("运行(R)")
        RUN = ['运行脚本', '运行调试', '运行解析指令', '调试指令', '运行指令模拟器']
        RUN_FUNC = [print, print, print, print, print]
        RUN_KEY = ['Ctrl+R', 'Ctrl+Alt+R',
                   'Ctrl+Shift+C', 'Ctrl+Alt+C', 'Ctrl+M']
        for i in range(len(RUN)):
            Act = QAction(QIcon('exit.png'), RUN[i], self)
            Act.setShortcut(RUN_KEY[i])
            Act.triggered.connect(RUN_FUNC[i])
            run.addAction(Act)
        ###
        window = menubar.addMenu("窗口(W)")
        WINDOW = ['方块(背包)', '实体(entites)', '掉落物(items)',
                  '指令聊天栏(/)', '渲染(renderer)']
        WINDOW_FUNC = [print, print, print, print, print]

        for i in range(len(RUN)):
            Act = QAction(QIcon('exit.png'), WINDOW[i], self)

            Act.triggered.connect(WINDOW_FUNC[i])
            window.addAction(Act)
        ###
        setting = menubar.addMenu("设置(C)")
        SETTING = ['偏好设置', '从外部导入设置', '新建设置文件', '恢复初始设置', '颜色主题']
        SETTING_FUNC = [self.Tool_control_clicked,
                        print, print, print, self.setting_theme]
        SETTING_KEY = ['Ctrl+Alt+C', '', '', 'Ctrl+Alt+H', '']
        for i in range(len(SETTING)):
            Act = QAction(QIcon('exit.png'), SETTING[i], self)
            Act.setShortcut(SETTING_KEY[i])
            Act.triggered.connect(SETTING_FUNC[i])
            setting.addAction(Act)
        ###
        help = menubar.addMenu("帮助(H)")
        HELP = ['我们的网站', '帮助文档', '发行说明', '关于我们', '检查资源完整性']
        HELP_FUNC = [self.our_website,
                     self.help_document, print, self.Tool_about_APP, print]
        HELP_KEY = ['Ctrl+W', 'Ctrl+H', '', '', '']
        for i in range(len(HELP)):
            Act = QAction(QIcon('exit.png'), HELP[i], self)
            Act.setShortcut(HELP_KEY[i])
            Act.triggered.connect(HELP_FUNC[i])
            help.addAction(Act)
        ###
        license = QMenu('License', help)
        help.addMenu(license)
        for root, dirs, files in os.walk('./LICENSE'):
            get_license = files
        for license_file in get_license:
            globals()[license_file+'_menu'] = QAction(
                QIcon('exit.png'), license_file, self)
            print('license files :', license_file)
            this_open_function = f'''
def {license_file.split('-')[0]+'_license'} ():
    this_str = ''
    with open('./LICENSE/{license_file}', 'r', encoding='utf-8') as license:
        this_str = license.read()
    LICENSE_WINDOW = PanelWindow()
    LICENSE_WINDOW.resize(400, 500)
    LICENSE_WINDOW.setWindowTitle('{license_file}')
    this_text_viewer = QTextBrowser()
    this_text_viewer.setText(this_str)
    this_text_viewer.setReadOnly(True)
    #
    screen = QDesktopWidget().screenGeometry()
    size = LICENSE_WINDOW.geometry()
    newLeft = int((screen.width() - size.width()) / 2)
    newTop = int((screen.height() - size.height()) / 2)
    LICENSE_WINDOW.move(newLeft, newTop)
    LICENSE_WINDOW.WindowName.setText('{license_file}')
    LICENSE_WINDOW.WindowName.setStyleSheet('margin-left:7px;')
    MainLayout = QVBoxLayout()
    LICENSE_WINDOW.widget_2.setLayout(MainLayout)
    MainLayout.addWidget(this_text_viewer)
    #
    LICENSE_WINDOW.show()
'''
            exec(this_open_function)
            globals()[license_file.split(
                '-')[0]+'_license'] = locals()[license_file.split('-')[0]+'_license']
            globals()[license_file +
                      '_menu'].triggered.connect(globals()[license_file.split('-')[0]+'_license'])
            license.addAction(globals()[license_file+'_menu'])
    # 非UI的都写在下面

    def setting_theme(self):
        theme_choose = PanelWindow()
        theme_choose.setWindowTitle(
            'Setting - '+self.User+'- [color theme] 颜色主题')
        theme_choose.resize(460, 400)
        theme_choose.setFixedSize(460, 400)
        left_panel = QWidget()
        right_panel = QWidget()
        Mainwidget = QWidget()
        #
        screen = QDesktopWidget().screenGeometry()
        size = theme_choose.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)
        theme_choose.move(newLeft, newTop)
        theme_choose.WindowName.setText(
            'Setting - '+self.User+'- [color theme] 颜色主题')
        theme_choose.WindowName.setStyleSheet('margin-left:7px;')
        MainLayout = QVBoxLayout()
        theme_choose.widget_2.setLayout(MainLayout)
        MainLayout.addWidget(Mainwidget)
        #
        layout_1 = QHBoxLayout(Mainwidget)
        layout_1.addWidget(left_panel)
        layout_1.setContentsMargins(0, 20, 0, 0)
        layout_1.addWidget(right_panel)
        layout_1.setSpacing(10)
        left_panel.setMaximumWidth(150)
        # left_panel.set
        Lib_List = QListWidget()
        left_layout = QHBoxLayout(left_panel)
        left_layout.addWidget(Lib_List)
        lib1 = QListWidgetItem()
        lib1.setText('qtvscodestyle')
        lib1.setIcon(QIcon('./img/file/icons/database.svg'))
        lib2 = QListWidgetItem()
        lib2.setText('default(xk)')
        lib2.setIcon(QIcon('./img/file/icons/folder-css.svg'))
        lib3 = QListWidgetItem()
        lib3.setText('qdarktheme')
        lib3.setIcon(QIcon('./img/file/icons/database.svg'))
        lib4 = QListWidgetItem()
        lib4.setText('qdarkstyle')
        lib4.setIcon(QIcon('./img/file/icons/database.svg'))
        lib5 = QListWidgetItem()
        lib5.setText('QSS-master')
        lib5.setIcon(QIcon('./img/file/icons/folder-css.svg'))
        lib6 = QListWidgetItem()
        lib6.setText('qt_material')
        lib6.setIcon(QIcon('./img/file/icons/database.svg'))
        #
        Lib_List.insertItem(0, lib2)
        Lib_List.insertItem(0, lib3)
        Lib_List.insertItem(0, lib4)
        Lib_List.insertItem(0, lib5)
        Lib_List.insertItem(0, lib6)

        Lib_List.insertItem(0, lib1)
        #
        left_layout.addWidget(Lib_List)
        #
        label1 = QLabel(theme_choose)
        label1.setText('主题库')
        label1.move(35, 40)
        label2 = QLabel(theme_choose)
        label2.setText('主题样式')
        label2.move(180, 40)
        theme_choose.show()
        # right panel
        theme_list = QListWidget()
        right_layout = QHBoxLayout(right_panel)
        right_layout.addWidget(theme_list)
        this_mode = ['vs_theme']
        qtvscodestyle_list = {'Light(Visual Studio)': 'LIGHT_VS',
                              'Quiet Light': 'QUIET_LIGHT',
                              'Solarized Light': 'SOLARIZED_LIGHT',
                              'Abyss': 'ABYSS',
                              'Dark(Visual Studio)': 'DARK_VS',
                              'Kimbie Dark': 'KIMBIE_DARK',
                              'Monokai': ' MONOKAI',
                              'Monokai Dimmed': 'MONOKAI_DIMMED',
                              'Red': 'RED',
                              'Solarized Dark': 'SOLARIZED_DARK',
                              'Tomorrow Night Blue': 'TOMORROW_NIGHT_BLUE',
                              'Dark High Contrast': 'DARK_HIGH_CONTRAST'}
        xkTheme = {'main.qss': 'main.qss',
                   'main_default.qss': 'main_dark.qss'}
        qdarktheme_list = {'dark': 'dark',
                           'light': 'light', 'auto (System)': 'auto'}
        qdarkstyle_list = ['darkstyle', 'lightstyle']
        QSS_list = ['AMOLED.qss', 'Aqua.qss',
                    'ConsoleStyle.qss', 'ElegantDark.qss', 'MacOS.qss',
                    'ManjaroMix.qss', 'MaterialDark.qss', 'NeonButtons.qss', 'Ubuntu.qss', 'darkstyle.qss']
        qt_material_list = [
            'dark_amber.xml',
            'dark_blue.xml',
            'dark_cyan.xml',
            'dark_lightgreen.xml',
            'dark_pink.xml',
            'dark_purple.xml',
            'dark_red.xml',
            'dark_teal.xml',
            'dark_yellow.xml',
            'light_amber.xml',
            'light_blue.xml',
            'light_blue_500.xml',
            'light_cyan.xml',
            'light_cyan_500.xml',
            'light_lightgreen.xml',
            'light_lightgreen_500.xml',
            'light_orange.xml',
            'light_pink.xml',
            'light_pink_500.xml',
            'light_purple.xml',
            'light_purple_500.xml',
            'light_red.xml',
            'light_red_500.xml',
            'light_teal.xml',
            'light_teal_500.xml',
            'light_yellow.xml']

        def on_listWidget_itemClicked(item):
            if item.text() == 'qtvscodestyle':
                theme_list.clear()
                for i in qtvscodestyle_list:
                    theme = QListWidgetItem()
                    theme.setText(i)
                    theme.setIcon(QIcon('./img/file/icons/python.svg'))
                    theme_list.insertItem(0, theme)
                this_mode[0] = 'vs_theme'
                print('changed vs_theme')

            elif item.text() == 'default(xk)':
                theme_list.clear()
                for i in xkTheme:
                    theme = QListWidgetItem()
                    theme.setText(i)
                    theme.setIcon(QIcon('./img/file/icons/file.svg'))
                    theme_list.insertItem(0, theme)
                this_mode[0] = 'xk_theme'
                print('changed xk_theme')

            elif item.text() == 'qdarktheme':
                theme_list.clear()
                for i in qdarktheme_list:
                    theme = QListWidgetItem()
                    theme.setText(i)
                    theme.setIcon(QIcon('./img/file/icons/python.svg'))
                    theme_list.insertItem(0, theme)
                this_mode[0] = 'qdark_theme'
                print('changed qdark_theme')

            elif item.text() == 'qdarkstyle':
                theme_list.clear()
                for i in qdarkstyle_list:
                    theme = QListWidgetItem()
                    theme.setText(i)
                    theme.setIcon(QIcon('./img/file/icons/python.svg'))
                    theme_list.insertItem(0, theme)
                this_mode[0] = 'qdarkstyle_theme'
                print('changed qdarkstyle_theme')
            elif item.text() == 'QSS-master':
                theme_list.clear()
                for i in QSS_list:
                    theme = QListWidgetItem()
                    theme.setText(i)
                    theme.setIcon(QIcon('./img/file/icons/file.svg'))
                    theme_list.insertItem(0, theme)
                this_mode[0] = 'QSS_theme'
                print('changed QSS_theme')
            elif item.text() == 'qt_material':
                theme_list.clear()
                for i in qt_material_list:
                    theme = QListWidgetItem()
                    theme.setText(i)
                    theme.setIcon(QIcon('./img/file/icons/xml.svg'))
                    theme_list.insertItem(0, theme)
                this_mode[0] = 'qt_material_theme'
                print('changed qt_material_theme')

        def qt_material_theme(item_):
            apply_stylesheet(self.app, theme=item_.text(),
                             invert_secondary=True)
            self.UseTheme()

        def vs_theme(item_):
            stylesheet = qtvsc.load_stylesheet(
                eval(f'qtvsc.Theme.{qtvscodestyle_list[item_.text()]}'))
            # stylesheet = load_stylesheet(qtvsc.Theme.LIGHT_VS)
            self.app.setStyleSheet(stylesheet)
            self.UseTheme()

        def xk_theme(item_):
            style = QStyleFactory.create('Fusion')
            QApplication.setStyle(style)
            palette = style.standardPalette()
            palette.setColor(QPalette.Mid, QColor(232, 243, 251))
            QApplication.setPalette(palette)

            qssStyle = StyleReader.readQSS(
                './style/'+xkTheme[item_.text()])
            self.setStyleSheet(qssStyle)

        def qdark_theme(item_):
            qdarktheme.setup_theme(qdarktheme_list[item_.text()])
            self.UseTheme()

        def qdarkstyle_theme(item_):
            if item_.text() == 'darkstyle':
                self.app.setStyleSheet(qdarkstyle.load_stylesheet())
            else:
                self.app.setStyleSheet(qdarkstyle.load_stylesheet(
                    qt_api='pyqt5', palette=LightPalette()))
            self.UseTheme()

        def QSS_theme(item_):
            style = QStyleFactory.create('Fusion')
            QApplication.setStyle(style)
            palette = style.standardPalette()
            palette.setColor(QPalette.Mid, QColor(232, 243, 251))
            QApplication.setPalette(palette)
            qssStyle = StyleReader.readQSS(
                './QSS-master/'+item_.text())
            self.setStyleSheet(qssStyle)

        def theme_change(item):
            print(this_mode)
            if this_mode[0] == 'vs_theme':
                vs_theme(item)
            elif this_mode[0] == 'xk_theme':
                xk_theme(item)
            elif this_mode[0] == 'qdark_theme':
                qdark_theme(item)
            elif this_mode[0] == 'qdarkstyle_theme':
                qdarkstyle_theme(item)
            elif this_mode[0] == 'QSS_theme':
                QSS_theme(item)
            elif this_mode[0] == 'qt_material_theme':
                qt_material_theme(item)
        theme_list.itemClicked.connect(theme_change)
        Lib_List.itemClicked.connect(on_listWidget_itemClicked)
        theme_list.clear()
        for i in qdarkstyle_list:
            theme = QListWidgetItem()
            theme.setText(i)
            theme.setIcon(QIcon('./img/file/icons/python.svg'))
            theme_list.insertItem(0, theme)
        this_mode[0] = 'qdarkstyle_theme'
        print('changed qdarkstyle_theme')

    def our_website(self):
        os.system('start https://www.google.com')

    def help_document(self):
        self.thisPath = sys.argv[0].replace(sys.argv[0].split(
            '\\')[-1], '').replace('\\', '/')
        self.helpurl = self.thisPath+'help.html'
        ################################################################
        print('open help document')
        # window.menu function this -> Tool_control_clicked
        HELP_WINDOW = PanelWindow()
        HELP_WINDOW.setWindowTitle('help document')
        HELP_WINDOW.WindowName.setText('help document')
        #
        HELP_WINDOW.resize(720, 560)
        # HELP_WINDOW.move(newLeft, newTop)
        This_layout = QVBoxLayout()
        This_layout.setContentsMargins(0, 0, 0, 0)
        WEB_ThisHelpDOC = QWebEngineView()
        WEB_ThisHelpDOC.load(QUrl(self.helpurl))
        WEB_ThisHelpDOC.setStyleSheet('background-color:rgba(0,0,0,0);')
        WEB_ThisHelpDOC.reload()
        #
        This_layout.addWidget(WEB_ThisHelpDOC)
        HELP_WINDOW.widget_2.setLayout(This_layout)
        #
        HELP_WINDOW.show()
        self.SettingWindowCount += 1  # 自加

    def license_document(self):
        pass
