import pygame
from constants import *
from functions import *

pygame.init()

def display_discover():
    pygame.draw.rect(SCREEN, WHITE, [40,40,104,254], 2)

def display_deck():
    pygame.draw.rect(SCREEN, WHITE, [SCREENWIDTH-147, (SCREENHEIGHT-50)/2+68,104,154], 2)

def display_field():
    pos = get_centered([0,0,SCREENWIDTH,SCREENHEIGHT], [900,2])
    pygame.draw.line(SCREEN, SADDLEBROWN, pos, [pos[0]+900,pos[1]], 2)

def display_hand():
    pos_x = get_centered([0,0,SCREENWIDTH,SCREENHEIGHT], [855,154])[0]
    rect = [pos_x, SCREENHEIGHT-172, 855, 154]
    pygame.draw.rect(SCREEN, SADDLEBROWN, rect)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)

def display_health():
    pos_x = get_centered([0,0,SCREENWIDTH,SCREENHEIGHT], [855,154])[0]
    pos_x = get_centered([0,0,pos_x,SCREENHEIGHT-170], [150,200])[0]
    rect = [pos_x+115, SCREENHEIGHT-85, 40, 40]
    pygame.draw.rect(SCREEN, RED, rect)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)

def display_hero():
    pos_x = get_centered([0,0,SCREENWIDTH,SCREENHEIGHT], [855,154])[0]
    pos_x = get_centered([0,0,pos_x,SCREENHEIGHT-170], [150,200])[0]
    SCREEN.blit(PRIEST_IMAGE, [pos_x,SCREENHEIGHT-210])

def display_hero_power():
    pos_x = get_centered([0,0,SCREENWIDTH,SCREENHEIGHT], [855,154])[0]
    pos_x = get_centered([0,0,pos_x,SCREENHEIGHT-170], [150,200])[0]
    rect = [pos_x+115, SCREENHEIGHT-130, 40, 40]
    SCREEN.blit(LESSER_HEAL_IMAGE, rect)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)

def display_mana():
    pos_x = get_centered([0,0,SCREENWIDTH,SCREENHEIGHT], [855,154])[0] + 855
    pos_y = get_centered([pos_x,SCREENHEIGHT-172,1280-pos_x,172], [104,104])[1]
    pygame.draw.rect(SCREEN, WHITE, [SCREENWIDTH-147,pos_y,102,102], 2)

def display_pass_button():
    rect = [SCREENWIDTH-170, (SCREENHEIGHT-50)/2, 150, 50]
    pygame.draw.rect(SCREEN, LIGHTYELLOW, rect)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)
    text = FONT.render("END TURN", True, BLACK)
    SCREEN.blit(text, get_centered(rect,text.get_size()))

def display_opponent_deck():
    pygame.draw.rect(SCREEN, WHITE, [SCREENWIDTH-147,(SCREENHEIGHT-50)/2-172,104,154], 2)

def display_opponent_hand():
    pos_x = get_centered([0,0,SCREENWIDTH,SCREENHEIGHT], [150,200])[0] + 200
    rect = [pos_x, 18, 260, 154]
    pygame.draw.rect(SCREEN, SADDLEBROWN, rect)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)

def display_opponent_health():
    pos_x = get_centered([0,0,SCREENWIDTH,SCREENHEIGHT], [150,200])[0]
    rect = [pos_x+115, 135, 40, 40]
    pygame.draw.rect(SCREEN, RED, rect)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)
    text = FONT.render(str(opponent_health), True, HONEYDEW)
    SCREEN.blit(text, get_centered(rect,text.get_size()))

def display_opponent_hero():
    pos_x = get_centered([0,0,SCREENWIDTH,SCREENHEIGHT], [150,200])[0]
    SCREEN.blit(PRIEST_IMAGE, [pos_x,10])

def display_opponent_hero_power():
    pos_x = get_centered([0,0,SCREENWIDTH,SCREENHEIGHT], [150,200])[0]
    rect = [pos_x+115, 90, 40, 40]
    SCREEN.blit(LESSER_HEAL_IMAGE, rect)
    pygame.draw.rect(SCREEN, WHITE, rect, 2)

def display_board():
    SCREEN.fill(PERU)
    display_discover()
    display_deck()
    display_field()
    display_hand()
    display_hero()
    display_health()
    display_mana()
    display_hero_power()
    display_pass_button()
    display_opponent_deck()
    display_opponent_hand()
    display_opponent_hero()
    display_opponent_health()
    display_opponent_hero_power()
