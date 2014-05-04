import pygame
import Button
import Items

class itemCatergory:
    def __init__(self, name, id, items, location, width, height, icon, command, originalSurface):
        self.name = name
        self.id = id
        self.items = items #List containing all item objects
        self.location = location
        self.width = width
        self.height = height
        self.icon = icon #String of image icon location
        self.surface = pygame.image.load(icon).convert()
        self.button = Button.Button(width, height, location, command, None, originalSurface)
        
        
    def getSurface(self):
        return self.surface
    def getButton(self):
        return self.button
        