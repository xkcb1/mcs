import os,sys
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from lib.StyleReader import StyleReader
from lib.newWindow import *
from newProject import NewProjectWindow
from Main import NewEditor
from lib.ProjectType import ProjectType,ProjectTypeTab
#定义APP_LOG
from lib.base import *
clearLog()
print('Already running the application in Python '+sys.version)
settings = {'IfUseMorePackage':False,
            'IfUseMoreCompiler':False,
            'IfSaveAsProjectAuto':False}
settings['name'] = ""
settings['path'] = ""
settings['type'] = ""
settings['info'] = ""
settings['w'] = 1000 + 14
settings['h'] = 800 + 14
settings['x'] = None
settings['y'] = None
def readConfigFile():
    if os.path.exists('./config/config.json') == False:
        with open('./config/config.json','w',encoding='utf-8') as NewConfig:
            NewConfig.write(str(settings))
        return "new"
    else:
        with open('./config/config.json','r',encoding='utf-8') as ReadConfig:
            getSetting = eval(ReadConfig.read())
        return getSetting
def OpenNewProjectWindow():
    app = QApplication(sys.argv)
    Window = NewProjectWindow()
    Window.UseTheme()
    Window.show()
    sys.exit(app.exec())
getconfig = readConfigFile()
if getconfig == 'new':
    OpenNewProjectWindow()
elif settings == getconfig:
    OpenNewProjectWindow()
else:
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    editor = NewEditor()
    #apply_stylesheet(app, theme='dark_amber.xml')
    editor.setting = getconfig
    #editor.getAllWidget(editor)
    #editor.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    editor.W = getconfig['w']
    editor.H = getconfig['h']
    editor.resize(editor.W,editor.H)
    editor.title = f"MC studio ({editor.User}) - {ProjectType[getconfig['type']]} : {getconfig['name']}"
    editor.setWindowTitle(editor.title)
    editor.label_2.setText(f"MC studio ({editor.User}) - {ProjectType[getconfig['type']]} : {getconfig['name']}")#title
    if getconfig['x'] != None and getconfig['y'] != None:
        editor.move(getconfig['x'],getconfig['y'])
    editor.show()
    sys.exit(app.exec())
