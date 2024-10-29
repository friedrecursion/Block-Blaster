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
WHITE = 8

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
    WHITE : (255,255,255),
}

# Shapes
ONE_BY_ONE_SQUARE = [(0,0)]
TWO_BY_TWO_SQUARE = [(0,0),(1,0),(0,1),(1,1)]
THREE_BY_THREE_SQUARE = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
HORIZONTAL_LINE = [(i,0) for i in range(3)]
VERTICAL_LINE = [(0,i) for i in range(3)]
L = VERTICAL_LINE + [(1,2)]
REVERSE_L = VERTICAL_LINE + [(-1,2)]
FLAT_L = HORIZONTAL_LINE + [(2,-1)]
REVERSE_FLAT_L = HORIZONTAL_LINE + [(0,-1)]

SHAPES = [
    ONE_BY_ONE_SQUARE,
    TWO_BY_TWO_SQUARE,
    THREE_BY_THREE_SQUARE,
    HORIZONTAL_LINE,
    VERTICAL_LINE,
    L,
    REVERSE_L,
    FLAT_L,
    REVERSE_FLAT_L,
]
