from lib.base import *
def Cube(x,y,z,texture:list,face=None):
    glBegin(GL_QUADS)
    #开始绘制时是一个绘制一个或多个四边形，就是独立的那种
    glColor3f(1.0,1.0,1.0)
    #绘制顶面,在y=1的地方，分别在xz+- 1处
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0) 

    glColor3f(1.0,1.0,1.0)
    #绘制底面,在y=-1的地方，分别在xz+- 1处
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 1.0,-1.0,-1.0)

    glColor3f(1.0,1.0,1.0)
    #绘制一个侧面1，在z正方向1处
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    #
    glColor3f(1.0,1.0,1.0)
    #z负方向的1处侧面
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0,-1.0)

    glColor3f(1.0,1.0,1.0)
    #x负的侧面
    glVertex3f(-1.0, 1.0, 1.0) 
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0) 
    glVertex3f(-1.0,-1.0, 1.0)

    glColor3f(1.0,1.0,1.0)
    #x正的侧面
    glVertex3f( 1.0, 1.0,-1.0) 
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    #完成
    glEnd()
Materials=[
        {
            'ambient_light':[0.329412,0.223529,0.02745,1.000000],
            'diffuse':[0.780392,0.568627,0.113725,1.000000],
            'specular':[0.992157, 0.941176,0.807843,1.000000],
            'shininess':27.897400
        },#黄铜
        {
            'ambient_light':[0.212500,0.127500,0.054000,1.000000],
            'diffuse':[0.714000,0.428400,0.181440,1.000000],
            'specular':[0.393548,0.271906,0.166721,1.000000],
            'shininess':25.600000
        },#青铜
        {
            'ambient_light':[0.250000,0.148000,0.064750,1.000000],
            'diffuse':[0.400000,0.236800,0.103600,1.000000],
            'specular':[0.774597,0.458561,0.200621,1.000000],
            'shininess':76.800003
        },#亮青铜
        {
            'ambient_light':[0.250000,0.250000,0.250000,1.000000],
            'diffuse':[0.400000,0.400000, 0.400000,1.000000],
            'specular':[0.774597,0.774597,0.774597,1.000000],
            'shininess':76.800003
        },#铬
        {
            'ambient_light':[0.191250, 0.073500, 0.022500, 1.000000],
            'diffuse':[0.703800, 0.270480, 0.082800, 1.000000],
            'specular':[0.256777, 0.137622, 0.086014, 1.000000],
            'shininess':12.800000
        },#铜
        {
            'ambient_light':[0.229500, 0.088250, 0.027500, 1.000000],
            'diffuse':[0.550800, 0.211800, 0.066000, 1.000000],
            'specular':[0.580594, 0.223257, 0.069570, 1.000000],
            'shininess':51.200001
        },#亮铜
       {
            'ambient_light':[0.247250, 0.199500, 0.074500, 1.000000],
            'diffuse':[0.751640, 0.606480, 0.226480, 1.000000],
            'specular':[0.628281, 0.555802, 0.366065, 1.000000],
            'shininess':51.200001
        },#金
        {
            'ambient_light':[0.247250, 0.224500, 0.064500, 1.000000],
            'diffuse':[0.346150, 0.314300, 0.090300, 1.000000],
            'specular':[0.797357, 0.723991, 0.208006, 1.000000],
            'shininess':83.199997
        },#亮金
        {
            'ambient_light':[0.105882, 0.058824, 0.113725, 1.000000],
            'diffuse':[0.427451, 0.470588, 0.541176, 1.000000],
            'specular':[0.333333, 0.333333, 0.521569, 1.000000],
            'shininess':9.846150
        },#白蜡
        {
            'ambient_light':[0.192250, 0.192250, 0.192250, 1.000000],
            'diffuse':[0.507540, 0.507540, 0.507540, 1.000000],
            'specular':[0.508273, 0.508273, 0.508273, 1.000000],
            'shininess':51.200001
        },#银
        {
            'ambient_light':[0.231250, 0.231250, 0.231250, 1.000000],
            'diffuse':[0.277500, 0.277500, 0.277500, 1.000000],
            'specular':[0.773911, 0.773911, 0.773911, 1.000000],
            'shininess':89.599998
        },#亮银
        {
            'ambient_light':[0.021500, 0.174500,0.021500,0.550000],
            'diffuse':[0.075680,0.614240,0.075680,0.550000],
            'specular':[ 0.633000,0.727811,0.633000,0.550000],
            'shininess':76.800003
        },#翠绿
        {
            'ambient_light':[0.135000, 0.222500, 0.157500, 0.950000],
            'diffuse':[0.540000, 0.890000, 0.630000, 0.950000],
            'specular':[0.316228, 0.316228, 0.316228, 0.950000],
            'shininess':12.800000
        },#墨绿
        {
            'ambient_light':[0.053750,0.050000,0.066250,0.820000],
            'diffuse':[0.182750,0.17000,0.225250,0.820000],
            'specular':[ 0.332741, 0.328634,0.346435,0.820000],
            'shininess':38.400002
        },#黑曜石
        {
            'ambient_light':[0.250000, 0.207250, 0.207250, 0.922000],
            'diffuse':[1.000000, 0.829000, 0.829000, 0.922000],
            'specular':[ 0.296648, 0.296648, 0.296648, 0.922000],
            'shininess':11.264000
        },#珍珠
        {
            'ambient_light':[0.174500, 0.011750, 0.011750, 0.550000],
            'diffuse':[0.614240, 0.041360, 0.041360, 0.550000],
            'specular':[0.727811, 0.626959, 0.626959, 0.550000],
            'shininess':76.800003
        },#红宝石
        {
            'ambient_light':[0.100000, 0.187250, 0.174500, 0.800000],
            'diffuse':[0.396000, 0.741510, 0.691020, 0.800000],
            'specular':[0.297254, 0.308290, 0.306678, 0.800000],
            'shininess':12.800000
        },#绿宝石
        {
            'ambient_light':[0.000000, 0.000000, 0.000000, 1.000000],
            'diffuse':[0.010000, 0.010000, 0.010000, 1.000000],
            'specular':[0.500000, 0.500000, 0.500000, 1.000000],
            'shininess':32.000000
        },#黑塑料
        {
            'ambient_light':[0.020000, 0.020000, 0.020000, 1.000000],
            'diffuse':[0.010000, 0.010000, 0.010000, 1.000000],
            'specular':[0.400000, 0.400000, 0.400000, 1.000000],
            'shininess':10.000000
        },#黑橡胶
        {
            'ambient_light':[0.110000, 0.060000, 0.090000, 1.000000],
            'diffuse':[0.430000, 0.470000, 0.540000, 1.000000],
            'specular':[0.330000, 0.330000, 0.520000, 1.000000],
            'shininess':22.000000
        }#紫罗兰
]
class World(QOpenGLWidget):
    def __init__(self, *args, **kwargs):
        super(World, self).__init__(*args, **kwargs)
        self.setGeometry(QtCore.QRect(10, 10,700, 700))#窗口位置和大小
        self.isMove=False
        self.isRotate=False
        self.model=[]#该列表需要存储一个一个的字典，字典形式为{'material':Materials,'data':numpy.array()}，每一个model[x]代表一个模型，包含材质和点的数据
    def initdata(self,data):
        self.model=data
    def initializeGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(1,1,1,0)
        self.camera=camera()
        self.light=Light(Materials[0])
    def paintGL(self):
        self.camera.Update()
        for i in range(len(self.model)):
            #print("Load")
            glPushMatrix()
            self.light.Update(self.model[i]['material'])
            self.VBO(self.model[i]['data'])
            glPopMatrix()
    def VBO(self,data):
        #glPushMatrix()
        vb=vbo.VBO(data)
        vb.bind()
        glEnableClientState(GL_NORMAL_ARRAY)
        glEnableClientState(GL_VERTEX_ARRAY)
        glNormalPointer(GL_FLOAT, 24, vb+12)
        glVertexPointer(3, GL_FLOAT, 24, vb )#在每一个周期里，都有6个32-bit浮点数据，总共4*6=24     3代表数量
        glDrawArrays(GL_TRIANGLES, 0, len(data))
        vb.unbind()
        glDisableClientState(GL_NORMAL_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)
        #glPopMatrix()
    def mousePressEvent(self,event):
        self.myMousePosition=event.pos()
        if event.button()==QtCore.Qt.LeftButton:
            self.isMove=True
        if event.button()==QtCore.Qt.RightButton:
            self.isRotate=True
        #self.update()
    def wheelEvent(self,event):
        if event.angleDelta().y()>0:
            self.camera.right*=0.95
            self.camera.top*=0.95
        if event.angleDelta().y()<0:
            self.camera.right/=0.95
            self.camera.top/=0.95
        self.update()
    def mouseReleaseEvent(self,event):
        if event.button()==QtCore.Qt.LeftButton:
            self.isMove=False
        if event.button()==QtCore.Qt.RightButton:
            self.isRotate=False
    def mouseMoveEvent(self,event):
        if self.isMove:
            moveX=event.pos().x()-self.myMousePosition.x()
            moveY=event.pos().y()-self.myMousePosition.y()
            self.camera.Move(moveX*self.camera.right/200,moveY*self.camera.right/200)
            self.myMousePosition=event.pos()
        if self.isRotate:
            moveX=event.pos().x()-self.myMousePosition.x()
            moveY=event.pos().y()-self.myMousePosition.y()
            self.camera.Yaw(-moveX)
            self.camera.Pitch(-moveY)
            self.light.lightpos=[-self.camera.forwardDir.X,-self.camera.forwardDir.Y,-self.camera.forwardDir.Z,0]
            self.myMousePosition=event.pos()
        self.update()
