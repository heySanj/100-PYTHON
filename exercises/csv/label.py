from turtle import Turtle

FONT = ('Arial', 14, 'bold')

class Label(Turtle):
    """Create a label object that inherits from Turtle""" 

    def __init__(self, text, pos):
        super().__init__()        
        # Write text
        self.hideturtle()        
        self.pencolor('black')
        self.penup()        
        self.goto(pos)
        self.write(text, align='center', font=FONT)
        
