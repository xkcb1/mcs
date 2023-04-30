# 每个module要求实现一个init(parent,Name,self)函数，来获取此次初始化
import os
import sys
import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import *
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
def init(parent: QVBoxLayout, Name, self) -> None:
    global SELF
    globals()['SELF'] = self
    SELF = self
    # 可以统一不用定义在self下
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
    background-color: #eee;
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
    background-color: #eee;
    padding: 0px;
    border: 0px !important;
}
QTabBar::tab-bar{
    background-color: #ddd;
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

    ThisWidget_layout.addWidget(self.ModelToptabs)
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


def ClickTextEditor():
    pass
def openNbtFile():
    filepath = QFileDialog.getOpenFileName(SELF, "选择文件")[0]
    obj_file_path = MakeStlFileByNbt(filepath)
    fileName = filepath.split('\\')[-1]
    print(SELF)
    AddModelEditor(SELF, fileName, 'openNBT',obj_file_path)
    print_(SELF.vtk_widget)
    SELF.iren.Start()
class renderX(QThread):   # 创建线程类
    def __init__(self,Filepath,parent):
        super(renderX, self).__init__()
        self.Filepath = Filepath
        self.parent = parent
    def run(self):     # 重写run()方法
        self.parent.frame = QWidget()
        self.parent.ModelToptabs.addTab(
        self.parent.frame, QIcon(ModelFile[mode]), Name + '.nbt')
        # self.ModelToptabs.currentChanged.connect(ClickTextEditor)
        self.parent.index = self.index + 1
        #
        self.parent.vtk_vertical_layout = QVBoxLayout(self.frame)
        self.parent.frame.setLayout(self.vtk_vertical_layout)
        self.parent.vtk_widget = QVTKRenderWindowInteractor(self.frame)
        self.parent.vtk_vertical_layout.addWidget(self.vtk_widget)
        # 1.创建RenderWindow窗口
        self.parent.render_window = self.vtk_widget.GetRenderWindow()
        # 2.创建render
        self.parent.renderer = vtk.vtkRenderer()
        self.parent.renderer.SetBackground(1.0, 1.0, 1.0)  # 设置页面底部颜色值
        self.parent.render_window.AddRenderer(self.renderer)
        self.parent.render_window.Render()
        # 3.设置交互方式
        self.parent.iren = self.render_window.GetInteractor()  # 获取交互器
        self.parent.style = vtk.vtkInteractorStyleTrackballCamera()  # 交互器样式的一种，该样式下，用户是通过控制相机对物体作旋转、放大、缩小等操作
        self.parent.style.SetDefaultRenderer(self.renderer)
        self.parent.iren.SetInteractorStyle(self.style)
        # 4.添加世界坐标系
        self.parent.axesActor = vtk.vtkAxesActor()
        self.parent.axes_widget = vtk.vtkOrientationMarkerWidget()
        self.parent.axes_widget.SetOrientationMarker(self.axesActor)
        self.parent.axes_widget.SetInteractor(self.iren)
        self.axes_widget.EnabledOn()
        self.axes_widget.InteractiveOff()  # 坐标系是否可移动
        self.renderer.ResetCamera()
        self.iren.Initialize()
        self.iren.Start()