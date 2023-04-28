#Starter core module
import os,sys
import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#import lib
import lib.WindowMenu
#import base functions
from lib.base import *
#end
def PanelStarter(Sender:QPushButton,self,Name) -> None:#导入模块部分
    #Start the panel
    #初始化面板
    print(Name,self)
    #要从一个sender的Text推导出此panel,推荐用parent
    ParentWidget = Sender.parentWidget()
    #准备更改Sender
    #Sender.setText(Name)
    for item in lib.WindowMenu.WindowMenu:
        if item == Name:
            Exec_Code = f'''
try:
    import lib.core.module.{item}
    starterFromModule("{item}",ParentWidget,self)
    print("import lib.core.module.{item} successful")
except Exception as e:
    print(traceback.format_exc())
    print("Error import from module <lib.core.module.{item}>\\n")
        '''
            exec(Exec_Code)
    pass
def starterFromModule(Name:str,Parent:QWidget,self) -> None:#主初始化部分
    #print(Name,Parent)#获取到参数，表示初始化导入模块成功
    #准备清除现有的面板内容
    #print(dir(Parent))
    Parent_ = Parent.parent()
    #print(Parent_.children())
    for widget in Parent_.children():
        if widget.objectName()[0:len('Child_main_widget')] == 'Child_main_widget' and type(widget) == QWidget:
            IndexFromParent = widget.objectName()[len('Child_main_widget'):]
            try:
                if globals().get("_Layout"+IndexFromParent) != None:
                    print('clear :',"_Layout"+IndexFromParent)
                    item_list = list(range(globals()["_Layout"+IndexFromParent].count()))
                    item_list.reverse()# 倒序删除，避免影响布局顺序
                    for i in item_list:
                        item = globals()["_Layout"+IndexFromParent].itemAt(i)
                        globals()["_Layout"+IndexFromParent].removeItem(item)
                        if item.widget():
                            item.widget().deleteLater()
                    #删除全部控件
                    globals()["_Layout"+IndexFromParent].setContentsMargins(0,0,0,0)
                    globals()["_Layout"+IndexFromParent].setSpacing(0)
                else:
                    print('new :',"_Layout"+IndexFromParent)
                    globals()["_Layout"+IndexFromParent] = QVBoxLayout()
                        #控件
                    globals()["_Layout"+IndexFromParent].setContentsMargins(0,0,0,0)
                    globals()["_Layout"+IndexFromParent].setSpacing(0)
                    widget.setLayout(globals()["_Layout"+IndexFromParent])
                globals()["_Layout"+IndexFromParent].parent().setStyleSheet('')
            except Exception as e:
                print('[!]:no widget in change panel')
            exec(f"lib.core.module.{Name}.init(globals()['_Layout'+IndexFromParent],'{Name}',self)")#进入主初始化模块
            break