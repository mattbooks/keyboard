import pcbnew
import math

file = "/home/matt/projects/keyboard/hardware/keyboard.kicad_pcb"
bak = file + ".bak"

X_OFFSET = 25000000
Y_OFFSET = 40000000
K_WIDTH  =  19050000
TILT_D   = 10
TILT     = math.radians(TILT_D)
D_OFFSET_X = 3000000.0
D_OFFSET_Y = 6000000.0

Z = math.sqrt(D_OFFSET_X * D_OFFSET_X + D_OFFSET_Y * D_OFFSET_Y)
D_ANGLE = math.atan(D_OFFSET_Y / D_OFFSET_X)

pcb = pcbnew.LoadBoard(file)
pcb.BuildListOfNets()

def moveS(module, point, angle):
    pcb.FindModuleByReference("S" + str(module)).SetOrientation(angle)
    pcb.FindModuleByReference("S" + str(module)).SetPosition(pcbnew.wxPoint(point.x + X_OFFSET, point.y + Y_OFFSET))

def moveD(module, point, angle, negate=False):
    pcb.FindModuleByReference("D" + str(module)).SetOrientation(1800 + angle)
    d = pcb.FindModuleByReference("D" + str(module))
    if d.GetLayerName() == 'F.Cu':
        d.Flip(d.GetPosition())
    d_pos = pcbnew.wxPoint(
        pos.x + X_OFFSET - Z * math.cos(D_ANGLE - math.radians(angle / 10)),
        pos.y + Y_OFFSET - Z * math.sin(D_ANGLE - math.radians(angle / 10))
    )
    d.SetPosition(d_pos)

def drawEdge(start, end):
    edge = pcbnew.DRAWSEGMENT()
    edge.SetLayer(pcb.GetLayerID('Edge.Cuts'))
    edge.SetStart(pcbnew.wxPoint(start.x + X_OFFSET, start.y + Y_OFFSET))
    edge.SetEnd(pcbnew.wxPoint(end.x + X_OFFSET, end.y + Y_OFFSET))

    pcb.Add(edge)


def addHole(p):
    io = pcbnew.PCB_IO()
    mod = io.FootprintLoad('/home/matt/projects/kicad-library/cache/Mounting_Holes.pretty', 'MountingHole_3.2mm_M3')
    mod.SetPosition(pcbnew.wxPoint(p.x + X_OFFSET, p.y + Y_OFFSET))
    mod.SetReference("")
    pcb.Add(mod)


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
    Column(-75000000,[61], 1800),
    Column(0,[62])
]

RIGHT_HAND = [
    Column(0,[56,57,58,59,60]),
    Column(2000000,[51,52,53,54,55]),
    Column(3000000,[46,47,48,49,50]),
    Column(3000000,[41,42,43,44,45]),
    Column(-3000000,[36,37,38,39,40]),
    Column(-3000000,[31,32,33,34,35]),
    Column(-75000000,[63]),
    Column(0,[64], 1800)
]

pos = pcbnew.wxPoint(0,0)
top_left = None
last_start_pos = pos

for c in LEFT_HAND:
    pos = pcbnew.wxPoint(last_start_pos.x + K_WIDTH * math.cos(TILT) + c.offset * math.sin(TILT),
                         last_start_pos.y + K_WIDTH * math.sin(TILT) - c.offset * math.cos(TILT))
    top_left = pos if not top_left else top_left
    last_start_pos = pos
    # for k in c.keys:
    #     moveS(k, pcbnew.wxPoint(pos.x, pos.y), c.rotation + -10 * TILT_D)
    #     moveD(k, pcbnew.wxPoint(pos.x, pos.y), c.rotation + -10 * TILT_D)
    #     pos = pcbnew.wxPoint(round(pos.x - math.sin(TILT) * K_WIDTH), round(pos.y + math.cos(TILT) * K_WIDTH))

pos = pcbnew.wxPoint(308000000,0)
top_right = None
last_start_pos = pos

for c in RIGHT_HAND:
    pos = pcbnew.wxPoint(last_start_pos.x - K_WIDTH * math.cos(TILT) - c.offset * math.sin(TILT),
                         last_start_pos.y + K_WIDTH * math.sin(TILT) - c.offset * math.cos(TILT))
    top_right = pos if not top_right else top_right
    last_start_pos = pos
    # for k in c.keys:
    #     moveS(k, pcbnew.wxPoint(pos.x, pos.y), c.rotation + 10 * TILT_D)
    #     moveD(k, pcbnew.wxPoint(pos.x, pos.y), c.rotation + 10 * TILT_D, True)
    #     pos = pcbnew.wxPoint(round(pos.x + math.sin(TILT) * K_WIDTH), round(pos.y + math.cos(TILT) * K_WIDTH))

