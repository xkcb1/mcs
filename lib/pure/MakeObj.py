import nbtlib, os, sys, numpy
from time import process_time

def Xprint(*argv):
    pass
ThisName = ''
log = print
is_open_now = False
if len(sys.argv) > 2:
    if sys.argv[2] == '-!output':
        def print(*arg, SELF=None, widgetList=None):
            log(*arg, file=open("./log_file/log_pureObj.txt", "a"))
    if sys.argv[2] == '-name':
        ThisName = sys.argv[3]
    if sys.argv[2] == '-open':
        is_open_now = True
process_time()

def MakeStlFileByNbt(NbtFIlePath: str,name='',is_open_now=False):
    NbtFIleName = NbtFIlePath.split('/')[-1].split('.')[0]
    if name == '':
        ObjFilePath = f'./obj/{NbtFIleName}.obj'
    else:
        ObjFilePath = f'./obj/{name}.obj'
    Nbt_File = nbtlib.load(NbtFIlePath)
    Nbt_Block = Nbt_File['blocks']
    Nbt_getAirState = -1
    for state in Nbt_File['palette']:
        if state['Name'] == 'minecraft:air':
            Nbt_getAirState = Nbt_File['palette'].index(state)
    getBlocksList = []
    countAir = 0
    Numpy_BlockList = [(block['pos'][0], block['pos'][1], block['pos'][2]) for block in Nbt_Block if
                       block['state'] != Nbt_getAirState]
    Obj_ThisFile = f'''#From (Pure NbtRender Core) v0.01
#Use obj file
#NBT file : {NbtFIlePath}
#NBT file size : {str(int(os.path.getsize(NbtFIlePath)) / 1024)} kb
#Structure size :{str(int(Nbt_File['size'][0]))},{str(int(Nbt_File['size'][1]))},{str(int(Nbt_File['size'][2]))}
#Blocks count : {str(len(Numpy_BlockList))}
#Air count : {str(len(Nbt_Block) - len(Numpy_BlockList))}
o {NbtFIleName.split('.')[0]}
'''
    # 内部剔除
    print('Block internal culling')
    old_block_len = len(Numpy_BlockList)
    print('old', old_block_len)
    BLOCK_DEL_list = []
    BLOCK_All = Numpy_BlockList.copy()  # 备份一个方块列表
    for block in Numpy_BlockList:
        x = int(block[0])
        y = int(block[1])
        z = int(block[2])
        if (x, y + 1, z) in Numpy_BlockList and (x, y - 1, z) in Numpy_BlockList and (
        x + 1, y, z) in Numpy_BlockList and (x - 1, y, z) in Numpy_BlockList and (x, y, z + 1) in Numpy_BlockList and (
        x, y, z - 1) in Numpy_BlockList:
            BLOCK_DEL_list.append(block)
            # 如果一个方块的所有面上都有方块，则删去这个方块
    for block in BLOCK_DEL_list:
        Numpy_BlockList.remove(block)
    Numpy_BlockList = numpy.array(Numpy_BlockList)
    new_block_len = len(Numpy_BlockList)
    print('new', new_block_len)
    print(f' <1> -Optimization rate [{str(new_block_len / old_block_len * 100)}%]')
    # Numpy_BlockList -> numpy.array( [(x,y,z) ,(x1,y1,z1) . . .] )

    Obj_Point_Pos = []
    for block in Numpy_BlockList:
        # 通过方块推导出点的坐标,可见方块的点
        x = int(block[0])
        y = int(block[1])
        z = int(block[2])
        Obj_Point_Pos.append((x, y, z))  # G
        Obj_Point_Pos.append((x + 1, y, z))  # H
        Obj_Point_Pos.append((x, y, z + 1))  # E
        Obj_Point_Pos.append((x + 1, y, z + 1))  # F
        Obj_Point_Pos.append((x, y + 1, z))  # C
        Obj_Point_Pos.append((x + 1, y + 1, z))  # D
        Obj_Point_Pos.append((x, y + 1, z + 1))  # A
        Obj_Point_Pos.append((x + 1, y + 1, z + 1))  # B
        '''<===3d.cube===>
         (y)
          ↑
          ┃ A───────B
          ┃╱│      ╱│
          C─┼─────D │
          ┃ E─────┼─F
          ┃╱      │╱
          G━━━━━━━H━━━━━━→ (x)
        (原点),face:->z
          .append(G,H,E,F,C,D,A,B)
        '''
        pass
    # 再次对点进行内部剔除
    print('DELe duplicate points')
    old_point_len = len(Obj_Point_Pos)
    print('old', old_point_len)
    Obj_Point_Pos = list(set(Obj_Point_Pos))
    new_point_len = len(Obj_Point_Pos)
    print('new', new_point_len)
    print(f' <2> -Optimization rate [{str(new_point_len / old_point_len * 100)}%]')
    # 点的外层剔除
    print('Internal elimination of points')
    old_point_cen_len = len(Obj_Point_Pos)
    print('old', old_point_cen_len)
    POINT_DEL_List = []
    for point in Obj_Point_Pos:
        x = int(point[0])
        y = int(point[1])
        z = int(point[2])
        if (x, y, z) in BLOCK_All and (x - 1, y, z) in BLOCK_All and (x - 1, y, z - 1) in BLOCK_All and (x, y,
                                                                                                         z - 1) in BLOCK_All and (
        x, y - 1, z) in BLOCK_All and (x - 1, y - 1, z) in BLOCK_All and (x - 1, y - 1,
                                                                          z - 1) in BLOCK_All and (
        x, y - 1, z - 1) in BLOCK_All:
            POINT_DEL_List.append(point)
            # 如果一个点的2x2x2内都是方块，则这个点可以被剔除
    for point in POINT_DEL_List:
        Obj_Point_Pos.remove(point)
    new_point_cen_len = len(Obj_Point_Pos)
    print('new', new_point_cen_len)
    print(f' <3> -Optimization rate [{str(new_point_cen_len / old_point_cen_len * 100)}%]')
    # total
    old_total = len(Nbt_Block) * 8
    new_total = len(Obj_Point_Pos)
    print('old total points : ', old_total)
    print('new total points : ', new_total)
    print(f' <Total> -Optimization rate [{str(new_total / old_total * 100)}%]')
    # make obj file here
    # 创建4种类型
    OBJ_V = ''
    OBJ_VT = ''
    OBJ_VN = ''
    OBJ_F = ''
    V_countLine = 0
    for block in Numpy_BlockList:
        x = int(block[0])
        y = int(block[1])
        z = int(block[2])
        # 推导出各个面
        Point_List = [
            (x, y, z),
            (x + 1, y, z),
            (x, y, z + 1),
            (x + 1, y, z + 1),
            (x, y + 1, z),
            (x + 1, y + 1, z),
            (x, y + 1, z + 1),
            (x + 1, y + 1, z + 1),
        ]  # 8个点的坐标
        can_see_points = []
        addLines = 0
        for point in Point_List:
            if point in Obj_Point_Pos:
                # 如果这个方块的某一个点在可视点列表里
                can_see_points.append(point)
                # 生成点
                OBJ_V += f'v {str(point[0])} {str(point[1])} {str(point[2])}\n'
                addLines += 1
        # 生成面
        can_see_face = []
        # 直接判断上下左右前后面的情况
        if (x, y, z) in can_see_points and (x, y + 1, z) in can_see_points and (x + 1, y + 1, z) in can_see_points and (
        x + 1, y, z) in can_see_points:
            # 后面
            can_see_face.append(
                (can_see_points.index((x, y, z)) + 1 + V_countLine,
                 can_see_points.index((x, y + 1, z)) + 1 + V_countLine,
                 can_see_points.index((x + 1, y + 1, z)) + 1 + V_countLine,
                 can_see_points.index((x + 1, y, z)) + 1 + V_countLine,
                 )
            )
        if (x, y, z + 1) in can_see_points and (x, y + 1, z + 1) in can_see_points and (
                x + 1, y + 1, z + 1) in can_see_points and (x + 1, y, z + 1) in can_see_points:
            # 前面
            can_see_face.append(
                (can_see_points.index((x, y, z + 1)) + 1 + V_countLine,
                 can_see_points.index((x, y + 1, z + 1)) + 1 + V_countLine,
                 can_see_points.index((x + 1, y + 1, z + 1)) + 1 + V_countLine,
                 can_see_points.index((x + 1, y, z + 1)) + 1 + V_countLine,
                 )
            )
        if (x, y + 1, z) in can_see_points and (x, y + 1, z + 1) in can_see_points and (
                x + 1, y + 1, z + 1) in can_see_points and (x + 1, y + 1, z) in can_see_points:
            # 上面
            can_see_face.append(
                (can_see_points.index((x, y + 1, z)) + 1 + V_countLine,
                 can_see_points.index((x, y + 1, z + 1)) + 1 + V_countLine,
                 can_see_points.index((x + 1, y + 1, z + 1)) + 1 + V_countLine,
                 can_see_points.index((x + 1, y + 1, z)) + 1 + V_countLine,
                 )
            )
        if (x, y, z) in can_see_points and (x, y, z + 1) in can_see_points and (
                x + 1, y, z + 1) in can_see_points and (x + 1, y, z) in can_see_points:
            # 下面
            can_see_face.append(
                (can_see_points.index((x, y, z)) + 1 + V_countLine,
                 can_see_points.index((x, y, z + 1)) + 1 + V_countLine,
                 can_see_points.index((x + 1, y, z + 1)) + 1 + V_countLine,
                 can_see_points.index((x + 1, y, z)) + 1 + V_countLine,
                 )
            )
        if (x, y, z) in can_see_points and (x, y, z + 1) in can_see_points and (
                x, y + 1, z + 1) in can_see_points and (x, y + 1, z) in can_see_points:
            # 左面
            can_see_face.append(
                (can_see_points.index((x, y, z)) + 1 + V_countLine,
                 can_see_points.index((x, y, z + 1)) + 1 + V_countLine,
                 can_see_points.index((x, y + 1, z + 1)) + 1 + V_countLine,
                 can_see_points.index((x, y + 1, z)) + 1 + V_countLine,
                 )
            )
        if (x + 1, y, z) in can_see_points and (x + 1, y, z + 1) in can_see_points and (
                x + 1, y + 1, z + 1) in can_see_points and (x + 1, y + 1, z) in can_see_points:
            # 右面
            can_see_face.append(
                (can_see_points.index((x + 1, y, z)) + 1 + V_countLine,
                 can_see_points.index((x + 1, y, z + 1)) + 1 + V_countLine,
                 can_see_points.index((x + 1, y + 1, z + 1)) + 1 + V_countLine,
                 can_see_points.index((x + 1, y + 1, z)) + 1 + V_countLine,
                 )
            )
        # log(can_see_face)
        for face in can_see_face:
            OBJ_F += f'f {face[0]} {face[1]} {face[2]} {face[3]}\n'
        V_countLine += addLines  # 确定上一次的count数，为面的index作开头行
    # log(len(OBJ_F.split('\n'))-1)
    Obj_ThisFile = Obj_ThisFile + OBJ_V + OBJ_F
    if os.path.exists('./obj') == False:
        os.mkdir('./obj')
    with open(ObjFilePath, 'w', encoding='utf-8') as OBJ:
        OBJ.write(Obj_ThisFile)
    log('create Obj file in : ' + ObjFilePath)
    if is_open_now == True:
        os.system('start '+ObjFilePath)
    return ObjFilePath

helpStr = '''
<argv [1]>
-help       output the help
-version    check the version
$file       make the .obj file file from .nbt file
<argv [2]>
-!output    output <OFF>
-name       set output Obj file's Name
-open       open obj file now
<argv [3]>
$filename   use -name and set output file name
'''
if len(sys.argv) > 1:
    if sys.argv[1] == '-help':
        log(helpStr)
    elif sys.argv[1] == '-version':
        log('[Pure NBT to OBJ] v0.0.1')
    else:
        MakeStlFileByNbt(sys.argv[1],ThisName,is_open_now)
    # ./test/nbt/base_plate5
    log(f'use time:{process_time()}s')
else:
    log('no file input')