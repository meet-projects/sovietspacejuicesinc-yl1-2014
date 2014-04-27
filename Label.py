import pygame
from pygame.locals import *

class Label():
    def __init__(self, rectangle, text):
        myfont = pygame.font.SysFont("monospace", 15)
        
        self._rect = rectangle
        self._text = text
        self._surface = pygame.Surface([self._rect.width, self._rect.height])
        self._surface.blit(myfont.render(self._text, 1, (255,255,0)), (0, 0))

    def getSurface(self):
        return self._surface
