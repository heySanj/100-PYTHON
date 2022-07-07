from turtle import Turtle

class Paddle(Turtle):
    """Create a Paddle object that inherits from Turtle""" 
    
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)
        
    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)
        
    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
