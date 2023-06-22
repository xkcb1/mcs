import darkdetect
import os
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from lib.StyleReader import StyleReader
from newProject import NewProjectWindow
from Main import NewEditor
from lib.ProjectType import ProjectType, ProjectTypeTab
# 定义APP_LOG
from lib.base import *
from threading import Thread, current_thread
# theme
from threading import *
# start
import qdarkstyle
from qdarkstyle.light.palette import LightPalette
import qdarktheme
import qtvscodestyle as qtvsc
from qt_material import apply_stylesheet
from start import START
#
process_time()

if darkdetect.isDark():
    print("Dark mode is enabled.")
else:
    print("Dark mode is not enabled.")

# setting
'''QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QGuiApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)'''
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setHighDpiScaleFactorRoundingPolicy(
    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
# QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
# qdarktheme.enable_hi_dpi()
app = QApplication(sys.argv)
# app.setStyleSheet(qdarkstyle.load_stylesheet())
# app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
# qdarktheme.setup_theme("auto")

stylesheet = qtvsc.load_stylesheet(qtvsc.Theme.LIGHT_VS)
app.setStyleSheet(stylesheet)

QWebEngineSettings.globalSettings().setAttribute(
    QWebEngineSettings.PluginsEnabled, True)
QWebEngineSettings.globalSettings().setAttribute(
    QWebEngineSettings.ScreenCaptureEnabled, True)
clearLog()
print('Already running the application in Python '+sys.version)

settings = {'IfUseMorePackage': False,
            'IfUseMoreCompiler': False,
            'IfSaveAsProjectAuto': False}
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
        with open('./config/config.json', 'w', encoding='utf-8') as NewConfig:
            NewConfig.write(str(settings))
        return "new"
    else:
        with open('./config/config.json', 'r', encoding='utf-8') as ReadConfig:
            getSetting = eval(ReadConfig.read())
        return getSetting


def OpenNewProjectWindow():
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
    start = START()
    start.show()
    app.processEvents()
    start.prompt.setText(f'正在加载主程序 . . . {str(start.pv)}%')
    editor = NewEditor(app, start)
    start.prompt.setText(
        f'程序已经准备好了! {str(start.pv)}%')
    # apply_stylesheet(app, theme='dark_amber.xml')
    editor.setting = getconfig
    # editor.getAllWidget(editor)
    # editor.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    editor.W = getconfig['w']
    editor.H = getconfig['h']
    editor.resize(editor.W, editor.H)
    editor.title = f"MC studio ({editor.User}) - {ProjectType[getconfig['type']]} : {getconfig['name']}"
    editor.setWindowTitle(
        f"MC studio ({editor.User}) - {ProjectType[getconfig['type']]} : {getconfig['name']}")  # title
    if getconfig['x'] != None and getconfig['y'] != None:
        editor.move(getconfig['x'], getconfig['y'])
    editor.show()
    editor.activateWindow()
    start.hide()
    sys.exit(app.exec())
