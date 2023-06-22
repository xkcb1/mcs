# 每个module要求实现一个init(parent,Name,self)函数，来获取此次初始化
import os
import sys
import PyQt5.QtGui
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import *
from lib.readConfig import readConfig
from lib.StyleReader import StyleReader
# terminal
import subprocess
from threading import Thread
# import base functions
from lib.base import *
# end
SELF = None
widgetList = []
consoleIndex = 0
Terminalindex = 0


def init(parent: QVBoxLayout, Name, self):
    globals()['SELF'] = self
    global SELF
    SELF = self
    # 可以统一不用定义在self下
    ThisWidget = QWidget()
    parent.addWidget(ThisWidget)
    self.TerminalToptabs = QTabWidget()
    self.TerminalToptabs.TabShape(1)
    self.TerminalToptabs.setObjectName('Terminal')
    self.TerminalToptabs.setMovable(True)
    self.TerminalToptabs.setTabsClosable(True)
    self.TerminalToptabs.setContentsMargins(0, 0, 0, 0)
    ThisWidget_layout = QVBoxLayout()
    ThisWidget.setLayout(ThisWidget_layout)
    ThisWidget_layout.setContentsMargins(0, 0, 0, 0)
    ThisWidget_layout.setSpacing(0)
    # 一个按钮+
    OptionBar = QWidget()
    OptionBar.setMaximumHeight(25)
    OptionBar.setMinimumHeight(25)
    OptionBar.setObjectName('OptionBar')
    OptionBar.setStyleSheet('''
#terminal_button {
    border-top: 1px solid '''+self.theme+';'+'''
    border-right: 1px solid '''+self.theme+';'+'''
    border-bottom: 1px solid '''+self.theme+';'+'''
}
''')
    ThisWidget_layout.addWidget(OptionBar)
    ThisWidget_layout.addWidget(self.TerminalToptabs)
    # make the topbar=OptionBar
    clearAll = QPushButton('清除')
    clearAll.setObjectName('terminal_button')
    clearAll.setMaximumWidth(70)
    clearAll.setIcon(QIcon('./img/icons/delete.svg'))
    savethis = QPushButton('保存')
    savethis.setObjectName('terminal_button')
    savethis.setMaximumWidth(70)
    savethis.setIcon(QIcon('./img/icons/save.svg'))
    checkhistory = QPushButton('记录')
    checkhistory.setObjectName('terminal_button')
    checkhistory.setMaximumWidth(70)
    checkhistory.setIcon(QIcon('./img/icons/camera.svg'))
    run = QPushButton('运行')
    run.setObjectName('terminal_button')
    run.setMaximumWidth(70)
    run.setIcon(QIcon('./img/icons/play.svg'))
    stop = QPushButton('停止')
    stop.setObjectName('terminal_button')
    stop.setMaximumWidth(70)
    stop.setIcon(QIcon('./img/icons/stop-circle.svg'))
    add = QPushButton('新建')
    add.setObjectName('terminal_button')
    add.setMaximumWidth(70)
    add.setIcon(QIcon('./img/icons/file-plus.svg'))
    ThisTopBarLayout = QHBoxLayout()
    ThisTopBarLayout.addWidget(clearAll)
    ThisTopBarLayout.addWidget(savethis)
    ThisTopBarLayout.addWidget(checkhistory)
    ThisTopBarLayout.addWidget(run)
    ThisTopBarLayout.addWidget(stop)
    ThisTopBarLayout.addWidget(add)
    ThisTopBarLayout.addWidget(QWidget())
    ThisTopBarLayout.setContentsMargins(0, 0, 0, 0)
    ThisTopBarLayout.setSpacing(0)
    #
    OptionBar.setLayout(ThisTopBarLayout)
    # this
    # parent.addWidget(self.AddButton)
    # test
    AddTerminal('terminal-python', 'python')
    AddTerminal('terminal-output', 'output')
    AddTerminal('terminal-luad2', 'lua')


TerminalType = {'local': './img/cmd.ico',
                'python': './img/file/icons/python.svg',
                'lua': './img/file/icons/lua.svg',
                'output': './img/file/icons/log.svg'}


