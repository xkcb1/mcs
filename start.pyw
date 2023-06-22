import os
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import PyQt5.QtGui as QtGui


class START(QMainWindow):
    def __init__(self):
        super(START, self).__init__()
        self.pv = 0
        self.timer1 = QBasicTimer()
        self.setFixedSize(600, 400)

        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.activateWindow()
        self.setStyleSheet('''
#ThisBg{
    background-image:url(./img/untitled3.png);
    background-color:rgba(0,0,0,0.0) !important;
}
#Version {
    color:rgba(255,255,255,0.8);
    background-color:rgba(0,0,0,0.0) !important;
    border:0px !important;
    outline:0px !important;
}
#Label {
    color:#CFDEFF;
    font-style:italic;
    background-color:rgba(0,0,0,0.0) !important;
}
#Label2 {
    color:#eee;
    font-style:italic;
    background-color:rgba(0,0,0,0.0) !important;
}
QProgressBar {
    
    background-color:  rgba(0,0,0,0) !important;
    text-align: center;
    color: rgba(255,255,255,0.0);
}
QProgressBar::chunk {
    border: 0px solid grey !important;
    background:QLinearGradient(x1:0,y1:0,x2:1.25,y2:0,stop:0 rgba(12, 123, 179,0.9),stop:1  rgba(242, 186, 232,0.9)); 
}
#pgb_G {
    border: 1px solid grey;
    background-color:rgba(0,0,0,0);
}
#info {
    color:#aaa;
    background-color:rgba(0,0,0,0.0) !important;
}


                           ''')
        self.UIinit()

    def UIinit(self):
        font_id = QtGui.QFontDatabase.addApplicationFont(
            './ttf/minecraft_z2font.ttf')

        font = QFont(
            QtGui.QFontDatabase.applicationFontFamilies(font_id)[0], 10)
        font2 = QFont(
            QtGui.QFontDatabase.applicationFontFamilies(font_id)[0], 34)
        font3 = QFont(
            QtGui.QFontDatabase.applicationFontFamilies(font_id)[0], 27)
        self.ThisBg = QWidget(self)
        self.ThisBg.setObjectName('ThisBg')
        self.setCentralWidget(self.ThisBg)
        # untitled_600x400

        self.Label = QLabel(self)
        self.Label.setObjectName('Label')
        self.Label.setScaledContents(True)
        self.Label.move(40, 50)
        self.Label.setText('MC')
        self.Label.resize(300, 70)
        self.Label.setFont(font2)
        #
        self.Label2 = QLabel(self)
        self.Label2.setObjectName('Label2')
        self.Label2.setScaledContents(True)
        self.Label2.move(145, 50)
        self.Label2.setText('STUDIO')
        self.Label2.resize(300, 80)
        self.Label2.setFont(font3)
        #
        self.versionLabel = QLabel(self)
        self.versionLabel.setObjectName('Version')
        self.versionLabel.setFont(font)
        self.versionLabel.setText('VERSION 0.0.1')
        self.versionLabel.move(60, 120)
        self.versionLabel.resize(200, 30)
        #
        self.prompt = QTextBrowser(self)
        self.prompt.setObjectName('Version')
        self.prompt.setText('正在加载主程序 . . . 0%')
        self.prompt.move(40, 270)
        self.prompt.resize(400, 30)
        self.prompt.setFont(QFont('Arial', 9))
        # self.pgb.
        self.pgb = QProgressBar(self)
        self.pgb.move(42, 302)
        self.pgb.resize(516, 6)
        #

        self.myTimerState()
        #
        self.info = QLabel(self)
        self.setFont(QFont('Arial', 4))
        self.info.move(40, 325)
        self.info.setObjectName('info')
        self.info.setText(
            'MCstudio is free for everyone to read and use (MIT). \nIt is a software used to generate and create "mc datapack" or "mc mode".\n(C) CopyRight PureXK 2022')
        self.info.resize(440, 50)
        self.info.setWordWrap(True)
        self.info.setAlignment(QtCore.Qt.AlignTop)

    def myTimerState(self):
        if self.timer1.isActive():
            self.timer1.stop()
        else:
            self.timer1.start(15, self)

    def timerEvent(self, e):

        if self.pv == 100:
            self.timer1.stop()
            # self.hide()

            # self.mainWindow.show()
        else:
            self.pv += 3
            self.pgb.setValue(self.pv)

    def update_event(self):
        if self.timer1.isActive():
            self.timer1.stop()
        self.pv = 0
        self.pgb.setValue(self.pv)
