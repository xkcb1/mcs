# 每个module要求实现一个init(parent,Name,self)函数，来获取此次初始化
import os
import sys
import PyQt5.QtGui
<<<<<<< HEAD
=======
import vtk
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import *
<<<<<<< HEAD

from lib.readConfig import readConfig
from lib.StyleReader import StyleReader
# model需要opengl的功能，不使用qt3d
# import base functions
from lib.base import *
# end
# 不知道为什么，qt系列的3d功能好混乱，而且教程很少
SELF = None


=======
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from lib.readConfig import readConfig
from lib.StyleReader import StyleReader
#model需要opengl的功能，不使用qt3d
#import base functions
from lib.base import *
#end
#不知道为什么，qt系列的3d功能好混乱，而且教程很少
vtk.qt.QVTKRWIBase = "QGLWidget"
SELF = None
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
def init(parent: QVBoxLayout, Name, self) -> None:
    global SELF
    globals()['SELF'] = self
    SELF = self
    # 可以统一不用定义在self下
<<<<<<< HEAD
    MODELThisWidget = QWidget()
    MODELThisWidget.setStyleSheet('border:0px;')
    parent.addWidget(MODELThisWidget)
    thisLayout = QVBoxLayout(MODELThisWidget)
    MODELThisWidget.setLayout(thisLayout)
    # add
    # PureEditor = UrsinaPureEditor(thisLayout, self, MODELThisWidget)


class UrsinaPureEditor:
    def __init__(self, Layout, parent, MODELThisWidget):
        self.Layout = Layout
        self.parent = parent
        self.MODELThisWidget = MODELThisWidget
        self.UrsinaPureEditor()

    def UrsinaPureEditor(self):
        cmd = 'python UrsinaPureEditor/UrsinaPureEditor.init.py '
        pid = subprocess.Popen(cmd, shell=True).pid
        print(pid)
        #
        time.sleep(1)
        hwnd = win32gui.FindWindowEx(
            0, 0, "WinGraphicsWindow0", "UrsinaPureEditor")
        window = QWindow.fromWinId(hwnd)
        UrsinaWidget = self.parent.createWindowContainer(
            window, self.MODELThisWidget)
        self.Layout.addWidget(UrsinaWidget)
=======
    self.MODELThisWidget = QWidget()
    self.MODELThisWidget.setStyleSheet('border:0px;')
    parent.addWidget(self.MODELThisWidget)
    self.ThisLeftDiv = QWidget()  # noqa: F405
    self.ThisLeftDiv.setMinimumWidth(30)
    self.ThisLeftDiv.setMaximumWidth(30)
    self.ThisLeftDiv.setObjectName('thisModelLeftDiv')
    #add
    LEFT_layout = QVBoxLayout(self.ThisLeftDiv)
    LEFT_layout.setContentsMargins(3,3,3,3)
    LEFT_layout.setSpacing(0)
    self.ThisLeftDiv.setLayout(LEFT_layout)
    LEFT_add = QPushButton()
    LEFT_add.setIcon(QIcon('./img/file/icons/3d.svg'))
    LEFT_layout.addWidget(LEFT_add)
    LEFT_add.setMaximumSize(QSize(24,24))
    LEFT_add.setMinimumSize(QSize(24, 24))
    LEFT_add.clicked.connect(openNbtFile)
    LEFT_layout.addStretch(999)
    self.ModelToptabs = QTabWidget()
    self.ModelToptabs.TabShape(1)
    self.ModelToptabs.setObjectName('ModelEditor')
    self.ModelToptabs.setStyleSheet('''
QTabBar::tab {
    padding-left: 5px;
    border-right: 1px solid #ccc;
    background-color: rgba(0,0,0,0);
    padding-right:0px;
    padding-top:4px;
    border-left: 0px;
}
QTabBar::tab:selected {
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
#ModelEditor {
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
}e
''')
    # tabs.setTabPosition(QTabWidget.West)
    self.ModelToptabs.setMovable(True)
    self.ModelToptabs.setTabsClosable(True)
    self.ModelToptabs.setContentsMargins(0, 0, 0, 0)
    ThisWidget_layout = QHBoxLayout()
    self.MODELThisWidget.setLayout(ThisWidget_layout)
    ThisWidget_layout.addWidget(self.ThisLeftDiv)
    #TOP
    TopDIV = QWidget()
    TopDIV.setMaximumHeight(25)
    TopDIV.setMinimumHeight(25)
    TOP_Layout = QHBoxLayout()
    TopDIV.setLayout(TOP_Layout)
    #
    ChooseColor = QComboBox()
    ChooseColor.addItem('black')
    #
    MAIN_Widget = QWidget()
    VLayout = QVBoxLayout()
    VLayout.setContentsMargins(0,0,0,0)
    MAIN_Widget.setLayout(VLayout)
    #
    VLayout.addWidget(self.TopDIV)
    VLayout.addWidget(self.ModelToptabs)
    ThisWidget_layout.addWidget(MAIN_Widget)#self.ModelToptabs
    ThisWidget_layout.setContentsMargins(0, 0, 0, 0)
    ThisWidget_layout.setSpacing(0)
    # test

    # AddModelEditor(self,'Model','openNBT')
