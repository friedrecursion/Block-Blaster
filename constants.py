# board constants
N = 8       
CELL_SIZE = 100
BACKGROUND_COLOR = (60,74,128) # Dark Blue
EMPTY_TILE_COLOR = (32,36,69)
# Derived constants
LINE_THICKNESS = CELL_SIZE//20
LINE_COLOR = (25,32,59)
WIDTH, HEIGHT = N * CELL_SIZE, N * CELL_SIZE

HOVER_ALPHA = 100 # Brightness of Block hover

OUT_OF_BOUND = -1 # Out of Grid value

# Possible colors to display
EMPTY = 0
PURPLE = 1
BLUE = 2
LIGHT_BLUE = 3
GREEN = 4
YELLOW = 5
ORANGE = 6
RED = 7

# Possible Block colors
COLORS = [BLUE,RED,GREEN,PURPLE,ORANGE]

# Color MACRO to RGB conversion
RGB_COLORS = {
    EMPTY : EMPTY_TILE_COLOR,
    PURPLE : (141,92,211),
    BLUE : (75,99,230),
    LIGHT_BLUE : (63,178,226),
    GREEN : (80,194,91),
    YELLOW : (235,185,58),
    ORANGE : (238,125,40),
    RED : (217,62,60),
}

# SHAPES
# SHAPE_Rn : rotate SHAPE 90 degrees clockwise n times

# Squares
SQ1 = [(0,0)] # 1x1
SQ2 = [(0,0),(1,0)] +[(0,-1),(1,-1)] # 2x2
SQ3 = [(i,0) for i in range(-1,2)] + [(i,-1) for i in range(-1,2)] + [(i,-2) for i in range(-1,2)]# 3x3

# Lines
LINE2 = [(0,0),(0,-1)]
LINE3 = [(0,i) for i in range(0,-3,-1)]
LINE4 = [(0,i) for i in range(0,-4,-1)]
LINE5 = [(0,i) for i in range(0,-5,-1)]
LINE2_R1 = [(0,0),(1,0)]
LINE3_R1 = [(i,0) for i in range(-1,2)]
LINE4_R1 = [(i,0) for i in range(-1,3)]
LINE5_R1 = [(i,0) for i in range(-2,3)]

# 3x2 Rectangle
RECT23 = LINE3 + [(1,i) for i in range(0,-3,-1)]
RECT23_R1 = [(-1,-1),(-1,0)] + LINE2 + [(1,-1),(1,0)]

# Corner Shape
CORNER_SMALL = LINE2 + [(1,0)]
CORNER_SMALL_R1 = LINE2 + [(1,-1)]
CORNER_SMALL_R2 = [(0,-1),(1,-1),(1,0)]
CORNER_SMALL_R3 = [(0,0),(1,-1),(1,0)]
CORNER_BIG = LINE3 + [(i,0) for i in range(1,3)]
CORNER_BIG_R1 = LINE3 + [(1,-2),(2,-2)]
CORNER_BIG_R2 = [(-1,-2),(0,-2),(1,-2),(1,-1),(1,0)]
CORNER_BIG_R3 = [(-1,0),(0,0),(1,0),(1,-1),(1,-2)]

# L Shape
L_SHAPE = LINE3 + [(1,0)]
L_SHAPE_R1 = [(-1,0),(-1,-1),(0,-1),(1,-1)] 
L_SHAPE_R2 = [(0,-2),(1,0),(1,-1),(1,-2)]
L_SHAPE_R3 = LINE3_R1 + [(1,-1)]
REV_L_SHAPE = [(0,0),(1,0),(1,-1),(1,-2)]
REV_L_SHAPE_R1 = LINE3_R1 + [(-1,-1)]
REV_L_SHAPE_R2 = LINE3 + [(1,-2)]
REV_L_SHAPE_R3 = [(-1,-1),(0,-1),(1,-1),(1,0)]

# T Shape
T_SHAPE = [(-1,0)] + LINE2 + [(1,0)]
T_SHAPE_R1 = LINE3 + [(1,-1)]
T_SHAPE_R2 = [(0,0),(-1,-1),(0,-1),(1,-1)]
T_SHAPE_R3 = [(0,-1),(1,0),(1,-1),(1,-2)]

# Z Shape
Z_SHAPE =  [(-1,-1),(0,-1),(0,0),(1,0)]
Z_SHAPE_R1 = LINE2 + [(1,-1),(1,-2)]
REV_Z_SHAPE = [(-1,0)] + LINE2 + [(1,-1)]
REV_Z_SHAPE_R1 = [(0,-2),(0,-1),(1,-1),(1,0)]

SHAPES = (
    (SQ1,SQ2,SQ3),
    (LINE2,LINE3,LINE4,LINE5,LINE2_R1,LINE3_R1,LINE4_R1,LINE5_R1),
    (RECT23, RECT23_R1),
    (CORNER_SMALL,CORNER_SMALL_R1,CORNER_SMALL_R2,CORNER_SMALL_R3),
    (CORNER_BIG,CORNER_BIG_R1,CORNER_BIG_R2,CORNER_BIG_R3),
    (L_SHAPE,L_SHAPE_R1,L_SHAPE_R2,L_SHAPE_R3,
    REV_L_SHAPE,REV_L_SHAPE_R1,REV_L_SHAPE_R2,REV_L_SHAPE_R3),
    (T_SHAPE,T_SHAPE_R1,T_SHAPE_R2,T_SHAPE_R3),
    (Z_SHAPE,Z_SHAPE_R1,
    REV_Z_SHAPE,REV_Z_SHAPE_R1)
)