def AddTerminal(Name, mode):
    global consoleIndex
    global Terminalindex
    globals()[Name+"_Widget"+str(Terminalindex)] = QWidget()
    ThisTabWidget = globals()[Name+"_Widget"+str(Terminalindex)]
    SELF.TerminalToptabs.addTab(
        ThisTabWidget, QIcon(TerminalType[mode]), Name)
    SELF.TerminalToptabs.currentChanged.connect(ClickTextEditor)
    if mode == 'python':
        ThisLayout = QVBoxLayout()
        ThisLayout.setContentsMargins(0, 0, 0, 0)
        ThisLayout.setSpacing(0)
        thisOutput = QTextBrowser()
        thisOutput.setStyleSheet('''font-family:Courier New;''')
        ThisInputEdit = PPythonConsole()
        ThisInputEdit.setEnterFunction(thisOutput, running, Terminalindex)
        print('start at:widget->Terminalindex->', Terminalindex)
        ThisLayout.addWidget(thisOutput)
        ThisLayout.addWidget(ThisInputEdit)
        ThisTabWidget.setLayout(ThisLayout)
        # add
    elif mode == 'output':
        ThisLayout = QVBoxLayout()
        ThisLayout.setContentsMargins(0, 0, 0, 0)
        ThisLayout.setSpacing(0)
        globals()['output_'+str(SELF.outputIndex)] = QTextBrowser()
        thisOutput = globals()['output_'+str(SELF.outputIndex)]
        thisOutput.setStyleSheet('''font-family:Courier New;''')
        ThisLayout.addWidget(thisOutput)
        ThisTabWidget.setLayout(ThisLayout)
        thisOut = ''
        SELF.outputIndex += 1
        for i in range(0, len(getLog().split('\n'))):
            thisOut = thisOut + f'[{i}] : ' + getLog().split('\n')[i]+'\n'
        for i in range(0, SELF.outputIndex):
            globals()['output_'+str(i)].setText(thisOut)
        widgetList.append(thisOutput)
        thisOutput.ensureCursorVisible()
    elif mode == 'lua':
        ThisLayout = QVBoxLayout()
        ThisLayout.setContentsMargins(0, 0, 0, 0)
        ThisLayout.setSpacing(0)
        thisOutput = QTextBrowser()
        thisOutput.setStyleSheet('''font-family:Courier New;''')
        ThisInputEdit = PLuaConsole()
        ThisInputEdit.setEnterFunction(thisOutput, runningLua, Terminalindex)
        print('start at:widget->Terminalindex->', Terminalindex)
        ThisLayout.addWidget(thisOutput)
        ThisLayout.addWidget(ThisInputEdit)
        ThisTabWidget.setLayout(ThisLayout)
        # add
    else:
        pass
    Terminalindex = Terminalindex + 1


def log(SELF=SELF, widgetList=widgetList, *argv):
    print(*argv, SELF=SELF, widgetList=widgetList)
# log(SELF,1,2,3,4)


def ClickTextEditor():
    pass


