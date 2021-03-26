from random import random
from tile import Tile
PROBABILITY = 0.5

class Board():
    def __init__(self, size):
        self.size = size
        self.fillboard()

    def fillboard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                contains_bomb = random() < PROBABILITY
                tile = Tile(contains_bomb)
                row.append(tile)
            self.board.append(row)
        self.getNeighbors()
        
    def getNeighbors(self): #for each tile, get a list of its neighbors, assign tile.neighbors to this list
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                neighbors = []
                tile = self.board[row][col]
                for row2 in range(row-1, row+2):
                    for col2 in range(col-1, col+2):
                        out_of_bounds = row2 < 0 or row2 >= self.size[0] or (row2 == row and col2 == col) or col2 < 0 or col2 >= self.size[1] 
                        if not out_of_bounds:
                            neighbors.append(self.board[row2][col2])
                tile.addNeighbors(neighbors)
        return True

    def getSize(self):
        return self.size
    
    def getTile(self, row, col):
        return self.board[row][col]