ANG = math.radians(45 - TILT_D)
DIAG = 0.5 * math.sqrt(2 * (K_WIDTH * K_WIDTH))
EDGE_OFF_X = DIAG * math.sin(ANG)
EDGE_OFF_Y = DIAG * math.cos(ANG)

EXTRA_SPACE = 7500000
EDGE_HEIGHT = 5 * K_WIDTH + 2 * EXTRA_SPACE
HAND_WIDTH = 8 * K_WIDTH

top_left = pcbnew.wxPoint(
    top_left.x - EDGE_OFF_X + math.sin(TILT) * EXTRA_SPACE,
    top_left.y - EDGE_OFF_Y - math.cos(TILT) * EXTRA_SPACE
)
top_right = pcbnew.wxPoint(
    top_right.x + EDGE_OFF_X - math.sin(TILT) * EXTRA_SPACE,
    top_right.y - EDGE_OFF_Y - math.cos(TILT) * EXTRA_SPACE
)

bottom_left = pcbnew.wxPoint(
    top_left.x - math.sin(TILT) * EDGE_HEIGHT,
    top_left.y + math.cos(TILT) * EDGE_HEIGHT
)

middle_left = pcbnew.wxPoint(
    bottom_left.x + math.cos(TILT) * HAND_WIDTH,
    bottom_left.y + math.sin(TILT) * HAND_WIDTH
)

bottom_right = pcbnew.wxPoint(
    top_right.x + math.sin(TILT) * EDGE_HEIGHT,
    top_right.y + math.cos(TILT) * EDGE_HEIGHT
)

middle_right = pcbnew.wxPoint(
    bottom_right.x - math.cos(TILT) * HAND_WIDTH,
    bottom_right.y + math.sin(TILT) * HAND_WIDTH
)

# drawEdge(top_left, bottom_left)
# drawEdge(bottom_left,middle_left)
# drawEdge(middle_left, middle_right)
# drawEdge(middle_right, bottom_right)
# drawEdge(bottom_right, top_right)
# drawEdge(top_right, top_left)

HOLE_WIDTH = 4000000
HOLE_OFFSET_X = 1.3 * HOLE_WIDTH * math.sin(TILT + math.radians(45))
HOLE_OFFSET_Y = 1.3 * HOLE_WIDTH * math.cos(TILT + math.radians(45))

BOTTOM_HOLE_SPACE = 6 * K_WIDTH - 2 * HOLE_WIDTH

mounting_holes = [
    pcbnew.wxPoint(top_left.x + HOLE_WIDTH, top_left.y + HOLE_WIDTH),
    pcbnew.wxPoint(top_left.x + 90000000, top_left.y + HOLE_WIDTH),
    pcbnew.wxPoint(top_right.x - 90000000, top_right.y + HOLE_WIDTH),
    pcbnew.wxPoint(top_right.x - HOLE_WIDTH, top_right.y + HOLE_WIDTH),
    pcbnew.wxPoint(bottom_left.x + HOLE_OFFSET_X, bottom_left.y - HOLE_OFFSET_Y),
    pcbnew.wxPoint(bottom_right.x - HOLE_OFFSET_X, bottom_left.y - HOLE_OFFSET_Y),
    pcbnew.wxPoint((middle_left.x + middle_right.x) / 2, middle_left.y - HOLE_WIDTH),
    pcbnew.wxPoint(bottom_left.x + HOLE_OFFSET_X + BOTTOM_HOLE_SPACE * math.cos(TILT),
                   bottom_left.y - HOLE_OFFSET_Y + BOTTOM_HOLE_SPACE * math.sin(TILT)),
    pcbnew.wxPoint(bottom_right.x - HOLE_OFFSET_X - BOTTOM_HOLE_SPACE * math.cos(TILT),
                   bottom_right.y - HOLE_OFFSET_Y + BOTTOM_HOLE_SPACE * math.sin(TILT)),
]

for hole in mounting_holes:
    addHole(hole)

pcb.Save(file)


