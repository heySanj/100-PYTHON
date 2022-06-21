def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

from turtle import Screen, Turtle
import time
from snake import Snake

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

# Turn of screen animations to manually update graphics
screen.tracer(0)

# Make Snake
snake = Snake()

# Controls
screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)          

# Game
game_is_on = True

while game_is_on:
    
    # Refresh the screen every sloop
    screen.update()
    time.sleep(0.1)
    
    # Move head forwards and chain all the body parts
    snake.move()
    



# Exit on click at the end of the code
screen.exitonclick()