ModelFile = {'newNBT': './img/icons/box.svg',
             'openNBT': './img/icons/codesandbox.svg',
             'newJson': '', 
             'openJson': ''}
model = []
def AddModelEditor(self, Name, mode,filepath):
    frame = QWidget()
    self.ModelToptabs.addTab(
        frame, QIcon(ModelFile[mode]), Name + '.nbt')
    # self.ModelToptabs.currentChanged.connect(ClickTextEditor)
    self.index = self.index + 1

    ThisModelLayout = QVBoxLayout(frame)
    ThisModelLayout.setContentsMargins(0,0,0,0)
    frame.setLayout(ThisModelLayout)
    ren = vtk.vtkRenderer()
    vtkWidget = QVTKRenderWindowInteractor(frame)
    ThisModelLayout.addWidget(vtkWidget)
    vtkWidget.GetRenderWindow().AddRenderer(ren)
    iren = vtkWidget.GetRenderWindow().GetInteractor()
    ren.SetBackground(0, 0, 0) # 设置背景颜色
    ##############################################################################
    # 加载stl三维模型
    filename = filepath
    ren.AddActor(Add3DByReadSTLFile(self,ren,filename))
    ##############################################################################
    # 绘制三维线
    ren.AddActor(Add3DLine(self,ren))
    ###############################################################################
    # 绘制三维坐标轴
    ##########################################################################
    #ren.AddActor(Add3DSphere(self,ren))
    ###########################################################################
    ren.ResetCamera()
    iren.Initialize()
def Add3DByReadSTLFile(self,ren,filename):
    """读取STL文件加载三维模型"""
    # Read stl
    reader = vtk.vtkOBJReader()
    reader.SetFileName(filename)
    # Create a mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    # Create an actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().EdgeVisibilityOn()  # 加载边缘信息
    # actor.GetProperty().SetColor(0.0, 1.0, 2.0)  # rgb 红绿蓝
    ren.AddActor(actor)

def Add3DLine(self,ren):
    """绘制三维图上的线"""
    colors = vtk.vtkNamedColors()
    for i in range(32):
        lineSource = vtk.vtkLineSource()
        lineSource.SetPoint1([0,0,i])
        lineSource.SetPoint2([32,0,i])
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(lineSource.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetLineWidth(1)
        actor.GetProperty().SetColor(colors.GetColor3d("gray"))
        ren.AddActor(actor)
    for i in range(32):
        lineSource = vtk.vtkLineSource()
        lineSource.SetPoint1([i,0,0])
        lineSource.SetPoint2([i,0,32])
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(lineSource.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetLineWidth(1)
        actor.GetProperty().SetColor(colors.GetColor3d("gray"))
        ren.AddActor(actor)
    #xx
    lineSource = vtk.vtkLineSource()
    lineSource.SetPoint1([0, 0, 32])
    lineSource.SetPoint2([32, 0, 32])
    Z = vtk.vtkPolyDataMapper()
    Z.SetInputConnection(lineSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(Z)
    actor.GetProperty().SetLineWidth(2)
    actor.GetProperty().SetColor(colors.GetColor3d("gray"))
    ren.AddActor(actor)
    lineSource = vtk.vtkLineSource()
    lineSource.SetPoint1([32, 0, 0])
    lineSource.SetPoint2([32, 0, 32])
    Z = vtk.vtkPolyDataMapper()
    Z.SetInputConnection(lineSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(Z)
    actor.GetProperty().SetLineWidth(2)
    actor.GetProperty().SetColor(colors.GetColor3d("gray"))
    ren.AddActor(actor)
    #z
    lineSource = vtk.vtkLineSource()
    lineSource.SetPoint1([0, 0, 0])
    lineSource.SetPoint2([0, 0, 32])
    Z = vtk.vtkPolyDataMapper()
    Z.SetInputConnection(lineSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(Z)
    actor.GetProperty().SetLineWidth(2)
    actor.GetProperty().SetColor(colors.GetColor3d("green"))
    ren.AddActor(actor)
    #x
    lineSource = vtk.vtkLineSource()
    lineSource.SetPoint1([0, 0, 0])
    lineSource.SetPoint2([32, 0, 0])
    X = vtk.vtkPolyDataMapper()
    X.SetInputConnection(lineSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(X)
    actor.GetProperty().SetLineWidth(2)
    actor.GetProperty().SetColor(colors.GetColor3d("red"))
    ren.AddActor(actor)
    #y
    lineSource = vtk.vtkLineSource()
    lineSource.SetPoint1([0, 0, 0])
    lineSource.SetPoint2([0, 32, 0])
    Y = vtk.vtkPolyDataMapper()
    Y.SetInputConnection(lineSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(Y)
    actor.GetProperty().SetLineWidth(2)
    actor.GetProperty().SetColor(colors.GetColor3d("blue"))
    ren.AddActor(actor)
# endregion
def ClickTextEditor():
    pass
def openNbtFile():
    filepath = QFileDialog.getOpenFileName(SELF, "选择文件")[0]
    obj_file_path = MakeStlFileByNbt(filepath)
    fileName = filepath.split('/')[-1]
    print(SELF)
    AddModelEditor(SELF, fileName, 'openNBT',obj_file_path)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
