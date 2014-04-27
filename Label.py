import pygame
from pygame.locals import *

class Label():
    def __init__(self, text):
        myfont = pygame.font.SysFont("monospace", 15)
        self.widthOffSet = 5 #number of pixels on either side of text
        self.height = myfont.get_height()
        self.width = 0
      

        for character in myfont.metrics(text):
            self.width += (character[1]-character[0])
            
     
        self.dimentions = (self.width + 3*self.widthOffSet), self.height # is *3 and not *2 to account for slight rounding errors in .metrics(text) -- just ignore
        self._text = text
        self._surface = pygame.Surface(self.dimentions)
        self._surface.blit(myfont.render(self._text, 1, (255,255,0)), (self.widthOffSet-1, 0))

    def getSurface(self):
        return self._surface
