class Tile():
    def __init__(self, contains_bomb):
        self.contains_bomb = contains_bomb
        self.clicked = False
        self.flagged = False
        self.neighbors = []
        self.numBombs = 0
    
    def setNumBombs(self):
        for tile in self.neighbors:
            if tile.contains_bomb:
                self.numBombs += 1

    def addNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumBombs()