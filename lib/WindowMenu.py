WindowMenu = {
    # base
    "Editor": {"icon": "./img/main_3/Editor.png", "Menu": {"select": {'icon': '', 'function': 'lib.core.function.Editor.select'}}},
    "Resource": {"icon": "./img/main_3/Resource.png", "Menu": {}},
    "Attribute": {"icon": "./img/main_3/Attribute.png", "Menu": {}},
    "Model": {"icon": "./img/main_3/Model.png", "Menu": {}},
    "Painter": {"icon": "./img/main_3/Painter.png", "Menu": {}},
    "Builtin": {"icon": "./img/main_3/White.png", "Menu": {}},
    "White": {"icon": "./img/main_3/White.png", "Menu": {}},
    # more windows
    "Node": {"icon": "./img/main_3/Node.png", "Menu": {}},
    "Asset": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "Renderer": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "Terminal": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "Blocks": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "Entities": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "Tools": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "Example": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "Commands": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "McsLib": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "Designer": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "WorldEditor": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "TerrainMaker": {"icon": "./img/main_3/Editor.png", "Menu": {}},
    "White": {"icon": "./img/main_3/White.png", "Menu": {}},
    "NbtViewer": {"icon": "./img/main_3/Nbt.png", "Menu": {}},
    "HexEditor": {"icon": "./img/main_3/HexEditor.png", "Menu": {}},
    "pakage": {"icon": "./img/main_3/pakage.png", "Menu": {}},
    'ItemList': {"icon": "./img/main_3/ModelList.png", "Menu": {}},
    'Info': {"icon": "./img/main_3/CoreApi.png", "Menu": {}},
}
# set the icon there
'''WindowMenu:  { 
                    icon:*Path,
                    Menu:{*MenuName:{widget:*QObject,tip:*text,func:*func}} 
                    // to top menu :QPushButton
                }
'''
WindowMenuInChoice = {
    'Standard': {"Editor": {"icon": "./img/main_3/Editor.png", "Menu": {}},
                 "Resource": {"icon": "./img/main_3/Resource.png", "Menu": {}},
                 "Attribute": {"icon": "./img/main_3/Attribute.png", "Menu": {}},
                 "Model": {"icon": "./img/main_3/Model.png", "Menu": {}},
                 "Painter": {"icon": "./img/main_3/Painter.png", "Menu": {}},
                 "Builtin": {"icon": "./img/main_3/Builtin.png", "Menu": {}},
                 "White": {"icon": "./img/main_3/White.png", "Menu": {}},
                 },
    # Convention
    "Convention": {
        "Node": {"icon": "./img/main_3/Node.png", "Menu": {}},
        "Asset": {"icon": "./img/main_3/Asset.png", "Menu": {}},
        "Renderer": {"icon": "./img/main_3/Renderer.png", "Menu": {}},
        "Terminal": {"icon": "./img/main_3/Terminal.png", "Menu": {}},
        "Commands": {"icon": "./img/main_3/Commands.png", "Menu": {}},
        'Info': {"icon": "./img/main_3/CoreApi.png", "Menu": {}},
    },
    # extend
    "extend": {
        "Blocks": {"icon": "./img/main_3/Blocks.png", "Menu": {}},
        "Designer": {"icon": "./img/main_3/Designer.png", "Menu": {}},
        "McsLib": {"icon": "./img/main_3/McsLib.png", "Menu": {}},
        "WorldEditor": {"icon": "./img/main_3/WorldEditor.png", "Menu": {}},
        "TerrainMaker": {"icon": "./img/main_3/TerrainMaker.png", "Menu": {}},
        "Entities": {"icon": "./img/main_3/Entities.png", "Menu": {}},
    },
    'tools': {
        "NbtViewer": {"icon": "./img/main_3/Nbt.png", "Menu": {}},
        "HexEditor": {"icon": "./img/main_3/HexEditor.png", "Menu": {}},
        "Pakage": {"icon": "./img/main_3/pakage.png", "Menu": {}},
        "Tools": {"icon": "./img/main_3/Tools.png", "Menu": {}},
        "Example": {"icon": "./img/main_3/Example.png", "Menu": {}},
        'ItemList': {"icon": "./img/main_3/ModelList.png", "Menu": {}},
    },
}

StarterInfo = {
    "Start": {
        "A": {"size": 10, "Window": 'Resource', "Children": None, "float": "left"},
        "B": {"size": 50, "Window": 'Info', "Children": None, "float": "right"},
        "PROJECT_LIST": ['None']},
    "Editor": {
        "rightDIV": {"size": 40, "Window": None, "Children": {
            "LeftTopDiv": {"size": 10, "Window": "Resource", "Children": None, "float": "top"},
            "LeftBottomDiv": {"size": 10, "Window": "Asset", "Children": None, "float": "bottom"},
        }, "float": "right"},
        "leftDIV": {"size": 10, "Window": 'Editor', "Children": None, "float": "left"},
        "PROJECT_LIST": ['None']},
    "Model": {
        "B": {"size": 10, "Window": None,
              "Children": {
                  "LeftTopDiv": {"size": 10, "Window": "Resource", "Children": None,  "float": "top"},
                  "LeftBottomDiv": {"size": 10, "Window": "NbtViewer", "Children": None, "float": "bottom"},
              }, "float": "left"},
        "A": {"size": 40, "Window": 'Model', "Children": None, "float": "right"},
        "PROJECT_LIST": ['None']},
    "World": {
        "B": {"size": 10, "Window": None,
              "Children": {
                  "LeftTopDiv": {"size": 10, "Window": "Resource", "Children": None,  "float": "top"},
                  "LeftBottomDiv": {"size": 10, "Window": "Tools", "Children": None, "float": "bottom"},
              }, "float": "left"},
        "A": {"size": 40, "Window": 'WorldEditor', "Children": None, "float": "right"},
        "PROJECT_LIST": ['None']},
    "Node": {
        "B": {"size": 10, "Window": None, "Children": {
            "LeftTopDiv": {"size": 10, "Window": "Resource", "Children": None, "float": "top"},
            "LeftBottomDiv": {"size": 20, "Window": None, "Children": {
                "A": {"size": 10, "Window": "Builtin", "Children": None, "float": "top"},
                "B": {"size": 10, "Window": "Attribute", "Children": None, "float": "bottom"},
            }, "float": "bottom"},
        }, "float": "left"},
        "A": {"size": 40, "Window": 'Node', "Children": None, "float": "right"},
        "PROJECT_LIST": ['None']},
    "Terminal": {
        "A": {"size": 40, "Window": 'Terminal', "Children": None, "float": "left"},
        "B": {"size": 10, "Window": 'Resource', "Children": None, "float": "right"},
        "PROJECT_LIST": ['None']},
    'Nbt': {
        "A": {"size": 50, "Window": None, "Children": {
            "LeftTopDiv": {"size": 30, "Window": "NbtViewer", "Children": None, "float": "top"},
            "LeftBottomDiv": {"size": 20, "Window": "Asset", "Children": None, "float": "bottom"},
        }, "float": "left"},
        "B": {"size": 40, "Window": 'HexEditor', "Children": None, "float": "right"},
        "PROJECT_LIST": ['None'],
    },
}
