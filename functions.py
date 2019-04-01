import pygame, sys
from constants import *

def get_centered(rect, size):
    return [rect[0]+(rect[2]-size[0])/2, rect[1]+(rect[3]-size[1])/2]

def quit_game():
    pygame.quit()
    sys.exit()

def search(cards, mechanic):
    for i in range(len(cards)):
        if mechanic in cards[i].get_mechanism():
            print(True)
            return i
        else:
            print(cards[i].get_mechanism())
    return None

def move(rect, pos):
    rect[0] = pos[0]
    rect[1] = pos[1]

def update():
    CLOCK.tick(FPS)
    pygame.display.update()
