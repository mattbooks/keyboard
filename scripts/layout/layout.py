import pcbnew
import math

file = "/home/matt/projects/keyboard/hardware/keyboard.kicad_pcb"
bak = file + ".bak"

X_OFFSET = 70000000
Y_OFFSET = 106000000
K_WIDTH  =  19000000
TILT_D   = 10
TILT     = math.radians(TILT_D)
D_OFFSET_X = 2000000
D_OFFSET_Y = 6000000

pcb = pcbnew.LoadBoard(file)
pcb.BuildListOfNets()

def move(module, point):
    d = pcb.FindModuleByReference("D" + str(module))
    d.Flip(d.GetPosition())
    d.SetPosition(pcbnew.wxPoint(point.x + X_OFFSET - D_OFFSET_X, point.y + Y_OFFSET - D_OFFSET_Y))
    pcb.FindModuleByReference("S" + str(module)).SetPosition(pcbnew.wxPoint(point.x + X_OFFSET, point.y + Y_OFFSET))

def rotate(module, angle):
    pcb.FindModuleByReference("D" + str(module)).SetOrientation(1800 + angle)
    pcb.FindModuleByReference("S" + str(module)).SetOrientation(angle)

pcb.Save(bak)

class Column:
    def __init__(self, offset, keys, rotation=0):
        self.offset = offset
        self.keys = keys
        self.rotation = rotation

    def offset(self):
        return self.offset

    def keys(self):
        return self.keys

    def rotation(self):
        return self.rotation

LEFT_HAND = [
    Column(0,[1,2,3,4,5]),
    Column(2000000,[6,7,8,9,10]),
    Column(3000000,[11, 12, 13, 14, 15]),
    Column(3000000,[16, 17, 18, 19, 20]),
    Column(-3000000,[21, 22, 23, 24, 25]),
    Column(-3000000,[26, 27, 28, 29, 30]),
    Column(-75000000,[61], 900),
    Column(0,[62], 900)
]

pos = pcbnew.wxPoint(0,0)
last_start_pos = pos

for c in LEFT_HAND:
    pos = pcbnew.wxPoint(last_start_pos.x + K_WIDTH * math.cos(TILT) + c.offset * math.sin(TILT),
                         last_start_pos.y + K_WIDTH * math.sin(TILT) - c.offset * math.cos(TILT))
    last_start_pos = pos
    for k in c.keys:
        move(k, pcbnew.wxPoint(pos.x, pos.y))
        rotate(k, c.rotation + -10 * TILT_D)
        pos = pcbnew.wxPoint(round(pos.x - math.sin(TILT) * K_WIDTH), round(pos.y + math.cos(TILT) * K_WIDTH))

pcb.Save(file)


