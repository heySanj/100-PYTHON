from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 34, 'bold')

class Scoreboard(Turtle):
    """A Scoreboard Object that inherits from Turtle"""  
    
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        
        # Draw line
        self.hideturtle()        
        self.pencolor('white')
        self.penup()
        
        self.goto(0,-300)
        
        
        # Conclude
        self.penup()
        self.goto(0,240)
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0,-30)
        self.write(f"Score: {self.left_score}", align=ALIGNMENT, font=FONT)