class camera:
    def __init__(self):
        self.mPos=Vector3f(0.0,0.0,0.0)
        self.mViewCenter=Vector3f(0.0,0.0,-1.0)
        self.mUp=Vector3f(0.0,1.0,0.0)
        self.right=100
        self.top=100
        self.forwardDir=self.mViewCenter-self.mPos
        self.rithtDir=self.forwardDir.cross(self.mUp)
    def Update(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.right,self.right,-self.top,self.top,-200,200)
        gluLookAt(self.mPos.X,self.mPos.Y,self.mPos.Z,self.mViewCenter.X,self.mViewCenter.Y,self.mViewCenter.Z,self.mUp.X,self.mUp.Y,self.mUp.Z)
    def Move(self,deltax,deltay):
        self.forwardDir.Normalize()
        self.rithtDir.Normalize()
        self.mUp.Normalize()
        dx=self.rithtDir*deltax
        dy=self.mUp*deltay
        self.mPos=self.mPos-dx+dy
        self.mViewCenter=self.mPos+self.forwardDir
    def Rotate(self,viewDirection,angle,x,y,z):
        #x，y，z组成旋转轴
        C=math.cos(angle*math.pi/180)
        S=math.sin(angle*math.pi/180)
        newX=viewDirection.X * (x * x + (1 - x * x) * C) + viewDirection.Y * (x * y * (1 - C) - z * S) + viewDirection.Z * (x * z * (1 - C) + y * S)
        newY=viewDirection.X * (x * y * (1 - C) + z * S) + viewDirection.Y * (y * y + (1 - y * y) * C) + viewDirection.Z * (y * z * (1 - C) - x * S)
        newZ=viewDirection.X * (x * z * (1 - C) - y * S) + viewDirection.Y * (y * z * (1 - C) + x * S) + viewDirection.Z * (z * z + (1 - z * z) * C)
        newdir=Vector3f(newX,newY,newZ)
        #newdir.Normalize()
        return newdir
    def Yaw(self,angle):
        self.forwardDir=self.Rotate(self.forwardDir,angle,self.mUp.X,self.mUp.Y,self.mUp.Z)
        self.rithtDir=self.Rotate(self.rithtDir,angle,self.mUp.X,self.mUp.Y,self.mUp.Z)
        self.mPos = self.mViewCenter-self.forwardDir
    def Pitch(self,angle):
        self.forwardDir=self.Rotate(self.forwardDir,angle,self.rithtDir.X,self.rithtDir.Y,self.rithtDir.Z)
        self.mUp=self.Rotate(self.mUp,angle,self.rithtDir.X,self.rithtDir.Y,self.rithtDir.Z)
        self.mPos = self.mViewCenter-self.forwardDir
