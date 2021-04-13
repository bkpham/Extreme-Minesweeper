from game import Game
from board import Board
import pygame
print("Choose a difficulty: Easy, Medium, or Hard")
print("test")
while(True):
    print("Press e for Easy, m for Medium, h for Hard")
    difficulty = input()
    if difficulty == 'e':
        size = (8,8)
        screen_size = (800,800)
        break
    if difficulty == 'm':
        size = (15,15)
        screen_size = (800,800)
        break
    if difficulty == 'h':
        size = (15,30)
        screen_size = (1400,700)
        break
    print("Invalid Input")
board = Board(size)
game = Game(board, screen_size)
game.run()
