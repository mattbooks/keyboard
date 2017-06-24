import pcbnew
import math

file = "/home/matt/projects/keyboard/hardware/keyboard.kicad_pcb"
bak = file + ".bak"

X_OFFSET = 70000000
Y_OFFSET = 106000000
K_WIDTH  =  19000000
TILT_D   = 10
TILT     = math.radians(TILT_D)

pcb = pcbnew.LoadBoard(file)
pcb.BuildListOfNets()

def move(module, point):
    pcb.FindModuleByReference(module).SetPosition(pcbnew.wxPoint(point.x + X_OFFSET, point.y + Y_OFFSET))

def rotate(module, angle):
    pcb.FindModuleByReference(module).SetOrientation(angle)

pcb.Save(bak)

class Column:
    def __init__(self, offset, keys):
        self.offset = offset
        self.keys = keys

    def offset(self):
        return self.offset

    def keys(self):
        return self.keys

LEFT_HAND = [
    Column(0,["S1", "S2", "S3", "S4", "S5"]),
    Column(2000000,["S6", "S7", "S8", "S9", "S10"]),
    Column(3000000,["S11", "S12", "S13", "S14", "S15"]),
    Column(3000000,["S16", "S17", "S18", "S19", "S20"]),
    Column(-3000000,["S21", "S22", "S23", "S24", "S25"]),
    Column(-3000000,["S26", "S27", "S28", "S29", "S30"]),
    Column(-75000000,["S31"]),
    Column(0,["S32"])
]

pos = pcbnew.wxPoint(0,0)
last_start_pos = pos

for c in LEFT_HAND:
    pos = pcbnew.wxPoint(last_start_pos.x + K_WIDTH * math.cos(TILT) + c.offset * math.sin(TILT),
                         last_start_pos.y + K_WIDTH * math.sin(TILT) - c.offset * math.cos(TILT))
    last_start_pos = pos
    for k in c.keys:
        move(k, pcbnew.wxPoint(pos.x, pos.y))
        rotate(k, -10 * TILT_D)
        pos = pcbnew.wxPoint(round(pos.x - math.sin(TILT) * K_WIDTH), round(pos.y + math.cos(TILT) * K_WIDTH))

pcb.Save(file)


