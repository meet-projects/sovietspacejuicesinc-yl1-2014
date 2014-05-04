import pygame
from pygame.locals import *

import events
import Label
import Button
import itemCategory as iC
import Items
 
class Game(events.Event):
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._image_loc = None
        self.size = self.width, self.height = 800, 500
        self._background = (96,96,96)
 
    
            
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(self._background)
        self._running = True
        self._screen = "Main" #Main - original screen. itemCat - screen showing items. checkOut - checkout screen.
        self.buttons = []
        self._itemCategories = []
        def itemCategory0Command():
            print "itemCat0Command"
            self._screen = "itemCatScreen:00"
            
        def itemCat0ItemNumber0Command():
            print "itemCat0ItemNumber1Command"
            self._itemCategories[0].items[0].incriment()
        
        def itemCat0ItemNumber0CommandRight():
            print "itemCat0ItemNumber1Command"
            self._itemCategories[0].items[0].decrement()
            
        itemCat0ItemNumber0 = Items.item("Apollo", 0000, 40000, 0, (100,100), 144, 144, "Images/APOLLO.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)
        
        itemCat0ItemNumber1 = Items.item("Mercury", 0001, 40000, 0, (100,100), 144, 144, "Images/Mercury.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)
        
        itemCat0ItemNumber2 = Items.item("x38", 0002, 40000, 0, (100,100), 144, 144, "Images/x38c.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)
        
         itemCat0ItemNumber3 = Items.item("GEMINI", 0003, 40000, 0, (100,100), 144, 144, "Images/GEMINI.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)
       
        itemCat1ItemNumber0 = Items.item("Sputnik", 0100, 40000, 0, (100,100), 144, 144, "Images/Sputnik.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)
       
        itemCat1ItemNumber1 = Items.item("Vostok", 0101, 40000, 0, (100,100), 144, 144, "Images/Vostok.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)
       
        itemCat1ItemNumber2 = Items.item("Voskhod", 0102, 40000, 0, (100,100), 144, 144, "Images/voskhod-1__1.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)
       
        
        itemCat3ItemNumber0 = Items.item("SPACEX - DRAGON 7", 0100, 40000, 0, (100,100), 144, 144, "Images/SPACEX - DRAGON 7.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)        itemsToAdd = []
       
        itemCat3ItemNumber1 = Items.item("DREAMCHASER 7", 0101, 40000, 0, (100,100), 144, 144, "Images/DREAMCHASER 7.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)       
       
        itemCat3itemNumber2 = Items.item("CST-100", 0102, 40000, 0, (100,100), 144, 144, "Images/CST-100.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)       
       
        itemCat4ItemNumber0 = Items.item("Lemonade", 0200, 40000, 0, (100,100), 144, 144, "Images/Lemonade.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)       
       
        itemCat4ItemNumber1 = Items.item("Orange", 0201, 40000, 0, (100,100), 144, 144, "Images/", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)       
       
        itemCat4ItemNumber2 = Items.item("Grapefruit", 0202, 40000, 0, (100,100), 144, 144, "Images/Grapefruit.jpg	", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)       
       
        itemCat4ItemNumber3 = Items.item("Peach Mango", 0203, 40000, 0, (100,100), 144, 144, "Images/Peach Mango.jpg", itemCat0ItemNumber0Command, itemCat0ItemNumber0CommandRight)       
       

       
       
       
        itemsToAdd.append(itemCat0ItemNumber0)
        self._itemCategories.append(iC.itemCatergory("NASA", 00, itemsToAdd, (100,100), 144, 144, "Images/NASA.jpg", itemCategory0Command))
        self._itemCategories.append(iC.itemCatergory("Russian Spaceships", 01, itemsToAdd, (100,100), 144, 144, "Images/.jpg", itemCategory0Command))
        self._itemCategories.append(iC.itemCatergory("Other Spaceships", 02, itemsToAdd, (100,100), 144, 144, "Images/.jpg", itemCategory0Command))        
        self._itemCategories.append(iC.itemCatergory("TROPICANA FLORIDA SUNSHINE", 03, itemsToAdd, (100,100), 144, 144, "Images/.jpg", itemCategory0Command))
      
      
        #self._image_surf = pygame.image.load("Images/myimage.jpg").convert()
        #self._image_loc = pygame.Rect(70, 70, 50, 20)
        #self._testText = Label.Label("Heyyy")
        
 
    def on_event(self, event):
        if event.type == QUIT:
            self.on_exit()
 
        elif event.type >= USEREVENT:
            self.on_user(event)
 
        elif event.type == VIDEOEXPOSE:
            self.on_expose()
 
        elif event.type == VIDEORESIZE:
            self.on_resize(event)
 
        elif event.type == KEYUP:
            self.on_key_up(event)
 
        elif event.type == KEYDOWN:
            self.on_key_down(event)
 
        elif event.type == MOUSEMOTION:
            self.on_mouse_move(event)
 
        elif event.type == MOUSEBUTTONUP:
            if event.button == 0:
                self.on_lbutton_up(event)
            elif event.button == 1:
                self.on_mbutton_up(event)
            elif event.button == 2:
                self.on_rbutton_up(event)
 
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.on_lbutton_down(event)
            elif event.button == 2:
                self.on_mbutton_down(event)
            elif event.button == 3:
                self.on_rbutton_down(event)
 
        elif event.type == ACTIVEEVENT:
            if event.state == 1:
                if event.gain:
                    self.on_mouse_focus()
                else:
                    self.on_mouse_blur()
            elif event.state == 2:
                if event.gain:
                    self.on_input_focus()
                else:
                    self.on_input_blur()
            elif event.state == 4:
                if event.gain:
                    self.on_restore()
                else:
                    self.on_minimize()
    def on_loop(self):
        if self._screen == "Main":
            self.buttons = []
            for itemCat in self._itemCategories:
                self.buttons.append(itemCat.getButton())
                
        if self._screen.find("itemCatScreen:") != -1:
            itemCatNumber = int(self._screen.replace("itemCatScreen:", ""))
            self.buttons = []
            for item in self._itemCategories[itemCatNumber].items:
                self.buttons.append(item.getButton())
            
    def on_render(self):
        self._display_surf.fill(self._background)
        for button in self.buttons:
            self._display_surf.blit(button.getSurface(), button.location)
            
        
        if self._screen == "Main":
            for itemCat in self._itemCategories:
                self._display_surf.blit(itemCat.getSurface(), itemCat.location)
        
        elif self._screen.find("itemCatScreen:") != -1:
            itemCatNumber = int(self._screen.replace("itemCatScreen:", ""))
            for item in self._itemCategories[itemCatNumber].items:
                self._display_surf.blit(item.getSurface(), item.location)
        
        #self._display_surf.blit(self._image_surf, self._image_loc, pygame.Rect(0, 0, 144, 144))
        #self._display_surf.blit(self._testText.getSurface(), (100,100))
        pygame.display.flip()


    #Event Handling:
    def on_exit(self):
         self._running = False

    def on_mouse_move(self, event):
        for button in self.buttons:
            button.onMouseMove(event.pos)
        #print event.pos
        #if event.pos[0]>=0 and event.pos[0]<=self.width and event.pos[1]>=0 and event.pos[1]<=self.height:
            #self._image_loc = pygame.Rect(event.pos[0], event.pos[1], 100, 70)
            
    def on_lbutton_down(self, event):
        for button in self.buttons:
            button.onMouseClick(event.pos)

    def on_rbutton_down(self, event):
        for button in self.buttons:
            button.onRightClick(event.pos)

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    game = Game()
    game.on_execute()
