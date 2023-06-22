import os,sys
from PyQt5 import QtCore ,QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#from newproject.py
SummonTheProject = {"mcfunction":["./img/func.png",'.mcfunction,.txt,.*','yellow',1],
                                 "datapack":["./img/pack.png",'.mcsProject (.json,.mcfuntion,.nbt,.png...)','cadetblue',1],
                                 "3d file":["./img/cb-be.png",".mcr,.mca,.nbt,.json(3d)","skyblue",1],
                                 "2d file":["./img/func-be.png",".png,.jpg,.json(2d)","orange",1],
                                 "viewer":["./img/dat.png","some files viewer","gray",1],
                                 "white project":["./img/white.png",'the white project','lightgray',1]}
def readConfig():
    with open('./config/config.json','r',encoding='utf-8') as f:
        getConfig = f.read()
    config =  eval(getConfig)
    if config['path'] == '~/':
        config['path'] = 'C:/'
    tempList = []
    for item in SummonTheProject:
        tempList.append(item)
    for i in range(len(SummonTheProject)):
        if i == config['type']:
            config['type'] = tempList[i]
    return config
def makeProject(self):
    setting = readConfig()
    VMFile = {}
    Maindiv = ''
    if setting['type'] == 'mcfunction':
        Maindiv = 'Editor'
    elif setting['type'] == 'datapack':
        Maindiv = 'Editor'
    elif setting['type'] == '3d':
        Maindiv = 'Model'
    elif setting['type'] == '2d':
        Maindiv = 'Painter'
    elif setting['type'] == 'viewer':
        Maindiv = 'White'
    else:
        Maindiv = 'White'
    ProjectStarter = str({'version':'0.0.1'})
    if setting['type'] == 'command' or setting['type'] == 'command-BE':
        VMFile = {
            setting['name']:{
                setting['name']+'.mcfunction':"",
                'readme':setting['info'],
                '.mcstudio':{
                    setting['name']+'.mcsProject':ProjectStarter
                }
            }
        }
    elif setting['type'] == 'mcfunction' or setting['type'] == 'mcfuntion-BE':
        VMFile = {
            setting['name']:{
                'data':{
                    setting['name']:{
                        'functions':{
                            setting['name']+'.mcfunction':"",
                        }
                    }
                },
                'pack.mcmeta':'',
                'pack.png':None,
                'readme':'',
                '.mcstudio':{
                    setting['name']+'.mcsProject':ProjectStarter
                }
            }
        }
    elif setting['type'] == 'datapack':
        VMFile = {
            setting['name']:{
                'data':{
                    setting['name']:{
                        'functions':{
                            setting['name']+'.mcfunction':"",
                        },
                        'advanceements':{
                            'advanceements.json':''
                        },
                        'item_modifiers':{
                            'modifier.json':''
                        },
                        'predicates':{
                            'predicates.json':''
                        },
                        'loot_tables':{
                            'loot_tables.json':''
                        },
                    },
                    'minecraft':{
                        'tags':{
                            'functions':{
                                'tick.json':'',
                                'load.json':'',
                            }
                        }
                    }
                },
                'pack.mcmeta':'',
                'pack.png':None,
                'readme':'',
                '.mcstudio':{
                    setting['name']+'.mcsProject':ProjectStarter
                }
            }
        }
    elif setting['type'] == 'viewer':
        VMFile = {
            setting['name']:{
                setting['name']+'.nbt':"",
                'readme':setting['info'],
                '.mcstudio':{
                    setting['name']+'.mcsProject':ProjectStarter
                }
            }
        }
    elif setting['type'] == '3d':
        VMFile = {
            setting['name']:{
                setting['name']+'.mcr':None,
                'readme':setting['info'],
                '.mcstudio':{
                    setting['name']+'.mcsProject':ProjectStarter
                }
            }
        }
    elif setting['type'] == '2d':
       VMFile = {
            setting['name']:{
                setting['name']+'.dat':'',
                'readme':setting['info'],
                '.mcstudio':{
                    setting['name']+'.mcsProject':ProjectStarter
                }
            }
        }
    elif setting['type'] == 'white project':
        VMFile = {
            setting['name']:{
                'readme':setting['info'],
                '.mcstudio':{
                    setting['name']+'.mcsProject':ProjectStarter
                }
            }
        }
    ReadDictFromVMfile(VMFile[setting['name']],path=setting['path'],name=setting['name'],self=self)
def getFrist(dict):
    tempList = []
    for item in dict:
        tempList.append(item)
    return tempList[0]
def ReadDictFromVMfile(lastDict,path,name,self=None):
    if type(lastDict) == type({}):#怪，为什么不能type == "dict"
        print('folder-',name)
        try:
            os.makedirs(path+'/'+name)
        except:
            QMessageBox.warning(self, "warning", "项目 '"+name+"' 已存在。", QMessageBox.Cancel)
            return
        for item in lastDict:
            ReadDictFromVMfile(lastDict[item],path+'/'+name,item)
    elif type(lastDict) == type(''):
        with open(path+'/'+name,'w') as n:
            n.write(lastDict)
        print('file-',name)