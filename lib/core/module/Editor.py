<<<<<<< HEAD
# 每个module要求实现一个init(parent,Name,self)函数，来获取此次初始化
# 这个是编辑器主函数
import os
import sys
import PyQt5.QtGui as QtGui
from PyQt5 import QtCore, QtGui
=======
#每个module要求实现一个init(parent,Name,self)函数，来获取此次初始化
#这个是编辑器主函数
import os,sys
import PyQt5.QtGui as QtGui
from PyQt5 import QtCore
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
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
=======
from pathlib import Path
import qutepart
import PyQt5.Qsci as Qsci
import lib.core.function.FileIcon
#import base functions
from lib.base import *
#end
def init(parent,Name,self):
    globals()['SELF'] = self
    print("init ->",Name)#输出调试
    self.EditorToptabs = QTabWidget()
    self.EditorToptabs.TabShape(1)
    self.EditorToptabs.setObjectName('TextEditor')
    self.EditorToptabs.setStyleSheet('''
QTabBar::tab {
    padding-left: 5px;
    border-right: 1px solid #e5e5e5;
    background-color: rgba(0,0,0,0);
    padding-right:0px;
    padding-top:4px;
    border-left: 0px;
}
QTabBar::tab:selected {
    margin-top: 0px;
    border-top: 2px solid #4888ff !important;
    padding-left: 5px;
    padding-right:0px;
    border-right: 1px solid #ccc;
    border-bottom: 0px;
}
QTabBar::tab:!selected{

}
QTabBar::tab:first {
    border-left: 0px !important;
}
#TextEditor {
    padding: 0px;
    border: 0px !important;
}
QTabBar::tab-bar{
    
}
QTabWidget::pane{
	border:none;
    border-top: 1px solid #e5e5e5;
}
QTabWidget {
    border: 0px;
    border-top: 1px solid #e5e5e5;
}
''')
    #tabs.setTabPosition(QTabWidget.West)
    self.EditorToptabs.setMovable(True)
    self.EditorToptabs.setTabsClosable(True)
    self.EditorToptabs.setContentsMargins(0,0,0,0)
    #self.EditorToptabs.
    parent.addWidget(self.EditorToptabs)
    parent.parent().setStyleSheet('border: 0px !important;')
    #new一个新的
    NewTextEditor(self,'untitled','print(1)','python',index=0)
    NewTextEditor(self,'text','print(2)','python',index=0)
    NewTextEditor(self,'text2','print(2)','javascript',index=0)
    self.Editorindex = self.Editorindex + 1
def ClickTextEditor():
    pass
def NewTextEditor(self,Name,Text,filetype,index):
    globals()[Name+"_Widget"] = QWidget()
    globals()[Name+"_Widget"].setStyleSheet('border: 0px !important;border-radius: 0px 0px 5px 5px !important;')
    globals()[Name+"_Path"] = QWidget()
    InfoLabelLayout = QHBoxLayout(globals()[Name+"_Path"])
    InfoLabelLayout.setContentsMargins(0,0,0,0)
    globals()[Name+"_Path_Label"] = QLabel()
    globals()[Name+"_Path_Label"].setStyleSheet('text-align: left;')
    globals()[Name+"_Path_Label"].setText('行 0, 列 0')
    globals()[Name+"_Path_Label"].setMinimumHeight(20)
    globals()[Name+"_Path_Label"].setMaximumWidth(50)
    InfoLabelLayout.addWidget(globals()[Name+"_Path_Label"])
    InfoLabelLayout.setSpacing(10)
    #创建一个tab长度info
    TabLength = QLabel()
    TabLength.setText('空格:4')
    InfoLabelLayout.addWidget(TabLength)
    
    globals()[Name] = CodeWidget(globals()[Name+"_Path_Label"])
    
    globals()[Name+"_Path"].setObjectName("Function_Path")
    globals()[Name+"_Path"].setStyleSheet('border: 0px !important;border-radius: 0px 0px 5px 5px !important;border-top:1px solid #e5e5e5;')
    globals()[Name+"_Path"].setMaximumHeight(20)
    globals()[Name+"_Path"].setMinimumHeight(20)
    globals()[Name+"_Layout"] = QVBoxLayout()
    globals()[Name+"_Layout"].setContentsMargins(0,0,0,0)
    globals()[Name+"_Layout"].setSpacing(0)
    #
    globals()[Name+"_Layout"].addWidget(globals()[Name])
    globals()[Name+"_Layout"].addWidget(globals()[Name+"_Path"])
    globals()[Name+"_Path_PATHWIDGET"] = QWidget()
    InfoLabelLayout.addWidget(globals()[Name+"_Path_PATHWIDGET"])
    #
    globals()[Name+"_Widget"].setLayout(globals()[Name+"_Layout"])
    #
    globals()[Name].setContentsMargins(0,0,0,0)
    self.EditorToptabs.addTab(globals()[Name+"_Widget"],QIcon(lib.core.function.FileIcon.getIcon(filetype)),Name+'.'+filetype[:2])
    self.EditorToptabs.currentChanged.connect(ClickTextEditor)
    #tabwidget
    globals()[Name].setText(Text)#Path(__file__).read_text(encoding='utf-8')
    
    #EditorWidget = QWidget()
    self.EditorList.append(globals()[Name])
    pass
