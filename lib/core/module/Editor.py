# 每个module要求实现一个init(parent,Name,self)函数，来获取此次初始化
# 这个是编辑器主函数
import os
import sys
import PyQt5.QtGui as QtGui
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import *
from lib.readConfig import readConfig
from lib.StyleReader import StyleReader
# import base functions
from lib.base import *
# end
from OpenGL import GL
SELF = None


def init(parent, Name, self):
    global SELF
    globals()['SELF'] = self
    SELF = self
    print("init ->", Name)  # 输出调试
    #  main
    MainW_widget = QWidget()
    MainLayout = QHBoxLayout(MainW_widget)
    MainLayout.setContentsMargins(0, 0, 0, 0)
    MainLayout.setSpacing(0)
    ################################################################
    this_main = QWidget()
    This_main_right = QVBoxLayout(this_main)
    This_main_right.setContentsMargins(0, 0, 0, 0)
    This_main_right.setSpacing(0)
    # main
    EditorToptabs = QTabWidget()
    EditorToptabs.TabShape(1)
    EditorToptabs.setObjectName('TextEditor')
    EditorToptabs.setMovable(True)
    EditorToptabs.setTabsClosable(True)
    EditorToptabs.setContentsMargins(0, 0, 0, 0)
    # self.EditorToptabs.currentChanged.connect(ClickTextEditor)
    EditorToptabs.setStyleSheet('''
QTabWidget::pane{
	border-right:0px;
    border-bottom:0px;
}
QTabWidget {
    border-right:0px;
    border-bottom:0px;
}
''')
    # self.EditorToptabs.
    parent.addWidget(MainW_widget)
    parent.parent().setStyleSheet('border: 0px !important;')
    # leftPanel
    Eidtor_left = QWidget()
    leftLayout = QVBoxLayout(Eidtor_left)
    leftLayout.setContentsMargins(0, 5, 0, 0)
    leftLayout.setSpacing(7)
    Eidtor_left.setFixedWidth(25)
    #################################################################
    addFile = QPushButton()
    addFile.setIcon(QIcon('./img/icons/file-plus.svg'))
    leftLayout.addWidget(addFile)
    #
    saveFile = QPushButton()
    saveFile.setIcon(QIcon('./img/icons/save.svg'))
    leftLayout.addWidget(saveFile)
    #
    openFile = QPushButton()
    openFile.setIcon(QIcon('./img/icons/file.svg'))
    leftLayout.addWidget(openFile)
    #
    leftLayout.addStretch(99)
    #################################################################
    MainLayout.addWidget(Eidtor_left)
    MainLayout.addWidget(this_main)
    #
    EditorToptabs.setMaximumHeight(27)
    #
    WEB_EDITOR = QWebEngineView()
    WEB_EDITOR.setAttribute(Qt.WA_DontShowOnScreen, True)
    WEB_EDITOR.setAttribute(Qt.WA_DeleteOnClose, True)
    self.thisPath = sys.argv[0].replace(sys.argv[0].split(
        '\\')[-1], '').replace('\\', '/')
    self.url = self.thisPath+'editor.html'
    WEB_EDITOR.load(QUrl(self.url))
    WEB_EDITOR.reload()
    This_main_right.addWidget(EditorToptabs)
    This_main_right.addWidget(WEB_EDITOR)
    #
    self.Editorindex = self.Editorindex + 1
    #
    self.ThisFileName = 'untitled'
    #
    WEB_EDITOR.VM_FOLDER = {}

    def func_addFile():

        # 把新建的文件放进 虚拟文件夹
        WEB_EDITOR.VM_FOLDER['untitled'+str(self.newUntitledFileCount)] = ''
        print(WEB_EDITOR.VM_FOLDER)
        #
        widget = NewTextEditor(self, 'untitled'
                               + str(self.newUntitledFileCount), '')
        # print(SELF.EditorToptabs.currentWidget().children()[-1])
        index = EditorToptabs.indexOf(widget)
        EditorToptabs.setCurrentIndex(index)
        #
        self.newUntitledFileCount = self.newUntitledFileCount + 1

    def NONE_FUNCTION(a0):
        pass

    def ClickTextEditor(a0):
        # 改变选项卡时，(1)先去html里获取thisName和Data，(2)然后同步到python里，(3)最后获取新的文件，去同步和设置
        # step 1,2
        WEB_EDITOR.page().runJavaScript(
            f'''postTextToPython();''', js_callback)
        # step 3
        thisFile = EditorToptabs.currentIndex()
        fileName = EditorToptabs.tabText(thisFile)
        get_data = WEB_EDITOR.VM_FOLDER[fileName]
        WEB_EDITOR.page().runJavaScript(
            f'''setEitorText(`{get_data}`,"{fileName}");''', NONE_FUNCTION)
        #

    def NewTextEditor(self, Name, filetype):
        # step 1
        WEB_EDITOR.page().runJavaScript(
            f'''postTextToPython();''', js_callback)
        # step 2
        widget = QWidget()
        widget.setStyleSheet(
            'border: 0px !important;border-radius: 0px 0px 5px 5px !important;')
        if filetype != '':
            fileName = Name+'.'+filetype
        else:
            fileName = Name
        EditorToptabs.addTab(widget, QIcon(
            lib.core.function.FileIcon.getIcon(filetype)), fileName)
        # step 3
        return widget

    def js_callback(result):
        if result != None:
            # result = eval(str(result))
            WEB_EDITOR.VM_FOLDER[result[0]] = result[1]
    addFile.clicked.connect(func_addFile)
    NewTextEditor(self, 'untitled', '')
    EditorToptabs.currentChanged.connect(ClickTextEditor)
    self.WebList.append(WEB_EDITOR)
    #
