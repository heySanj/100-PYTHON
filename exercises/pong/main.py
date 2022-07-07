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
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.colormode(255)

# Turn of screen animations to manwually update graphics
screen.tracer(0)

# Create Paddle
paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))

# Create ball
ball = Ball()

# Scoreboard
score = Scoreboard()

# Controls
def controls():
    screen.listen()
    screen.onkey(key="Up", fun=paddle1.move_up)
    screen.onkey(key="Down", fun=paddle1.move_down)
    screen.onkey(key="w", fun=paddle2.move_up)
    screen.onkey(key="s", fun=paddle2.move_down)


# Game
game_is_on = True

while game_is_on:
    
    # Refresh the screen every loop
    time.sleep(0.02)
    screen.update()
    controls()
    score.write_score()
    
    # Move the ball
    ball.move()
    
    # Collided with top or bottom wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.y_dir *= -1
    
    # Detect Collision with paddles    
    if (ball.distance(paddle1) < 50 and ball.xcor() > 330
        or ball.distance(paddle2) < 50 and ball.xcor() < -330):
        ball.x_dir *= -1
        ball.inc_speed()

    # Detect Loss
    if ball.xcor() < -400:
        score.right_score += 1
        ball.reset()
    elif ball.xcor() > 400:
        score.left_score += 1
        ball.reset()

# Exit on click at the end of the code
screen.exitonclick()