def running(widget: QTextBrowser, command: str, ThisTerminalindex):
    print(SELF)
    global widgetList
    widgetList = []
    for i in range(0, SELF.outputIndex):
        widgetList.append(globals()['output_'+str(i)])
    try:
        widget.prompt = True
        # print(command.replace('print(',f'PureConsoleOutPut(globals()["ThisConsoleWidget_"+str({ThisTerminalindex})],'))
        exec(command.replace('print(', f'PureConsoleOutPut(globals()["ThisConsoleWidget_"+str({ThisTerminalindex})],').replace(
            'input(', 'Pinput(').replace('log(', f'log(SELF,widgetList,'), globals())
        if len(command) >= 4:
            if command[:4] == 'def ':
                something = '<b style="color:skyblue;">run:"'+command+'"</b>'
                PureConsoleOutPut(widget, something)
        if 'print(' not in command:
            something = '<b style="color:skyblue;">run:"'+command+'"</b>'
            PureConsoleOutPut(widget, something)
        widget.prompt = False
        widget.ThisLine += 1
    except Exception as e:
        out = e
        msg = traceback.format_exc()
        widget.prompt = True
        prompt = '<b style="color:#111;">[</b><b style="color:red;">'+str(
            widget.ThisLine)+'</b><b style="color:#111;">] : </b>'
        for line in msg.split('\n'):
            if line != msg.split('\n')[0]:
                prompt = '&nbsp;'*6
            if line == msg.split('\n')[0]:
                line = '<a style="color:red;">'+line + '</a>'
            if line == msg.split('\n')[-1]:
                pass
            if line != msg.split('\n')[2]:
                widget.append(prompt+'<a style="color:red;">'+str(line)+'</a>')
        widget.prompt = False
        widget.ThisLine += 1
    thisOut = ''
    for i in range(0, len(getLog().split('\n'))):
        thisOut = thisOut + f'[{i}] : ' + getLog().split('\n')[i]+'\n'
    for i in range(0, SELF.outputIndex):
        globals()['output_'+str(i)].setText(thisOut)
    widget.ensureCursorVisible()


def Pinput(*argv):
    pass


def PureConsoleOutPut(widget, *argv):
    outstr = ''
    if widget.prompt == True:
        for value in argv:
            outstr += str(value) + ' '
        prompt = '<b style="color:#111;">[</b><b style="color:red;">'+str(
            widget.ThisLine)+'</b><b style="color:#111;">] : </b>'
        widget.append(prompt+str(outstr))
        widget.prompt = False
    else:
        for value in argv:
            outstr += str(value) + ' '
        widget.append(' '*(len('['+str(widget.ThisLine)+'] : ')+0)+str(outstr))


class PPythonConsole(QLineEdit):
    # Pure [xk] makes this class
    def setEnterFunction(self, widget, func, ThisTerminalindex) -> None:
        self.runningFunc = func
        self.runWidget = widget
        widget.ThisLine = 0
        widget.prompt = False
        ThisFont = QFont()
        ThisFont.setFamily('Courier New')
        widget.setFont(ThisFont)
        widget.append(
            '<b style="color:blue;">Python</b> <a style="color:gray;">'+str(sys.version)+'</a>')
        self.Terminalindex = ThisTerminalindex
        widget.append(
            '<a style="color:gray;">Type "help", "copyright", "credits" or "license" for more information.</a>')
        globals()['ThisConsoleWidget_'+str(Terminalindex)] = widget

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.nativeVirtualKey() == 13 and self.text() != '':
            self.getcommand = self.text()
            self.runningFunc(self.runWidget, self.getcommand,
                             self.Terminalindex)
            self.setText('')
        return super().keyPressEvent(a0)
# for i in range(10):print('w',i)


class PLuaConsole(QLineEdit):
    def setEnterFunction(self, widget, func, ThisTerminalindex) -> None:
        self.runningFunc = func
        self.runWidget = widget
        widget.ThisLine = 0
        widget.prompt = False
        ThisFont = QFont()
        ThisFont.setFamily('Courier New')
        widget.setFont(ThisFont)
        widget.append(
            '<b style="color:blue;">Lua</b> <a style="color:gray;"> 5.4.4  Copyright (C) 1994-2022 Lua.org, PUC-Rio</a>')
        self.Terminalindex = ThisTerminalindex
        globals()['ThisConsoleWidget_'+str(Terminalindex)] = widget

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.nativeVirtualKey() == 13 and self.text() != '':
            self.getcommand = self.text()
            self.runningFunc(self.runWidget, self.getcommand,
                             self.Terminalindex)
            self.setText('')
        return super().keyPressEvent(a0)


def runningLua(widget: QTextBrowser, command: str, ThisTerminalindex):
    with open('./scripts/lua/run.lua', 'w', encoding='utf-8') as wf:
        wf.write(command)
    with os.popen('scripts\\lua\\lua.exe scripts\\lua\\run.lua 2>&1', 'r') as shell:
        widget.append(shell.read())
    print('run Lua: '+command+' in ', ThisTerminalindex,
          SELF=SELF, widgetList=widgetList)
