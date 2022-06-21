from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')

class Scoreboard(Turtle):
    """A Scoreboard Object that inherits from Turtle"""  
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()        
        self.pencolor('white')
        self.goto(0,270)
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0,-30)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)