import random

from constants import N, OUT_OF_BOUND, EMPTY, COLORS, SHAPES

class Board:

    def __init__(self,n = N):
        self.n = n
        self.debug_index = 0
        self.board = [[EMPTY for _ in range(n)] for  _ in range(n)]
        self.shape = SHAPES[self.debug_index]
        self.shapes = SHAPES
        self.color = COLORS[0]
        self.colors = COLORS

    def get_block(self,position):
        col, row = position
        if col >= self.n or col < 0 or row >= self.n or row < 0:
            return OUT_OF_BOUND
        return self.board[row][col]

    def add_block(self, position):
        # if self.__can_add_block(position):
        col, row = position
        for shape_col,shape_row in self.shape:
            self.board[row + shape_row][col + shape_col] = self.color
        self.__clear_lines()
        self.color = random.choice([c for c in self.colors if c != self.color])
        self.debug_index = (self.debug_index + 1) % len(self.shapes)
        self.shape = self.shapes[self.debug_index]
        # self.shape = random.choice(self.shapes)
    
    # private methods

    def __can_add_block(self,position):
        col, row = position
        for shape_col, shape_row in self.shape:
            if self.get_block((col+shape_col,row+shape_row)) != EMPTY:
                return False
        return True

    def __clear_lines(self):
        for i,row in enumerate(self.board):
            if all(x != EMPTY for x in row):
                self.board[i] = [EMPTY for _ in range(self.n)]
        for j in range(self.n):
            if all(self.board[i][j] != EMPTY for i in range(self.n)):
                for i in range(self.n):
                    self.board[i][j] = EMPTY
