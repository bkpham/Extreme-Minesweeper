class Board():
    def __init__(self, size):
        self.size = size
        self.fillboard()

    def fillboard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                piece = None
                row.append(piece)
            self.board.append(row)

    def getSize(self):
        return self.size

class Tile():
    def __init__(self, contains_bomb):
        self.contains_bomb = contains_bomb
        self.clicked = False
        self.flagged = False
    
    def isClicked(self):
        return self.clicked
    
    def isFlagged(self):
        return self.flagged