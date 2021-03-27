import pygame
import os
import time
class Game():
    def __init__(self, board, screen_size):
        self.board = board
        self.screen_size = screen_size
        self.tile_size = (self.screen_size[0]//self.board.getSize()[1], self.screen_size[1]//self.board.getSize()[0])
        self.loadImages()
    
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        running = True
        while running:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    running = False
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position,rightClick)
            pygame.display.flip()
            self.draw()
            if self.board.lost == True:
                pygame.display.flip()
                self.draw()
                pygame.mixer.music.load("boom.wav")
                pygame.mixer.music.play()
                time.sleep(1.2)
                pygame.mixer.music.stop()
                pygame.mixer.music.unload
                time.sleep(2)
                running = False
            if self.board.won == True:
                pygame.display.flip()
                self.draw()
                win = pygame.display.set_mode((500, 500))
                font = pygame.font.SysFont("comicsans", 30, True)
                text = font.render("Congratulations! You Won!", True, (255,255,255))
                win.blit(text, (70,240))
                pygame.mixer.music.load("victory.wav")
                pygame.mixer.music.play()
                pygame.display.flip()
                time.sleep(1.2)
                pygame.mixer.music.stop()
                pygame.mixer.music.unload
                time.sleep(2)
                running = False
        pygame.quit()

    def draw(self):
        position = (0,0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                tile = self.board.getTile(row,col)
                image = self.getImage(tile)
                self.screen.blit(image, position)
                position = position[0] + self.tile_size[0], position[1]
            position = 0, position[1] + self.tile_size[1]

    def loadImages(self):
        self.images = {}
        for filename in os.listdir("images"):
            if (not filename.endswith(".png")):
                continue
            image = pygame.image.load(os.path.join("images",filename))
            image = pygame.transform.scale(image, self.tile_size)
            self.images[filename] = image
    
    def getImage(self,tile):
        if tile.clicked:
            image = self.images[str(tile.numBombs)+".png"]
            if tile.contains_bomb:
                image = self.images["bomb_at_clicked.png"]
        elif(tile.flagged):
            image = self.images["flagged_block.png"]  
        else:
            image = self.images["empty_block.png"]
        return image
        
    def handleClick(self,position,rightClick):
        tile_index = position[1]//self.tile_size[1], position[0]//self.tile_size[0]
        self.board.doClick(tile_index,rightClick)