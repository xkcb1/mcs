from lib.base import *
<<<<<<< HEAD


=======
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
class MakeAbout(QWidget):
    def __init__(self):
        super().__init__()
        self.UIinit()
<<<<<<< HEAD

    def UIinit(self):
        self.mainLayout = QVBoxLayout()
        self.Icon = QLabel()
        self.Icon.setPixmap(QPixmap(r'./img/appicon/icon64.png'))
        self.Icon.setMinimumSize(96, 96)
        self.Icon.setAlignment(Qt.AlignCenter)
        self.mainLayout.addWidget(self.Icon)
        self.mainLayout.setContentsMargins(14, 14, 14, 14)
=======
    def UIinit(self):
        self.mainLayout = QHBoxLayout()
        self.Icon = QLabel()
        self.Icon.setPixmap(QPixmap(r'./img/appicon/icon64.png'))
        #self.Icon.setScaledContents(True)
        self.Icon.setMinimumSize(64,64)
        self.mainLayout.addWidget(self.Icon)
        self.mainLayout.setContentsMargins(4,4,2,4)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
        self.setLayout(self.mainLayout)
        self.Info = QTextBrowser()
        self.url = '???'
        self.Info.setStyleSheet('''
                                background-color: rgba(0,0,0,0);
                                border:0px;
                                outline: none;''')
        self.mainLayout.addWidget(self.Info)
        self.Info.setOpenExternalLinks(True)
        self.Info.setText(f'''
<<<<<<< HEAD
<b>McStudio</b><p><a>It is a software used to generate and create "mc datapack" or "mc mode".It free for every one to use.This software is completely open source, and is written in Python, pyqt5 and Unity3D. It adopts the theme libraries of qtvscodestyle, default(xk), qdarktheme, QSS-master, qt_material, and retains the license of monaco-editor and several other libraries.</a><a>This software has nothing to do with Mojang Studios and MoJang AB. This software is an independent Minecraft gameplay extension and production tool. The software reserves the ultimate ownership of the source code. If you want to contribute to the component development or gameplay expansion of Minecraft, please leave a message on our website and join us to contribute to the development and maintenance of this software.
</a><a href="{self.url}">  our website</a></p>
<b style="color:gray;text-align: center;">©Copyright 2023</b>
                          ''')
=======
<b>McStudio</b><p><a>It is a software used to generate and create "mc datapack" or "mc mode".</a><a href="{self.url}">  our website</a></p>
<b style="color:gray;text-align: center;">©Copyright 2023</b>
                          ''')
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
