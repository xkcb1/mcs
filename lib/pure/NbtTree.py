import nbtlib
<<<<<<< HEAD
import sys
import os
=======
import sys,os
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
import PyQt5.QtGui as QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import *
<<<<<<< HEAD
# import end
import gc


class NbtTrewwThread(QThread):   # 创建线程类
    def __init__(self, File, TreeWidget):
        super(NbtTrewwThread, self).__init__()
        self.File = File
        self.TreeWidget = TreeWidget

    def run(self):     # 重写run()方法
        TreePureNbtToStl(self.File, self.TreeWidget)
        print('finished Thread')
        del self
        gc.collect()
        return
#######################################################################


=======
#import end
class NbtTrewwThread(QThread):   # 创建线程类
    def __init__(self,File,TreeWidget):
        super(NbtTrewwThread, self).__init__()
        self.File = File
        self.TreeWidget = TreeWidget
    def run(self):     # 重写run()方法
        TreePureNbtToStl(self.File, self.TreeWidget)
#######################################################################
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
def deleteItem(TreeWidget):
    try:
        # 尝试删除子节点（通过其父节点，调用removeChild函数进行删除）
        currNode = TreeWidget.currentItem()
        parent1 = currNode.parent()
        parent1.removeChild(currNode)
    except Exception:
        # 遇到异常时删除根节点
        try:
            rootIndex = TreeWidget.indexOfTopLevelItem(currNode)
            TreeWidget.takeTopLevelItem(rootIndex)
        except Exception:
            print(Exception)
########################################################################
<<<<<<< HEAD


def TreePureNbtToStl(File, TreeWidget: QTreeWidget):
=======
def TreePureNbtToStl(File,TreeWidget:QTreeWidget):
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    TreeWidget.clear()
    nbt_file = nbtlib.load(File)
    nbt_file = nbtlib.Compound(nbt_file)
    tagParent = QTreeWidgetItem(TreeWidget)
<<<<<<< HEAD
    tagParent.setText(0, File.split('//')[-1])
    for item in nbt_file:
        if str(type(nbt_file[item])) == "<class 'nbtlib.tag.ByteArray'>":
            MakeTree(nbtlib.ByteArray(nbt_file[item]), tagParent, item)
        else:
            MakeTree(nbt_file[item], tagParent, item)
    # print(nbt_file)
    del nbt_file, tagParent
    gc.collect()


def MakeTree(parent, parentWidget, name=''):
    tag = QTreeWidgetItem(parentWidget)
    if str(type(parent)) == "<class 'nbtlib.tag.String'>":
        tag.setIcon(0, QIcon('./img/fileicon/str_1.png'))
        tag.setText(0, name)
        tag.setText(1, str(parent))
    elif str(type(parent)) == "<class 'nbtlib.tag.ByteArray'>":
        tag.setIcon(0, QIcon('./img/fileicon/B_LIST_1.png'))
        tag.setText(0, name+' ['+str(len(parent))+']')
        for item in parent:
            MakeTree(item, tag)
        if len(parent) == 0:
            tag.setText(1, '[ ]')
    elif str(parent)[:4] == 'Byte':
        tag.setIcon(0, QIcon('./img/fileicon/B_1.png'))
        tag.setText(0, name)
        tag.setText(1, str(parent))
    elif str(parent)[:4] == 'Long':
        tag.setIcon(0, QIcon('./img/fileicon/L_1.png'))
        tag.setText(0, name)
        tag.setText(1, str(parent))
    elif str(parent)[:5] == 'Short':
        tag.setIcon(0, QIcon('./img/fileicon/S_1.png'))
        tag.setText(0, name)
        tag.setText(1, str(parent))
    elif str(parent)[:5] == 'Float':
        tag.setIcon(0, QIcon('./img/fileicon/F_1.png'))
        tag.setText(0, name)
        tag.setText(1, str(parent))
    elif str(parent)[:8] == 'Compound':
        tag.setIcon(0, QIcon('./img/fileicon/COM_1.png'))
        tag.setText(0, name+' ['+str(len(parent))+']')
        for item in parent:
            if str(type(parent)) == "<class 'nbtlib.tag.String'>":
                # print(item,type(parent))
                MakeTree(nbtlib.String(item), tag, parent)
            else:
                MakeTree(parent[item], tag, item)
        if len(parent) == 0:
            tag.setText(1, '{ }')
    elif str(parent)[:6] == 'Double':
        tag.setIcon(0, QIcon('./img/fileicon/D_1.png'))
        tag.setText(0, name)
        tag.setText(1, str(parent))
    elif str(parent)[:3] == 'End':
        tag.setIcon(0, QIcon('./img/fileicon/NONE_1.png'))
        tag.setText(0, name)
        tag.setText(1, str(parent))
    elif str(parent)[:3] == 'Int':
        tag.setIcon(0, QIcon('./img/fileicon/I_1.png'))
        tag.setText(0, name)
        tag.setText(1, str(parent))
    elif str(parent)[:4] == 'List':
        tag.setIcon(0, QIcon('./img/fileicon/LIST_1.png'))
        tag.setText(0, name+' ['+str(len(parent))+']')
        for item in parent:
            MakeTree(item, tag)
        if len(parent) == 0:
            tag.setText(1, '[ ]')
    del tag