class Vector3f:
    def __init__(self,x,y,z):
        self.X=x
        self.Y=y
        self.Z=z
    def __add__(self,other):
        return Vector3f(self.X+other.X,self.Y+other.Y,self.Z+other.Z)
    def __sub__(self,other):
        return Vector3f(self.X-other.X,self.Y-other.Y,self.Z-other.Z)
    def __mul__(self,other):
        return Vector3f(self.X*other,self.Y*other,self.Z*other)
    def dot(self,other):
        return self.X*other.X+self.Y*other.Y+self.Z*other.Z
    def cross(self,other):
        return Vector3f(self.Y*other.Z-self.Z*other.Y,self.Z*other.X-self.X*other.Z,self.X*other.Y-self.Y*other.X)
    def magnitude(self):
        return math.sqrt(self.X*self.X+self.Y*self.Y+self.Z*self.Z)
    def Normalize(self):
        len=self.magnitude()
        self.X=self.X/len
        self.Y=self.Y/len
        self.Z=self.Z/len
class Light:
    def __init__(self,m):
        glShadeModel(GL_SMOOTH)
        self.lightpos=[0,0,1,0]
        whiltlitht=[1,1,1,1]
        glMaterial(GL_FRONT,GL_AMBIENT,m['ambient_light'])
        glMaterial(GL_FRONT,GL_SPECULAR, m['specular'])
        glMaterial(GL_FRONT,GL_SHININESS, m['shininess'])
        glMaterial(GL_FRONT,GL_DIFFUSE, m['diffuse'])
        
        #glLight(GL_LIGHT0,GL_POSITION, self.lightpos)
        #glLight(GL_LIGHT0,GL_DIFFUSE, whiltlitht)
       # glLight(GL_LIGHT0,GL_SPECULAR, whiltlitht)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)   
        glEnable(GL_DEPTH_TEST)
    def Update(self,m):
        glLight(GL_LIGHT0,GL_POSITION, self.lightpos)
        glMaterial(GL_FRONT,GL_AMBIENT,m['ambient_light'])
        glMaterial(GL_FRONT,GL_SPECULAR, m['specular'])
        glMaterial(GL_FRONT,GL_SHININESS, m['shininess'])
        glMaterial(GL_FRONT,GL_DIFFUSE, m['diffuse'])
