from turtle import Turtle

FONT = ('Courier', 22, 'bold')

class Scoreboard(Turtle):
    """A Scoreboard Object that inherits from Turtle"""
    
    def __init__(self):
        super().__init__()
        self.score = 1
        
        # Draw line
        self.hideturtle()        
        self.pencolor('black')
        self.penup()        
        self.goto(-260,240)
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align='left', font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=FONT)
        self.goto(0,-30)
        self.write(f"You made it to level {self.score}!", align='center', font=FONT)