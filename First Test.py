import pygame
from pygame.locals import *

import events
import Label
import Button
import itemCategory as iC
 
class Game(events.Event):
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._image_loc = None
        self.size = self.width, self.height = 640, 400
        self._background = (96,96,96)
 
    
            
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(self._background)
        self._running = True
        self._itemCategories = []
        def itemCategory1Command():
            print "itemCat1Command"
        self._itemCategories.append(iC.itemCatergory("NASA", 01, [], (100,100), 100, 100, "Images/NASA.jpg", itemCategory1Command))
        
        self._screen = "Main" #Main - original screen. itemCat - screen showing items. checkOut - checkout screen.
        self.buttons = []
        
        
        
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
            
    def on_render(self):
        self._display_surf.fill(self._background)
        for button in self.buttons:
            self._display_surf.blit(button.getSurface(), button.location)
            
        
        if self._screen == "Main":
            for itemCat in self._itemCategories:
                self._display_surf.blit(itemCat.getSurface(), itemCat.location)
        
        
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