=======
    tagParent.setText(0,File.split('//')[-1])
    for item in nbt_file:
        if str(type(nbt_file[item])) == "<class 'nbtlib.tag.ByteArray'>":
            MakeTree(nbtlib.ByteArray(nbt_file[item]),tagParent,item)
        else:
            MakeTree(nbt_file[item],tagParent,item)
    #print(nbt_file)
def MakeTree(parent,parentWidget,name=''):
    if str(type(parent)) == "<class 'nbtlib.tag.String'>":
        tag = QTreeWidgetItem(parentWidget)
        tag.setIcon(0,QIcon('./img/fileicon/str_1.png'))
        tag.setText(0,name)
        tag.setText(1,str(parent))
    elif str(type(parent)) == "<class 'nbtlib.tag.ByteArray'>":
        tagParent = QTreeWidgetItem(parentWidget)
        tagParent.setIcon(0,QIcon('./img/fileicon/B_LIST_1.png'))
        tagParent.setText(0,name+' ['+str(len(parent))+']')
        for item in parent:
            MakeTree(item,tagParent)
        if len(parent) == 0:
            tagParent.setText(1,'[ ]')
    elif str(parent)[:4] == 'Byte':
        tag = QTreeWidgetItem(parentWidget)
        tag.setIcon(0,QIcon('./img/fileicon/B_1.png'))
        tag.setText(0,name)
        tag.setText(1,str(parent))
    elif str(parent)[:4] == 'Long':
        tag = QTreeWidgetItem(parentWidget)
        tag.setIcon(0,QIcon('./img/fileicon/L_1.png'))
        tag.setText(0,name)
        tag.setText(1,str(parent))
    elif str(parent)[:5] == 'Short':
        tag = QTreeWidgetItem(parentWidget)
        tag.setIcon(0,QIcon('./img/fileicon/S_1.png'))
        tag.setText(0,name)
        tag.setText(1,str(parent))
    elif str(parent)[:5] == 'Float':
        tag = QTreeWidgetItem(parentWidget)
        tag.setIcon(0,QIcon('./img/fileicon/F_1.png'))
        tag.setText(0,name)
        tag.setText(1,str(parent))
    elif str(parent)[:8] == 'Compound':
        tagParent = QTreeWidgetItem(parentWidget)
        tagParent.setIcon(0,QIcon('./img/fileicon/COM_1.png'))
        tagParent.setText(0,name+' ['+str(len(parent))+']')
        for item in parent:
            if str(type(parent)) == "<class 'nbtlib.tag.String'>":
                #print(item,type(parent))
                MakeTree(nbtlib.String(item),tagParent,parent)
            else:
                MakeTree(parent[item],tagParent,item)
        if len(parent) == 0:
            tagParent.setText(1,'{ }')
    elif str(parent)[:6] == 'Double':
        tag = QTreeWidgetItem(parentWidget)
        tag.setIcon(0,QIcon('./img/fileicon/D_1.png'))
        tag.setText(0,name)
        tag.setText(1,str(parent))
    elif str(parent)[:3] == 'End':
        tag = QTreeWidgetItem(parentWidget)
        tag.setIcon(0,QIcon('./img/fileicon/NONE_1.png'))
        tag.setText(0,name)
        tag.setText(1,str(parent))
    elif str(parent)[:3] == 'Int':
        tag = QTreeWidgetItem(parentWidget)
        tag.setIcon(0,QIcon('./img/fileicon/I_1.png'))
        tag.setText(0,name)
        tag.setText(1,str(parent))
    elif str(parent)[:4] == 'List':
        tagParent = QTreeWidgetItem(parentWidget)
        tagParent.setIcon(0,QIcon('./img/fileicon/LIST_1.png'))
        tagParent.setText(0,name+' ['+str(len(parent))+']')
        for item in parent:
            MakeTree(item,tagParent)
        if len(parent) == 0:
            tagParent.setText(1,'[ ]')
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
