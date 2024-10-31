import random

from constants import N, OUT_OF_BOUND, EMPTY, COLORS, SHAPES

class Board:

    def __init__(self,n = N):
        self.score = 0
        self.score_adder = 0
        self.n = n
        self.board = [[EMPTY for _ in range(n)] for  _ in range(n)]
        self.shape = None
        self.shapes = [random.choice(random.choice(SHAPES)) for _ in range(3)]
        self.color = COLORS[0]
        self.colors = [random.choice(COLORS) for _ in range(3)]
        self.block_held = None
    
    def add_score(self):
        if self.score_adder > 0:
            self.score += 1
            self.score_adder -= 1

    def get_block(self,position):
        col, row = position
        if col >= self.n or col < 0 or row >= self.n or row < 0:
            return OUT_OF_BOUND
        return self.board[row][col]

    def add_block(self, position):
        if self.block_held != None:
            if self.can_add_block(position):
                self.score_adder += len(self.shape)
                col, row = position
                for shape_col,shape_row in self.shape:
                    self.board[row + shape_row][col + shape_col] = self.color
                self.__clear_lines()
                if all(shape is None for shape in self.shapes):
                    for i in range(3):
                        self.shapes[i] = random.choice(random.choice(SHAPES))
                        self.colors[i] = random.choice(COLORS)
            else:
                self.shapes[self.block_held] = self.shape
            self.block_held = None

    def can_add_block(self,position):
        col, row = position
        for shape_col, shape_row in self.shape:
            if self.get_block((col+shape_col,row+shape_row)) != EMPTY:
                return False
        return True

    def grab_block(self,position,index):
        if self.shapes[index] != None:
            x,y = position
            self.shape = self.shapes[index]
            self.shapes[index] = None
            self.color = self.colors[index]
            self.block_held = index

    def even_width(self,index = None):
        shape = self.shape if index == None else self.shapes[index]
        if shape != None:
            x_coords = [x for x, y in shape]
            min_x = min(x_coords)
            max_x = max(x_coords)
            distance = abs(max_x - (min_x-1))
            return distance % 2 == 0
        return False
    
    def height(self, index = None):
        shape = self.shape if index == None else self.shapes[index]
        y_coords = [y for x,y in shape]
        max_y = abs(min(y_coords))
        return max_y + 1
    
    # private methods

    def __clear_lines(self):
        score = 0
        rows_to_clear = set()
        cols_to_clear = set()
        for i, row in enumerate(self.board):
            if all(x != EMPTY for x in row):
                rows_to_clear.add(i)
                score += 16
        for j in range(self.n):
            if all(self.board[i][j] != EMPTY for i in range(self.n)):
                cols_to_clear.add(j)
                score += 16
        self.score += (len(rows_to_clear) + len(cols_to_clear))*score
        for i in rows_to_clear:
            self.board[i] = [EMPTY for _ in range(self.n)]
        for j in cols_to_clear:
            for i in range(self.n):
                self.board[i][j] = EMPTY

# def prefil(board):
#     for i in range(board.n):
#         for j in range(board.n):
#             if i != j:
#                 board.board[i][j] = random.choice(COLORS)
