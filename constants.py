import pygame

pygame.init()

# ---------- RGB ----------
BLACK       = (  0,  0,  0)
BLUE        = (  0,  0,255)
GREEN       = (  0,255,  0)
HONEYDEW    = (240,255,240)#white
LIGHTYELLOW = (255,255, 51)
ORANGERED   = (255, 69,  0)
PERU        = (205,133, 63)#brown
SADDLEBROWN = (139, 69, 19)
RED         = (255,  0,  0)
WHITE       = (255,255,255)

# ---------- Font ---------
FONT = pygame.font.SysFont('arial',28)

# -------- Setting --------
SCREENWIDTH = 1280
SCREENHEIGHT = 720
SCREEN = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
CLOCK = pygame.time.Clock()
FPS = 30

# --------- Image ---------
CARD_BACK = pygame.image.load('card-back.png')
PRIEST_IMAGE = pygame.image.load('priest_image.png')
LESSER_HEAL_IMAGE = pygame.image.load('lesser_heal_image.png')

# ------- Temporary -------
opponent_health = 30
