from PureBaseLib import *
getfile = ''
if len(sys.argv) > 1:
    getfile = sys.argv[1]
    print(getfile)
else:
    getfile = 'untitled'


class Vovel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            texture='white_cube',
            color=color.white,
            highlight_color=color.lime,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                vovel = Vovel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)


app = Ursina(editor_ui_enabled=True,
             borderless=False, development_mode=True)
face_list = MakeStlFileByNbt(getfile)

for block in face_list:
    # vovel = Vovel(position=(block[0], block[1], block[2]))
    for face in block:
        verts = (Vec3(face[0][0], face[0][1], face[0][2]), Vec3(face[1][0], face[1][1], face[1][2]),
                 Vec3(face[2][0], face[2][1], face[2][2]), Vec3(face[3][0], face[3][1], face[3][2]))
        uvs = ((1.0, 0.0), (0.0, 1.0), (0.0, 0.0), (1.0, 1.0))
        norms = ((0, 0, -1),) * len(verts)
        tris = (1, 2, 0, 2, 3, 0)
        colors = (color.white, color.white, color.white, color.white)
        Entity(model=Mesh(vertices=verts, triangles=tris,
                          uvs=uvs, normals=norms, colors=colors))

cam = FirstPersonController()

player = Entity(model='cube',
                origin=(0, 0, -2),
                parent=cam)
app.run()
