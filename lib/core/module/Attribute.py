from lib.base import *
# 从今以后，所有的parent都是一个布局了，可以直接addwidget
# 我们想的是，创建一个class，他实现一个属性框的UI部分，提供一组dictionary或者json类型
# 作为构造参数，提供一个string作为名字，以及一个Boolean作为是否展开的标志
# start
<<<<<<< HEAD


=======
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
def init(parent: QVBoxLayout, Name, self):
    globals()['SELF'] = self
    lb = QVBoxLayout()
    scroll = QScrollArea()
    scroll.setObjectName('scroll')
    scroll.setStyleSheet(
        '#scroll{border:0px !important;}')
    lb.setContentsMargins(10, 5, 5, 0)
    MainWidgetThis = QWidget()
<<<<<<< HEAD
=======
    MainWidgetThis.setObjectName('MainWidgetThis_Attr')
    MainWidgetThis.setStyleSheet(
        '''#MainWidgetThis_Attr{border:0px !important;border-bottom-left-radius: 7px;
    border-bottom-right-radius: 7px;}''')
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    MainWidgetThis.setLayout(lb)
    MainWidgetThis.setContentsMargins(0, 0, 0, 0)
    lb.setSpacing(5)
    UiInit(lb, self)
    scroll.setWidget(MainWidgetThis)
    scroll.setContentsMargins(0, 0, 0, 0)
    scroll.setWidgetResizable(True)
    scroll.widgetResizable()
    # scroll.set
    parent.addWidget(scroll)

<<<<<<< HEAD

def UiInit(layout: QVBoxLayout, self) -> None:
=======
def UiInit(layout: QVBoxLayout, self) -> None:
    SearchInput_Attribute_Widget = QWidget()
    SearchInput_Attribute_Widget.setMaximumHeight(20)
    # SearchInput_Attribute_Widget.setStyleSheet('background-color:red;')
    SearchInput_Attribute = QHBoxLayout()
    SearchInput_Attribute.setContentsMargins(0, 0, 0, 0)
    SearchInput_Attribute.setSpacing(0)
    SearchInput_Attribute_Widget.setLayout(SearchInput_Attribute)
    layout.addWidget(SearchInput_Attribute_Widget)
    searchComBox = QComboBox()
    searchComBox.setStyleSheet('''
border:1px solid #ccc;
outline:none;
border-radius:4px;
border-top-right-radius:0px;
border-bottom-right-radius:0px;
border-right:0px;
    ''')
    SearchInput_Attribute.addWidget(searchComBox)
    Search = QLineEdit()
    Search.setMinimumHeight(20)
    Search.setStyleSheet('''
border:1px solid #ccc;
border-radius:4px;
border-top-left-radius:0px;
border-bottom-left-radius:0px;
''')
    SearchInput_Attribute.addWidget(Search)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    # AttributeEitor = QWidget()
    projectInfo = {'name': self.Config['name'],
                   'version': '0.0.1',
                   'path': self.Config['path'],
                   'dataVersion': 10,
                   'readonly': False}
<<<<<<< HEAD
    ThisProject = AttributePanel('project', projectInfo, None, False)
    ConfigInfo = {'PythonVersion': str(sys.version)}
    ThisConfig = AttributePanel('config', ConfigInfo, None, False)
=======
    ThisProject = AttributePanel('project', projectInfo, None,False)
    ConfigInfo = {'PythonVersion': str(sys.version)}
    ThisConfig = AttributePanel('config', ConfigInfo,None, False)
>>>>>>> 037f18edb9621da7e1dc8afbb4567a646a056396
    layout.addWidget(ThisProject)
    layout.addWidget(ThisConfig)
    layout.addWidget(QWidget())
# 暂停这个模块的开发


def ConnectToAttr():
    pass
