import pygame, player
from display import *

player1 = player.Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
    display_board()
    player1.update()
    update()