class CodeWidget(Qsci.QsciScintilla):
    #init
    def __init__(self,InfoLabel):
        super().__init__()
        self.Font_ = QtGui.QFont('Consolas', 9)
        self.InfoLabel = InfoLabel
        self.setSelectionForegroundColor(QColor("#000"))
        self.setSelectionBackgroundColor(QColor("#d9e1ec"))
        self.setEolMode(self.SC_EOL_LF)    # 以\n换行
        self.setWrapMode(self.WrapWord)    # 自动换行。self.WrapWord是父类QsciScintilla的
        self.setAutoCompletionSource(self.AcsAll)  # 自动补全。对于所有Ascii字符
        self.setAutoCompletionCaseSensitivity(False)  # 自动补全大小写敏感
        self.setAutoCompletionThreshold(1)  # 输入多少个字符才弹出补全提示
        self.setFolding(True)  # 代码可折叠
        self.setFont(QtGui.QFont('Consolas', 15))  # 设置默认字体
        # self.setMarginType(0, self.NumberMargin)    # 0~4。第0个左边栏显示行号
        # self.setMarginLineNumbers(0, True)  # 我也不知道
        # self.setMarginsBackgroundColor(QtGui.QColor(120, 220, 180))  # 边栏背景颜色
        # self.setMarginWidth(0, 30)  # 边栏宽度
        self.setAutoIndent(True)  # 换行后自动缩进
        self.setUtf8(True)  # 支持中文字符
        self.setUtf8(True)        
        self.setEolMode(self.SC_EOL_CRLF)#文件中的每一行都以EOL字符结尾（换行符为 \r \n）
        #2.设置括号匹配模式
        self.setBraceMatching(self.StrictBraceMatch)# 
        #3.设置 Tab 键功能
        self.setIndentationsUseTabs(True)#行首缩进采用Tab键，反向缩进是Shift +Tab
        self.setIndentationWidth(4)     #行首缩进宽度为4个空格
        self.setIndentationGuides(True)#    显示虚线垂直线的方式来指示缩进
        self.setTabIndents(True)    #编辑器将行首第一个非空格字符推送到下一个缩进级别
        self.setAutoIndent(True)    #插入新行时，自动缩进将光标推送到与前一个相同的缩进级别
        self.setBackspaceUnindents(True)
        self.setTabWidth(4)         # Tab 等于 4 个空格
        #4.设置光标
        self.setCaretWidth(2)           #光标宽度（以像素为单位），0表示不显示光标
        self.setCaretForegroundColor(QColor("darkCyan"))    #光标颜色
        self.setCaretLineVisible(True)      #是否高亮显示光标所在行
        self.setCaretLineBackgroundColor(QColor('#fff'))     #光标所在行的底色
        #5.设置页边特性。        这里有3种Margin：[0]行号    [1]改动标识   [2]代码折叠
            #5.1 设置行号
        self.setMarginsFont(self.Font_)      #行号字体
        self.setMarginLineNumbers(0,True)    #设置标号为0的页边显示行号    
        self.setMarginWidth(0,'0000')  #行号宽度
        self.setMarkerForegroundColor(QColor("#FFFFFF"),0)  
            #5.2 设置改动标记    
        self.setMarginType(1, self.SymbolMargin)   # 设置标号为1的页边用于显示改动标记 
        self.setMarginWidth(1, "000")          #改动标记占用的宽度
        self.setMarginMarkerMask(1, 0b1111)
        self.setMarkerForegroundColor(QColor("#ee1111"),1)  #00ff00    
            #5.3  设置代码自动折叠区域
        self.setFolding(self.PlainFoldStyle)
        self.setMarginWidth(16,16)
                #5.3.1 设置代码折叠和展开时的页边标记 - +
        self.markerDefine(self.Minus, self.SC_MARKNUM_FOLDEROPEN)
        self.markerDefine(self.Plus, self.SC_MARKNUM_FOLDER)
        self.markerDefine(self.Minus, self.SC_MARKNUM_FOLDEROPENMID)
        self.markerDefine(self.Plus, self.SC_MARKNUM_FOLDEREND)
                #5.3.2 设置代码折叠后，+ 的颜色FFFFFF
        self.setMarkerBackgroundColor(QColor("#FFBCBC"), self.SC_MARKNUM_FOLDEREND)
        self.setMarkerForegroundColor(QColor("0,0,0,0"), self.SC_MARKNUM_FOLDEREND)
        self.setSyntax()
    def setSyntax(self):
        lexer = Qsci.QsciLexerPython()
        # lexer.setDefaultFont(这里填 QFont 类型的字体)
        self.setLexer(lexer)    # 关键是这句
    def keyPressEvent(self, e):
        '''和 QWidget 一样'''
        if e.key() == QtCore.Qt.Key_Escape:
            print ('hehe')
            #out in here

        super().keyPressEvent(e)
    def mousePressEvent(self,e):
        #重载这个方法，并且第一时间调用父方法
        super().mousePressEvent(e)
        self.InfoLabel.setText('行 '+str(self.getCursorPosition()[0]+1)+', '+'列 '+str(self.getCursorPosition()[1]))
    def wheelEvent(self, e):
        ''' Ctrl + 滚轮 控制字体缩放 '''
        if QtWidgets.QApplication.keyboardModifiers() == QtCore.Qt.ControlModifier:
            da = e.angleDelta()
            if da.y() > 0:
                self.zoomIn(1)    # QsciScintilla 自带缩放的功能。参数是增加的字体点数
                #print(self.marginWidth(0))
            elif da.y() < 0:
                self.zoomOut(1)
        else:
            super().wheelEvent(e)   # 留点汤给父类，不然滚轮无法翻页
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
