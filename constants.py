# board constants
N = 8       
CELL_SIZE = 100
BACKGROUND_COLOR = (18, 22, 70) # Dark Blue
# Derived constants
LINE_THICKNESS = CELL_SIZE//20
LINE_COLOR = tuple(BACKGROUND_COLOR[i]//2 for i in range(3)) # Darker Blue
WIDTH, HEIGHT = N * CELL_SIZE, N * CELL_SIZE

HOVER_ALPHA = 100 # Brightness of Block hover

OUT_OF_BOUND = -1 # Out of Grid value

# Possible colors to display
EMPTY = 0
BLUE = 1
RED = 2
GREEN = 3
PURPLE = 4
YELLOW = 5
ORANGE = 6

# Possible Block colors
COLORS = [BLUE,RED,GREEN,PURPLE,ORANGE]

# Color MACRO to RGB conversion
RGB_COLORS = {
    EMPTY : BACKGROUND_COLOR,
    BLUE : (53, 178, 224),     # Muted Blue
    RED : (202, 50, 49),      # Muted Red
    GREEN : (58, 180, 59),    # Muted Green
    PURPLE : (210, 95, 214),   # Muted Purple
    YELLOW : (236, 182, 50),   # Muted Yellow
    ORANGE : (220, 180, 100),   # Muted Orange
}

# Squares
SQ1 = [(0,0)] # 1x1
SQ2 = [(0,0),(1,0)] +[(0,-1),(1,-1)] # 2x2
SQ3 = [(i,0) for i in range(-1,2)] + [(i,-1) for i in range(-1,2)] + [(i,-2) for i in range(-1,2)]# 3x3

# Lines
LINE2 = [(0,0),(0,-1)]
LINE3 = [(0,i) for i in range(0,-3,-1)]
LINE4 = [(0,i) for i in range(0,-4,-1)]
LINE5 = [(0,i) for i in range(0,-5,-1)]

# 3x2 Rectangle
RECT23 = LINE3 + [(1,i) for i in range(0,-3,-1)]

# Corner Shape
CORNER_SMALL = LINE2 + [(1,0)]
CORNER_BIG = LINE3 + [(i,0) for i in range(1,3)]

# L Shape
L_SHAPE = LINE3 + [(1,0)]

# T Shape
T_SHAPE = [(-1,0)] + LINE2 + [(1,0)]

# Z Shape
Z_SHAPE = [(-1,0)] + LINE2 + [(1,-1)]

SHAPES = [
    SQ1,SQ2,SQ3,
    LINE2,LINE3,LINE4,LINE5,
    RECT23,
    CORNER_SMALL,CORNER_BIG,
    L_SHAPE,
    T_SHAPE,
    Z_SHAPE
]
