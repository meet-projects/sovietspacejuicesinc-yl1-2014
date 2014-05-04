import pygame

class itemCatergory:
    def __init__(self, name, id, items, location, icon):
        self.name = name
        self.id = id
        self.itemList = items #List containing all item objects
        self.location = location
        self.icon = icon #String of image icon location
        self.surface = pygame.image.load(icon).convert()
        
        
    def getSurface(self):
        return self.surface
        