from turtle import Turtle

class Ball(Turtle):
    """Create a Ball object that inherits from Turtle""" 
    

    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=1)
        # self.seth(heading)
        
        self.x_move = 4
        self.y_move = 4
        self.x_dir = 1
        self.y_dir = 1
        
    def move(self):
        self.goto(self.xcor() + (self.x_move * self.x_dir), self.ycor() + (self.y_move * self.y_dir))
        
    def reset(self):
        self.goto(0,0)
        self.x_dir *= -1
        self.x_move = 4
        self.y_move = 4
        
    def inc_speed(self):
        self.x_move += 1
        self.y_move += 1
        

