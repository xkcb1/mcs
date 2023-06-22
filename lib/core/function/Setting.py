import os
import sys
import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import getpass
from lib.StyleReader import StyleReader
from lib.fileTreeView import CreateFileTree
from lib.readConfig import readConfig
import lib.WindowMenu as WindowMenu
# import base functions
from lib.core.ui.newPanelWindow import *
from lib.base import *
from lib.core.function.theme import *
# end


class SettingWindow(PanelWindow):
    def __init__(self, parent, User):
        super().__init__()
        self.parent = parent
        self.User = User
        self.setWindowTitle('setting - User')
        globals()['SELF'] = self
        self.lb = QVBoxLayout()
        scroll = QScrollArea()
        scroll.setObjectName('scroll')
        scroll.setStyleSheet(
            '''#scroll{border:0px !important;border-left:1px solid #999;
        }''')
        self.lb.setContentsMargins(10, 5, 5, 0)
        MainWidgetThis = QWidget()
        MainWidgetThis.setObjectName('MainWidgetThis_Attr')
        MainWidgetThis.setStyleSheet(
            '''#MainWidgetThis_Attr{border:0px !important;
        }''')
        MainWidgetThis.setLayout(self.lb)
        MainWidgetThis.setContentsMargins(0, 0, 0, 0)
        self.lb.setSpacing(5)
        self.UiInit(self.lb)
        scroll.setWidget(MainWidgetThis)
        scroll.setContentsMargins(0, 0, 0, 0)
        scroll.setWidgetResizable(True)
        scroll.widgetResizable()
        # scroll.set
        self.MainLayout = QHBoxLayout()
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setSpacing(0)
        self.MAINWIDGET = QWidget()
        
        self.MAINWIDGET.setLayout(self.MainLayout)
        self.leftPanel = QWidget()
        self.leftPanel.setObjectName('settingleftPanel')
        self.leftLayout = QVBoxLayout(self.leftPanel)  # 左侧边栏的布局
        self.leftLayout.setSpacing(0)
        self.leftLayout.setContentsMargins(5, 5, 5, 0)
        self.leftPanel.setMaximumWidth(150)
        self.leftPanel.setMinimumWidth(150)
        self.MainLayout.addWidget(self.leftPanel)
        self.MainLayout.addWidget(scroll)
        #
        self.WindowName.setStyleSheet('margin-left:7px;')
        MainLayout_ = QVBoxLayout()
        self.widget_2.setLayout(MainLayout_)
        MainLayout_.addWidget(self.MAINWIDGET)
        #

        FristAll = QPushButton()
        FristAll.setText('首选项')
        window = QPushButton()
        window.setText('窗口设置')
        editor = QPushButton()
        editor.setText('编辑器')
        workspace = QPushButton()
        workspace.setText('工作区')
        manager = QPushButton()
        manager.setText('管理包')
        extend = QPushButton()
        extend.setText('扩展')
        self.leftLayout.addWidget(FristAll)
        self.leftLayout.addWidget(window)
        self.leftLayout.addWidget(editor)
        self.leftLayout.addWidget(workspace)
        self.leftLayout.addWidget(manager)
        self.leftLayout.addWidget(extend)
        self.leftLayout.addWidget(QWidget())
        FristAll.setObjectName('settingButtons')
        window.setObjectName('settingButtons')
        editor.setObjectName('settingButtons')
        workspace.setObjectName('settingButtons')
        manager.setObjectName('settingButtons')
        extend.setObjectName('settingButtons')
        #
        FristAll.setMaximumHeight(27)
        FristAll.setMinimumHeight(27)
        window.setMaximumHeight(27)
        window.setMinimumHeight(27)
        editor.setMaximumHeight(27)
        editor.setMinimumHeight(27)
        workspace.setMaximumHeight(27)
        workspace.setMinimumHeight(27)
        manager.setMaximumHeight(27)
        manager.setMinimumHeight(27)
        extend.setMaximumHeight(27)
        extend.setMinimumHeight(27)
        #
        self.ThisButton = [FristAll, window,
                           editor, workspace, manager, extend]
        FristAll.clicked.connect(self.SettingButtonClick)
        window.clicked.connect(self.SettingButtonClick)
        editor.clicked.connect(self.SettingButtonClick)
        workspace.clicked.connect(self.SettingButtonClick)
        manager.clicked.connect(self.SettingButtonClick)
        extend.clicked.connect(self.SettingButtonClick)
        FristAll.setObjectName('focus_button')

        self.setWindowTitle('Setting - '+self.User+' - 首选项')

    def changeTheme(self, parent):
        data = parent.sender().currentText()
        rewrite_print(data)
        ChangeTheme(self.parent, data)

    def cleanWidget(self, layout):
        item_list = list(range(layout.count()))
        item_list.reverse()  # 倒序删除，避免影响布局顺序
        for i in item_list:
            item = layout.itemAt(i)
            layout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()

    def Sstart(self):
        theme = {'主题': ['default', 'dark', 'light', 'blue', 'green', 'darkblue'],
                 '主题文件': Ppath('./style/main.qss'),
                 '主题版本': '0.0.1',
                 '启用主题': True}
        themePanel = AttributePanel(
            '设置主题样式', theme, [self.changeTheme, print, print, print], True)
        self.lb.addWidget(themePanel)
        # themePanel.toBig()
        self.lb.addWidget(AttributePanel('设置字体', {'字体大小': 12,
                                                  '字体': 'System UI',
                                                  '字体宽度': 'default',
                                                  '字体样式': 'not defined', }, None, True))
        self.lb.addWidget(AttributePanel('设置语言', {'系统语言': ['Chinese', 'English'],
                                                  '系统语言文件': Ppath('not defined(.lang)'),
                                                  '语言版本': '0.0.1',
                                                  }, None, True))
        self.lb.addWidget(AttributePanel('功能设置', {'设置游戏版本': ['1.8.x', '1.9.x', '1.10.x'],
                                                  '设置游戏启动路径': Ppath('not defined(.lang)'),
                                                  '启动器版本': '0.0.1',
                                                  '最大线程数(更快但是占用大)': 5,
                                                  '启动C++库扩展功能': False,
                                                  'Python版本': sys.version,
                                                  '系统版本': sys.platform,
                                                  '软件运行内存限制(mb)': 2048,
                                                  '日志文件': Ppath('./log_file/log.txt')
                                                  }, None, True))
        self.lb.addWidget(AttributePanel('2d引擎设置', {'python引擎库': ['pygame', 'opengl', 'opencv'],
                                                    '引擎库版本': 'not defined',
                                                    '引擎更新': False,
                                                    '使用外部引擎以及代码': False,
                                                    '外部引擎文件(.whl)': Ppath('not defined'),
                                                    '启用2d引擎辅助功能': True
                                                    }, None, True))
        self.lb.addWidget(AttributePanel('3d引擎设置', {'python引擎库': ['opengl', 'vtk(内存占用大)', 'Qt3d(不稳定)'],
                                                    '引擎库版本': 'not defined',
                                                    '引擎更新': False,
                                                    '使用外部引擎以及代码': False,
                                                    '外部引擎文件(.whl)': Ppath('not defined'),
                                                    '启用3d引擎辅助功能': True,
                                                    '3d摄像机缩放极限(scala)': 20,
                                                    '3d摄像机分辨率': ['auto', '100x100', '200x200', '300x300', '自定义'],
                                                    '自定义3d摄像机分辨率': '(x)',
                                                    '3d摄像机平移速度(m/s)': 1,
                                                    '启用第一人称视角': True,
                                                    '天空盒子': Ppath('./skybox/default.ext'),
                                                    '启用天空盒子': True,
                                                    '3d文件解析器': ['PureNbtToStl', '自定义'],
                                                    '材质文件': Ppath('not defined'),
                                                    '3d文件解析器版本': '0.0.1',
                                                    '3d文件解析器源': ['Python', 'Lua', 'C++', 'Java(需扩展)', '自定义'],
                                                    '3d文件保存目录': Ppath('./temp/stl/'),
                                                    'nbt文件解析模式': ['大端', '小端'],
                                                    'nbt文件解析库': ['nbtlib', 'nbt', '自定义'],
                                                    'nbt文件解析器线程数限制': 3
                                                    }, None, True))
        self.lb.addWidget(AttributePanel('command解析', {'command语法解析器': ['default', '自定义'],
                                                       'command命令文件': Ppath('not defined(.lang)'),
                                                       'command编译器': ['default', '自定义'],
                                                       '启用command编译器': True,
                                                       '启用多线程编译': True,
                                                       '编译最大线程': 3,
                                                       '编译输出文件': Ppath('$This.Editor.NewFile("output.txt")'),
                                                       '启用解释command': True,
                                                       'command版本': ['Je', 'Be', '自定义'],
                                                       'command文件后缀': ['.mcfunction', '.txt', '.cb', '自定义'],
                                                       'command文件后缀自定义': '(x)',
                                                       'command解析器内核': ['PureCommandLexer', '自定义'],
                                                       'command解析器内核版本': '0.0.1',
                                                       '启用command向下兼容(可能产生冗杂)': False,
                                                       '启用command扩展库': True,
                                                       'command扩展库文件后缀': '.cblib',
                                                       'command扩展库文件': Ppath('./'),
                                                       'command扩展库编译器': ['default', '自定义'],
                                                       'command扩展库链接器': ['PureCommandLexer', '自定义'],
                                                       '启用command示例文件': True,
                                                       '启用command基础设置函数': True,
                                                       '启用command扩展设置函数': True,
                                                       '允许commandLib跨文件导入': True,
                                                       '允许将.mcfunction识别为.cblib': True,
                                                       '启用command自动注释': True,
                                                       '启用便捷数学计算器': True,
                                                       '启用command变量监测': True,
                                                       '启用command变量模拟运行': True,
                                                       '允许command解析器接入3d引擎模拟': True
                                                       }, None, True))
        self.lb.addWidget(QWidget())
        pass

    def Swindow(self):
        self.lb.addWidget(QWidget())
        pass

    def Seditor(self):
        self.lb.addWidget(QWidget())
        pass

    def Swork(self):
        self.lb.addWidget(QWidget())
        pass

    def Spack(self):
        self.lb.addWidget(QWidget())
        pass

    def Sextend(self):
        self.lb.addWidget(QWidget())
        pass

    def SettingButtonClick(self):
        sender = self.sender()
        sender.setObjectName('focus_button')
        self.cleanWidget(self.lb)
        self.addSearch()
        if sender.text() == '首选项':
            rewrite_print('Setting 首选项')
            self.setWindowTitle('Setting - '+self.User+' - 首选项')
            self.Sstart()
        elif sender.text() == '窗口设置':
            rewrite_print('Setting 窗口设置')
            self.setWindowTitle('Setting - '+self.User+' - 窗口设置')
            self.Swindow()
        elif sender.text() == '编辑器':
            rewrite_print('Setting 编辑器')
            self.setWindowTitle('Setting - '+self.User+' - 编辑器')
            self.Seditor()
        elif sender.text() == '工作区':
            rewrite_print('Setting 工作区')
            self.setWindowTitle('Setting - '+self.User+' - 工作区')
            self.Swork()
        elif sender.text() == '管理包':
            rewrite_print('Setting 管理包')
            self.setWindowTitle('Setting - '+self.User+' - 管理包')
            self.Spack()
        elif sender.text() == '扩展':
            rewrite_print('Setting 扩展')
            self.setWindowTitle('Setting - '+self.User+' - 扩展')
            self.Sextend()
        sender.setStyleSheet('''
#focus_button {
    color:#111;
    border-left: 2px solid #4888FF;
    outline: 0px;
    text-align: left;
    padding-left: 20px;
    border-top-left-radius:0px;
    border-bottom-left-radius:0px;
    font-weight: bold;
}
#focus_button:hover {
    color:#111;
    border-radius: 3px;
    border-top-left-radius:0px;
    border-bottom-left-radius:0px;
}
                             ''')
        for widget in self.ThisButton:
            if widget != sender:
                widget.setObjectName('no_focus_button')
                widget.setStyleSheet('''
#no_focus_button {
    color:#777;
    border: 0px;
    border-left:2px solid rgba(0,0,0,0);
    outline: 0px;
    text-align: left;
    padding-left: 20px;
    border-radius: 3px;
}
#no_focus_button:hover {
    color:#111;
    border-radius: 3px;
}
                                     ''')

    def addSearch(self):
        SearchInput_Attribute_Widget = QWidget()
        # SearchInput_Attribute_Widget.setStyleSheet('background-color:red;')
        SearchInput_Attribute = QHBoxLayout()
        SearchInput_Attribute.setContentsMargins(0, 0, 0, 0)
        SearchInput_Attribute.setSpacing(0)
        SearchInput_Attribute_Widget.setLayout(SearchInput_Attribute)
        self.lb.addWidget(SearchInput_Attribute_Widget)
        searchComBox = QComboBox()

        SearchInput_Attribute.addWidget(searchComBox)
        Search = QLineEdit()

        SearchInput_Attribute.addWidget(Search)

    def UiInit(self, layout: QVBoxLayout,) -> None:
        self.addSearch()
        # AttributeEitor = QWidget()
        self.Sstart()
        self.setWindowTitle('Setting - '+self.User+' - 首选项')
