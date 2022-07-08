STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    """Create a Player object that inherits from Turtle""" 
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('black')
        self.goto(STARTING_POSITION)
        self.seth(90)
        
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def reset(self):
        self.goto(STARTING_POSITION)