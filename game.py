import pygame
import os
class Game():
    def __init__(self, board, screen_size):
        self.board = board
        self.screen_size = screen_size
        self.block_size = (self.screen_size[0]//self.board.getSize()[1], self.screen_size[1]//self.board.getSize()[0])
        self.loadImages()
    
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        running = True
        while running:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    running = False
            pygame.display.flip()
            self.draw()
        pygame.quit()


    def draw(self):
        position = (0,0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                image = self.images["empty_block.png"]
                self.screen.blit(image, position)
                position = position[0] + self.block_size[0], position[1]
            position = 0, position[1] + self.block_size[1]

    def loadImages(self):
        self.images = {}
        for filename in os.listdir("images"):
            if (not filename.endswith(".png")):
                continue
            image = pygame.image.load(os.path.join("images",filename))
            image = pygame.transform.scale(image, self.block_size)
            self.images[filename] = image
