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
        self.finishButton = Button.Button(width,length, size, height, (x coord, y coord),none, self)
     
    def finishButtonClicked:
     If MoneyPutinside > totalMoneyNeeded:
      self.screen= "Main"
     for itemCat in self._itemCategories:
      item.amount = 0
     for item in self._itemCategories:
      item.amount = 0
      
      self.moneyin = 0
 
    def addMoney():
       global money
       money += 10
       budget.config(text='Budget: $'+str(money))
       moneyButton = Button(root,text='+ $10',width=15,height=7,command=addMoney)
    
       money += 1000000
       budget.config(text='Budget: $'+str(money))
       moneyButton = Button(root,text='+ $1000000',width=20,height=10,command=addMoney)
    
            
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(self._background)
        self._running = True
        self._screen = "Main" #Main - original screen. itemCat - screen showing items. checkOut - checkout screen.
        self.buttons = []
        self._itemCategories = []
        def itemCategory0Command(self):
            print "itemCat0Command"
            self._screen = "itemCatScreen:00"
        def itemCategory1Command(self):
            print "itemCat0Command"
            self._screen = "itemCatScreen:01"
        def itemCategory2Command(self):
            print "itemCat0Command"
            self._screen = "itemCatScreen:02"
        def itemCategory3Command(self):
            print "itemCat0Command"
            self._screen = "itemCatScreen:03"
            
        def itemIncrementCommand(self):
            print "itemCat0ItemNumber1Command"
            self.incriment()
        
        def itemDecrementCommand(self):
            print "itemCat0ItemNumber1Command"
            self.decrement()
        
        itemsToAdd = []    
        itemCat0ItemNumber0 = Items.item("Apollo", 0000, 40000, 0, (100,100), 144, 144, "Images/APOLLO.jpg", itemIncrementCommand, itemDecrementCommand)
        itemCat0ItemNumber1 = Items.item("Mercury", 0001, 40000, 0, (100,300), 144, 144, "Images/Mercury.jpg", itemIncrementCommand, itemDecrementCommand)
        itemCat0ItemNumber2 = Items.item("x38", 0002, 40000, 0, (300,100), 144, 144, "Images/x38c.jpg", itemIncrementCommand, itemDecrementCommand)
        itemCat0ItemNumber3 = Items.item("GEMINI", 0003, 40000, 0, (300,300), 144, 144, "Images/GEMINI.jpg", itemIncrementCommand, itemDecrementCommand)
       
        itemsToAdd.append(itemCat0ItemNumber0)
        itemsToAdd.append(itemCat0ItemNumber1)
        itemsToAdd.append(itemCat0ItemNumber2)
        itemsToAdd.append(itemCat0ItemNumber3)
        self._itemCategories.append(iC.itemCatergory("NASA", 00, itemsToAdd, (100,100), 144, 144, "Images/NASA.jpg", itemCategory0Command, self))
        
        itemsToAdd = []
        itemCat1ItemNumber0 = Items.item("Sputnik", 0100, 40000, 0, (100,100), 144, 144, "Images/Sputnik.jpg", itemIncrementCommand, itemDecrementCommand)
        itemCat1ItemNumber1 = Items.item("Vostok", 0101, 40000, 0, (100,300), 144, 144, "Images/Vostok.jpg", itemIncrementCommand, itemDecrementCommand)
        itemCat1ItemNumber2 = Items.item("Voskhod", 0102, 40000, 0, (300,100), 144, 144, "Images/voskhod-1__1.jpg", itemIncrementCommand, itemDecrementCommand)
       
        itemsToAdd.append(itemCat1ItemNumber0)
        itemsToAdd.append(itemCat1ItemNumber1)
        itemsToAdd.append(itemCat1ItemNumber2)
        self._itemCategories.append(iC.itemCatergory("Russian Spaceships", 01, itemsToAdd, (100,300), 144, 144, "Images/Sputnik.jpg", itemCategory1Command, self))
        
        itemsToAdd = []
        itemCat2ItemNumber0 = Items.item("SPACEX - DRAGON 7", 0200, 40000, 0, (100,100), 144, 144, "Images/SPACEX - DRAGON 7.jpg", itemIncrementCommand, itemDecrementCommand)        
        itemCat2ItemNumber1 = Items.item("DREAMCHASER 7", 0201, 40000, 0, (100,300), 144, 144, "Images/DREAMCHASER 7.jpg", itemIncrementCommand, itemDecrementCommand)       
        itemCat2ItemNumber2 = Items.item("CST-100", 0202, 40000, 0, (300,100), 144, 144, "Images/CST-100.jpg", itemIncrementCommand, itemDecrementCommand)       
       
        itemsToAdd.append(itemCat2ItemNumber0)
        itemsToAdd.append(itemCat2ItemNumber1)
        itemsToAdd.append(itemCat2ItemNumber2)
        self._itemCategories.append(iC.itemCatergory("Other Spaceships", 02, itemsToAdd, (300,100), 144, 144, "Images/CST-100.jpg", itemCategory2Command, self))        
        
        itemsToAdd = []
        itemCat3ItemNumber0 = Items.item("Lemonade", 0300, 40000, 0, (100,100), 144, 144, "Images/Lemonade.jpg", itemIncrementCommand, itemDecrementCommand)       
        itemCat3ItemNumber1 = Items.item("Orange", 0301, 40000, 0, (100,300), 144, 144, "Images/Orange.jpeg", itemIncrementCommand, itemDecrementCommand)       
        itemCat3ItemNumber2 = Items.item("Grapefruit", 0302, 40000, 0, (300,100), 144, 144, "Images/Grapefruit.jpg", itemIncrementCommand, itemDecrementCommand)       
        itemCat3ItemNumber3 = Items.item("Peach Mango", 0303, 40000, 0, (300,300), 144, 144, "Images/Peach Mango.jpg", itemIncrementCommand, itemDecrementCommand)       
       
        itemsToAdd.append(itemCat3ItemNumber0)
        itemsToAdd.append(itemCat3ItemNumber1)
        itemsToAdd.append(itemCat3ItemNumber2)
        itemsToAdd.append(itemCat3ItemNumber3)
        self._itemCategories.append(iC.itemCatergory("TROPICANA FLORIDA SUNSHINE", 03, itemsToAdd, (300,300), 144, 144, "Images/Orange.jpeg", itemCategory3Command, self))
      
      
        
        def goBackCommand(self):
            self._screen = "Main"
        self.backButton = Button.Button(144, 50, (50,50), goBackCommand, None, self)
        self.backButton.currentColor = self.backButton.default_color = self.backButton.hover_color = None #Make sure that the surface is not overwritten
        self.backButton.surface = Label.Label("BACK").getSurface()
      
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
            self.buttons.append(self.backButton)
            
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
