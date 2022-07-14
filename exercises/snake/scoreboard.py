from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')

class Scoreboard(Turtle):
    """A Scoreboard Object that inherits from Turtle"""  
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.penup()
        self.hideturtle()        
        self.pencolor('white')
        self.goto(0,270)
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        
        # Save high score if it is beat
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore()
            
        # Reset score
        self.score = 0
        self.write_score()    
        
    def get_highscore(self):
        with open("score.txt") as file:
            return int(file.read())
    
    def save_highscore(self):
        with open("score.txt", mode="w") as file:
            file.write(str(self.score))
            
            
    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.goto(0,-30)
    #     self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)