Michele's feedback on your group project
---

Great job finishing your group project! It was amazing to see you two being able to work together away from MEET while you were both in the states. The fact that you built a relationship with each other in the summer meant you could come together to face the challenge given to you. I have a few comments about your project: 

* When I want to run your program, I need to first look for an entry file - it is best to call this file "main.py" or something similar, so that it is clear that it is the main file of the project that I need to run to see your code. 
* Good job being consistent with your theme. The fonts and colors match, and your interface is easy to use. 
* The thing that makes your interface confusing is that the text labels and the buttons have the same color text / background. It would be helpful to make the buttons look different in some way from regular text. It looks like you tried to make "hovering" over a button work, but it does not work on my computer.
* Good job making the checkout screen work correctly. 
* One good coding practice is when you define functions and have other code in the same part, the functions should all be defined towards the top. For example, you have a function `on_init()` inside the `Game` class that had many functions INSIDE of this function. You should format the code so that all your inside functions are at the top inside the function, and all the code other than the inner functions come after. Like this: 

```
def on_init(self):
	 def itemIncrementCommand(self):
        print "itemIncerementCommand"
        self.incriment()
    
    def itemDecrementCommand(self):
        print "itemDecrementCommand"
        self.decrement()

    ...

    pygame.init()
	self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
	self._display_surf.fill(self._background)
	...
```

* You managed a lot of different events, which is great. In the yearlong we only talked about `MOUSEBUTTONDOWN`
* Good job using strings to decide which screen you are looking at. 
* It was an interesting idea to put all of your main running code inside of a class - it is very Java and C#-like. In Python, you do not need to put everything inside a class. It is fine the way you guys did it, but you did not have to. Instead, what you could have done was put all the code inside of the `Game` class outside of the class. The functions would be outside of the `if __name__=="__main__"`, and all the variables, main loop, event handling, etc, would be inside `if __name__=="__main__"`. 
* You should not have had to do `from pygame.locals import *`. In general, it is bad practice to import functions with the `*`, because then you are never sure where the function came from.
* Great job using functions as variables, for example to label what a button is supposed to do when you click it. 
* One design choice you could have considered is having a `Button` be a subclass of `Label`, since a Button has all the things a label has, and more. 
* Good job making `Label`s inside the `Items`, instead of making separate `Label`s and `Item`s for each item 