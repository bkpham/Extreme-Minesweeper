from random import random
from tile import Tile
PROBABILITY = 0.7

class Board():
    def __init__(self, size):
        self.size = size
        self.num_bombs = 0
        self.fillboard()
        self.lost = False
        self.won = False
        self.num_clicked = 0
        

    def fillboard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                contains_bomb = random() < PROBABILITY
                if contains_bomb:
                    self.num_bombs += 1
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
    
    def doClick(self, index, rightClick):
        row = index[0]
        col = index[1]
        tile = self.board[row][col]
        if(rightClick):
            tile.toggleFlagged()
        elif tile.clicked == True:
            pass 
        else:
            tile.setClickedTrue()
            self.num_clicked += 1
            if(tile.numBombs == 0 and not tile.contains_bomb): #recursively click
                self.recursivelyClick(index)
            #print(self.size[0]*self.size[1], self.num_clicked,self.num_bombs)
            if self.num_clicked >= (self.size[0] * self.size[1]) - self.num_bombs:
                self.won = True
            if tile.contains_bomb:
                self.lost = True
            
    def recursivelyClick(self,index):
        row = index[0]
        col = index[1]
        for row2 in range(row-1, row+2):
            for col2 in range(col-1, col+2):
                out_of_bounds = row2 < 0 or row2 >= self.size[0] or (row2 == row and col2 == col) or col2 < 0 or col2 >= self.size[1] 
                if not out_of_bounds and self.board[row2][col2].clicked == False:
                    (self.board[row2][col2]).setClickedTrue()
                    self.num_clicked += 1
                    if(self.board[row2][col2].numBombs == 0):
                        self.recursivelyClick((row2,col2))



