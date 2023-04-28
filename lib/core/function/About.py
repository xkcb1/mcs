from lib.base import *
class MakeAbout(QWidget):
    def __init__(self):
        super().__init__()
        self.UIinit()
    def UIinit(self):
        self.mainLayout = QHBoxLayout()
        self.Icon = QLabel()
        self.Icon.setPixmap(QPixmap(r'./img/appicon/icon64.png'))
        #self.Icon.setScaledContents(True)
        self.Icon.setMinimumSize(64,64)
        self.mainLayout.addWidget(self.Icon)
        self.mainLayout.setContentsMargins(4,4,2,4)
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
<b>McStudio</b><p><a>It is a software used to generate and create "mc datapack" or "mc mode".</a><a href="{self.url}">  our website</a></p>
<b style="color:gray;text-align: center;">©Copyright 2023</b>
                          ''')