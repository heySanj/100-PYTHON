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
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Rainbow Snake')
screen.colormode(255)

# Turn of screen animations to manually update graphics
screen.tracer(0)

# Make Snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Controls
def controls():
    screen.listen()
    screen.onkey(key="w", fun=snake.up)
    screen.onkey(key="s", fun=snake.down)
    screen.onkey(key="a", fun=snake.left)
    screen.onkey(key="d", fun=snake.right)
              
def reset_game():
    scoreboard.reset()
    snake.reset()

# Game
game_is_on = True

while game_is_on:
    
    # Refresh the screen every sloop
    screen.update()
    controls()
    time.sleep(0.1)
    
    # Move head forwards and chain all the body parts
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # Make snake longer and increase score
        snake.add_part(snake.snake_body[-1].pos(),food.rand_color)
        scoreboard.score += 1
        scoreboard.write_score()
    
    # Detect collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        # scoreboard.game_over()
        reset_game()

    # Detect collision with tail
    for part in snake.snake_body[1:]:
        if snake.head.distance(part) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            reset_game()
                
# Exit on click at the end of the code
screen.exitonclick()