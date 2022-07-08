MOVE_DISTANCE = 10


from turtle import Turtle, pos

class Car(Turtle):
    """Create a Car object that inherits from Turtle""" 
    
    def __init__(self, colour, start_pos):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(colour)
        self.seth(180)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(300, start_pos)
        
    def move(self, speed):
        self.forward(speed)
        
    def check_crash(self, player):
        if self.distance(player) <= 20:
            return True
        else:
            return False