import pygame
import Button

class items:
    def __init__(self, name, id, price, items, location, width, height, icon, command,totalPrice):
        self.name = name
        self.id = id
	self.price = price
        self.itemList = items 
        self.location = location
        self.width = width
        self.height = height
        self.icon = icon 
        self.surface = pygame.image.load(icon).convert()
        self.button = Button.Button(width, height, location, command)
        self.totalPrice = totalPrice

 def __init__(self, name, price):
        self.name = name
        self.price = price

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name
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
    item1 = Item("Apollo", 369M)
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

d