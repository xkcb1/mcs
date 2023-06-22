from lib.base import *
# 从今以后，所有的parent都是一个布局了，可以直接addwidget
# 我们想的是，创建一个class，他实现一个属性框的UI部分，提供一组dictionary或者json类型
# 作为构造参数，提供一个string作为名字，以及一个Boolean作为是否展开的标志
# start


def init(parent: QVBoxLayout, Name, self):
    globals()['SELF'] = self
    lb = QVBoxLayout()
    scroll = QScrollArea()
    scroll.setObjectName('scroll')
    scroll.setStyleSheet(
        '#scroll{border:0px !important;}')
    lb.setContentsMargins(10, 5, 5, 0)
    MainWidgetThis = QWidget()
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


def UiInit(layout: QVBoxLayout, self) -> None:
    # AttributeEitor = QWidget()
    projectInfo = {'name': self.Config['name'],
                   'version': '0.0.1',
                   'path': self.Config['path'],
                   'dataVersion': 10,
                   'readonly': False}
    ThisProject = AttributePanel('project', projectInfo, None, False)
    ConfigInfo = {'PythonVersion': str(sys.version)}
    ThisConfig = AttributePanel('config', ConfigInfo, None, False)
    layout.addWidget(ThisProject)
    layout.addWidget(ThisConfig)
    layout.addWidget(QWidget())
# 暂停这个模块的开发


def ConnectToAttr():
    pass
