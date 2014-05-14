import pygame
import Button
import Label

class item:
    def __init__(self, name, id, price, amount, location, width, height, icon, command, commandRight):
        self.name = name
        self.id = id
        self.price = price
        self.amount = amount
        self.location = location
        self.width = width
        self.height = height
        self.icon = icon 
        self.surface = pygame.image.load(icon).convert()
        self.button = Button.Button(width, height, location, command, commandRight, self)
        self.totalPrice = price*amount
        self.labelName = Label.Label("Name: " + str(name))
        self.labelPrice = Label.Label("Price: " + str(price))
        self.labelAmount = Label.Label("Amount: " + str(amount))
        self.surface.blit(self.labelName.getSurface(), (0, 0))
        self.surface.blit(self.labelPrice.getSurface(), (0, 0 + height/3))
        self.surface.blit(self.labelAmount.getSurface(), (0, 0 + height*2/3))

    def getButton(self):
        return self.button
    
    def getSurface(self):
        self.labelAmount = Label.Label("Amount: " + str(self.amount)) #Update the amount label
        #Recreate surface after amount change
        self.surface = pygame.image.load(self.icon).convert()
        self.surface.blit(self.labelName.getSurface(), (0, 0))
        self.surface.blit(self.labelPrice.getSurface(), (0, 0 + self.height/3))
        self.surface.blit(self.labelAmount.getSurface(), (0, 0 + self.height*2/3))
        return self.surface
    
    def incriment(self):
        self.amount+=1
        
    def decrement(self):
        if self.amount > 0:
            self.amount-=1
    
    def updateTotalPrice(self):
        self.totalPrice = self.amount * self.price
    
    def getTotalPrice(self):
        self.updateTotalPrice()
        return self.totalPrice
    
    def getPrice(self):
        return self.price
    
    def getName(self):
        return self.name
    
    
'''
class itemToBuy:
        
 	def __init__(self, list):
        	self.list = []

    	def addItem(self, item):
        	self.list.append(self.list)

    	def getTotal(self):
       		 total = 0
        	 for item in self.list:
          	  	name, price = item # or price = item[1]
            		total = total + price

    	def getItems(self):
      	  count = 0
      	  for c in range(self.list):
           	 count = self.list + 1
          return count

        def removeItem(self, item)
        #removes the item from the cart's item list

def main():
    item1 = Item("Apollo", 3M)
    item2 = Item("Tropicana Juice", 2.39)
    item3 = Item("Russian spaceship", 598M)
    c = Cart()
    c.addItem(item1)
    c.addItem(item2)
    c.addItem(item3)
    print "You have %i items in your cart for a total of $%.02f" %(c.getNumItems(), c.getTotal())
    c.removeItem(item3)
    print "You have %i items in your cart for a total of $%.02f" % (c.getNumItems(), c.getTotal())
main()  
'''
