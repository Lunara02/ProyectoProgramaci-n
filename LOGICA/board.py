import numpy as np

class Board:
    def __init__(self,n):
        self.n = n
        self.board = np.zeros((n,n), dtype = int)

    def fill_bloc(self, i, j):
        self.board[i][j] = 1

    def remove_block(self, i,j):
        self.board[i][j] = 0

    def reset(self):
        self.board.fill(0)

    def print_board(self):
        print(self.board)