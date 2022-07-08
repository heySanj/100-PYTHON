def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

from turtle import Screen
from player import Player
from car_manager import CarManager
from score import Scoreboard
import time


# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtler')
screen.colormode(255)

# Turn of screen animations to manually update graphics
screen.tracer(0)

# Create player
player = Player()
manager = CarManager()
score = Scoreboard()

def controls():
    # Controls
    screen.listen()
    screen.onkey(key="w", fun=player.move)
    

# Game
game_is_on = True

while game_is_on:
        
    # Refresh the screen every loop
    time.sleep(0.1)
    screen.update()
    controls()
    manager.create_car()    
    manager.move_cars()
    
    # Check Win
    if player.ycor() >= 280:
        score.score += 1
        score.write_score()
        manager.inc_speed()
        player.reset()
    
    # Collisions
    for car in manager.car_list:
        if car.check_crash(player):
            game_is_on = False
            score.game_over()
        


    
# Exit on click at the end of the code
screen.exitonclick()