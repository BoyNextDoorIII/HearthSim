import pygame

pygame.init()

class Cursor:
    def __init__(self):
        self.__image = None
        self.__pos = pygame.mouse.get_pos()
        self.__pressing = False
        self.__pressing2 = False
        self.__moving = False

    def get_is_pressing(self):
        return self.__pressing

    def set_is_pressing(self, boolean):
        self.__pressing = boolean

    def get_is_pressing2(self):
        return self.__pressing2

    def set_is_pressing2(self, boolean):
        self.__pressing2 = boolean
        
    def is_on_object(self,rect):
        if self.__pos[0] >= rect[0] and self.__pos[0] <= rect[0] + rect[2]:
            if self.__pos[1] >= rect[1] and self.__pos[1] <= rect[1] + rect[3]:
                return True
    def check_pressing(self):
        if not self.__pressing and pygame.mouse.get_pressed()[0]:
            self.__pressing = True
            return False
        elif self.__pressing and not pygame.mouse.get_pressed()[0]:
            self.__pressing = False
            return True
        return None
    
    def update(self):
        if self.__pos != pygame.mouse.get_pos():
            self.__moving = True
        self.__pos = pygame.mouse.get_pos()

mouse = Cursor()
