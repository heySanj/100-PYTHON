from turtle import Turtle
import random

class Food(Turtle):
    """A Food Object that inherits from Turtle"""  
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.refresh()
        self.rand_color = ()
        
        
        
    def refresh(self):
        # Colour
        self.rand_color = ( random.randint(30, 255),
                            random.randint(30, 255),
                            random.randint(30, 255))
        self.color(self.rand_color)        
        rand_x = 20 * round((random.randint(-280, 280))/20)
        rand_y = 20 * round((random.randint(-280, 280))/20)
        self.goto(rand_x, rand_y)
        

    