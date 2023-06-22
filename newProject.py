import sys, os
from PyQt5 import QtCore ,QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QGuiApplication
from lib.StyleReader import StyleReader
import getpass
from Main import NewEditor
from lib.readConfig import makeProject
#import base functions
from lib.base import *
#end
#import
class NewProjectWindow(QMainWindow):#继承Qwidget
    def __init__(self):
        #init <- super
        super().__init__()
        globals()['SELF'] = self
        self.initUI()#加载基础界面
    def center(self):#居中_方法
        ScreenWidth = QGuiApplication.primaryScreen().geometry().width()
        ScreenHeight = QGuiApplication.primaryScreen().geometry().height()
        self.move(int(ScreenWidth/2) - int(self.W/2), int(ScreenHeight/2) - int(self.H/2))
    def initUI(self):
        #setting
        #self.IfCanResize = False
        #基础界面
        self.W = 750+14
        self.H = 580+14
        self.resize(self.W,self.H)
        self.setFixedSize(self.W,self.H)#禁止改变大小
        self.center()
        self.User = getpass.getuser()
        #self.setGeometry(300, 300, 250, 150)
        # #(x, y, w, h)       
        self.setWindowTitle('新建项目 (new project) - '+self.User)#bg
        self.MainWidget = QWidget(self)
        self.MainWidget.move(0,0)
        self.MainWidget.resize(self.W,self.H)
        self.MainWidget.setObjectName('MainWidget')
        #bg END
        self.leftDiv = QFrame(self.MainWidget)#leftDiv
        self.leftDiv.move(0,0)
        self.leftDiv.resize(250,self.MainWidget.height() - 35)
        self.leftDiv.setObjectName('leftDiv')
        self._LeftUI_()#use function
        #self.setStyleSheet('border-radius:7px;')
        #END
        self.rightDiv = QFrame(self.MainWidget)#rightDiv
        self.rightDiv.move(250,0)
        self.rightDiv.resize(self.MainWidget.width() - 251,self.MainWidget.height() - 35)
        self.rightDiv.setObjectName('rightDiv')
        self._RightUI_()
        #END
        self.bottomDiv = QFrame(self.MainWidget)#bottomDiv
        self.bottomDiv.move(0,self.MainWidget.height() - 34)
        self.bottomDiv.resize(self.W,34)
        self.bottomDiv.setObjectName('bottomDiv')
        self._BottomUI_()
        #use newProject.qss theme
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
    def UseTheme(self):
        styleFile = './style/newProject_light.qss'
        qssStyle = StyleReader.readQSS(styleFile)
        self.setStyleSheet(qssStyle)
    #end
    def ProjectListChoose_MakeListItem(self,ParentWidget):
        self.ProjectChoose = {'空白项目':"./img/50.png",'新建项目':"./img/58.png"}
        for item in self.ProjectChoose:
            self.item_ = QListWidgetItem()
            self.item_.setSizeHint(QSize(218,28))
            self.TempWidget_ = QWidget()
            self.TempWidget_.setObjectName('_ListItem_')
            self.TempWidget_.resize(220,28)
            self.TempWidget_.move(5,0)
            ThisImage = self.ProjectChoose[item]
            #Map
            self.Map = QLabel(self.TempWidget_)
            self.Map.move(9,3)
            self.Map.resize(22, 22)
            maps = QPixmap(self.ProjectChoose[item]).scaled(22, 22)
            self.Map.setPixmap(maps)
            #
            self.TextMain = QLabel(self.TempWidget_)
            self.TextMain.move(0,8)
            self.TextMain.setObjectName('_BigText_')
            self.TextMain.setText(item)
            ParentWidget.addItem(self.item_)
            ParentWidget.setItemWidget(self.item_,self.TempWidget_)
        return self.item_
    def Item_clicked(self):
        Get_Item_Click = self.ProjectListChoose.selectedItems()[0]
        #
    def selectThis(self):
        getText = self.SearchProject.text()
        count = 0
        for item in self.SummonTheProject:
            count = count + 1
            if item == getText:
                QMessageBox.information(self, "info", f"find the Item in [{getText}:{count}]", QMessageBox.Cancel)
                return
        QMessageBox.information(self, "info", f"cannot find the item for {getText}", QMessageBox.Cancel)

    def _LeftUI_(self):
        #value
        self.SummonTheProject = {"mcfunction":["./img/func.png",'.mcfunction,.txt,.*','yellow',1],
                                 "datapack":["./img/pack.png",'.mcsProject (.json,.mcfuntion,.nbt,.png...)','cadetblue',1],
                                 "3d file":["./img/cb-be.png",".mcr,.mca,.nbt,.json(3d)","skyblue",1],
                                 "2d file":["./img/func-be.png",".png,.jpg,.json(2d)","orange",1],
                                 "viewer":["./img/dat.png","some files viewer","gray",1],
                                 "white project":["./img/white.png",'the white project','lightgray',1]}
        #left ui
        self.LeftWidgetTopFrame = QFrame(self.MainWidget)
        self.LeftWidgetTopFrame.move(0,0)
        self.LeftWidgetTopFrame.resize(249,139)
        self.LeftWidgetTopFrame.setObjectName('Left_BG')
        #
        self.Left_title1 = QLabel(self.LeftWidgetTopFrame)
        self.Left_title1.setText('新建项目')
        self.Left_title1.resize(self.leftDiv.width() - 1,25)
        self.Left_title1.move(0,0 + 25)
        self.Left_title1.setObjectName('LeftTitle1')
        #
        self.ProjectListChoose = QListWidget(self.LeftWidgetTopFrame)
        self.ProjectListChoose.move(0,25 + 25)
        self.ProjectListChoose.resize(249,60)
        self.ProjectListChoose.setObjectName('ProjectListChoose')
        out = self.ProjectListChoose_MakeListItem(self.ProjectListChoose)
        self.ProjectListChoose.itemClicked.connect(self.Item_clicked)
        self.ProjectListChoose.setCurrentItem(out)
        #NEWproject
        self.SearchProject = QLineEdit(self.LeftWidgetTopFrame)
        self.SearchProject.textChanged[str].connect(self.SearchonChanged)
        self.SearchProject.move(0,0)
        self.SearchProject.resize(180,25)
        self.SearchProject.setObjectName('SearchInput')
        #button
        self.SearchButton = QPushButton(self.LeftWidgetTopFrame)
        self.SearchButton.setText('搜索')
        self.SearchButton.clicked.connect(self.selectThis)
        self.SearchButton.move(180,0)
        self.SearchButton.resize(70,25)
        self.SearchButton.setObjectName('SearchButton')
        #end
        self.Left_title2 = QLabel(self.LeftWidgetTopFrame)
        self.Left_title2.setText('生成项目')
        self.Left_title2.resize(70,25)
        self.Left_title2.move(0,85 + 25)
        self.Left_title2.setObjectName('LeftTitle2')
        #List
        self.ProjectList = QListWidget(self.leftDiv)
        self.ProjectList.move(0,139)
        self.ProjectList.resize(249,self.MainWidget.height() -234 + 66)
        self.ProjectList.setObjectName('ListWidgetThis')
        self.ProjectList.itemClicked.connect(self.Itemclicked)
        self.ListItem_L = []
        #Make the List->
        for item in self.SummonTheProject:
            self.item = QListWidgetItem()
            self.item.setSizeHint(QSize(240,35))
            self.ListItem_L.append(self.item)
            self.TempWidget = QWidget()
            self.TempWidget.setObjectName('ListItem')
            self.TempWidget.resize(240,28)
            #big Text
            self.TextMain = QLabel(self.TempWidget)
            self.TextMain.move(35,1)
            self.TextMain.setObjectName('BigText')
            self.TextMain.setText(item)
            #small Text
            self.TextSmall = QLabel(self.TempWidget)
            self.TextSmall.setText(self.SummonTheProject[item][1])
            self.TextSmall.setObjectName('SmallText')
            getColor = self.SummonTheProject[item][2]
            self.TempWidget.setStyleSheet(f"border-left: 3px solid {getColor};")
            self.TextSmall.move(35,16)
            #img
            self.Map = QLabel(self.TempWidget)
            SCALED = self.SummonTheProject[item][3]
            self.Map.move(int(11/SCALED),int(8/SCALED - 1))
            self.Map.resize(int(20*SCALED),int(20*SCALED))
            maps = QPixmap(self.SummonTheProject[item][0]).scaled(int(20*SCALED),int(20*SCALED))
            self.Map.setPixmap(maps)
            self.ProjectList.addItem(self.item)
            self.ProjectList.setItemWidget(self.item,self.TempWidget)
        #propmt->
        '''self.more = QFrame(self.leftDiv)
        self.more.move(0,self.MainWidget.height() -96)
        self.more.resize(249,66)
        self.more.setObjectName('more')
        #on title
        self.Left_title3 = QLabel(self.more)
        self.Left_title3.setText('打开项目')
        self.Left_title3.resize(self.leftDiv.width() - 3,20)
        self.Left_title3.move(1,2)
        self.Left_title3.setObjectName('LeftTitle2')
        #
        #FRAME
        self.OPEN_Button = QPushButton(self.more)
        self.OPEN_Button.move(3,30)
        self.OPEN_Button.resize(243,27)
        self.OPEN_Button.setObjectName('OPEN_Button')
        self.OPEN_Button.setText('None(no choose): ~/')
        self.OPEN_Button.clicked.connect(self.selectPath)'''
        pass
    def Itemclicked(self):
        Get_Item_Click = self.ProjectList.selectedItems()[0]
        pass
    def _RightUI_(self):
        #right ui
        #Label This
        BaseSetting = QLabel(self.rightDiv)
        BaseSetting.setText('基础设置')
        BaseSetting.resize(self.MainWidget.width() - 290,25)
        BaseSetting.setObjectName('BaseSetting')
        BaseSetting.move(20,10)
        #WHAT
        '''
        self.WHAT = QPushButton(self.rightDiv)
        self.WHAT.move(5,self.rightDiv.height() - 30)
        self.WHAT.setText('?')
        self.WHAT.resize(26,26)
        self.WHAT.setObjectName('WHAT')
        '''
        self.lbltitle = QLabel("名称(name):")
        self.lblpath = QLabel("位置(path):")
        self.lblcontent= QLabel("描述(descripion):")
        self.lbltitle.setObjectName('RightTitle')
        self.lblpath.setObjectName('RightTitle')
        self.lblcontent.setObjectName('RightTitle')
        #
        self.letitle = QLineEdit()
        self.lepath = QPushButton()
        self.lepath.clicked.connect(self.OPEN_AN_PATH)
        self.lepath.setText('None(no choose): ~/')
        self.lepath.setObjectName('lepath')
        self.tecontent = QTextEdit()
        self.FrameTopRight = QFrame(self.rightDiv)
        self.FrameTopRight.resize(self.MainWidget.width() - 250 - 40,150)
        self.FrameTopRight.move(20,40)
        self.grid = QGridLayout(self.FrameTopRight)
        self.grid.setSpacing(10)
        self.grid.setObjectName('GRIDlayout')
        self.grid.addWidget(self.lbltitle,0,0)
        self.grid.addWidget(self.letitle,0,1)
        self.grid.addWidget(self.lblpath,1,0)
        self.grid.addWidget(self.lepath,1,1)
        #
        self.grid.addWidget(self.lblcontent,2,0)
        self.grid.addWidget(self.tecontent,2,1)
        #more settings
        MoreSetting = QLabel(self.rightDiv)
        MoreSetting.setText('高级设置')
        MoreSetting.resize(self.MainWidget.width() - 290,25)
        MoreSetting.setObjectName('BaseSetting')
        MoreSetting.move(20,210)
        #1
        self.IfUseMorePackage = QCheckBox("是否启用更多扩展(IfUseMorePackage)", self.rightDiv)
        self.IfUseMorePackage.clicked.connect(self.RadioIFUSE)
        self.IfUseMorePackage.move(20,240)
        self.IfUseMorePackage.setObjectName('IfUseMorePackage')
        #2
        self.IfUseMoreCompiler = QCheckBox("是否使用扩展编译器(IfUseMoreCompiler)", self.rightDiv)
        self.IfUseMoreCompiler.clicked.connect(self.RadioIFUSECOMPILER)
        self.IfUseMoreCompiler.move(20,260)
        self.IfUseMoreCompiler.setObjectName('IfUseMoreCompiler')
        #3
        self.IfSaveAsProjectAuto = QCheckBox("是否自动备份项目(IfSaveAsProjectAuto)", self.rightDiv)
        self.IfSaveAsProjectAuto.clicked.connect(self.RadioIFUSECOMPILER)
        self.IfSaveAsProjectAuto.move(20,280)
        self.IfSaveAsProjectAuto.setObjectName('IfSaveAsProjectAuto')
        pass
    def _BottomUI_(self):
        #bottom ui
        #YES
        self.AcceptButton = QPushButton(self.bottomDiv)
        self.AcceptButton.move(self.bottomDiv.width() - 110,2)
        self.AcceptButton.setText('创建(N)')
        self.AcceptButton.setObjectName('AcceptButton')
        self.AcceptButton.resize(85,28)
        self.AcceptButton.clicked.connect(self.CreateProject)
        #NO
        self.ExitButton = QPushButton(self.bottomDiv)
        self.ExitButton.move(self.bottomDiv.width() - 195,2)
        self.ExitButton.setText('取消(O)')
        self.ExitButton.resize(85,28)
        self.ExitButton.setObjectName('ExitButton')
        self.ExitButton.clicked.connect(self.close)
        pass
    def OPEN_AN_PATH(self):
        path = QFileDialog.getExistingDirectory(self, '选择目录(path)', './')
        if len(path) > 0 :
            if path[0]:
                self.lepath.setText('{}'.format(path))
        else :
            pass
        pass
    def CreateProject(self):
        settings = {'IfUseMorePackage':False,
                    'IfUseMoreCompiler':False,
                    'IfSaveAsProjectAuto':False}
        if self.IfUseMorePackage.isChecked():
            settings['IfUseMorePackage'] = True
        if self.IfUseMoreCompiler.isChecked():
            settings['IfUseMoreCompiler'] = True
        if self.IfSaveAsProjectAuto.isChecked():
            settings['IfSaveAsProjectAuto'] = True
        path = self.lepath.text()
        name = self.letitle.text()
        info = self.tecontent.toPlainText()
        if len(self.ProjectList.selectedItems()) != 0:
            project = self.ListItem_L.index(self.ProjectList.selectedItems()[0])
        else:
            QMessageBox.warning(self, "warning", "请选择项目类型 (project-type):\n\n在左侧列表里选择一个项目并创建", QMessageBox.Cancel)
            return
        if path == 'None(no choose): ~/':
            path = 'C:/'
        if name == '':
            QMessageBox.warning(self, "warning", "请输入项目名称 (project-name):\n\n在右侧输入框内输入项目名称", QMessageBox.Cancel)
            return
        settings['name'] = name
        settings['path'] = path
        settings['type'] = project
        settings['info'] = info
        settings['w'] = 1000 + 14
        settings['h'] = 800 + 14
        settings['x'] = None
        settings['y'] = None
        self.hide()
        #print(settings)
        with open('./config/config.json','w',encoding='utf-8') as NewConfig:
            NewConfig.write(str(settings))
        self.config = settings
        makeProject(self)
        #sys.exit(app.exec_())
        #app2 = QApplication(sys.argv)
        self.editor = NewEditor()
        self.editor.setting = settings
        self.editor.W = settings['w']
        self.editor.H = settings['h']
        self.editor.resize(self.editor.W,self.editor.H)
        self.editor.setWindowTitle(f"MC studio ({self.editor.User}) - {settings['name']}")#title
        self.editor.show()
        #sys.exit(app2.exec_())
    def RadioIFUSE(self):
        pass
    def RadioIFUSECOMPILER(self):
        pass
    def IfSAVEASPROJECT(self):
        pass
    def SearchonChanged(self, text):
        pass
    '''
    def closeEvent(self, event):
        #重写默认的关闭事件
        reply = QMessageBox.question(self, 'Message',
            "是否放弃新建项目(new project)", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    '''
    '''def selectPath(self):
        path = QFileDialog.getExistingDirectory(self, '打开项目(open)', './')
        if len(path) > 0 :
            if path[0]:
                self.OPEN_Button.setText('{}'.format(path))
                MAIN.openEditor([path,'','',''])
                self.close()
        else :
            pass'''
'''if __name__ == '__main__':
    #main
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    Window = NewProjectWindow()
    Window.UseTheme()
    Window.show()
    sys.exit(app.exec_())'''