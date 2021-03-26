from game import Game
from board import Board
size = (8,8)
board = Board(size)
screen_size = (800, 800)
game = Game(board, screen_size)
game.run()
