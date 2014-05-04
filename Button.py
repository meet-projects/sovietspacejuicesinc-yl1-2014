import pygame

class Button:
   def __init__(self, width, height, location, command):
      self.is_hover = False
      self.default_color = (200,250,100)
      self.hover_color = (255,255,255)
      self.currentColor = self.default_color
      self.width = width
      self.height = height
      self.location = location
      self.rect = pygame.Rect(location[0], location[1], width, height)
      self.command = command
      
   def color(self):
      if self.is_hover:
         return self.hover_color
      else:
         return self.default_color
         
      
   def check_hover(self, mouse):
      '''adjust is_hover value based on mouse over button - to change hover color'''
      if self.rect.collidepoint(mouse):
         self.is_hover = True 
      else:
         self.is_hover = False
         
   def onMouseMove(self, location):
        self.check_hover(location)
        self.currentColor = self.color()
        
   def onMouseClick(self, location):
        if self.rect.collidepoint(location):
            self.command()
            
   def getSurface(self):
     surface = pygame.Surface((self.width, self.height))
     surface.fill(self.color())
     return surface